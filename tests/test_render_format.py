from __future__ import annotations

import unittest
from datetime import UTC, date, datetime

from digest.models import Item, NewsSummary, PaperSummary
from digest.render import render_digest_markdown


class RenderFormatTest(unittest.TestCase):
    def test_sections_are_fixed(self) -> None:
        news_item = Item(
            source_id="openai_news",
            source_name="OpenAI",
            title="news",
            url="https://example.com/news",
            published_at=datetime(2026, 2, 18, 1, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 2, 19, 1, 0, tzinfo=UTC),
        )
        paper_item = Item(
            source_id="hf_papers_today",
            source_name="HF Papers",
            title="paper",
            url="https://example.com/paper",
            published_at=None,
            fetched_at=datetime(2026, 2, 19, 1, 0, tzinfo=UTC),
        )
        md = render_digest_markdown(
            target_date=date(2026, 2, 19),
            kst_yesterday=date(2026, 2, 18),
            news_items=[news_item],
            paper_items=[paper_item],
            news_summaries={
                news_item.url: NewsSummary(
                    headline_kr="헤드라인",
                    what=["a", "b"],
                    why_trend=["c"],
                    keywords=["ai"],
                )
            },
            paper_summaries={
                paper_item.url: PaperSummary(
                    one_liner_kr="요약",
                    core_idea_kr="핵심",
                    keywords=["agents"],
                )
            },
        )
        self.assertIn("## AI News", md)
        self.assertIn("## Papers (Hugging Face Top 10)", md)
        self.assertNotIn("## Top Themes", md)
        self.assertNotIn("## Source-wise Highlights", md)


if __name__ == "__main__":
    unittest.main()

