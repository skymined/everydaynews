from __future__ import annotations

import logging
import re
import threading
import time
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

try:
    import feedparser  # type: ignore
except Exception:  # pragma: no cover
    feedparser = None

try:
    import httpx  # type: ignore
except Exception:  # pragma: no cover
    httpx = None

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover
    BeautifulSoup = None  # type: ignore

from .models import DefaultsConfig, RawItem, SourceConfig
from .store import DigestStore

logger = logging.getLogger(__name__)

BLOCKED_HTML_LINK_HOSTS = {
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "www.gstatic.com",
    "gstatic.com",
}
BAD_LINK_SUFFIXES = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".css",
    ".js",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".xml",
)


class HostRateLimiter:
    def __init__(self, rps: float = 1.5) -> None:
        self.rps = max(rps, 0.1)
        self._min_interval = 1.0 / self.rps
        self._last_request: dict[str, float] = {}
        self._lock = threading.Lock()

    def wait(self, url: str) -> None:
        host = urlparse(url).netloc.lower()
        if not host:
            return
        with self._lock:
            now = time.monotonic()
            last = self._last_request.get(host, 0.0)
            delta = now - last
            if delta < self._min_interval:
                time.sleep(self._min_interval - delta)
                now = time.monotonic()
            self._last_request[host] = now


def _parse_datetime(raw: Any) -> datetime | None:
    if raw is None:
        return None
    if isinstance(raw, datetime):
        return raw if raw.tzinfo else raw.replace(tzinfo=UTC)
    if isinstance(raw, str):
        value = raw.strip()
        if not value:
            return None
        for parser in (datetime.fromisoformat, parsedate_to_datetime):
            try:
                dt = parser(value)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=UTC)
                return dt
            except Exception:
                pass
        return None
    if isinstance(raw, time.struct_time):
        try:
            return datetime(*raw[:6], tzinfo=UTC)
        except Exception:
            return None
    return None


