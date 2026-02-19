# AI Trend Digest

AI 뉴스와 Hugging Face Papers Top 10을 수집해 일일 리포트를 생성하는 프로젝트입니다.

기본 실행 모드는 로컬 LLM(`Ollama + qwen2.5:7b`)입니다.

## 1. 요구사항

- Python 3.11 이상
- Git
- (기본 모드) Ollama

## 2. 가장 빠른 실행 방법 (로컬 LLM, 권장)

### 2-1. 저장소 준비

```bash
git clone <YOUR_REPO_URL>
cd everydaynews
```

### 2-2. 가상환경 및 패키지 설치

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

### 2-3. Ollama 설치 및 Qwen 모델 다운로드

Windows:

```powershell
winget install -e --id Ollama.Ollama
```

macOS:

```bash
brew install ollama
```

Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

모델 다운로드:

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

## 3. 결과 확인

실행 후 아래 파일이 생성/갱신됩니다.

- `reports/YYYY-MM-DD.md`
- `reports/latest.md`
- `data/digest.sqlite3`

리포트 섹션은 고정입니다.

- `## AI News`
- `## Papers (Hugging Face Top 10)`

## 4. API 모드로 실행 (OpenAI/Gemini)

로컬 모델 대신 원격 API를 쓰려면 `LLM_MODE=api`로 실행합니다.

OpenAI 예시:

Windows PowerShell:

```powershell
$env:LLM_MODE="api"
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="<YOUR_KEY>"
$env:OPENAI_MODEL="gpt-4.1-mini"
python -m digest run
```

macOS/Linux:

```bash
export LLM_MODE=api
export LLM_PROVIDER=openai
export OPENAI_API_KEY=<YOUR_KEY>
export OPENAI_MODEL=gpt-4.1-mini
python -m digest run
```

Gemini 예시:

```bash
export LLM_MODE=api
export LLM_PROVIDER=gemini
export GEMINI_API_KEY=<YOUR_KEY>
export GEMINI_MODEL=gemini-2.0-flash
python -m digest run
```

## 5. 자주 쓰는 옵션

- `--skip-llm`: LLM 없이 휴리스틱만으로 실행
- `--refresh`: 캐시 무시하고 요약 재생성
- `--date YYYY-MM-DD`: 특정 날짜 리포트 생성
- `--out <path>`: 출력 파일 경로 지정
- `--window yesterday-kst|since-hours`
- `--since-hours <N>`

예시:

```bash
python -m digest run --date 2026-02-19 --out reports/2026-02-19.md --refresh
```

## 6. 사용자 커스터마이징 포인트

- 수집 소스/키워드: `sources.yaml`
- 뉴스 분류 프롬프트: `prompts/news_classify.md`
- 뉴스 요약 프롬프트: `prompts/news_summarize.md`
- 논문 요약 프롬프트: `prompts/paper_summarize.md`
- 후처리/요약 로직: `digest/summarize.py`

## 7. 자동화

GitHub Actions 워크플로우가 포함되어 있습니다.

- 파일: `.github/workflows/daily.yml`
- 스케줄: 매일 UTC 00:00
- 수동 실행: `workflow_dispatch`

## 8. 트러블슈팅

- `connection refused`:
  - Ollama 서버가 실행 중인지 확인 (`ollama list` 또는 `http://127.0.0.1:11434` 확인)
- `OPENAI_API_KEY is not set`:
  - API 모드에서 키가 누락된 상태입니다. 로컬 모드로 실행하거나 키를 설정하세요.
- 터미널 한글 깨짐:
  - 파일 저장은 UTF-8일 수 있으므로 `reports/*.md` 파일을 에디터에서 직접 확인하세요.

## 9. 보안 주의사항

- 로컬 LLM 서버는 가능하면 `127.0.0.1`만 사용하세요.
- `0.0.0.0` 공개 바인딩 시 외부 무인증 접근 위험이 생길 수 있습니다.
- API 키는 코드/리포트에 직접 넣지 말고 환경변수 또는 시크릿에만 저장하세요.
