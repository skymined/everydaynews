from __future__ import annotations

import json
import os
import random
import time
from typing import Any, Callable

from .json_utils import load_json_object


class APIBackend:
    def __init__(
        self,
        provider: str,
        classify_prompt: str,
        news_prompt: str,
        paper_prompt: str,
        openai_model: str,
        gemini_model: str,
    ) -> None:
        self.provider = provider.lower().strip()
        self.classify_prompt = classify_prompt
        self.news_prompt = news_prompt
        self.paper_prompt = paper_prompt
        self.openai_model = openai_model
        self.gemini_model = gemini_model

        self._openai_client = None
        self._gemini_client = None
        if self.provider == "openai":
            self._openai_client = self._build_openai_client()
        elif self.provider == "gemini":
            self._gemini_client = self._build_gemini_client()
        else:
            raise ValueError(f"Unsupported API provider: {provider}")

    def _build_openai_client(self):
        from openai import OpenAI  # type: ignore

        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        return OpenAI(api_key=api_key)

    def _build_gemini_client(self):
        from google import genai  # type: ignore

        api_key = os.getenv("GEMINI_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not set")
        return genai.Client(api_key=api_key)

    def _should_retry(self, exc: Exception) -> bool:
        message = str(exc).lower()
        retry_markers = ("429", "rate", "timeout", "timed out", "connection", "503", "502", "500")
        return any(marker in message for marker in retry_markers)

    def _with_backoff(self, fn: Callable[[], str], max_attempts: int = 3) -> str:
        last_exc: Exception | None = None
        for attempt in range(max_attempts):
            try:
                return fn()
            except Exception as exc:  # pragma: no cover - network dependent
                last_exc = exc
                if attempt == max_attempts - 1 or not self._should_retry(exc):
                    break
                sleep_sec = (2**attempt) + random.uniform(0.05, 0.25)
                time.sleep(sleep_sec)
        assert last_exc is not None
        raise last_exc

    def _parse_or_retry_json(self, call_fn: Callable[[str], str], schema_hint: str) -> dict:
        raw = call_fn("")
        try:
            return load_json_object(raw)
        except Exception:
            repaired = call_fn(
                "이전 응답의 JSON 파싱에 실패했습니다. 다른 텍스트 없이 JSON 객체 하나만 다시 출력하세요."
                f"\n스키마 힌트: {schema_hint}"
            )
            return load_json_object(repaired)

    def _chat_openai(
        self,
        system_prompt: str,
        payload: dict[str, Any],
        temperature: float,
        max_tokens: int,
        retry_instruction: str = "",
    ) -> str:
        assert self._openai_client is not None

        def _call() -> str:
            user_block = json.dumps(payload, ensure_ascii=False)
            extra = f"\n{retry_instruction}" if retry_instruction else ""
            resp = self._openai_client.chat.completions.create(
                model=self.openai_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"입력(JSON):\n{user_block}{extra}"},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                response_format={"type": "json_object"},
            )
            message = resp.choices[0].message
            return (message.content or "").strip()

        return self._with_backoff(_call, max_attempts=3)

    def _chat_gemini(
        self,
        system_prompt: str,
        payload: dict[str, Any],
        temperature: float,
        max_tokens: int,
        retry_instruction: str = "",
    ) -> str:
        assert self._gemini_client is not None

        def _call() -> str:
            prompt = (
                f"{system_prompt}\n\n"
                f"입력(JSON):\n{json.dumps(payload, ensure_ascii=False)}\n"
                f"{retry_instruction}\n"
            )
            resp = self._gemini_client.models.generate_content(
                model=self.gemini_model,
                contents=prompt,
                config={
                    "temperature": temperature,
                    "max_output_tokens": max_tokens,
                    "response_mime_type": "application/json",
                },
            )
            return (getattr(resp, "text", "") or "").strip()

        return self._with_backoff(_call, max_attempts=3)

    def _invoke(
        self,
        prompt: str,
        payload: dict[str, Any],
        temperature: float,
        max_tokens: int,
        schema_hint: str,
    ) -> dict:
        if self.provider == "openai":
            return self._parse_or_retry_json(
                lambda retry_msg: self._chat_openai(
                    system_prompt=prompt,
                    payload=payload,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    retry_instruction=retry_msg,
                ),
                schema_hint=schema_hint,
            )
        return self._parse_or_retry_json(
            lambda retry_msg: self._chat_gemini(
                system_prompt=prompt,
                payload=payload,
                temperature=temperature,
                max_tokens=max_tokens,
                retry_instruction=retry_msg,
            ),
            schema_hint=schema_hint,
        )

    def classify_news(self, payload: dict) -> dict:
        return self._invoke(
            prompt=self.classify_prompt,
            payload=payload,
            temperature=0.1,
            max_tokens=200,
            schema_hint='{"include": true, "reason_kr": "..."}',
        )

    def summarize_news(self, payload: dict) -> dict:
        return self._invoke(
            prompt=self.news_prompt,
            payload=payload,
            temperature=0.25,
            max_tokens=700,
            schema_hint='{"headline_kr":"...","what":["..."],"why_trend":["..."],"keywords":["..."]}',
        )

    def summarize_paper(self, payload: dict) -> dict:
        return self._invoke(
            prompt=self.paper_prompt,
            payload=payload,
            temperature=0.25,
            max_tokens=800,
            schema_hint='{"one_liner_kr":"...","core_idea_kr":"...","keywords":["..."]}',
        )

