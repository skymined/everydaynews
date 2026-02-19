from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class RawItem(BaseModel):
    source_id: str
    source_name: str
    title: str
    url: str
    published_at: datetime | None = None
    fetched_at: datetime
    author: str | None = None
    summary_raw: str | None = None


class Item(BaseModel):
    source_id: str
    source_name: str
    title: str
    url: str
    published_at: datetime | None = None
    fetched_at: datetime
    author: str | None = None
    summary_raw: str | None = None
    content_text: str | None = None
    content_hash: str | None = None
    score: float = 0.0
    published_unknown: bool = False


class ItemSummary(BaseModel):
    llm_summary_kr: str
    what_changed: str = "unknown"
    why_it_matters: str
    key_terms: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    unknowns: list[str] = Field(default_factory=list)
    followup_queries: list[str] = Field(default_factory=list)
    one_liner: str
    content_points: list[str] = Field(default_factory=list)
    trend_points: list[str] = Field(default_factory=list)


class NewsClassification(BaseModel):
    include: bool
    reason_kr: str


class NewsSummary(BaseModel):
    headline_kr: str
    what: list[str] = Field(default_factory=list)
    why_trend: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)


class PaperSummary(BaseModel):
    one_liner_kr: str
    core_idea_kr: str
    keywords: list[str] = Field(default_factory=list)


class DayTheme(BaseModel):
    theme: str
    narrative: str
    why_now: str
    supporting_items: list[str] = Field(default_factory=list)
    implications: str
    watchlist: list[str] = Field(default_factory=list)
    followup_queries: list[str] = Field(default_factory=list)


class DaySynthesis(BaseModel):
    tldr: list[str] = Field(default_factory=list)
    themes: list[DayTheme] = Field(default_factory=list)


SourceType = Literal["rss", "html"]


class SourceConfig(BaseModel):
    id: str
    name: str
    type: SourceType
    url: HttpUrl | str
    max_items: int = 10
    selectors: dict[str, str] = Field(default_factory=dict)
    include_keywords: list[str] = Field(default_factory=list)
    exclude_keywords: list[str] = Field(default_factory=list)


class DefaultsConfig(BaseModel):
    max_items_per_source: int = 10
    user_agent: str = "ai-trend-digest/0.1"
    timeout_sec: int = 30
    concurrency: int = 6
    host_rps: float = 1.5
    extract_max_chars: int = 8000


class LLMConfig(BaseModel):
    default_mode: str = "local"
    default_provider: str = "openai"
    openai_model: str = "gpt-4.1-mini"
    gemini_model: str = "gemini-2.0-flash"
    max_items_to_summarize: int = 30
    local_backend: str = "llama"
    local_base_url: str = "http://127.0.0.1:11434/v1"
    local_model: str = "qwen2.5:7b"


class ReportConfig(BaseModel):
    timezone: str = "Asia/Seoul"
    max_news_items: int = 12
    max_papers: int = 10


class ScoringConfig(BaseModel):
    source_weights: dict[str, float] = Field(default_factory=dict)
    priority_keywords: list[str] = Field(default_factory=list)
    tag_keywords: dict[str, list[str]] = Field(default_factory=dict)


class AppConfig(BaseModel):
    defaults: DefaultsConfig
    llm: LLMConfig
    report: ReportConfig = Field(default_factory=ReportConfig)
    scoring: ScoringConfig
    sources: list[SourceConfig]
    watch_sites: list[SourceConfig] = Field(default_factory=list)
