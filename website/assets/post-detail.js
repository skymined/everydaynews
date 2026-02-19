(function () {
  "use strict";

  const article = document.getElementById("report-article");
  const title = document.getElementById("report-title");
  const date = document.getElementById("report-date");
  const rawLink = document.getElementById("raw-link");

  async function run() {
    const fileName = window.REPORT_FILE || "";
    const dateSlug = window.REPORT_DATE || fileName.replace(/\.md$/, "");
    if (!fileName) {
      article.innerHTML = '<p class="muted">리포트 정보를 찾지 못했습니다.</p>';
      return;
    }

    date.textContent = dateSlug;
    rawLink.href = `../../reports/${fileName}`;

    try {
      const response = await fetch(`../../reports/${fileName}`, { cache: "no-cache" });
      if (!response.ok) {
        throw new Error(`리포트 로드 실패 (${response.status})`);
      }
      const markdown = await response.text();
      title.textContent = `AI Trend Digest - ${dateSlug}`;
      article.innerHTML = window.SiteCommon.markdownToHtml(markdown);
    } catch (error) {
      article.innerHTML = `<p class="muted">리포트를 불러오지 못했습니다: ${error.message}</p>`;
    }
  }

  run();
})();
