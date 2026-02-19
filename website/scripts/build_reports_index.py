from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path


REPORTS_DIR = Path("website/reports")
OUTPUT_PATH = Path("website/reports.json")
DATE_FILE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")


def _first_heading(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("# "):
                return stripped[2:].strip()
    except Exception:
        return ""
    return ""


def build_index() -> dict:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    items: list[dict] = []
    for path in REPORTS_DIR.glob("*.md"):
        if not DATE_FILE_PATTERN.match(path.name):
            continue
        items.append(
            {
                "date": path.stem,
                "file": path.name,
                "title": _first_heading(path),
            }
        )

    items.sort(key=lambda x: x["date"], reverse=True)
    latest_exists = (REPORTS_DIR / "latest.md").exists()
    latest_file = "latest.md" if latest_exists else (items[0]["file"] if items else "")

    return {
        "latest": latest_file,
        "items": items,
        "generated_at_utc": datetime.now(UTC).isoformat(),
    }


def main() -> int:
    index = build_index()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT_PATH} ({len(index['items'])} reports)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
