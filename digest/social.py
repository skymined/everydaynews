from __future__ import annotations

import logging
import os
import re
from datetime import UTC, datetime
from typing import Any

import httpx

from .models import DefaultsConfig, RawItem

logger = logging.getLogger(__name__)

DEFAULT_X_QUERY = (
    '(AI OR "artificial intelligence" OR LLM OR OpenAI OR Anthropic OR Gemini OR Claude '
    'OR NVIDIA OR DeepSeek OR agents OR robotics) lang:en -is:retweet'
)


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip()


def _title_from_text(text: str, limit: int = 110) -> str:
    cleaned = _clean_text(text)
    if len(cleaned) <= limit:
        return cleaned or "Untitled post"
    return cleaned[: limit - 1].rstrip() + "…"


def _parse_datetime(raw: str | None) -> datetime | None:
    if not raw:
        return None
    try:
        value = raw.replace("Z", "+00:00")
        if re.search(r"[+-]\d{4}$", value):
            value = f"{value[:-5]}{value[-5:-2]}:{value[-2:]}"
        dt = datetime.fromisoformat(value)
        return dt if dt.tzinfo else dt.replace(tzinfo=UTC)
    except ValueError:
        return None


def _to_int(value: str | None, default: int) -> int:
    try:
        return int(value or default)
    except ValueError:
        return default


def _parse_x_response(payload: dict[str, Any]) -> list[RawItem]:
    users = {
        str(user.get("id")): user
        for user in payload.get("includes", {}).get("users", [])
        if isinstance(user, dict) and user.get("id")
    }

    items: list[RawItem] = []
    fetched_at = datetime.now(UTC)
    for entry in payload.get("data", []):
        if not isinstance(entry, dict):
            continue
        post_id = str(entry.get("id") or "").strip()
        text = _clean_text(str(entry.get("text") or ""))
        if not post_id or not text:
            continue

        author = users.get(str(entry.get("author_id") or ""))
        username = str((author or {}).get("username") or "").strip()
        source_name = f"X @{username}" if username else "X"
        url = f"https://x.com/{username}/status/{post_id}" if username else f"https://x.com/i/web/status/{post_id}"

        items.append(
            RawItem(
                source_id="x_search",
                source_name=source_name,
                title=_title_from_text(text),
                url=url,
                published_at=_parse_datetime(str(entry.get("created_at") or "")),
                fetched_at=fetched_at,
                author=username or None,
                summary_raw=text,
            )
        )
    return items


def _parse_threads_response(payload: dict[str, Any]) -> list[RawItem]:
    items: list[RawItem] = []
    fetched_at = datetime.now(UTC)
    for entry in payload.get("data", []):
        if not isinstance(entry, dict):
            continue
        permalink = str(entry.get("permalink") or "").strip()
        text = _clean_text(str(entry.get("text") or ""))
        if not permalink or not text:
            continue

        username = str(entry.get("username") or "").strip()
        source_name = f"Threads @{username}" if username else "Threads"
        items.append(
            RawItem(
                source_id="threads_recent",
                source_name=source_name,
                title=_title_from_text(text),
                url=permalink,
                published_at=_parse_datetime(str(entry.get("timestamp") or "")),
                fetched_at=fetched_at,
                author=username or None,
                summary_raw=text,
            )
        )
    return items


def _fetch_x_items(defaults: DefaultsConfig) -> list[RawItem]:
    bearer = os.getenv("X_BEARER_TOKEN", "").strip()
    if not bearer:
        return []

    query = os.getenv("X_SEARCH_QUERY", "").strip() or DEFAULT_X_QUERY
    max_results = max(10, min(_to_int(os.getenv("X_MAX_RESULTS"), 15), 50))
    params = {
        "query": query,
        "max_results": max_results,
        "sort_order": "recency",
        "tweet.fields": "created_at,author_id,lang",
        "expansions": "author_id",
        "user.fields": "name,username",
    }
    headers = {
        "Authorization": f"Bearer {bearer}",
        "User-Agent": defaults.user_agent,
    }

    try:
        with httpx.Client(timeout=defaults.timeout_sec, follow_redirects=True) as client:
            response = client.get("https://api.x.com/2/tweets/search/recent", params=params, headers=headers)
            response.raise_for_status()
        return _parse_x_response(response.json())
    except Exception as exc:  # pragma: no cover - network dependent
        logger.warning("X fetch failed: %s", exc)
        return []


def _fetch_threads_items(defaults: DefaultsConfig) -> list[RawItem]:
    access_token = os.getenv("THREADS_ACCESS_TOKEN", "").strip()
    if not access_token:
        return []

    max_results = max(5, min(_to_int(os.getenv("THREADS_MAX_RESULTS"), 10), 25))
    params = {
        "fields": "id,text,timestamp,permalink,username",
        "limit": max_results,
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "User-Agent": defaults.user_agent,
    }

    try:
        with httpx.Client(timeout=defaults.timeout_sec, follow_redirects=True) as client:
            response = client.get("https://graph.threads.net/v1.0/me/threads", params=params, headers=headers)
            response.raise_for_status()
        return _parse_threads_response(response.json())
    except Exception as exc:  # pragma: no cover - network dependent
        logger.warning("Threads fetch failed: %s", exc)
        return []


def fetch_social_items(defaults: DefaultsConfig) -> list[RawItem]:
    items: list[RawItem] = []
    items.extend(_fetch_x_items(defaults))
    items.extend(_fetch_threads_items(defaults))
    return items
