from __future__ import annotations

import json
import os
import random
import time
from typing import Any, Callable

from .json_utils import load_json_object


class LlamaBackend:
    def __init__(
        self,
        classify_prompt: str,
        news_prompt: str,
        paper_prompt: str,
        base_url: str | None = None,
        model: str | None = None,
    ) -> None:
        from openai import OpenAI  # type: ignore

        self.base_url = (base_url or os.getenv("LOCAL_LLM_BASE_URL") or "http://127.0.0.1:11434/v1").strip()
        self.model = (model or os.getenv("LOCAL_LLM_MODEL") or "qwen2.5:7b").strip()
        self.client = OpenAI(base_url=self.base_url, api_key="local")
        self.classify_prompt = classify_prompt
        self.news_prompt = news_prompt
        self.paper_prompt = paper_prompt

    def _with_backoff(self, fn: Callable[[], str], max_attempts: int = 3) -> str:
        last_exc: Exception | None = None
        for attempt in range(max_attempts):
            try:
                return fn()
            except Exception as exc:  # pragma: no cover - network dependent
                last_exc = exc
                if attempt == max_attempts - 1:
                    break
                sleep_sec = (2**attempt) + random.uniform(0.05, 0.25)
                time.sleep(sleep_sec)
        assert last_exc is not None
        raise last_exc

    def _chat(
        self,
        system_prompt: str,
        payload: dict[str, Any],
        temperature: float,
        max_tokens: int,
        retry_instruction: str = "",
    ) -> str:
        prompt = json.dumps(payload, ensure_ascii=False)

        def _call() -> str:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": (
                            "아래 JSON 입력을 바탕으로 응답하세요.\n"
                            f"{prompt}\n"
                            f"{retry_instruction}"
                        ),
                    },
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return (resp.choices[0].message.content or "").strip()

        return self._with_backoff(_call, max_attempts=3)

    def _parse_or_retry(
        self,
        system_prompt: str,
        payload: dict[str, Any],
        temperature: float,
        max_tokens: int,
        schema_hint: str,
    ) -> dict:
        raw = self._chat(
            system_prompt=system_prompt,
            payload=payload,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        try:
            return load_json_object(raw)
        except Exception:
            repaired = self._chat(
                system_prompt=system_prompt,
                payload=payload,
                temperature=temperature,
                max_tokens=max_tokens,
                retry_instruction=(
                    "다른 텍스트 없이 JSON 객체 하나만 출력하세요.\n"
                    f"스키마 힌트: {schema_hint}"
                ),
            )
            return load_json_object(repaired)

    def classify_news(self, payload: dict) -> dict:
        return self._parse_or_retry(
            system_prompt=self.classify_prompt,
            payload=payload,
            temperature=0.1,
            max_tokens=200,
            schema_hint='{"include": true, "reason_kr": "..."}',
        )

    def summarize_news(self, payload: dict) -> dict:
        return self._parse_or_retry(
            system_prompt=self.news_prompt,
            payload=payload,
            temperature=0.25,
            max_tokens=700,
            schema_hint='{"headline_kr":"...","what":["..."],"why_trend":["..."],"keywords":["..."]}',
        )

    def summarize_paper(self, payload: dict) -> dict:
        return self._parse_or_retry(
            system_prompt=self.paper_prompt,
            payload=payload,
            temperature=0.25,
            max_tokens=800,
            schema_hint='{"one_liner_kr":"...","core_idea_kr":"...","keywords":["..."]}',
        )
