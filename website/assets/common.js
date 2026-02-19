(function () {
  "use strict";

  function escapeHtml(input) {
    return input
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;");
  }

  function formatInline(input) {
    const escaped = escapeHtml(input);
    return escaped
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\[(.+?)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
  }

  function markdownToHtml(markdown) {
    const lines = markdown.replace(/\r\n/g, "\n").split("\n");
    const out = [];
    let listMode = "";
    let inCode = false;

    function closeList() {
      if (listMode === "ul") out.push("</ul>");
      if (listMode === "ol") out.push("</ol>");
      listMode = "";
    }

    for (const rawLine of lines) {
      const line = rawLine.trimEnd();
      const trimmed = line.trim();

      if (trimmed.startsWith("```")) {
        closeList();
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
        closeList();
        continue;
      }

      if (trimmed.startsWith("### ")) {
        closeList();
        out.push(`<h3>${formatInline(trimmed.slice(4))}</h3>`);
        continue;
      }
      if (trimmed.startsWith("## ")) {
        closeList();
        out.push(`<h2>${formatInline(trimmed.slice(3))}</h2>`);
        continue;
      }
      if (trimmed.startsWith("# ")) {
        closeList();
        out.push(`<h1>${formatInline(trimmed.slice(2))}</h1>`);
        continue;
      }

      const ulMatch = trimmed.match(/^[-*]\s+(.+)$/);
      if (ulMatch) {
        if (listMode !== "ul") {
          closeList();
          out.push("<ul>");
          listMode = "ul";
        }
        out.push(`<li>${formatInline(ulMatch[1])}</li>`);
        continue;
      }

      const olMatch = trimmed.match(/^\d+\.\s+(.+)$/);
      if (olMatch) {
        if (listMode !== "ol") {
          closeList();
          out.push("<ol>");
          listMode = "ol";
        }
        out.push(`<li>${formatInline(olMatch[1])}</li>`);
        continue;
      }

      closeList();
      out.push(`<p>${formatInline(trimmed)}</p>`);
    }

    closeList();
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
      .replace(/\s+/g, " ")
      .trim();
    return text.length > maxLen ? `${text.slice(0, maxLen)}...` : text;
  }

  function formatDateLabel(isoDate) {
    const m = isoDate.match(/^(\d{4})-(\d{2})-(\d{2})$/);
    if (!m) return isoDate;
    return `${m[1]}-${m[2]}-${m[3]}`;
  }

  async function loadReportsIndex() {
    const response = await fetch("./reports.json", { cache: "no-cache" });
    if (!response.ok) {
      throw new Error(`reports.json 로드 실패 (${response.status})`);
    }
    return response.json();
  }

  window.SiteCommon = {
    markdownToHtml,
    stripMarkdown,
    formatDateLabel,
    loadReportsIndex,
  };
})();