def _http_get(
    url: str,
    defaults: DefaultsConfig,
    store: DigestStore,
    limiter: HostRateLimiter,
    include_cache_headers: bool = True,
) -> tuple[int, str, dict[str, str]]:
    limiter.wait(url)
    headers = {"User-Agent": defaults.user_agent}
    cached = store.get_http_cache(url) or {}
    if include_cache_headers:
        if cached.get("etag"):
            headers["If-None-Match"] = cached["etag"]
        if cached.get("last_modified"):
            headers["If-Modified-Since"] = cached["last_modified"]

    if httpx is not None:
        with httpx.Client(timeout=defaults.timeout_sec, follow_redirects=True) as client:
            resp = client.get(url, headers=headers)
            status = resp.status_code
            text = resp.text if status != 304 else ""
            resp_headers = {
                "etag": resp.headers.get("ETag", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
            }
    else:
        req = Request(url, headers=headers)  # noqa: S310
        try:
            with urlopen(req, timeout=defaults.timeout_sec) as resp:  # noqa: S310
                status = getattr(resp, "status", 200)
                text = resp.read().decode("utf-8", errors="replace")
                resp_headers = {
                    "etag": resp.headers.get("ETag", ""),
                    "last_modified": resp.headers.get("Last-Modified", ""),
                }
        except Exception as exc:
            status = 500
            text = ""
            resp_headers = {}
            logger.warning("HTTP fallback request failed for %s: %s", url, exc)

    if resp_headers.get("etag") or resp_headers.get("last_modified"):
        store.upsert_http_cache(
            url, etag=resp_headers.get("etag"), last_modified=resp_headers.get("last_modified")
        )
    return status, text, resp_headers


def _parse_rss_items(
    xml_text: str,
    source: SourceConfig,
    max_items: int,
    fetched_at: datetime,
) -> list[RawItem]:
    items: list[RawItem] = []
    if feedparser is None:
        import xml.etree.ElementTree as ET

        root = ET.fromstring(xml_text)
        entries = root.findall(".//item")
        for entry in entries[:max_items]:
            title = (entry.findtext("title") or "").strip()
            link = (entry.findtext("link") or "").strip()
            pub = _parse_datetime(entry.findtext("pubDate"))
            desc = (entry.findtext("description") or "").strip()
            if not title or not link:
                continue
            items.append(
                RawItem(
                    source_id=source.id,
                    source_name=source.name,
                    title=title,
                    url=link,
                    published_at=pub,
                    fetched_at=fetched_at,
                    summary_raw=desc[:2000] if desc else None,
                )
            )
        return items

    parsed = feedparser.parse(xml_text)
    for entry in parsed.entries[:max_items]:
        title = str(getattr(entry, "title", "")).strip()
        link = str(getattr(entry, "link", "")).strip()
        published = None
        for candidate in (
            getattr(entry, "published", None),
            getattr(entry, "updated", None),
            getattr(entry, "published_parsed", None),
            getattr(entry, "updated_parsed", None),
        ):
            published = _parse_datetime(candidate)
            if published:
                break
        summary_raw = str(getattr(entry, "summary", "")).strip() or None
        author = str(getattr(entry, "author", "")).strip() or None
        if not title or not link:
            continue
        items.append(
            RawItem(
                source_id=source.id,
                source_name=source.name,
                title=title,
                url=link,
                published_at=published,
                fetched_at=fetched_at,
                author=author,
                summary_raw=summary_raw[:2000] if summary_raw else None,
            )
        )
    return items


def _extract_text_from_element(node: Any, selector: str) -> str:
    if BeautifulSoup is None:
        return ""
    if not selector:
        return ""
    target = node.select_one(selector)
    if not target:
        return ""
    return target.get_text(" ", strip=True)


def _is_candidate_link(url: str, source_url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    host = parsed.netloc.lower()
    source_host = urlparse(source_url).netloc.lower()
    if host in BLOCKED_HTML_LINK_HOSTS:
        return False
    if source_host and not (host == source_host or host.endswith(f".{source_host}")):
        return False
    if parsed.path.lower().endswith(BAD_LINK_SUFFIXES):
        return False
    return True


def _extract_link_from_element(
    node: Any,
    selector: str,
    base_url: str,
    title_selector: str = "",
) -> str:
    if BeautifulSoup is None:
        return ""
    target = None
    if title_selector:
        title_node = node.select_one(title_selector)
        if title_node:
            target = title_node.find("a")
    if target is None:
        target = node.select_one(selector) if selector else node.find("a")
    if not target:
        return ""
    href = target.get("href") if hasattr(target, "get") else None
    if not href:
        return ""
    return urljoin(base_url, str(href).strip())


def _parse_html_items(
    html_text: str,
    source: SourceConfig,
    max_items: int,
    fetched_at: datetime,
) -> list[RawItem]:
    if BeautifulSoup is None:
        return _fallback_html_items(html_text, source, max_items, fetched_at)

    soup = BeautifulSoup(html_text, "lxml")
    selectors = source.selectors or {}
    item_selector = selectors.get("item", "")
    title_selector = selectors.get("title", "")
    link_selector = selectors.get("link", "a")
    results: list[RawItem] = []

    if source.id == "hf_papers_today":
        seen_hf_urls: set[str] = set()
        for tag in soup.select("a[href^='/papers/']"):
            href = tag.get("href")
            text = tag.get_text(" ", strip=True)
            if not href or not text:
                continue
            if "#" in href:
                continue
            if text.lower() in {"daily papers", "papers"}:
                continue
            url = urljoin(str(source.url), href)
            if not _is_candidate_link(url, str(source.url)):
                continue
            if "/papers/date/" in url or url.endswith("/papers/trending"):
                continue
            if url in seen_hf_urls:
                continue
            seen_hf_urls.add(url)
            results.append(
                RawItem(
                    source_id=source.id,
                    source_name=source.name,
                    title=text,
                    url=url,
                    published_at=None,
                    fetched_at=fetched_at,
                )
            )
            if len(results) >= max_items:
                break
        if results:
            return results[:max_items]

    item_nodes = soup.select(item_selector) if item_selector else soup.find_all("article")
    for node in item_nodes:
        title = _extract_text_from_element(node, title_selector) if title_selector else ""
        if not title:
            title_link = _extract_link_from_element(
                node, link_selector, str(source.url), title_selector=title_selector
            )
            if title_link and hasattr(node, "select_one"):
                title_anchor = node.select_one(f"{title_selector} a") if title_selector else None
                if title_anchor and hasattr(title_anchor, "get_text"):
                    title = title_anchor.get_text(" ", strip=True)
        if not title:
            if hasattr(node, "get_text"):
                title = node.get_text(" ", strip=True)
        link = _extract_link_from_element(
            node,
            link_selector,
            str(source.url),
            title_selector=title_selector,
        )
        if link and not _is_candidate_link(link, str(source.url)):
            continue
        if not title or not link:
            continue
        summary_raw = ""
        if hasattr(node, "get_text"):
            summary_raw = node.get_text(" ", strip=True)
        results.append(
            RawItem(
                source_id=source.id,
                source_name=source.name,
                title=title[:300],
                url=link,
                published_at=None,
                fetched_at=fetched_at,
                summary_raw=summary_raw[:2000] if summary_raw else None,
            )
        )
        if len(results) >= max_items:
            break

    if not results:
        return _fallback_html_items(html_text, source, max_items, fetched_at)
    return _dedupe_preserve_order(results, max_items)


def _fallback_html_items(
    html_text: str,
    source: SourceConfig,
    max_items: int,
    fetched_at: datetime,
) -> list[RawItem]:
    links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html_text, flags=re.IGNORECASE)
    titles = re.findall(r"<title>(.*?)</title>", html_text, flags=re.IGNORECASE | re.DOTALL)
    base_title = re.sub(r"\s+", " ", titles[0]).strip() if titles else source.name
    results: list[RawItem] = []
    for href in links:
        if href.startswith("#"):
            continue
        if href.startswith("javascript:"):
            continue
        url = urljoin(str(source.url), href)
        if not _is_candidate_link(url, str(source.url)):
            continue
        if source.id == "hf_papers_today" and "/papers/" not in url:
            continue
        results.append(
            RawItem(
                source_id=source.id,
                source_name=source.name,
                title=base_title,
                url=url,
                published_at=None,
                fetched_at=fetched_at,
            )
        )
        if len(results) >= max_items:
            break
    return _dedupe_preserve_order(results, max_items)


def _dedupe_preserve_order(items: list[RawItem], limit: int) -> list[RawItem]:
    seen: set[str] = set()
    out: list[RawItem] = []
    for item in items:
        if item.url in seen:
            continue
        seen.add(item.url)
        out.append(item)
        if len(out) >= limit:
            break
    return out


def _apply_source_keyword_filters(items: list[RawItem], source: SourceConfig) -> list[RawItem]:
    include = [k.lower() for k in source.include_keywords if k.strip()]
    exclude = [k.lower() for k in source.exclude_keywords if k.strip()]
    if not include and not exclude:
        return items

    filtered: list[RawItem] = []
    for item in items:
        title_text = item.title.lower()
        full_text = f"{item.title} {item.summary_raw or ''}".lower()
        if include and not any(keyword in title_text for keyword in include):
            continue
        if exclude and any(keyword in full_text for keyword in exclude):
            continue
        filtered.append(item)
    return filtered


def fetch_source(
    source: SourceConfig,
    defaults: DefaultsConfig,
    store: DigestStore,
    limiter: HostRateLimiter,
    max_items_override: int | None = None,
) -> list[RawItem]:
    fetched_at = datetime.now(UTC)
    max_items = max_items_override or source.max_items or defaults.max_items_per_source
    status, text, _ = _http_get(str(source.url), defaults=defaults, store=store, limiter=limiter)

    if status == 304:
        logger.info("Not modified (ETag/Last-Modified): %s, fallback to full fetch", source.id)
        status, text, _ = _http_get(
            str(source.url),
            defaults=defaults,
            store=store,
            limiter=limiter,
            include_cache_headers=False,
        )
    if status >= 400:
        logger.warning("Fetch failed %s (%s): status=%s", source.id, source.url, status)
        return []
    if not text.strip():
        logger.warning("Empty response: %s", source.id)
        return []

    try:
        if source.type == "rss":
            parsed = _parse_rss_items(text, source, max_items, fetched_at)
        else:
            parsed = _parse_html_items(text, source, max_items, fetched_at)
        return _apply_source_keyword_filters(parsed, source)
    except Exception as exc:  # pragma: no cover
        logger.exception("Parse failed for %s: %s", source.id, exc)
        return []
