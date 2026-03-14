from __future__ import annotations

import unittest
from datetime import UTC, date, datetime
from unittest.mock import patch

from digest.fetch import HostRateLimiter, fetch_source
from digest.models import DefaultsConfig, RawItem, SourceConfig


class _DummyStore:
    def get_http_cache(self, url: str):
        return None

    def upsert_http_cache(self, url: str, etag: str | None = None, last_modified: str | None = None) -> None:
        return None


class HFPapersDateFetchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.source = SourceConfig(
            id="hf_papers_today",
            name="Hugging Face Papers (Top today)",
            type="html",
            url="https://huggingface.co/papers",
            max_items=10,
        )
        self.defaults = DefaultsConfig()
        self.store = _DummyStore()
        self.limiter = HostRateLimiter(rps=10.0)

    def test_uses_target_date_url_for_hf_papers(self) -> None:
        with (
            patch(
                "digest.fetch._http_get",
                return_value=(
                    200,
                    "<html></html>",
                    {},
                    "https://huggingface.co/papers/date/2026-02-22",
                ),
            ) as mock_http_get,
            patch("digest.fetch._parse_html_items") as mock_parse_html_items,
        ):
            mock_parse_html_items.return_value = [
                RawItem(
                    source_id="hf_papers_today",
                    source_name="HF",
                    title="paper",
                    url="https://huggingface.co/papers/2602.17270",
                    published_at=None,
                    fetched_at=datetime(2026, 2, 22, 0, 0, tzinfo=UTC),
                )
            ]
            items = fetch_source(
                source=self.source,
                defaults=self.defaults,
                store=self.store,
                limiter=self.limiter,
                target_date=date(2026, 2, 22),
            )
            self.assertEqual(len(items), 1)
            self.assertIn(
                "/papers/date/2026-02-22",
                mock_http_get.call_args.args[0],
            )

    def test_falls_back_to_latest_available_hf_date(self) -> None:
        with (
            patch(
                "digest.fetch._http_get",
                return_value=(
                    200,
                    "<html></html>",
                    {},
                    "https://huggingface.co/papers/date/2026-02-20",
                ),
            ),
            patch("digest.fetch._parse_html_items") as mock_parse_html_items,
        ):
            mock_parse_html_items.return_value = [
                RawItem(
                    source_id="hf_papers_today",
                    source_name="HF",
                    title="paper",
                    url="https://huggingface.co/papers/2602.17270",
                    published_at=None,
                    fetched_at=datetime(2026, 2, 22, 0, 0, tzinfo=UTC),
                )
            ]
            items = fetch_source(
                source=self.source,
                defaults=self.defaults,
                store=self.store,
                limiter=self.limiter,
                target_date=date(2026, 2, 22),
            )
            self.assertEqual(len(items), 1)
            self.assertIn("2026-02-20 기준", items[0].source_name)
            mock_parse_html_items.assert_called_once()


if __name__ == "__main__":
    unittest.main()
