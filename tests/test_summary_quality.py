from __future__ import annotations

import unittest
from datetime import UTC, datetime

from digest.models import Item
from digest.models import NewsClassification
from digest.summarize import (
    _fallback_news_summary,
    _guard_against_false_negative,
    _validate_paper_summary,
    summarize_with_llm,
)


class FakeStore:
    def __init__(self, cached: dict | None = None) -> None:
        self.cached = cached

    def get_cached_summary(self, source_id: str, url: str) -> dict | None:
        return self.cached


class FakeBackend:
    def __init__(self) -> None:
        self.classify_calls = 0
        self.summary_calls = 0

    def classify_news(self, payload: dict) -> dict:
        self.classify_calls += 1
        return {"include": True, "reason_kr": "AI 서비스 변화와 직접 관련된 기사입니다."}

    def summarize_news(self, payload: dict) -> dict:
        self.summary_calls += 1
        return {
            "headline_kr": "Airbnb가 새 AI 연구 조직을 준비한다",
            "what": ["Airbnb CEO Brian Chesky가 자체 AI 연구 조직 구상을 밝혔습니다."],
            "why_trend": ["플랫폼 기업들이 외부 AI 모델 활용을 넘어 자체 연구 역량을 강화하는 흐름입니다."],
            "keywords": ["airbnb", "ai", "lab"],
        }

    def summarize_paper(self, payload: dict) -> dict:
        raise AssertionError("paper summary should not be called")


def _news_item() -> Item:
    return Item(
        source_id="techcrunch_ai",
        source_name="TechCrunch AI",
        title="Airbnb's Brian Chesky plans to launch a new AI lab",
        url="https://example.com/airbnb-ai-lab",
        published_at=datetime(2026, 6, 5, 1, 0, tzinfo=UTC),
        fetched_at=datetime(2026, 6, 5, 2, 0, tzinfo=UTC),
        summary_raw=(
            "Airbnb CEO Brian Chesky has had enough of merely being an artificial "
            "intelligence kingmaker. He now plans to back a new AI lab of his own."
        ),
    )


class SummaryQualityTest(unittest.TestCase):
    def test_news_fallback_does_not_embed_raw_excerpt_sentences(self) -> None:
        summary = _fallback_news_summary(_news_item())

        body = " ".join(summary.what)
        self.assertNotIn("원문에서 확인된 핵심 내용", body)
        self.assertNotIn("Airbnb CEO Brian Chesky has had enough", body)
        self.assertNotIn("LLM 요약을 만들지 못해", body)
        self.assertIn("세부 내용은 원문 확인이 필요합니다.", body)

    def test_bad_cached_fallback_artifact_is_regenerated(self) -> None:
        cached = {
            "kind": "news",
            "classification": {"include": True, "reason_kr": "AI 기사입니다."},
            "summary": {
                "headline_kr": "TechCrunch AI발 관련 AI 업데이트",
                "what": [
                    "원문에서 확인된 핵심 내용: Airbnb CEO Brian Chesky has had enough of merely being an artificial intelligence kingmaker.",
                ],
                "why_trend": ["새 모델·기능·API 변화는 생태계 경쟁 구도에 영향을 줍니다."],
                "keywords": ["airbnb", "ai"],
            },
        }
        backend = FakeBackend()

        included_news, news_summaries, _, cache_payloads = summarize_with_llm(
            news_items=[_news_item()],
            paper_items=[],
            backend=backend,
            store=FakeStore(cached),
            refresh=False,
        )

        self.assertEqual(1, len(included_news))
        self.assertEqual(1, backend.classify_calls)
        self.assertEqual(1, backend.summary_calls)
        summary = news_summaries[_news_item().url]
        self.assertNotIn("원문에서 확인된 핵심 내용", " ".join(summary.what))
        self.assertEqual("llm", cache_payloads[_news_item().url]["summary_source"])

    def test_cached_fallback_is_not_reused_when_backend_is_available(self) -> None:
        cached = {
            "kind": "news",
            "classification": {"include": True, "reason_kr": "AI 기사입니다."},
            "summary_source": "fallback",
            "summary": {
                "headline_kr": "TechCrunch AI 보도: Airbnb AI lab",
                 "what": ["LLM 요약을 만들지 못해 원문 문장을 자동 요약문으로 섞지 않았습니다."],
                "why_trend": ["새 모델·기능·API 변화는 생태계 경쟁 구도에 영향을 줍니다."],
                "keywords": ["airbnb", "ai"],
            },
        }
        backend = FakeBackend()

        summarize_with_llm(
            news_items=[_news_item()],
            paper_items=[],
            backend=backend,
            store=FakeStore(cached),
            refresh=False,
        )

        self.assertEqual(1, backend.classify_calls)
        self.assertEqual(1, backend.summary_calls)

    def test_ai_keyword_heuristic_prevents_local_classifier_false_negative(self) -> None:
        classification = _guard_against_false_negative(
            _news_item(),
            NewsClassification(include=False, reason_kr="비즈니스 기사로 판단했습니다."),
        )

        self.assertTrue(classification.include)
        self.assertIn("AI 관련 핵심 신호", classification.reason_kr)

    def test_rejects_korean_prefixed_english_artifact(self) -> None:
        with self.assertRaisesRegex(ValueError, "mixed-script artifact"):
            _validate_paper_summary(
                {
                    "one_liner_kr": "DataCOPE는 데이터 분석 기술을 언SUPERVISED한 탐색으로 발견합니다.",
                    "core_idea_kr": "DataCOPE는 검증자 신호를 활용해 데이터 분석 에이전트의 기술을 평가합니다.",
                    "keywords": ["DataCOPE", "agentic data analysis"],
                },
                title="Unsupervised Skill Discovery for Agentic Data Analysis",
            )

        with self.assertRaisesRegex(ValueError, "mixed-script artifact"):
            _validate_paper_summary(
                {
                    "one_liner_kr": "Cloudflare는 웹 트래픽 변화를 분석합니다.",
                    "core_idea_kr": "클라우드flare가 봇 트래픽 증가를 보고했습니다.",
                    "keywords": ["Cloudflare", "traffic"],
                },
                title="Cloudflare warns bot and agentic traffic has overtaken human traffic",
            )


if __name__ == "__main__":
    unittest.main()
