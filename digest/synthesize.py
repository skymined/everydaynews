from __future__ import annotations

import logging
from collections import defaultdict

from .models import DaySynthesis, DayTheme, Item, ItemSummary

logger = logging.getLogger(__name__)


def build_day_payload(items: list[Item], summaries: dict[str, ItemSummary]) -> list[dict]:
    payload: list[dict] = []
    for item in items:
        summary = summaries.get(item.url)
        if not summary:
            continue
        payload.append(
            {
                "source": item.source_name,
                "title": item.title,
                "url": item.url,
                "one_liner": summary.one_liner,
                "why_it_matters": summary.why_it_matters,
                "tags": summary.tags,
                "key_terms": summary.key_terms,
                "confidence": summary.confidence,
                "unknowns": summary.unknowns,
            }
        )
    return payload


def _fallback_synthesis(items: list[Item], summaries: dict[str, ItemSummary]) -> DaySynthesis:
    bucket: dict[str, list[tuple[Item, ItemSummary]]] = defaultdict(list)
    tldr: list[str] = []
    for item in items:
        summary = summaries.get(item.url)
        if not summary:
            continue
        tag = summary.tags[0] if summary.tags else "general"
        bucket[tag].append((item, summary))
        if len(tldr) < 5:
            tldr.append(f"{summary.one_liner} ({item.source_name})")

    themes: list[DayTheme] = []
    for tag, grouped in sorted(bucket.items(), key=lambda kv: len(kv[1]), reverse=True)[:5]:
        supporting = [item.url for item, _ in grouped[:6]]
        terms = []
        for _, summary in grouped:
            terms.extend(summary.key_terms[:2])
        watchlist = sorted({term for term in terms if term})[:5]
        followups = []
        for _, summary in grouped:
            followups.extend(summary.followup_queries[:2])
        dedup_followups = []
        seen: set[str] = set()
        for query in followups:
            if query in seen:
                continue
            seen.add(query)
            dedup_followups.append(query)
            if len(dedup_followups) >= 5:
                break
        themes.append(
            DayTheme(
                theme=f"{tag.title()} momentum",
                narrative=f"{tag} 관련 항목이 복수 소스에서 반복 관측되었습니다.",
                why_now="최근 게시물 빈도 증가와 공식 채널 업데이트가 동시에 나타났습니다.",
                supporting_items=supporting,
                implications="1~3개월 내 제품 전략/연구 우선순위/조달 계획에 영향 가능성이 있습니다.",
                watchlist=watchlist or ["official release notes", "benchmarks", "pricing"],
                followup_queries=dedup_followups
                or [f"{tag} AI trend validation", f"{tag} production case study"],
            )
        )
    return DaySynthesis(tldr=tldr[:5], themes=themes)


def synthesize_day(
    items: list[Item],
    summaries: dict[str, ItemSummary],
    provider: object | None = None,
) -> DaySynthesis:
    payload = build_day_payload(items, summaries)
    if provider is None:
        return _fallback_synthesis(items, summaries)

    try:
        result = provider.synthesize_day({"items": payload})
        return DaySynthesis.model_validate(result)
    except Exception as exc:
        logger.warning("LLM day synthesis failed: %s", exc)
        return _fallback_synthesis(items, summaries)

