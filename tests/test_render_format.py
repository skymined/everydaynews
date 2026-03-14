from __future__ import annotations

import unittest
from datetime import UTC, date, datetime

from digest.models import Item, NewsSummary, PaperSummary
from digest.render import render_digest_markdown


class RenderFormatTest(unittest.TestCase):
    def test_newsletter_style_output(self) -> None:
        news_item = Item(
            source_id="openai_news",
            source_name="OpenAI",
            title="OpenAI launches a new agent stack",
            url="https://example.com/news",
            published_at=datetime(2026, 2, 18, 1, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 2, 19, 1, 0, tzinfo=UTC),
        )
        signal_item = Item(
            source_id="reddit_localllama",
            source_name="Reddit r/LocalLLaMA",
            title="Community reacts to a new open model",
            url="https://example.com/reddit",
            published_at=datetime(2026, 2, 18, 2, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 2, 19, 1, 0, tzinfo=UTC),
        )
        paper_item = Item(
            source_id="hf_papers_today",
            source_name="HF Papers",
            title="A useful paper",
            url="https://example.com/paper",
            published_at=None,
            fetched_at=datetime(2026, 2, 19, 1, 0, tzinfo=UTC),
        )
        md = render_digest_markdown(
            target_date=date(2026, 2, 19),
            kst_date=date(2026, 2, 19),
            news_items=[news_item, signal_item],
            paper_items=[paper_item],
            news_summaries={
                news_item.url: NewsSummary(
                    headline_kr="OpenAI가 새 agent stack을 공개했다",
                    what=["API와 도구 연결 방식이 확장됐다", "기업 배포 흐름이 빨라질 수 있다"],
                    why_trend=["에이전트 제품 경쟁이 더 빨라질 수 있다"],
                    keywords=["openai", "agent", "api"],
                ),
                signal_item.url: NewsSummary(
                    headline_kr="커뮤니티에서 새 오픈 모델 반응이 빠르게 번졌다",
                    what=["성능 비교와 배포 후기가 빠르게 올라왔다"],
                    why_trend=["실사용 반응은 초기 시장 온도를 보여준다"],
                    keywords=["reddit", "open-model", "benchmark"],
                ),
            },
            paper_summaries={
                paper_item.url: PaperSummary(
                    one_liner_kr="이 논문은 멀티모달 모델의 핵심 성능을 높이려는 접근을 제안한다.",
                    core_idea_kr="문제는 복잡한 입력을 안정적으로 처리하는 것이다. 저자들은 새 방법을 제안하고 성능 향상을 주장한다.",
                    keywords=["multimodal", "benchmark", "reasoning"],
                )
            },
        )
        self.assertIn("## 오늘의 뉴스", md)
        self.assertIn("## 커뮤니티와 검색에서 읽힌 흐름", md)
        self.assertIn("## 오늘의 논문", md)
        self.assertIn("2026-02-19 KST 기준으로 수집한 AI 뉴스레터입니다.", md)
        self.assertIn("### [OpenAI가 새 agent stack을 공개했다](https://example.com/news)", md)
        self.assertIn("출처는 OpenAI입니다.", md)
        self.assertIn("### 1. [A useful paper](https://example.com/paper)", md)
        self.assertNotIn("- 핵심:", md)
        self.assertNotIn("- 왜 중요한가:", md)
        self.assertNotIn("- 태그:", md)


if __name__ == "__main__":
    unittest.main()
