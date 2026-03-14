# AI Trend Digest

Gemini를 우선 사용해 오늘의 AI 뉴스와 커뮤니티 반응, Hugging Face Top 10 Papers를 모아 일일 리포트를 만들고 `website/` 정적 페이지로 자동 발행하는 프로젝트입니다.

## 구조

- 리포트 마크다운: `website/reports/`
- 웹 페이지 소스: `website/`
- 자동 인덱스: `website/reports.json`
- 스케줄 실행: `.github/workflows/daily.yml`

## 수집 범위

- 공식 블로그: OpenAI, Google DeepMind, Google Research, Microsoft Research, AWS ML, NVIDIA
- 검색형 뉴스: Google News AI 검색 RSS
- 소셜/커뮤니티: X 최근 검색, Threads 최근 게시물, Reddit
- 커뮤니티: Reddit `r/MachineLearning`, `r/LocalLLaMA`, `r/artificial`
- 논문: Hugging Face Papers 날짜별 Top 10

Hugging Face가 당일 페이지를 아직 열지 않은 경우에는 가장 최근 공개된 날짜의 Top 10을 가져오고, 리포트에 기준 날짜를 함께 표시합니다.

## 로컬 실행

### 1. 설치

Windows PowerShell:

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

### 2. `.env` 준비

프로젝트 루트의 `.env`를 자동으로 읽습니다.

```dotenv
LLM_MODE=api
LLM_PROVIDER=gemini
GEMINI_API_KEY=YOUR_GEMINI_KEY
GEMINI_MODEL=gemini-2.5-flash
X_BEARER_TOKEN=YOUR_X_BEARER
THREADS_ACCESS_TOKEN=YOUR_THREADS_TOKEN
```

Gemini 호출이 실패하면 규칙 기반 요약으로 폴백합니다.
X와 Threads 토큰이 없으면 해당 소스는 자동으로 건너뜁니다.

### 3. 리포트 생성

```powershell
python -m digest run
```

특정 날짜를 다시 만들려면:

```powershell
python -m digest run --date 2026-03-14 --refresh
```

생성 결과:

- `website/reports/YYYY-MM-DD.md`
- `website/reports/latest.md`
- `website/reports.json`
- `website/posts/YYYY-MM-DD/index.html`

인덱스만 다시 만들려면:

```powershell
python website/scripts/build_reports_index.py
```

## 웹 확인

```powershell
python -m http.server 8000
```

브라우저:

- `http://127.0.0.1:8000/website/`

## 자동 발행

### GitHub Actions

파일: `.github/workflows/daily.yml`

- 매일 `00:00 UTC`, 즉 `09:00 KST`에 실행
 - 매일 `22:00 UTC`, 즉 `07:00 KST`에 실행
- Gemini로 리포트를 생성
- `website/reports/`, `website/posts/`, `website/reports.json`을 갱신
- `main` 브랜치로 자동 커밋/푸시

필수 GitHub Secret:

- `GEMINI_API_KEY`

선택 GitHub Secret:

- `X_BEARER_TOKEN`
- `THREADS_ACCESS_TOKEN`

### GitHub Pages

파일: `.github/workflows/pages.yml`

- `website/**` 변경 시 자동 배포
- `website/` 디렉터리를 GitHub Pages에 게시

## 커스터마이징 포인트

- 수집 소스/우선순위: `sources.yaml`
- 뉴스 분류 프롬프트: `prompts/news_classify.md`
- 뉴스 요약 프롬프트: `prompts/news_summarize.md`
- 논문 요약 프롬프트: `prompts/paper_summarize.md`
- 렌더링 포맷: `digest/render.py`

## 보안

- `.env`는 `.gitignore`에 포함되어 커밋되지 않습니다.
- API 키는 로컬 `.env` 또는 GitHub Secrets로만 관리하세요.
