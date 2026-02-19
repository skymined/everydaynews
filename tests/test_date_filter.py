from __future__ import annotations

import unittest
from datetime import UTC, date, datetime

from digest.cli import _split_items_by_window
from digest.models import Item


class DateFilterTest(unittest.TestCase):
    def test_yesterday_kst_filter(self) -> None:
        target = date(2026, 2, 19)
        # KST 2026-02-18 10:00 => UTC 2026-02-18 01:00
        in_range = Item(
            source_id="google_the_keyword",
            source_name="Google",
            title="in",
            url="https://example.com/in",
            published_at=datetime(2026, 2, 18, 1, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 2, 19, 2, 0, tzinfo=UTC),
        )
        # KST 2026-02-17 23:00 => UTC 2026-02-17 14:00
        out_range = Item(
            source_id="openai_news",
            source_name="OpenAI",
            title="out",
            url="https://example.com/out",
            published_at=datetime(2026, 2, 17, 14, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 2, 19, 2, 0, tzinfo=UTC),
        )

        news, papers, yesterday = _split_items_by_window(
            items=[in_range, out_range],
            target_date=target,
            window="yesterday-kst",
            since_hours=36,
            timezone_name="Asia/Seoul",
        )
        self.assertEqual(yesterday.isoformat(), "2026-02-18")
        self.assertEqual(len(papers), 0)
        self.assertEqual(len(news), 1)
        self.assertEqual(news[0].url, in_range.url)


if __name__ == "__main__":
    unittest.main()

