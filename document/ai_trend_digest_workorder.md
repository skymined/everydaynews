# AI 트렌드 데일리 다이제스트 자동 생성기 — 작업지시서 (Markdown 저장)

> 목표: 매일 “유명 AI 기업/기관의 공식 소식 + Hugging Face Daily Papers Top 10”을 수집·요약·해석(트렌드/의미/추가 조사 포인트)하여 **하나의 Markdown 파일**로 저장한다.  
> 출력은 “오늘의 카드 1장”이 아니라 **아카이브 가능한 리서치 노트** 형태(출처/근거/불확실성/후속 조사 쿼리 포함)여야 한다.

---

## 0) 핵심 요구사항(반드시 만족)

- **산출물:** `reports/YYYY-MM-DD.md` 1개(옵션: `reports/latest.md`도 갱신)
- **입력 소스:**
  - (필수) OpenAI / Google(또는 Google AI/Developers, Research) / Hugging Face Blog / Hugging Face Papers(Top 10)
  - (확장) Microsoft Research, AWS ML, NVIDIA, arXiv RSS 등
- **중점:** “요약”이 아니라 **트렌드 이해 + 더 찾아보기(추가 조사)**  
  - “무슨 일이 있었는가” + “왜 중요한가” + “무엇이 바뀌었나(기술/정책/제품 관점)” + “다음에 뭘 보면 좋나”
- **품질 제약:**
  - 각 항목은 **출처 URL**을 반드시 포함
  - 추측/불확실성은 명시 (Confidence/Unknown)
  - 과장 금지, 원문에 없는 숫자/스펙/성능은 “불명” 처리
- **안전/윤리:** robots.txt 존중, 과도한 트래픽 금지(레이트리밋/캐시/ETag), 유료/저작권 본문 무단 저장 금지

---

## 1) 추천 기술 스택(가성비 + 안정성)

- 언어: Python 3.11+
- 의존성(권장)
  - 수집: `httpx`, `feedparser`, `beautifulsoup4`, `lxml`
  - 본문 추출: `trafilatura` (또는 `readability-lxml`)
  - 캐시/중복: `sqlite`(표준), 또는 `requests-cache`
  - 스키마 검증: `pydantic`
  - 설정: `pyyaml`
  - CLI: `typer`(선택)
- LLM 호출
  - OpenAI: 공식 SDK `openai` (Python) (Responses API 기반 권장)
  - Gemini: `google-genai` (Google GenAI SDK)

> NOTE: LLM 없이도 “수집+정리”까지만 만들고, 나중에 요약 파트를 붙일 수 있게 **Provider 추상화**를 강제한다.

---

## 2) 저장 구조(레포/폴더)

```
ai-trend-digest/
  README.md
  pyproject.toml
  sources.yaml
  prompts/
    item_summary.md
    day_synthesis.md
    theme_deepdive.md
  digest/
    __init__.py
    cli.py
    config.py
    fetch.py
    extract.py
    dedupe.py
    llm/
      __init__.py
      base.py
      openai_provider.py
      gemini_provider.py
    summarize.py
    synthesize.py
    render.py
    store.py
  data/
    digest.sqlite3
  reports/
    2026-02-19.md
    latest.md
  .github/workflows/
    daily.yml
```

---

## 3) 소스 정의(`sources.yaml`) — “RSS 우선, 없으면 HTML 스크랩”

아래는 예시. 실제 구현에서는 `type`에 따라 파서를 분기한다.

```yaml
defaults:
  max_items_per_source: 10
  user_agent: "ai-trend-digest/0.1 (+https://github.com/<you>/ai-trend-digest)"
  timeout_sec: 30
  concurrency: 6

sources:
  - id: openai_news
    name: OpenAI News
    type: rss
    url: "https://openai.com/news/rss.xml"
    max_items: 10

  - id: google_the_keyword
    name: Google Blog (The Keyword)
    type: html   # RSS가 있긴 하지만 페이지 구조가 더 안정적일 수도 있음
    url: "https://blog.google/"
    max_items: 10
    selectors:
      item: "article"
      title: "h2, h3"
      link: "a"

  - id: google_research
    name: Google Research Blog
    type: html
    url: "https://research.google/blog/"
    max_items: 10

  - id: microsoft_research
    name: Microsoft Research Blog
    type: rss
    url: "https://www.microsoft.com/en-us/research/blog/feed/"
    max_items: 10

  - id: aws_ml_blog
    name: AWS Machine Learning Blog
    type: rss
    url: "https://aws.amazon.com/blogs/machine-learning/feed/"
    max_items: 10

  - id: nvidia_dev_blog
    name: NVIDIA Developer Blog
    type: rss
    url: "https://developer.nvidia.com/blog/feed/"
    max_items: 10

  - id: arxiv_cs_ai
    name: arXiv cs.AI (new)
    type: rss
    url: "https://export.arxiv.org/rss/cs.AI"
    max_items: 10

  - id: hf_blog
    name: Hugging Face Blog
    type: rss
    url: "https://huggingface.co/blog/feed.xml"
    max_items: 10

  - id: hf_papers_today
    name: Hugging Face Papers (Top today)
    type: html
    url: "https://huggingface.co/papers"
    max_items: 10
```

