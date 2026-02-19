(function () {
  "use strict";

  const listContainer = document.getElementById("posts-list");

  async function run() {
    try {
      const index = await window.SiteCommon.loadReportsIndex("../reports.json");
      const items = Array.isArray(index.items) ? index.items : [];

      if (!items.length) {
        listContainer.innerHTML = '<p class="muted">표시할 리포트가 없습니다.</p>';
        return;
      }

      listContainer.innerHTML = items
        .map((item) => {
          const detailPath = `./${item.date}/`;
          const title = window.SiteCommon.normalizeDigestTitle(item.title || `IMDIGEST - ${item.date}`);
          return `
            <article class="post-card">
              <div class="meta">${window.SiteCommon.formatDateLabel(item.date)}</div>
              <h3><a href="${detailPath}">${title}</a></h3>
              <p>${item.excerpt || "요약 없음"}</p>
              <p class="meta"><a href="${detailPath}">자세히 보기</a></p>
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
