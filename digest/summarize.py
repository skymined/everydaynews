from __future__ import annotations

import logging
import re
from datetime import UTC, datetime
from typing import Iterable

from .models import Item, NewsClassification, NewsSummary, PaperSummary, ScoringConfig
from .store import DigestStore

logger = logging.getLogger(__name__)

HANGUL_RE = re.compile(r"[\uac00-\ud7a3]")
FORBIDDEN_SCRIPT_RE = re.compile(r"[\u3040-\u30ff\u31f0-\u31ff\u0400-\u04ff]")
TECH_TERM_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9]*(?:[._/-][A-Za-z0-9]+)+\b")
TECH_TERM_STOPWORDS = {"ai", "llm", "ml", "nlp"}


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


def _require_korean_text(text: str, field_name: str) -> str:
    normalized = _clean_text(text)
    if not normalized:
        raise ValueError(f"{field_name} is empty")
    if FORBIDDEN_SCRIPT_RE.search(normalized):
        raise ValueError(f"{field_name} contains unsupported script")
    if not HANGUL_RE.search(normalized):
        raise ValueError(f"{field_name} must include Korean text")
    return normalized


def _extract_technical_terms(title: str, limit: int = 3) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()
    for token in TECH_TERM_RE.findall(title or ""):
        lowered = token.lower()
        if lowered in TECH_TERM_STOPWORDS or len(token) < 6:
            continue
        if lowered in seen:
            continue
        seen.add(lowered)
        terms.append(token)
        if len(terms) >= limit:
            break
    return terms


def _ensure_english_terms(text: str, terms: list[str]) -> str:
    normalized = _clean_text(text)
    if not normalized or not terms:
        return normalized
    lower_text = normalized.lower()
    missing = [term for term in terms if term.lower() not in lower_text]
    if not missing:
        return normalized
    return _clean_text(f"{normalized} (영문 용어: {', '.join(missing[:2])})")


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


def _is_sentence_usable(text: str) -> bool:
    normalized = _clean_text(text)
    return bool(normalized) and not FORBIDDEN_SCRIPT_RE.search(normalized)


def _excerpt_sentences(excerpt: str) -> list[str]:
    cleaned = _clean_text(excerpt)
    if not cleaned:
        return []
    parts = re.split(r"(?<=[\.\!\?])\s+", cleaned)
    out: list[str] = []
    for part in parts:
        sentence = part.strip(" -")
        if len(sentence) < 20:
            continue
        if not _is_sentence_usable(sentence):
            continue
        out.append(sentence[:180])
        if len(out) >= 6:
            break
    return out


def _fallback_classify_news(item: Item) -> NewsClassification:
    text = f"{item.title} {item.summary_raw or ''}".lower()
    include = any(
        key in text
        for key in (
            "ai",
            "artificial intelligence",
            "model",
            "agent",
            "llm",
            "safety",
            "governance",
            "inference",
            "benchmark",
            "research",
            "api",
            "gpu",
            "paper",
            "robot",
            "vision-language",
        )
    )
    reason = (
        "AI 모델, 제품, 연구, 정책, 인프라 변화와 직접 연결된 항목으로 판단했습니다."
        if include
        else "AI 변화와 직접 연결된 신호가 약해서 이번 다이제스트에서는 제외했습니다."
    )
    return NewsClassification(include=include, reason_kr=reason)


def _build_news_points(item: Item, excerpt: str) -> list[str]:
    sentences = _excerpt_sentences(excerpt)
    if sentences:
        return [f"원문에서 확인된 핵심 내용: {sentence}" for sentence in sentences[:3]]

    return [
        f"{item.source_name}에서 '{item.title}' 관련 업데이트를 다뤘습니다.",
        "세부 내용은 원문 링크를 통해 추가 확인이 필요합니다.",
    ]