---

## 4) 데이터 모델(필수 필드)

`pydantic` 모델 권장.

```python
class Item(BaseModel):
    source_id: str
    source_name: str
    title: str
    url: str
    published_at: datetime | None
    fetched_at: datetime

    # optional
    author: str | None = None
    summary_raw: str | None = None     # RSS summary
    content_text: str | None = None    # extracted main text (shortened)
    content_hash: str | None = None

    # LLM outputs
    llm_summary_kr: str | None = None
    why_it_matters: str | None = None
    key_terms: list[str] = []
    tags: list[str] = []
    confidence: float | None = None
    followup_queries: list[str] = []
```

---

## 5) 파이프라인 설계(매일 실행)

### 단계 A. 수집(Fetch)
- RSS: `feedparser.parse(url)`
- HTML: `httpx.get(url)` 후 `BeautifulSoup`으로 목록에서 **(title, link, date)** 추출
- **레이트리밋**: host별 1~2 rps, 전체 동시성 제한(semaphore)
- **캐시**: ETag/Last-Modified 저장(가능하면), 동일 URL 반복 다운로드 방지

### 단계 B. 중복 제거(Dedupe)
- URL 정규화: UTM 제거, trailing slash normalize
- `sqlite`에 `seen(url_hash)` 저장
- 이미 본 링크는 스킵(단, “오늘 날짜로 새로 올라온데 링크 동일” 같은 경우는 갱신 옵션)

### 단계 C. 본문 추출(Extract)
- `trafilatura` 또는 `readability-lxml`로 main content만 뽑음
- 토큰 예산을 위해:
  - `content_text`는 **최대 N자(예: 6,000~10,000자)**로 잘라 LLM 입력
  - 가능하면 “리드(요약문/첫 단락) + 핵심 섹션” 위주

### 단계 D. 항목 요약(Item Summarize)
- 각 Item에 대해 LLM 1회 호출(또는 2-pass)
- 출력은 **구조화된 JSON**으로 받도록 강제(파싱 실패 시 재시도)

### 단계 E. 하루 트렌드 합성(Day Synthesis)
- 전체 item 요약을 묶어 1회 호출
- Top themes 3~5개, 공통 서사, 기술적 변화, 위험/기회, 다음에 볼 것(링크/키워드)

### 단계 F. Markdown 렌더(Render)
- 아래 템플릿대로 파일 1개 생성
- 마지막에 “내일 확인할 체크리스트” 생성

---

## 6) 프롬프트 설계(핵심) — *트렌드+추가조사 중심*

### 6.1 Item 요약 프롬프트(`prompts/item_summary.md`)
- **역할:** “리서치 어시스턴트(편집자+애널리스트)”
- **규칙:** 원문 기반, 추정은 추정이라 말함, 과장 금지, 링크 포함

**SYSTEM(예시)**  
- 너는 기술 리서치 편집자다.  
- 출력은 반드시 JSON 하나.  
- 원문에 없는 수치/스펙/성능을 만들어내지 마라. 불명은 `unknown`.  
- 한국어로 쓰되, 고유명사/모델명/핵심 용어는 원문 표기(영문) 병기.

**USER(예시 입력 형식)**  
- `title`, `url`, `published_at`, `source`, `content_excerpt`(본문 발췌) 제공

**JSON 스키마(예시)**  
```json
{
  "llm_summary_kr": "3~5문장 핵심 요약",
  "what_changed": "이전과 달라진 점 1~2문장",
  "why_it_matters": "영향/의미 3~5문장 (누구에게/무엇에)",
  "key_terms": ["..."],
  "tags": ["product", "policy", "research", "release", "security", "benchmark"],
  "confidence": 0.0,
  "unknowns": ["원문에 없는 중요한 공백/불확실성"],
  "followup_queries": ["검색 쿼리 2~4개"],
  "one_liner": "한 줄 헤드라인"
}
```

### 6.2 Day 합성 프롬프트(`prompts/day_synthesis.md`)
입력: `[{source,title,url,one_liner,why_it_matters,tags,key_terms}, ...]`

출력(권장):
- `themes`: 3~5개
  - theme name
  - narrative(무슨 흐름인지)
  - supporting_items(관련 url 3~6개)
  - implications(1주~3개월 관점)
  - watchlist(내일 볼 지표/키워드)
  - followup_queries(더 파볼 질문/검색어)

