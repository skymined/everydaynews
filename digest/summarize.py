from __future__ import annotations

import logging
import re
from datetime import UTC, datetime
from typing import Iterable

from .models import Item, NewsClassification, NewsSummary, PaperSummary, ScoringConfig
from .store import DigestStore

logger = logging.getLogger(__name__)


def score_item(item: Item, scoring: ScoringConfig, now: datetime | None = None) -> float:
    now = now or datetime.now(UTC)
    source_weight = scoring.source_weights.get(item.source_id, 0.5)
    text = f"{item.title} {item.summary_raw or ''}".lower()
    keyword_hits = 0
    for keyword in scoring.priority_keywords:
        if keyword.lower() in text:
            keyword_hits += 1

    recency_score = 0.2
    if item.published_at:
        age_hours = max((now - item.published_at.astimezone(UTC)).total_seconds() / 3600.0, 0.0)
        recency_score = max(0.0, 1.0 - age_hours / 72.0)
    return source_weight + (0.15 * keyword_hits) + recency_score


def rank_items(items: Iterable[Item], scoring: ScoringConfig) -> list[Item]:
    ranked: list[Item] = []
    for item in items:
        scored = item.model_copy()
        scored.score = score_item(scored, scoring=scoring)
        ranked.append(scored)
    ranked.sort(key=lambda x: x.score, reverse=True)
    return ranked


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _excerpt(item: Item, max_chars: int = 1800) -> str:
    base = item.content_text or item.summary_raw or item.title
    base = re.sub(r"<[^>]+>", " ", base)
    return _clean_text(base)[:max_chars]


def _payload(item: Item) -> dict:
    return {
        "title": item.title,
        "source": item.source_name,
        "url": item.url,
        "published_at": item.published_at.isoformat() if item.published_at else None,
        "excerpt": _excerpt(item, max_chars=1800),
    }


def _fallback_classify_news(item: Item) -> NewsClassification:
    text = f"{item.title} {item.summary_raw or ''}".lower()
    include = any(
        key in text
        for key in (
            "ai",
            "model",
            "agent",
            "llm",
            "safety",
            "governance",
            "inference",
            "benchmark",
            "research",
            "api",
        )
    )
    reason = "AI 모델/제품/정책/연구 관련 키워드가 포함되어 트렌드 후보로 판단했습니다." if include else "AI 트렌드 직접 연관성이 낮아 제외했습니다."
    return NewsClassification(include=include, reason_kr=reason)


def _fallback_news_summary(item: Item) -> NewsSummary:
    excerpt = _excerpt(item, max_chars=700)
    points = []
    for sentence in re.split(r"(?<=[\.\!\?])\s+", excerpt):
        sentence = sentence.strip(" -")
        if len(sentence) < 15:
            continue
        points.append(sentence[:170])
        if len(points) >= 4:
            break
    if not points:
        points = [item.title]

    headline = f"{item.source_name}에서 '{item.title}' 관련 핵심 발표"
    why = ["해당 발표는 AI 제품/연구/정책 변화 흐름을 보여줘 후속 발표와 비교 가치가 큽니다."]
    keywords = re.findall(r"[A-Za-z0-9\-\_]{3,}", item.title)[:6]
    if not keywords:
        keywords = ["ai", "trend", "news"]
    return NewsSummary(
        headline_kr=headline,
        what=points[:4],
        why_trend=why,
        keywords=[k.lower() for k in keywords][:6],
    )


def _paper_sentences(excerpt: str) -> list[str]:
    cleaned = excerpt.replace("Abstract", " ").replace("摘要", " ")
    cleaned = _clean_text(cleaned)
    if not cleaned:
        return []
    parts = re.split(r"(?<=[\.\!\?])\s+", cleaned)
    out: list[str] = []
    for part in parts:
        s = part.strip(" -")
        if len(s) < 30:
            continue
        if s.lower() in {"abstract"}:
            continue
        out.append(s)
    return out


