from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterator

from pydantic import BaseModel

from .dedupe import hash_url, normalize_url
from .models import Item


class DigestStore:
    def __init__(self, db_path: str | Path = "data/digest.sqlite3") -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    @contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA foreign_keys=ON;")
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS seen (
                    url_hash TEXT PRIMARY KEY,
                    url TEXT NOT NULL,
                    first_seen_at TEXT NOT NULL,
                    last_seen_at TEXT NOT NULL,
                    source_id TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    item_id TEXT PRIMARY KEY,
                    url_hash TEXT NOT NULL,
                    source_id TEXT NOT NULL,
                    source_name TEXT NOT NULL,
                    title TEXT NOT NULL,
                    url TEXT NOT NULL,
                    published_at TEXT,
                    fetched_at TEXT NOT NULL,
                    json_summary TEXT,
                    json_item TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS http_cache (
                    url TEXT PRIMARY KEY,
                    etag TEXT,
                    last_modified TEXT,
                    updated_at TEXT NOT NULL
                )
                """
            )

    def is_seen(self, url: str) -> bool:
        url_hash = hash_url(url)
        with self._connect() as conn:
            row = conn.execute(
                "SELECT 1 FROM seen WHERE url_hash = ? LIMIT 1", (url_hash,)
            ).fetchone()
            return row is not None

    def mark_seen(self, url: str, source_id: str) -> None:
        normalized = normalize_url(url)
        url_hash = hash_url(normalized)
        now = datetime.now(UTC).isoformat()
        with self._connect() as conn:
            existing = conn.execute(
                "SELECT url_hash FROM seen WHERE url_hash = ? LIMIT 1", (url_hash,)
            ).fetchone()
            if existing:
                conn.execute(
                    """
                    UPDATE seen
                    SET last_seen_at = ?, url = ?, source_id = ?
                    WHERE url_hash = ?
                    """,
                    (now, normalized, source_id, url_hash),
                )
            else:
                conn.execute(
                    """
                    INSERT INTO seen(url_hash, url, first_seen_at, last_seen_at, source_id)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (url_hash, normalized, now, now, source_id),
                )

    def upsert_item(self, item: Item, summary: dict[str, Any] | BaseModel | None = None) -> None:
        normalized = normalize_url(item.url)
        url_hash = hash_url(normalized)
        item_id = f"{item.source_id}:{url_hash}"
        if isinstance(summary, BaseModel):
            json_summary = summary.model_dump_json()
        elif isinstance(summary, dict):
            json_summary = json.dumps(summary, ensure_ascii=False)
        else:
            json_summary = None
        json_item = item.model_dump_json()
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO items(
                    item_id, url_hash, source_id, source_name, title, url,
                    published_at, fetched_at, json_summary, json_item
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(item_id) DO UPDATE SET
                    title = excluded.title,
                    source_name = excluded.source_name,
                    published_at = excluded.published_at,
                    fetched_at = excluded.fetched_at,
                    json_summary = excluded.json_summary,
                    json_item = excluded.json_item
                """,
                (
                    item_id,
                    url_hash,
                    item.source_id,
                    item.source_name,
                    item.title,
                    normalized,
                    item.published_at.isoformat() if item.published_at else None,
                    item.fetched_at.isoformat(),
                    json_summary,
                    json_item,
                ),
            )

    def get_cached_summary(self, source_id: str, url: str) -> dict[str, Any] | None:
        normalized = normalize_url(url)
        url_hash = hash_url(normalized)
        item_id = f"{source_id}:{url_hash}"
        with self._connect() as conn:
            row = conn.execute(
                "SELECT json_summary FROM items WHERE item_id = ? LIMIT 1",
                (item_id,),
            ).fetchone()
        if not row:
            return None
        raw = row[0]
        if not raw:
            return None
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                return parsed
            return None
        except Exception:
            return None

    def get_http_cache(self, url: str) -> dict[str, str] | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT etag, last_modified FROM http_cache WHERE url = ? LIMIT 1",
                (url,),
            ).fetchone()
            if not row:
                return None
            etag, last_modified = row
            return {
                "etag": etag or "",
                "last_modified": last_modified or "",
            }

    def upsert_http_cache(
        self, url: str, etag: str | None = None, last_modified: str | None = None
    ) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO http_cache(url, etag, last_modified, updated_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(url) DO UPDATE SET
                    etag = excluded.etag,
                    last_modified = excluded.last_modified,
                    updated_at = excluded.updated_at
                """,
                (url, etag, last_modified, datetime.now(UTC).isoformat()),
            )

    def recent_items(self, limit: int = 200) -> list[dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT title, url, source_name, published_at, fetched_at, json_summary
                FROM items
                ORDER BY fetched_at DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        result: list[dict[str, Any]] = []
        for row in rows:
            title, url, source_name, published_at, fetched_at, json_summary = row
            payload: dict[str, Any] = {
                "title": title,
                "url": url,
                "source_name": source_name,
                "published_at": published_at,
                "fetched_at": fetched_at,
            }
            if json_summary:
                payload["summary"] = json.loads(json_summary)
            result.append(payload)
        return result
