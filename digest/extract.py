from __future__ import annotations

import logging
import re
from urllib.request import Request, urlopen

try:
    import httpx  # type: ignore
except Exception:  # pragma: no cover
    httpx = None

try:
    import trafilatura  # type: ignore
except Exception:  # pragma: no cover
    trafilatura = None

try:
    from readability import Document  # type: ignore
except Exception:  # pragma: no cover
    Document = None  # type: ignore

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover
    BeautifulSoup = None  # type: ignore

logger = logging.getLogger(__name__)


def _download(url: str, timeout_sec: int, user_agent: str) -> str:
    headers = {"User-Agent": user_agent}
    if httpx is not None:
        with httpx.Client(timeout=timeout_sec, follow_redirects=True) as client:
            resp = client.get(url, headers=headers)
            resp.raise_for_status()
            return resp.text
    req = Request(url, headers=headers)  # noqa: S310
    with urlopen(req, timeout=timeout_sec) as resp:  # noqa: S310
        return resp.read().decode("utf-8", errors="replace")


def _normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_main_text(
    url: str,
    timeout_sec: int = 30,
    user_agent: str = "ai-trend-digest/0.1",
    max_chars: int = 8000,
) -> str:
    try:
        html = _download(url, timeout_sec=timeout_sec, user_agent=user_agent)
    except Exception as exc:
        logger.warning("Extract download failed for %s: %s", url, exc)
        return ""

    if trafilatura is not None:
        try:
            text = trafilatura.extract(
                html,
                include_links=False,
                include_images=False,
                favor_precision=True,
                with_metadata=False,
            )
            if text:
                return _normalize_text(text)[:max_chars]
        except Exception:
            pass

    if Document is not None and BeautifulSoup is not None:
        try:
            doc = Document(html)
            cleaned = doc.summary(html_partial=True)
            soup = BeautifulSoup(cleaned, "lxml")
            text = soup.get_text(" ", strip=True)
            if text:
                return _normalize_text(text)[:max_chars]
        except Exception:
            pass

    if BeautifulSoup is not None:
        try:
            soup = BeautifulSoup(html, "lxml")
            main = soup.find("article") or soup.find("main") or soup.find("body")
            text = main.get_text(" ", strip=True) if main else soup.get_text(" ", strip=True)
            return _normalize_text(text)[:max_chars]
        except Exception:
            pass

    return _normalize_text(html)[:max_chars]