def _build_news_why(item: Item) -> list[str]:
    text = f"{item.title} {item.summary_raw or ''}".lower()
    reasons: list[str] = []
    if any(token in text for token in ("release", "launch", "api", "model", "agent", "gemini", "gpt", "claude")):
        reasons.append("새 모델·기능·API 변화는 실제 도입 속도와 생태계 경쟁 구도에 바로 영향을 줍니다.")
    if any(token in text for token in ("benchmark", "research", "paper", "evaluation")):
        reasons.append("연구·평가 결과는 다음 제품 발표와 기술 방향성을 미리 보여주는 신호입니다.")
    if any(token in text for token in ("policy", "regulation", "safety", "security", "governance")):
        reasons.append("정책·안전 이슈는 배포 범위와 기업 대응 전략을 바꿀 수 있는 변수입니다.")
    if not reasons:
        reasons.append("오늘 AI 흐름에서 제품, 연구, 커뮤니티 반응을 함께 읽을 수 있는 참고 신호입니다.")
    return reasons[:2]


def _build_keywords(text: str, fallback: list[str]) -> list[str]:
    keywords = re.findall(r"[A-Za-z0-9][A-Za-z0-9\-_\.]{2,}", text)
    stopwords = {
        "with",
        "from",
        "that",
        "this",
        "have",
        "will",
        "their",
        "today",
        "about",
        "more",
        "news",
    }
    picked: list[str] = []
    for token in keywords:
        lowered = token.lower()
        if lowered in stopwords or lowered in picked:
            continue
        picked.append(lowered)
        if len(picked) >= 6:
            return picked
    return fallback[:6]


def _fallback_news_summary(item: Item) -> NewsSummary:
    excerpt = _excerpt(item, max_chars=700)
    headline = f"{item.source_name}발 '{item.title}' 관련 AI 업데이트"
    points = _build_news_points(item, excerpt)
    why = _build_news_why(item)
    keywords = _build_keywords(
        f"{item.title} {excerpt}",
        fallback=["ai", "daily", "trend"],
    )
    return _validate_news_summary(
        NewsSummary(
            headline_kr=headline,
            what=points[:4],
            why_trend=why[:2],
            keywords=keywords[:6],
        ).model_dump(),
        title=item.title,
    )


def _infer_paper_domain(text: str) -> str:
    lowered = text.lower()
    mapping: list[tuple[tuple[str, ...], str]] = [
        (("agent", "planner", "tool use"), "에이전트"),
        (("robot", "embodied", "humanoid"), "로보틱스"),
        (("video", "diffusion"), "생성 모델"),
        (("multimodal", "vision-language", "vlm"), "멀티모달"),
        (("rag", "retrieval", "memory"), "검색 결합형 모델"),
        (("benchmark", "evaluation", "leaderboard"), "평가"),
        (("alignment", "safety", "hallucination", "factual"), "안전성과 신뢰성"),
    ]
    for keys, label in mapping:
        if any(key in lowered for key in keys):
            return label
    return "AI 연구"


def _infer_paper_contribution(text: str) -> str:
    lowered = text.lower()
    if any(key in lowered for key in ("benchmark", "leaderboard", "evaluation")):
        return "새 벤치마크 또는 평가 방법"
    if any(key in lowered for key in ("dataset", "corpus", "data generation")):
        return "새 데이터셋 또는 데이터 생성 방식"
    if any(key in lowered for key in ("framework", "system", "pipeline", "agent")):
        return "새 시스템 또는 프레임워크"
    if any(key in lowered for key in ("model", "architecture", "method", "approach")):
        return "새 모델 또는 방법론"
    return "새 연구 접근"


