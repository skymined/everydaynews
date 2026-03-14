from __future__ import annotations

import unittest

from digest.social import _parse_threads_response, _parse_x_response


class SocialSourceParseTest(unittest.TestCase):
    def test_parse_x_response(self) -> None:
        payload = {
            "data": [
                {
                    "id": "123",
                    "text": "OpenAI launches a new API for agents",
                    "created_at": "2026-03-14T01:02:03Z",
                    "author_id": "42",
                }
            ],
            "includes": {
                "users": [
                    {
                        "id": "42",
                        "username": "openai",
                    }
                ]
            },
        }
        items = _parse_x_response(payload)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].source_id, "x_search")
        self.assertEqual(items[0].source_name, "X @openai")
        self.assertEqual(items[0].url, "https://x.com/openai/status/123")

    def test_parse_threads_response(self) -> None:
        payload = {
            "data": [
                {
                    "id": "abc",
                    "text": "Today we shipped a new AI feature on Threads.",
                    "timestamp": "2026-03-14T04:05:06+0000",
                    "permalink": "https://www.threads.net/@meta/post/abc",
                    "username": "meta",
                }
            ]
        }
        items = _parse_threads_response(payload)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].source_id, "threads_recent")
        self.assertEqual(items[0].source_name, "Threads @meta")
        self.assertEqual(items[0].url, "https://www.threads.net/@meta/post/abc")


if __name__ == "__main__":
    unittest.main()
