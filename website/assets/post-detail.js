(function () {
  "use strict";

  const article = document.getElementById("report-article");
  const titleNode = document.getElementById("report-title");
  const dateNode = document.getElementById("report-date");
  const downloadLink = document.getElementById("raw-download-link");

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
    } catch (error) {
      article.innerHTML = `<p class="muted">리포트를 불러오지 못했습니다: ${error.message}</p>`;
    }
  }

  run();
})();
