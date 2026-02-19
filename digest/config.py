from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import AppConfig


def load_config(path: str | Path = "sources.yaml") -> AppConfig:
    cfg_path = Path(path)
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")
    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    return AppConfig.model_validate(data)


def load_prompt(path: str | Path) -> str:
    prompt_path = Path(path)
    return prompt_path.read_text(encoding="utf-8").strip()


def dump_json(data: dict[str, Any], path: str | Path) -> None:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

