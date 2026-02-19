from __future__ import annotations

import json
import re
import shutil
from datetime import UTC, datetime
from pathlib import Path


WEBSITE_DIR = Path("website")
REPORTS_DIR = WEBSITE_DIR / "reports"
POSTS_DIR = WEBSITE_DIR / "posts"
OUTPUT_PATH = WEBSITE_DIR / "reports.json"
DATE_FILE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")


DETAIL_TEMPLATE = """<!doctype html>
<html lang=\"ko\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>IMEVERYDAY | {date}</title>
  <link rel=\"stylesheet\" href=\"../../assets/style.css\">
</head>
<body>
  <header class=\"site-header\">
    <div class=\"header-inner\">
      <a class=\"logo\" href=\"../../\">IMEVERYDAY</a>
      <nav class=\"nav\">
        <a href=\"../../\">Home</a>
        <a class=\"active\" href=\"../\">목록</a>
        <a href=\"../../about/\">About</a>
      </nav>
    </div>
  </header>

  <main class=\"page\">
    <section class=\"card\">
      <div class=\"article-meta\">
        <div>
          <div class=\"meta\" id=\"report-date\">{date}</div>
          <h1 id=\"report-title\">{title}</h1>
        </div>
        <a id=\"raw-link\" class=\"btn-link\" href=\"../../reports/{file}\" target=\"_blank\" rel=\"noopener noreferrer\">원본 Markdown</a>
      </div>
      <article id=\"report-article\" class=\"article\">
        <p class=\"muted\">리포트를 불러오는 중...</p>
      </article>
    </section>
  </main>

  <script>window.REPORT_FILE = \"{file}\"; window.REPORT_DATE = \"{date}\";</script>
  <script src=\"../../assets/common.js\"></script>
  <script src=\"../../assets/post-detail.js\"></script>
</body>
</html>
"""


def _first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def _extract_excerpt(path: Path, max_len: int = 220) -> str:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)

    lines = []
    for raw in text.splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        if s.startswith("- 기준일"):
            continue
        s = re.sub(r"^[-*]\s+", "", s)
        s = re.sub(r"^\d+\.\s+", "", s)
        lines.append(s)

    joined = " ".join(lines)
    joined = re.sub(r"\s+", " ", joined).strip()
    if len(joined) > max_len:
        return joined[:max_len] + "..."
    return joined


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
                "title": _first_heading(path) or f"AI Trend Digest - {path.stem}",
                "excerpt": _extract_excerpt(path),
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


def sync_detail_pages(items: list[dict]) -> None:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    expected_dates = {item["date"] for item in items}

    for entry in POSTS_DIR.iterdir():
        if not entry.is_dir():
            continue
        if DATE_FILE_PATTERN.match(f"{entry.name}.md") and entry.name not in expected_dates:
            shutil.rmtree(entry)

    for item in items:
        post_dir = POSTS_DIR / item["date"]
        post_dir.mkdir(parents=True, exist_ok=True)
        html = DETAIL_TEMPLATE.format(
            date=item["date"],
            file=item["file"],
            title=item["title"],
        )
        (post_dir / "index.html").write_text(html, encoding="utf-8")


def main() -> int:
    index = build_index()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    sync_detail_pages(index["items"])
    (WEBSITE_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print(f"wrote {OUTPUT_PATH} ({len(index['items'])} reports)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
