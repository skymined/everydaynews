from __future__ import annotations

import argparse
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from .config import load_config, load_prompt
from .dedupe import normalize_url
from .extract import extract_main_text
from .fetch import HostRateLimiter, fetch_source
from .llm import create_backend
from .models import Item, RawItem, SourceConfig
from .render import render_digest_markdown
from .store import DigestStore
from .summarize import rank_items, summarize_with_llm

logger = logging.getLogger(__name__)


def _today_kst() -> str:
    return datetime.now(ZoneInfo("Asia/Seoul")).date().isoformat()


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI Trend Digest runner")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run = subparsers.add_parser("run", help="Run digest pipeline")
    run.add_argument("--date", dest="target_date", default=_today_kst())
    run.add_argument("--out", default="")
    run.add_argument("--provider", choices=["openai", "gemini"], default="")
    run.add_argument("--max-items", type=int, default=0, help="Per source override")
    run.add_argument("--skip-llm", action="store_true")
    run.add_argument(
        "--window",
        choices=["yesterday-kst", "since-hours"],
        default="yesterday-kst",
        help="Default is yesterday KST window.",
    )
    run.add_argument("--since-hours", type=int, default=36)
    run.add_argument("--refresh", action="store_true", help="Ignore cached summaries and regenerate.")
    run.add_argument("--config", default="sources.yaml")
    run.add_argument("--db-path", default="data/digest.sqlite3")
    run.add_argument("--latest-path", default="website/reports/latest.md")
    run.add_argument("--log-level", default="INFO")
    return parser


def _to_item(raw: RawItem) -> Item:
    return Item(
        source_id=raw.source_id,
        source_name=raw.source_name,
        title=raw.title,
        url=normalize_url(raw.url),
        published_at=raw.published_at,
        fetched_at=raw.fetched_at,
        author=raw.author,
        summary_raw=raw.summary_raw,
    )


def _extract_for_items(items: list[Item], timeout_sec: int, user_agent: str, max_chars: int) -> None:
    def _task(item: Item) -> tuple[str, str]:
        text = extract_main_text(
            item.url,
            timeout_sec=timeout_sec,
            user_agent=user_agent,
            max_chars=max_chars,
        )
        return item.url, text

    with ThreadPoolExecutor(max_workers=6) as pool:
        future_map = {pool.submit(_task, item): item for item in items}
        for future in as_completed(future_map):
            item = future_map[future]
            try:
                url, text = future.result()
                if url == item.url:
                    item.content_text = text
            except Exception as exc:
                logger.warning("Extract failed for %s: %s", item.url, exc)


def _fetch_all_sources(
    sources: list[SourceConfig],
    cfg,
    store: DigestStore,
    max_items_override: int,
) -> list[RawItem]:
    limiter = HostRateLimiter(rps=cfg.defaults.host_rps)
    logger.info("Fetch start: %s sources", len(sources))

    raw_items: list[RawItem] = []
    with ThreadPoolExecutor(max_workers=cfg.defaults.concurrency) as pool:
        future_map = {
            pool.submit(
                fetch_source,
                source=source,
                defaults=cfg.defaults,
                store=store,
                limiter=limiter,
                max_items_override=max_items_override if max_items_override > 0 else None,
            ): source
            for source in sources
        }
        for future in as_completed(future_map):
            source = future_map[future]
            try:
                source_items = future.result()
                raw_items.extend(source_items)
                logger.info("Fetched %s items from %s", len(source_items), source.id)
            except Exception as exc:
                logger.warning("Fetch failed for %s: %s", source.id, exc)
    return raw_items


def _dedupe_current_run(items: list[Item], store: DigestStore) -> list[Item]:
    seen_urls: set[str] = set()
    deduped: list[Item] = []
    for item in items:
        if item.url in seen_urls:
            continue
        seen_urls.add(item.url)
        store.mark_seen(item.url, source_id=item.source_id)
        deduped.append(item)
    return deduped