def _fallback_paper_summary(item: Item) -> PaperSummary:
    excerpt = _excerpt(item, max_chars=900)
    text = f"{item.title} {excerpt}"
    domain = _infer_paper_domain(text)
    contribution = _infer_paper_contribution(text)
    sentences = _excerpt_sentences(excerpt)

    one_liner = f"이 논문은 {domain} 영역에서 {contribution}을 제안하거나 검증하려는 연구입니다."

    details: list[str] = [
        f"문제의식은 {domain} 영역의 성능, 안정성, 또는 활용성을 개선하는 데 있습니다.",
        f"핵심 접근은 {contribution}을 통해 기존 한계를 줄이려는 것입니다.",
    ]
    if sentences:
        details.append(f"원문 초록 기준 핵심 설명: {sentences[0]}")
    if len(sentences) > 1:
        details.append(f"추가로 눈에 띄는 주장: {sentences[1]}")

    core_idea = " ".join(details[:4])
    keywords = _build_keywords(text, fallback=["ai", "paper", "research"])
    return _validate_paper_summary(
        PaperSummary(
            one_liner_kr=one_liner,
            core_idea_kr=core_idea,
            keywords=keywords[:6],
        ).model_dump(),
        title=item.title,
    )


def _validate_news_classification(raw: dict) -> NewsClassification:
    return NewsClassification.model_validate(raw)


def _validate_news_summary(raw: dict, title: str = "") -> NewsSummary:
    summary = NewsSummary.model_validate(raw)
    summary.headline_kr = _require_korean_text(summary.headline_kr, "headline_kr")
    summary.what = [_require_korean_text(w, "what") for w in summary.what if w and w.strip()][:4]
    summary.why_trend = [_require_korean_text(w, "why_trend") for w in summary.why_trend if w and w.strip()][:2]
    summary.keywords = [
        k.strip()
        for k in summary.keywords
        if k and k.strip() and not FORBIDDEN_SCRIPT_RE.search(k)
    ][:6]
    if not summary.keywords:
        summary.keywords = ["ai"]
    required_terms = _extract_technical_terms(title)
    if required_terms:
        combined = f"{summary.headline_kr} {' '.join(summary.what)}".lower()
        missing = [term for term in required_terms if term.lower() not in combined]
        if missing:
            if summary.what:
                summary.what[0] = _ensure_english_terms(summary.what[0], missing)
            else:
                summary.what = [f"원문 핵심 용어: {', '.join(missing[:2])}"]
    return summary


def _validate_paper_summary(raw: dict, title: str = "") -> PaperSummary:
    summary = PaperSummary.model_validate(raw)
    summary.one_liner_kr = _require_korean_text(summary.one_liner_kr, "one_liner_kr")
    summary.core_idea_kr = _require_korean_text(summary.core_idea_kr, "core_idea_kr")
    summary.keywords = [
        k.strip()
        for k in summary.keywords
        if k and k.strip() and not FORBIDDEN_SCRIPT_RE.search(k)
    ][:6]
    if not summary.keywords:
        summary.keywords = ["ai"]
    required_terms = _extract_technical_terms(title)
    if required_terms:
        combined = f"{summary.one_liner_kr} {summary.core_idea_kr}".lower()
        missing = [term for term in required_terms if term.lower() not in combined]
        if missing:
            summary.one_liner_kr = _ensure_english_terms(summary.one_liner_kr, missing)
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
                    summary = _validate_news_summary(cached.get("summary", {}), title=item.title)
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
                    summary = _validate_news_summary(backend.summarize_news(_payload(item)), title=item.title)
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
                summary = _validate_paper_summary(cached.get("summary", {}), title=item.title)
            except Exception:
                summary = None

        if summary is None:
            if backend is None:
                summary = _fallback_paper_summary(item)
            else:
                try:
                    summary = _validate_paper_summary(backend.summarize_paper(_payload(item)), title=item.title)
                except Exception as exc:
                    logger.warning("summarize_paper failed (%s): %s", item.url, exc)
                    summary = _fallback_paper_summary(item)

        paper_summaries[item.url] = summary
        cache_payloads[item.url] = {
            "kind": "paper",
            "summary": summary.model_dump(),
        }

    return included_news, news_summaries, paper_summaries, cache_payloads
