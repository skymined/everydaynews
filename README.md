# AI Trend Digest

LLM-based daily digest generator for AI News and Hugging Face Papers Top 10.

## Quick Start

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e .
python -m digest run --date 2026-02-19 --out reports/2026-02-19.md --skip-llm
```

## Output

The report always renders two fixed sections:

- `## AI News`
- `## Papers (Hugging Face Top 10)`

## LLM Modes

Default mode is local Qwen via Ollama:
`LLM_MODE=local`, `LOCAL_LLM_BASE_URL=http://127.0.0.1:11434/v1`, `LOCAL_LLM_MODEL=qwen2.5:7b`.

### A) Remote API mode

```bash
set LLM_MODE=api
set LLM_PROVIDER=openai
set OPENAI_API_KEY=...
set OPENAI_MODEL=gpt-4.1-mini
python -m digest run --date 2026-02-19 --out reports/2026-02-19.md
```

Gemini:

```bash
set LLM_MODE=api
set LLM_PROVIDER=gemini
set GEMINI_API_KEY=...
set GEMINI_MODEL=gemini-2.0-flash
python -m digest run --date 2026-02-19 --out reports/2026-02-19.md
```

### B) Local Qwen mode (Ollama default)

```bash
winget install -e --id Ollama.Ollama
ollama pull qwen2.5:7b
```

Then run digest:

```bash
set LLM_MODE=local
set LOCAL_LLM_BASE_URL=http://127.0.0.1:11434/v1
set LOCAL_LLM_MODEL=qwen2.5:7b
python -m digest run --date 2026-02-19 --out reports/2026-02-19.md
```

## CLI options

- `--skip-llm` use heuristic fallback only
- `--window yesterday-kst|since-hours` (default `yesterday-kst`)
- `--since-hours H` used when `--window since-hours`
- `--refresh` ignore cached LLM summaries and regenerate
- `--provider openai|gemini` override API provider

## User-tunable files

- `sources.yaml`
- `prompts/news_classify.md`
- `prompts/news_summarize.md`
- `prompts/paper_summarize.md`
