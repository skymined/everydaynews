from __future__ import annotations

from datetime import date

from .models import Item, NewsSummary, PaperSummary

SIGNAL_PREFIXES = ("google_news_", "reddit_")


def _is_signal_item(item: Item) -> bool:
    source_id = item.source_id.lower()
    source_name = item.source_name.lower()
    return source_id.startswith(SIGNAL_PREFIXES) or "reddit" in source_name or "google news" in source_name


def _normalize_sentence(text: str) -> str:
    value = " ".join((text or "").split()).strip()
    if not value:
        return ""
    if value[-1] not in ".!?":
        value = f"{value}."
    return value


def _join_sentences(parts: list[str], limit: int) -> str:
    picked: list[str] = []
    for part in parts:
        sentence = _normalize_sentence(part)
        if not sentence:
            continue
        picked.append(sentence)
        if len(picked) >= limit:
            break
    return " ".join(picked)


def _lead_paragraph(
    target_date: date,
    news_items: list[Item],
    signal_items: list[Item],
    paper_items: list[Item],
) -> str:
    pieces: list[str] = [f"{target_date.isoformat()} AI 브리핑입니다."]
    if news_items:
        top_sources = ", ".join(item.source_name for item in news_items[:3])
        pieces.append(f"오늘은 {top_sources}에서 나온 업데이트를 중심으로 흐름을 정리했습니다.")
    if signal_items:
        pieces.append("공식 발표만이 아니라 검색과 커뮤니티에서 어떤 이야기가 같이 올라오는지도 함께 묶었습니다.")
    if paper_items:
        pieces.append(f"Hugging Face에서 집계한 최신 인기 논문 {len(paper_items)}편도 함께 덧붙였습니다.")
    return " ".join(pieces)


def _format_keywords(keywords: list[str]) -> str:
    cleaned: list[str] = []
    seen: set[str] = set()
    for keyword in keywords:
        value = " ".join((keyword or "").split()).strip()
        if not value:
            continue
        lowered = value.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        cleaned.append(value)
        if len(cleaned) >= 4:
            break
    return " · ".join(f"`{keyword}`" for keyword in cleaned)


def _briefing_notes(
    target_date: date,
    official_news: list[Item],
    signal_news: list[Item],
    paper_items: list[Item],
) -> list[str]:
    notes: list[str] = []
    if official_news:
        top_sources = ", ".join(item.source_name for item in official_news[:3])
        notes.append(f"**핵심 흐름:** {top_sources}에서 확인된 제품, 연구, 인프라 변화를 먼저 배치했습니다.")
    if signal_news:
        notes.append(f"**현장 신호:** 커뮤니티와 검색에서 함께 떠오른 항목 {len(signal_news)}개를 별도 섹션으로 묶었습니다.")
    if paper_items:
        notes.append(f"**논문 큐:** Hugging Face 인기 논문 {len(paper_items)}편을 방법과 의미 중심으로 압축했습니다.")
    if not notes:
        notes.append(f"**발행 기준:** {target_date.isoformat()}에 수집된 항목을 짧은 브리핑 형식으로 정리했습니다.")
    return notes


def _render_news_item(lines: list[str], item: Item, summary: NewsSummary) -> None:
    what = _join_sentences(summary.what, limit=3) or "원문을 기반으로 핵심 내용을 정리 중입니다."
    why = _join_sentences(summary.why_trend, limit=1)
    keywords = _format_keywords(summary.keywords)

    lines.append(f"### [{summary.headline_kr}]({item.url})")
    lines.append("")
    lines.append(f"- **핵심:** {what}")
    if why:
        lines.append(f"- **맥락:** {why}")
    lines.append(f"- **출처:** {item.source_name}")
    if keywords:
        lines.append(f"- **키워드:** {keywords}")
    lines.append("")


def _render_paper_item(lines: list[str], index: int, item: Item, summary: PaperSummary) -> None:
    one_liner = _normalize_sentence(summary.one_liner_kr)
    core_idea = _normalize_sentence(summary.core_idea_kr)
    keywords = _format_keywords(summary.keywords)
    lines.append(f"### {index}. [{item.title}]({item.url})")
    lines.append("")
    if one_liner:
        lines.append(f"- **한 줄:** {one_liner}")
    if core_idea:
        lines.append(f"- **아이디어:** {core_idea}")
    lines.append(f"- **출처:** {item.source_name}")
    if keywords:
        lines.append(f"- **키워드:** {keywords}")
    lines.append("")


def render_digest_markdown(
    *,
    target_date: date,
    kst_date: date,
    news_items: list[Item],
    paper_items: list[Item],
    news_summaries: dict[str, NewsSummary],
    paper_summaries: dict[str, PaperSummary],
) -> str:
    lines: list[str] = []
    lines.append(f"# IMDIGEST - {target_date.isoformat()}")
    lines.append("")
    lines.append(f"> {kst_date.isoformat()} KST 기준 수집. AI 제품, 연구, 인프라, 커뮤니티 신호를 짧게 읽히는 브리핑으로 정리했습니다.")
    lines.append("")

    official_news = [item for item in news_items if not _is_signal_item(item)]
    signal_news = [item for item in news_items if _is_signal_item(item)]

    lines.append(_lead_paragraph(target_date, official_news, signal_news, paper_items))
    lines.append("")

    lines.append("## 브리핑 노트")
    lines.append("")
    for note in _briefing_notes(target_date, official_news, signal_news, paper_items):
        lines.append(f"- {note}")
    lines.append("")

    lines.append("## 주요 뉴스")
    lines.append("")
    if not official_news:
        lines.append("오늘은 이 섹션에 담을 공식 발표형 뉴스가 많지 않았습니다.")
        lines.append("")
    else:
        for item in official_news:
            summary = news_summaries.get(item.url)
            if summary is None:
                continue
            _render_news_item(lines, item, summary)

    if signal_news:
        lines.append("## 커뮤니티 시그널")
        lines.append("")
        lines.append("공식 발표와 함께 사람들의 반응이나 현장성 있는 문제의식이 보인 항목만 따로 모았습니다.")
        lines.append("")
        for item in signal_news:
            summary = news_summaries.get(item.url)
            if summary is None:
                continue
            _render_news_item(lines, item, summary)

    lines.append("## 오늘의 논문")
    lines.append("")
    if not paper_items:
        lines.append("오늘 반영할 Hugging Face 논문 목록은 아직 충분히 열리지 않았습니다.")
        lines.append("")
    else:
        lines.append("Hugging Face 인기 논문 목록을 바탕으로, 오늘 눈에 띄는 논문들을 짧게 읽을 수 있게 정리했습니다.")
        lines.append("")
        for index, item in enumerate(paper_items, start=1):
            summary = paper_summaries.get(item.url)
            if summary is None:
                continue
            _render_paper_item(lines, index, item, summary)

    return "\n".join(lines).strip() + "\n"
