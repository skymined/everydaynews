(function () {
  "use strict";

  const THEME_KEY = "imdigest-theme";

  function escapeHtml(input) {
    return input
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;");
  }

  function autoLinkText(text) {
    return text.replace(/https?:\/\/[^\s<]+/g, (match) => {
      let url = match;
      let tail = "";
      while (/[),.;!?]$/.test(url)) {
        tail = url.slice(-1) + tail;
        url = url.slice(0, -1);
      }
      return `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>${tail}`;
    });
  }

  function autoLinkOutsideAnchors(html) {
    return html
      .split(/(<a\s+[\s\S]*?<\/a>)/g)
      .map((segment) => {
        if (segment.startsWith("<a ")) {
          return segment;
        }
        return autoLinkText(segment);
      })
      .join("");
  }

  function formatInline(input) {
    let out = escapeHtml(input);
    out = out.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    out = out.replace(/`([^`]+)`/g, "<code>$1</code>");
    out = out.replace(/\[(.+?)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
    out = autoLinkOutsideAnchors(out);
    return out;
  }

  function markdownToHtml(markdown) {
    const lines = markdown.replace(/\r\n/g, "\n").split("\n");
    const out = [];
    const listStack = [];
    let inCode = false;

    function closeLists(targetDepth = 0) {
      while (listStack.length > targetDepth) {
        const type = listStack.pop();
        out.push(`</${type}>`);
      }
    }

    function openList(type) {
      out.push(`<${type}>`);
      listStack.push(type);
    }

    for (const rawLine of lines) {
      const line = rawLine.replace(/\t/g, "    ").replace(/\s+$/, "");
      const trimmed = line.trim();

      if (trimmed.startsWith("```")) {
        closeLists();
        if (!inCode) {
          out.push("<pre><code>");
          inCode = true;
        } else {
          out.push("</code></pre>");
          inCode = false;
        }
        continue;
      }

      if (inCode) {
        out.push(escapeHtml(rawLine));
        continue;
      }

      if (!trimmed) {
        closeLists();
        continue;
      }

      if (trimmed.startsWith("### ")) {
        closeLists();
        out.push(`<h3>${formatInline(trimmed.slice(4))}</h3>`);
        continue;
      }
      if (trimmed.startsWith("## ")) {
        closeLists();
        out.push(`<h2>${formatInline(trimmed.slice(3))}</h2>`);
        continue;
      }
      if (trimmed.startsWith("# ")) {
        closeLists();
        out.push(`<h1>${formatInline(trimmed.slice(2))}</h1>`);
        continue;
      }

      const listMatch = line.match(/^(\s*)([-*]|\d+\.)\s+(.+)$/);
      if (listMatch) {
        const indent = listMatch[1].length;
        const marker = listMatch[2];
        const content = listMatch[3];
        const level = Math.floor(indent / 2) + 1;
        const type = /^\d+\.$/.test(marker) ? "ol" : "ul";

        while (listStack.length > level) {
          closeLists(listStack.length - 1);
        }

        while (listStack.length < level) {
          openList(type);
        }

        if (listStack[listStack.length - 1] !== type) {
          closeLists(listStack.length - 1);
          openList(type);
        }

        out.push(`<li>${formatInline(content)}</li>`);
        continue;
      }

      closeLists();
      out.push(`<p>${formatInline(trimmed)}</p>`);
    }

    closeLists();
    if (inCode) {
      out.push("</code></pre>");
    }
    return out.join("\n");
  }

  function stripMarkdown(md, maxLen) {
    const text = md
      .replace(/```[\s\S]*?```/g, " ")
      .replace(/\[(.*?)\]\((.*?)\)/g, "$1")
      .replace(/^#{1,6}\s+/gm, "")
      .replace(/^[-*]\s+/gm, "")
      .replace(/^\d+\.\s+/gm, "")
      .replace(/`([^`]+)`/g, "$1")
      .replace(/\*\*(.*?)\*\*/g, "$1")
      .replace(/https?:\/\/\S+/g, "")
      .replace(/\s+/g, " ")
      .trim();
    return text.length > maxLen ? `${text.slice(0, maxLen)}...` : text;
  }

  function stripFirstHeading(markdown) {
    const lines = markdown.replace(/\r\n/g, "\n").split("\n");
    for (let i = 0; i < lines.length; i += 1) {
      const trimmed = lines[i].trim();
      if (!trimmed) {
        continue;
      }
      const m = trimmed.match(/^#\s+(.+)$/);
      if (m) {
        lines.splice(i, 1);
        while (lines.length && !lines[0].trim()) {
          lines.shift();
        }
        return { title: m[1].trim(), markdown: lines.join("\n") };
      }
      break;
    }
    return { title: "", markdown };
  }

  function normalizeDigestTitle(title) {
    if (!title) return "";
    return title.replace(/^AI Trend Digest/i, "IMDIGEST");
  }

  function formatDateLabel(isoDate) {
    const m = isoDate.match(/^(\d{4})-(\d{2})-(\d{2})$/);
    if (!m) return isoDate;
    return `${m[1]}-${m[2]}-${m[3]}`;
  }

  function withCacheBust(path) {
    const separator = path.includes("?") ? "&" : "?";
    return `${path}${separator}v=${Date.now()}`;
  }

  async function loadReportsIndex(path = "./reports.json") {
    const response = await fetch(withCacheBust(path), { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`reports.json 로드 실패 (${response.status})`);
    }
    return response.json();
  }

  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    try {
      localStorage.setItem(THEME_KEY, theme);
    } catch {
      // ignore
    }
  }

  function setupThemeToggle() {
    let saved = "";
    try {
      saved = localStorage.getItem(THEME_KEY) || "";
    } catch {
      saved = "";
    }
    const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    applyTheme(saved || (prefersDark ? "dark" : "light"));

    const btn = document.querySelector("[data-theme-toggle]");
    if (!btn) {
      return;
    }

    function renderLabel() {
      const isDark = document.documentElement.dataset.theme === "dark";
      btn.textContent = isDark ? "라이트 모드" : "다크 모드";
      btn.setAttribute("aria-label", isDark ? "라이트 모드 전환" : "다크 모드 전환");
    }

    renderLabel();
    btn.addEventListener("click", () => {
      const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      applyTheme(next);
      renderLabel();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupThemeToggle);
  } else {
    setupThemeToggle();
  }

  window.SiteCommon = {
    markdownToHtml,
    stripMarkdown,
    stripFirstHeading,
    normalizeDigestTitle,
    formatDateLabel,
    withCacheBust,
    loadReportsIndex,
  };
})();