### 6.3 Theme Deep-dive 프롬프트(`prompts/theme_deepdive.md`)
- theme별로 “리서치 플랜” 뽑기:
  - 읽을 만한 2차 자료 유형(논문/블로그/표준/레포)
  - 질문 5개(“확인해야 트렌드가 진짜인지”)
  - 다음 액션(코드로 실험하면 뭘 하면 되는지)

---

## 7) Markdown 출력 템플릿(권장)

```md
# AI Trend Digest — 2026-02-19

## TL;DR (오늘의 큰 흐름 3~5줄)
- ...
- ...

## Top Themes
### 1) {Theme}
- Narrative:
- Why now:
- Implications (1~3 months):
- Watchlist:
- Follow-up queries:
- Supporting links:
  - ...

## Source-wise Highlights
### OpenAI News
- **{one_liner}** — {title}  
  - 링크: {url}
  - 요약: ...
  - 왜 중요?: ...
  - 불확실/확인 필요: ...
  - 태그: ...
  - 추가 조사 쿼리: ...

### Hugging Face Papers (Top 10)
1. {paper_title} (arXiv:{id}) — {url}
   - 한 줄: ...
   - 핵심: ...
   - novelty/limitations: ...
   - follow-ups: ...

## What I would investigate next (내일/이번 주 할 일)
- ...
```

---

## 8) 구현 상세(코드 작업 지시)

### 8.1 CLI (`digest/cli.py`)
필수 명령:
- `python -m digest run --date 2026-02-19 --out reports/2026-02-19.md`
- 옵션:
  - `--provider openai|gemini`
  - `--max-items 10`
  - `--skip-llm` (수집만)
  - `--since-hours 36` (최신성 필터)

### 8.2 Store (`digest/store.py`)
- sqlite 테이블:
  - `seen(url_hash PRIMARY KEY, url, first_seen_at, last_seen_at, source_id)`
  - `items(item_id PRIMARY KEY, url_hash, title, published_at, json_summary, ...)`
- 기능:
  - `is_seen(url) -> bool`
  - `mark_seen(url)`
  - `upsert_item(item)`

### 8.3 Fetch/Extract
- `fetch.py`: `fetch_source(source_cfg) -> list[RawItem]`
- `extract.py`: `extract_main_text(url) -> str`
- 실패 처리:
  - 4xx/5xx, timeout, 파서 실패 시 로그 남기고 스킵
  - HTML 구조 변경 대비: selector 실패하면 fallback(links only)

### 8.4 LLM Provider 추상화 (`digest/llm/base.py`)
```python
class LLMProvider(Protocol):
    def summarize_item(self, payload: dict) -> dict: ...
    def synthesize_day(self, payload: dict) -> dict: ...
```

- OpenAIProvider: Responses API 사용(Structured Outputs/JSON 강제)
- GeminiProvider: google-genai 사용(가능하면 JSON 모드)

### 8.5 비용/속도 제어
- 1일 최대 호출 수:
  - sources (대략 6~10개) × 10 items = 60~100 items → 그대로 다 요약하면 비쌈
- **전략(권장): “선별→요약”**
  1) 1차 스코어링(LLM 없이): 제목 키워드 + 출처 중요도 + recency
  2) 상위 N개(예: 25~40개)만 본문 추출/요약
  3) HF papers는 top 10 고정

---

## 9) 자동 실행(스케줄)

### 옵션 A: GitHub Actions (추천)
- `.github/workflows/daily.yml`
- cron은 UTC 기준이므로 KST(UTC+9)에 맞춰 설정
- 실행 후 `reports/` 커밋/푸시

### 옵션 B: 로컬 크론
- `crontab -e`
- `0 9 * * * cd /path/ai-trend-digest && ./run.sh`

---

## 10) 완료 기준(Definition of Done)

- [ ] `sources.yaml`로 소스 확장/축소 가능
- [ ] `python -m digest run` 한 번으로 `reports/YYYY-MM-DD.md` 생성
- [ ] 중복 링크는 스킵되고 sqlite에 기록
- [ ] 각 항목에 URL 포함 + 불확실성 표시
- [ ] HF Papers top 10이 매일 포함
- [ ] “Top Themes” 섹션이 실제로 **여러 소스 요약을 묶어** 만든 흔적이 있음
- [ ] 실패해도 전체 작업이 중단되지 않고 로그로 남음

---

## 11) (선택) 추천 확장 아이디어

- 주간 리포트: `weekly/YYYY-WW.md` 생성(테마 추이/빈도)
- 태그 기반 인덱스: `index.md`에 tags → 링크 모아두기
- Obsidian 호환: frontmatter 추가(`date`, `tags`, `sources`)
