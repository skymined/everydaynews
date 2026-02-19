from __future__ import annotations

import json
import re


def extract_json_text(raw: str) -> str:
    text = raw.strip()
    if not text:
        raise ValueError("Empty response")

    fenced = re.findall(r"```(?:json)?\s*([\s\S]*?)```", text, flags=re.IGNORECASE)
    if fenced:
        text = fenced[0].strip()

    if text.startswith("{") and text.endswith("}"):
        return text

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found")
    return text[start : end + 1]


def load_json_object(raw: str) -> dict:
    text = extract_json_text(raw)
    return json.loads(text)

