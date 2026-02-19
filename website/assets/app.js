(function () {
  "use strict";

  const SELECT_ID = "report-select";
  const STATUS_ID = "status";
  const CONTENT_ID = "report-content";
  const RAW_LINK_ID = "raw-link";
  const FALLBACK_REPORT = "latest.md";

  function $(id) {
    return document.getElementById(id);
  }

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

    function closeList() {
      if (listMode === "ul") out.push("</ul>");
      if (listMode === "ol") out.push("</ol>");
      listMode = "";
    }

    for (const rawLine of lines) {
      const line = rawLine.trimEnd();
      const trimmed = line.trim();

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

      const ulMatch = trimmed.match(/^-\s+(.+)$/);
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
    return out.join("\n");
  }

  function queryReportName() {
    const url = new URL(window.location.href);
    const report = (url.searchParams.get("report") || "").trim();
    if (!report) return "";
    return report.endsWith(".md") ? report : `${report}.md`;
  }

  function setQueryReport(fileName) {
    const url = new URL(window.location.href);
    const stem = fileName.endsWith(".md") ? fileName.slice(0, -3) : fileName;
    url.searchParams.set("report", stem);
    window.history.replaceState({}, "", url.toString());
  }

  async function loadReport(fileName) {
    const status = $(STATUS_ID);
    const content = $(CONTENT_ID);
    const rawLink = $(RAW_LINK_ID);

    const path = `./reports/${fileName}`;
    status.textContent = `${fileName} 로딩 중...`;
    rawLink.href = path;

    const response = await fetch(path, { cache: "no-cache" });
    if (!response.ok) {
      throw new Error(`리포트 로딩 실패 (${response.status})`);
    }

    const markdown = await response.text();
    content.innerHTML = markdownToHtml(markdown);
    status.textContent = `${fileName} 로드 완료`;
    setQueryReport(fileName);
  }

  function buildOptions(items, latest) {
    const select = $(SELECT_ID);
    select.innerHTML = "";

    const optionLatest = document.createElement("option");
    optionLatest.value = latest;
    optionLatest.textContent = "latest";
    select.appendChild(optionLatest);

    for (const item of items) {
      if (item.file === latest) {
        continue;
      }
      const option = document.createElement("option");
      option.value = item.file;
      option.textContent = item.date;
      select.appendChild(option);
    }
  }

  async function loadIndex() {
    const response = await fetch("./reports.json", { cache: "no-cache" });
    if (!response.ok) {
      return {
        latest: FALLBACK_REPORT,
        items: [],
      };
    }
    return response.json();
  }

  async function init() {
    const select = $(SELECT_ID);
    const status = $(STATUS_ID);

    try {
      const index = await loadIndex();
      const latest = index.latest || FALLBACK_REPORT;
      const items = Array.isArray(index.items) ? index.items : [];
      buildOptions(items, latest);

      const requested = queryReportName();
      const available = new Set([latest, ...items.map((x) => x.file)]);
      const selected = available.has(requested) ? requested : latest;

      select.value = selected;
      await loadReport(selected);

      select.addEventListener("change", async () => {
        try {
          await loadReport(select.value);
        } catch (error) {
          status.textContent = `오류: ${error.message}`;
        }
      });
    } catch (error) {
      status.textContent = `초기화 실패: ${error.message}`;
    }
  }

  init();
})();