def _infer_paper_subject(title: str, excerpt: str) -> str:
    text = f"{title} {excerpt}".lower()
    mapping: list[tuple[tuple[str, ...], str]] = [
        (("agent", "policy", "planner"), "AI 에이전트"),
        (("robot", "humanoid", "embodied"), "로보틱스/체화 AI"),
        (("diffusion", "video generation"), "생성 모델(diffusion)"),
        (("retrieval", "rag", "memory"), "리트리벌/메모리 기반 AI"),
        (("benchmark", "evaluation", "reliability"), "모델 평가·신뢰성"),
        (("multimodal", "vision-language", "vlm"), "멀티모달 AI"),
        (("attention", "transformer"), "모델 아키텍처/연산 최적화"),
        (("factual", "hallucination"), "사실성/환각 완화"),
    ]
    for keys, label in mapping:
        if any(key in text for key in keys):
            return label
    return "AI 모델/시스템"


def _infer_paper_contribution(title: str, excerpt: str) -> str:
    text = f"{title} {excerpt}".lower()
    if any(key in text for key in ("benchmark", "bench", "leaderboard")):
        return "새 벤치마크/평가 프레임"
    if any(key in text for key in ("dataset", "data generation", "corpus")):
        return "새 데이터셋/데이터 생성 방법"
    if any(key in text for key in ("framework", "pipeline", "system", "agent")):
        return "새 프레임워크/시스템"
    if any(key in text for key in ("model", "architecture", "method", "approach")):
        return "새 모델/방법론"
    return "새 접근"


def _infer_paper_goal(title: str, excerpt: str) -> str:
    text = f"{title} {excerpt}".lower()
    if any(key in text for key in ("efficient", "sparse", "linear", "latency", "throughput", "speed")):
        return "효율과 처리속도"
    if any(key in text for key in ("robust", "reliability", "safety", "factual", "uncertainty")):
        return "신뢰성과 안정성"
    if any(key in text for key in ("generalization", "zero-shot", "transfer", "open-vocabulary")):
        return "일반화 성능"
    if any(key in text for key in ("accuracy", "performance", "sota")):
        return "성능"
    return "실사용 성능"


def _build_paper_keywords(title: str, excerpt: str) -> list[str]:
    text = f"{title} {excerpt}".lower()
    priority = [
        "agents",
        "agent",
        "multimodal",
        "diffusion",
        "retrieval",
        "rag",
        "rl",
        "robotics",
        "humanoid",
        "alignment",
        "benchmark",
        "evaluation",
        "memory",
        "attention",
        "policy",
        "inference",
        "safety",
        "factuality",
    ]
    picked: list[str] = []
    for token in priority:
        if token in text and token not in picked:
            picked.append(token)
        if len(picked) >= 6:
            return picked

    fallback = re.findall(r"[A-Za-z0-9\-\_]{3,}", title)
    stop = {
        "with",
        "for",
        "the",
        "and",
        "are",
        "through",
        "from",
        "using",
        "towards",
        "learning",
    }
    for token in fallback:
        t = token.lower()
        if t in stop or t in picked:
            continue
        picked.append(t)
        if len(picked) >= 6:
            break
    if not picked:
        picked = ["ai", "research", "paper"]
    return picked[:6]


def _fallback_paper_summary(item: Item) -> PaperSummary:
    excerpt = _excerpt(item, max_chars=800)
    subject = _infer_paper_subject(item.title, excerpt)
    contribution = _infer_paper_contribution(item.title, excerpt)
    goal = _infer_paper_goal(item.title, excerpt)
    one_liner = f"{subject} 영역에서 {contribution}을 제안해 {goal} 개선을 노린 연구입니다."

    sentences = _paper_sentences(excerpt)
    concrete_1 = sentences[0][:170] if len(sentences) >= 1 else item.title
    concrete_2 = sentences[1][:170] if len(sentences) >= 2 else ""
    concrete_3 = sentences[2][:170] if len(sentences) >= 3 else ""

    detail_lines = [
        f"문제 설정: {subject}에서 기존 방법의 한계를 개선하려는 목적을 가집니다.",
        f"접근 방법: {contribution} 중심으로 해결 전략을 제시합니다.",
    ]
    if concrete_1:
        detail_lines.append(f"원문 핵심 1: {concrete_1}")
    if concrete_2:
        detail_lines.append(f"원문 핵심 2: {concrete_2}")
    if concrete_3:
        detail_lines.append(f"원문 핵심 3: {concrete_3}")

    core = " ".join(detail_lines[:4])
    keywords = _build_paper_keywords(item.title, excerpt)
    return PaperSummary(
        one_liner_kr=one_liner,
        core_idea_kr=core,
        keywords=keywords[:6],
    )


