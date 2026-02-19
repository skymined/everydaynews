from __future__ import annotations

import logging
import os

from .api_provider import APIBackend
from .base import LLMBackend
from .llama_provider import LlamaBackend

logger = logging.getLogger(__name__)


def create_backend(
    *,
    provider_override: str,
    cfg,
    classify_prompt: str,
    news_prompt: str,
    paper_prompt: str,
) -> LLMBackend | None:
    mode = (os.getenv("LLM_MODE") or cfg.llm.default_mode or "local").strip().lower()
    try:
        if mode == "local":
            local_backend = (os.getenv("LOCAL_LLM_BACKEND") or cfg.llm.local_backend or "llama").strip().lower()
            if local_backend != "llama":
                raise ValueError(f"Unsupported local backend: {local_backend}")
            return LlamaBackend(
                classify_prompt=classify_prompt,
                news_prompt=news_prompt,
                paper_prompt=paper_prompt,
                base_url=os.getenv("LOCAL_LLM_BASE_URL") or cfg.llm.local_base_url,
                model=os.getenv("LOCAL_LLM_MODEL") or cfg.llm.local_model,
            )

        provider = (
            provider_override
            or os.getenv("LLM_PROVIDER")
            or cfg.llm.default_provider
            or "openai"
        ).strip()
        return APIBackend(
            provider=provider,
            classify_prompt=classify_prompt,
            news_prompt=news_prompt,
            paper_prompt=paper_prompt,
            openai_model=os.getenv("OPENAI_MODEL") or cfg.llm.openai_model,
            gemini_model=os.getenv("GEMINI_MODEL") or cfg.llm.gemini_model,
        )
    except Exception as exc:
        logger.warning("LLM backend init failed: %s", exc)
        return None