def _split_items_by_window(
    items: list[Item],
    target_date: date,
    window: str,
    since_hours: int,
    timezone_name: str,
) -> tuple[list[Item], list[Item], date]:
    tz = ZoneInfo(timezone_name)
    yesterday = target_date - timedelta(days=1)
    start = datetime.combine(yesterday, time.min, tzinfo=tz)
    end = datetime.combine(yesterday, time.max, tzinfo=tz)

    papers: list[Item] = []
    news: list[Item] = []
    cutoff = datetime.now(UTC) - timedelta(hours=since_hours)

    for item in items:
        if item.source_id == "hf_papers_today":
            papers.append(item)
            continue
        if item.source_id.startswith("arxiv_"):
            continue

        if window == "since-hours":
            ref_time = item.published_at or item.fetched_at
            if ref_time >= cutoff:
                news.append(item)
            continue

        if item.published_at is not None:
            published_kst = item.published_at.astimezone(tz)
            if start <= published_kst <= end:
                news.append(item)
            continue

        fetched_kst = item.fetched_at.astimezone(tz)
        if start <= fetched_kst <= end:
            unknown_item = item.model_copy()
            unknown_item.published_unknown = True
            news.append(unknown_item)

    return news, papers, yesterday


def run_pipeline(args: argparse.Namespace) -> int:
    cfg = load_config(args.config)
    classify_prompt = load_prompt("prompts/news_classify.md")
    news_prompt = load_prompt("prompts/news_summarize.md")
    paper_prompt = load_prompt("prompts/paper_summarize.md")

    target_date = datetime.fromisoformat(args.target_date).date()
    out_path = Path(args.out) if args.out else Path(f"website/reports/{target_date.isoformat()}.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    latest_path = Path(args.latest_path)
    latest_path.parent.mkdir(parents=True, exist_ok=True)

    store = DigestStore(args.db_path)
    all_sources = list(cfg.sources) + list(cfg.watch_sites)
    raw_items = _fetch_all_sources(
        sources=all_sources,
        cfg=cfg,
        store=store,
        max_items_override=args.max_items,
    )
    items = _dedupe_current_run([_to_item(raw) for raw in raw_items], store=store)
    logger.info("Items after dedupe(current run): %s", len(items))

    news_candidates, paper_candidates, kst_yesterday = _split_items_by_window(
        items=items,
        target_date=target_date,
        window=args.window,
        since_hours=args.since_hours,
        timezone_name=cfg.report.timezone,
    )
    logger.info("News candidates: %s | Paper candidates: %s", len(news_candidates), len(paper_candidates))

    ranked_news = rank_items(news_candidates, scoring=cfg.scoring)
    news_pool = ranked_news[: cfg.llm.max_items_to_summarize]
    selected_papers = paper_candidates[: cfg.report.max_papers]

    extract_targets = news_pool + selected_papers
    _extract_for_items(
        extract_targets,
        timeout_sec=cfg.defaults.timeout_sec,
        user_agent=cfg.defaults.user_agent,
        max_chars=cfg.defaults.extract_max_chars,
    )

    backend = None
    if not args.skip_llm:
        backend = create_backend(
            provider_override=args.provider,
            cfg=cfg,
            classify_prompt=classify_prompt,
            news_prompt=news_prompt,
            paper_prompt=paper_prompt,
        )
    included_news, news_summaries, paper_summaries, cache_payloads = summarize_with_llm(
        news_items=news_pool,
        paper_items=selected_papers,
        backend=backend,
        store=store,
        refresh=args.refresh,
    )
    selected_news = included_news[: cfg.report.max_news_items]

    markdown = render_digest_markdown(
        target_date=target_date,
        kst_yesterday=kst_yesterday,
        news_items=selected_news,
        paper_items=selected_papers,
        news_summaries=news_summaries,
        paper_summaries=paper_summaries,
    )
    out_path.write_text(markdown, encoding="utf-8")
    latest_path.write_text(markdown, encoding="utf-8")
    logger.info("Digest written: %s", out_path)

    for item in news_pool + selected_papers:
        store.upsert_item(item, cache_payloads.get(item.url))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=getattr(logging, str(args.log_level).upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )
    if args.command == "run":
        return run_pipeline(args)
    parser.print_help()
    return 1