def _validate_news_classification(raw: dict) -> NewsClassification:
    return NewsClassification.model_validate(raw)


def _validate_news_summary(raw: dict) -> NewsSummary:
    summary = NewsSummary.model_validate(raw)
    summary.what = [w.strip() for w in summary.what if w and w.strip()][:4]
    summary.why_trend = [w.strip() for w in summary.why_trend if w and w.strip()][:2]
    summary.keywords = [k.strip() for k in summary.keywords if k and k.strip()][:6]
    return summary


def _validate_paper_summary(raw: dict) -> PaperSummary:
    summary = PaperSummary.model_validate(raw)
    summary.keywords = [k.strip() for k in summary.keywords if k and k.strip()][:6]
    return summary


def summarize_with_llm(
    *,
    news_items: list[Item],
    paper_items: list[Item],
    backend: object | None,
    store: DigestStore,
    refresh: bool,
) -> tuple[list[Item], dict[str, NewsSummary], dict[str, PaperSummary], dict[str, dict]]:
    included_news: list[Item] = []
    news_summaries: dict[str, NewsSummary] = {}
    paper_summaries: dict[str, PaperSummary] = {}
    cache_payloads: dict[str, dict] = {}

    for item in news_items:
        cached = None if refresh else store.get_cached_summary(item.source_id, item.url)
        classification: NewsClassification | None = None
        summary: NewsSummary | None = None

        if cached and cached.get("kind") == "news":
            try:
                classification = _validate_news_classification(cached.get("classification", {}))
                if classification.include:
                    summary = _validate_news_summary(cached.get("summary", {}))
            except Exception:
                classification = None
                summary = None

        if classification is None:
            if backend is None:
                classification = _fallback_classify_news(item)
            else:
                try:
                    classification = _validate_news_classification(backend.classify_news(_payload(item)))
                except Exception as exc:
                    logger.warning("classify_news failed (%s): %s", item.url, exc)
                    classification = _fallback_classify_news(item)

        if classification.include and summary is None:
            if backend is None:
                summary = _fallback_news_summary(item)
            else:
                try:
                    summary = _validate_news_summary(backend.summarize_news(_payload(item)))
                except Exception as exc:
                    logger.warning("summarize_news failed (%s): %s", item.url, exc)
                    summary = _fallback_news_summary(item)

        payload: dict = {
            "kind": "news",
            "classification": classification.model_dump(),
        }
        if summary is not None:
            payload["summary"] = summary.model_dump()
        cache_payloads[item.url] = payload

        if classification.include and summary is not None:
            included_news.append(item)
            news_summaries[item.url] = summary

    for item in paper_items:
        cached = None if refresh else store.get_cached_summary(item.source_id, item.url)
        summary: PaperSummary | None = None
        if cached and cached.get("kind") == "paper":
            try:
                summary = _validate_paper_summary(cached.get("summary", {}))
            except Exception:
                summary = None

        if summary is None:
            if backend is None:
                summary = _fallback_paper_summary(item)
            else:
                try:
                    summary = _validate_paper_summary(backend.summarize_paper(_payload(item)))
                except Exception as exc:
                    logger.warning("summarize_paper failed (%s): %s", item.url, exc)
                    summary = _fallback_paper_summary(item)

        paper_summaries[item.url] = summary
        cache_payloads[item.url] = {
            "kind": "paper",
            "summary": summary.model_dump(),
        }

    return included_news, news_summaries, paper_summaries, cache_payloads
