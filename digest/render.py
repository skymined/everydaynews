from __future__ import annotations

from datetime import date

from .models import Item, NewsSummary, PaperSummary


def _render_tags(tags: list[str]) -> str:
    clean = []
    seen: set[str] = set()
    for tag in tags:
        token = tag.strip().lower().replace(" ", "-")
        if not token or token in seen:
            continue
        seen.add(token)
        clean.append(f"#{token}")
    return " ".join(clean[:6]) if clean else "#ai"


def render_digest_markdown(
    *,
    target_date: date,
    kst_yesterday: date,
    news_items: list[Item],
    paper_items: list[Item],
    news_summaries: dict[str, NewsSummary],
    paper_summaries: dict[str, PaperSummary],
) -> str:
    lines: list[str] = []
    lines.append(f"# IMDIGEST - {target_date.isoformat()}")
    lines.append("")
    lines.append(f"- 기준일(KST): {kst_yesterday.isoformat()} 00:00:00 ~ 23:59:59")
    lines.append("")

    lines.append("## AI News")
    lines.append("")
    if not news_items:
        lines.append("- 어제자 기준으로 트렌드 포함 뉴스가 없습니다.")
        lines.append("")
    else:
        for item in news_items:
            summary = news_summaries.get(item.url)
            if summary is None:
                continue
            unknown_mark = " (게시일 불명)" if item.published_unknown else ""
            lines.append(f"### {summary.headline_kr}{unknown_mark}")
            lines.append("  - 내용 요약")
            for point in summary.what[:4]:
                lines.append(f"    - {point}")
            lines.append(f"  - 링크: {item.url}")
            lines.append("")

    lines.append("## Papers (Hugging Face Top 10)")
    lines.append("")
    if not paper_items:
        lines.append("- Hugging Face Top 10 논문을 가져오지 못했습니다.")
        lines.append("")
    else:
        for item in paper_items:
            summary = paper_summaries.get(item.url)
            if summary is None:
                continue
            lines.append(f"### {item.title}")
            lines.append(f"- 한 줄 요약: {summary.one_liner_kr}")
            lines.append(f"- 핵심 아이디어: {summary.core_idea_kr}")
            lines.append(f"- 키워드: {_render_tags(summary.keywords)}")
            lines.append(f"- 링크: {item.url}")
            lines.append("")

    return "\n".join(lines).strip() + "\n"