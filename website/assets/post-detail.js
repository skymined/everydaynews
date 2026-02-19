(function () {
  "use strict";

  const article = document.getElementById("report-article");
  const titleNode = document.getElementById("report-title");
  const dateNode = document.getElementById("report-date");
  const downloadLink = document.getElementById("raw-download-link");
  const toc = document.getElementById("report-toc");
  const tocList = document.getElementById("toc-list");

  function makeSlug(text) {
    return text
      .toLowerCase()
      .replace(/[^a-z0-9가-힣\s-]/g, "")
      .trim()
      .replace(/\s+/g, "-")
      .replace(/-+/g, "-");
  }

  function setHeadingIds(headings) {
    const usedIds = new Set();
    for (const heading of headings) {
      const base = makeSlug(heading.textContent || "") || "section";
      let nextId = base;
      let seq = 2;
      while (usedIds.has(nextId) || document.getElementById(nextId)) {
        nextId = `${base}-${seq}`;
        seq += 1;
      }
      heading.id = nextId;
      usedIds.add(nextId);
    }
  }

  function renderToc() {
    if (!toc || !tocList) {
      return;
    }
    const headings = Array.from(article.querySelectorAll("h2, h3"));
    if (!headings.length) {
      toc.hidden = true;
      tocList.innerHTML = "";
      return;
    }

    setHeadingIds(headings);
    const groups = [];
    let currentGroup = null;

    for (const heading of headings) {
      const title = (heading.textContent || "").trim();
      if (!title) {
        continue;
      }
      if (heading.tagName === "H2") {
        currentGroup = { title, id: heading.id, children: [] };
        groups.push(currentGroup);
        continue;
      }

      if (!currentGroup) {
        currentGroup = { title: "기타", id: "", children: [] };
        groups.push(currentGroup);
      }
      currentGroup.children.push({ title, id: heading.id });
    }

    const listMarkup = groups
      .map((group) => {
        const parent = group.id
          ? `<a href="#${group.id}">${group.title}</a>`
          : `<span>${group.title}</span>`;
        const children = group.children.length
          ? `<ul>${group.children.map((child) => `<li><a href="#${child.id}">${child.title}</a></li>`).join("")}</ul>`
          : "";
        return `<li>${parent}${children}</li>`;
      })
      .join("");

    tocList.innerHTML = `<ul class="toc-list">${listMarkup}</ul>`;

    toc.hidden = false;
  }

  async function run() {
    const fileName = window.REPORT_FILE || "";
    const dateSlug = window.REPORT_DATE || fileName.replace(/\.md$/, "");
    if (!fileName) {
      article.innerHTML = '<p class="muted">리포트 정보를 찾지 못했습니다.</p>';
      return;
    }

    dateNode.textContent = dateSlug;
    downloadLink.href = `../../reports/${fileName}`;
    downloadLink.setAttribute("download", fileName);

    try {
      const reportPath = `../../reports/${fileName}`;
      const reportUrl = window.SiteCommon.withCacheBust
        ? window.SiteCommon.withCacheBust(reportPath)
        : reportPath;
      const response = await fetch(reportUrl, { cache: "no-store" });
      if (!response.ok) {
        throw new Error(`리포트 로드 실패 (${response.status})`);
      }

      const markdown = await response.text();
      const stripped = window.SiteCommon.stripFirstHeading(markdown);
      const heading = window.SiteCommon.normalizeDigestTitle(stripped.title || `IMDIGEST - ${dateSlug}`);

      titleNode.textContent = heading;
      article.innerHTML = window.SiteCommon.markdownToHtml(stripped.markdown);
      renderToc();
    } catch (error) {
      article.innerHTML = `<p class="muted">리포트를 불러오지 못했습니다: ${error.message}</p>`;
      if (toc) {
        toc.hidden = true;
      }
    }
  }

  run();
})();
