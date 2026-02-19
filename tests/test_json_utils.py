from __future__ import annotations

import unittest

from digest.llm.json_utils import load_json_object


class JsonUtilsTest(unittest.TestCase):
    def test_load_plain_json(self) -> None:
        raw = '{"include": true, "reason_kr": "ok"}'
        parsed = load_json_object(raw)
        self.assertEqual(parsed["include"], True)

    def test_load_json_inside_codeblock(self) -> None:
        raw = "```json\n{\"include\": false, \"reason_kr\": \"x\"}\n```"
        parsed = load_json_object(raw)
        self.assertEqual(parsed["include"], False)

    def test_load_json_with_extra_text(self) -> None:
        raw = "result:\n{\"headline_kr\":\"h\",\"what\":[\"a\"],\"why_trend\":[\"b\"],\"keywords\":[\"k\"]}\nend"
        parsed = load_json_object(raw)
        self.assertEqual(parsed["headline_kr"], "h")


if __name__ == "__main__":
    unittest.main()

