(function () {
  "use strict";

  const preview = document.getElementById("latest-preview");
  const todayPostLink = document.getElementById("today-post-link");
  const todayRawLink = document.getElementById("today-raw-link");

  async function run() {
    try {
      const index = await window.SiteCommon.loadReportsIndex();
      const latestFile = index.latest || "latest.md";
      const latestItem = Array.isArray(index.items) ? index.items[0] : null;

      const latestDate = latestFile === "latest.md"
        ? (latestItem?.date || "latest")
        : latestFile.replace(/\.md$/, "");

      const detailPath = `./posts/${latestDate}/`;
      const reportPath = `./reports/${latestFile}`;
      const title = latestItem?.title || `AI Trend Digest - ${latestDate}`;
      const excerpt = latestItem?.excerpt || "리포트 본문을 열어 상세 내용을 확인해 주세요.";

      todayPostLink.href = detailPath;
      todayRawLink.href = reportPath;

      preview.innerHTML = `
        <article class="preview-card">
          <div class="meta">${window.SiteCommon.formatDateLabel(latestDate)}</div>
          <h3><a href="${detailPath}">${title}</a></h3>
          <p>${excerpt}</p>
        </article>
      `;
    } catch (error) {
      preview.innerHTML = `<p class="muted">최신 리포트를 불러오지 못했습니다: ${error.message}</p>`;
    }
  }

  run();
})();
