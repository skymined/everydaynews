(function () {
  "use strict";

  const listContainer = document.getElementById("posts-list");

  async function run() {
    try {
      const response = await fetch("../reports.json", { cache: "no-cache" });
      if (!response.ok) {
        throw new Error(`reports.json 로드 실패 (${response.status})`);
      }
      const index = await response.json();
      const items = Array.isArray(index.items) ? index.items : [];

      if (!items.length) {
        listContainer.innerHTML = '<p class="muted">표시할 리포트가 없습니다.</p>';
        return;
      }

      listContainer.innerHTML = items
        .map((item) => {
          const detailPath = `./${item.date}/`;
          const reportPath = `../reports/${item.file}`;
          return `
            <article class="post-card">
              <div class="meta">${window.SiteCommon.formatDateLabel(item.date)}</div>
              <h3><a href="${detailPath}">${item.title || `AI Trend Digest - ${item.date}`}</a></h3>
              <p>${item.excerpt || "요약 없음"}</p>
              <p class="meta"><a href="${detailPath}">자세히 보기</a> · <a href="${reportPath}" target="_blank" rel="noopener noreferrer">원본</a></p>
            </article>
          `;
        })
        .join("\n");
    } catch (error) {
      listContainer.innerHTML = `<p class="muted">목록을 불러오지 못했습니다: ${error.message}</p>`;
    }
  }

  run();
})();
