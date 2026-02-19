from __future__ import annotations

from typing import Protocol


class LLMBackend(Protocol):
    def classify_news(self, payload: dict) -> dict: ...

    def summarize_news(self, payload: dict) -> dict: ...

    def summarize_paper(self, payload: dict) -> dict: ...
