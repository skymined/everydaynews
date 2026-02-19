# AI Trend Digest

AI 뉴스와 Hugging Face Papers Top 10을 수집해 일일 리포트를 생성하고, `website/` 정적 페이지로 바로 게시하는 프로젝트입니다.

## 1. 구조

- 리포트 생성 경로: `website/reports/`
- 웹 페이지 소스: `website/`
- 자동 리포트 인덱스: `website/reports.json`

## 2. 빠른 실행 (로컬 LLM)

### 2-1. 저장소 준비

```bash
git clone <YOUR_REPO_URL>
cd everydaynews
```

### 2-2. 가상환경/의존성 설치

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

### 2-3. Ollama + Qwen 준비

```bash
ollama pull qwen2.5:7b
```

### 2-4. 리포트 생성

Windows PowerShell:

```powershell
$env:LLM_MODE="local"
$env:LOCAL_LLM_BASE_URL="http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_MODEL="qwen2.5:7b"
python -m digest run
```

macOS/Linux:

```bash
export LLM_MODE=local
export LOCAL_LLM_BASE_URL=http://127.0.0.1:11434/v1
export LOCAL_LLM_MODEL=qwen2.5:7b
python -m digest run
```

생성 결과:

- `website/reports/YYYY-MM-DD.md`
- `website/reports/latest.md`
- `website/reports.json`

필요 시 인덱스만 수동 재생성:

```bash
python website/scripts/build_reports_index.py
```

## 3. API 모드 실행

OpenAI:

```bash
export LLM_MODE=api
export LLM_PROVIDER=openai
export OPENAI_API_KEY=<YOUR_KEY>
export OPENAI_MODEL=gpt-4.1-mini
python -m digest run
```

Gemini:

```bash
export LLM_MODE=api
export LLM_PROVIDER=gemini
export GEMINI_API_KEY=<YOUR_KEY>
export GEMINI_MODEL=gemini-2.0-flash
python -m digest run
```

## 4. 웹페이지 로컬 확인

가볍게 정적 서버로 확인:

```bash
python -m http.server 8000
```

브라우저에서 접속:

- `http://127.0.0.1:8000/website/`

## 5. GitHub 자동화

### Daily 리포트 생성/커밋

- 파일: `.github/workflows/daily.yml`
- 동작:
  - 매일 UTC 00:00 실행
  - `main` 브랜치 기준으로 실행
  - `website/reports/*.md` 생성
  - `website/reports.json` 생성
  - `main` 브랜치로 자동 커밋/푸시

### Website 배포 (GitHub Pages, GitHub Actions)

- 파일: `.github/workflows/pages.yml`
- 동작:
  - `main` 브랜치의 `website/**` 변경 시 자동 배포
  - `website/` 디렉터리를 Pages 아티팩트로 업로드 후 배포

- 저장소 설정:
  - `Settings > Pages > Build and deployment > Source`: `GitHub Actions`
- 주의:
  - `schedule` 트리거는 GitHub 기본 브랜치의 워크플로우 파일을 기준으로 실행됨
  - 기본 브랜치가 `main`이면, 스케줄 워크플로우는 `main`의 `.github/workflows/daily.yml`로 동작함

## 6. 커스터마이징 포인트

- 수집 소스/키워드: `sources.yaml`
- 뉴스 분류 프롬프트: `prompts/news_classify.md`
- 뉴스 요약 프롬프트: `prompts/news_summarize.md`
- 논문 요약 프롬프트: `prompts/paper_summarize.md`
- 후처리 로직: `digest/summarize.py`

## 7. 보안 체크

- API 키는 환경변수/Secrets만 사용
- 로컬 LLM 서버는 `127.0.0.1` 바인딩 권장
- `.env`, 키 파일(`*.key`, `*.pem`) 커밋 금지
