# Keyless LLM Stack

OpenAI-compatible LLM access with **zero API keys, zero registration, zero user credentials**.
Everything is driven by public keyless endpoints — tested live, end to end.

- **Live site:** https://mn3-99.github.io/keyless-llm-stack/
- **Always-hosted smart API (no auth):** `https://api.kilo.ai/api/gateway` with `model=kilo-auto/free`
- **Auto-refresh:** a GitHub Actions workflow re-runs the whole benchmark daily and commits fresh numbers.

## What's inside

| File | Purpose |
|---|---|
| `free_llm_start.sh` | One-shot launcher: starts two local OpenAI-compatible gateways (`freellmpool` on :18090, `g4f` on :18091) and verifies them. |
| `benchmark_models.py` | Real benchmark harness that probes **every model** on both gateways + the Kilo gateway direct, measuring latency, correctness, and errors. |
| `model_benchmark_report.md` | Full results report (fastest correct models, per-worker family, failure taxonomy). |
| `model_benchmark.jsonl` | Raw measurements, one JSON object per model. |

## Quickstart

```bash
git clone https://github.com/mn3-99/keyless-llm-stack.git
cd keyless-llm-stack
pip install g4f freellmpool

./free_llm_start.sh
```

Then point any OpenAI client at:

```
freellmpool  http://127.0.0.1:18090/v1   model=auto
g4f          http://127.0.0.1:18091/v1   model=gpt-4
```

The `Bearer` keys printed by the launcher are **local-only**, generated per launch —
no external service ever sees a credential from you.

## Verified keyless provider pool (no auth at all)

- **OVHcloud AI Endpoints** — `Qwen3.5-397B-A17B`, `gpt-oss-120b`, `Qwen3-Coder-30B`
- **Kilo Gateway (direct, no auth)** — 17 `:free` models incl. `nvidia/nemotron-3-ultra-550b-a55b:free`, `openrouter/free`, `stepfun/step-3.7-flash:free`
- **LLM7** — `default`, `fast`, `codestral-latest`
- **g4f no-credential providers** — `gpt-4` (Yqcloud), Cohere `command-r*` family (incl. Arabic `command-r7b-arabic`), Gemini anonymous tier

## Benchmark headline (329 routes probed, on this machine)

- 64 responded OK, **49 answered correctly** (7+8=15)
- Fastest correct: `llm7/codestral-latest` **0.34s**, `llm7/default` **0.38s**
- Best quality/speed: `kilo/nvidia/nemotron-3-ultra-550b-a55b:free` ~1.2s, `gpt-4` (Yqcloud) ~3.3s
- Remaining g4f routes fail because they require real authentication — not a defect of this stack.

## Notes

- Upstream public endpoints change; rerun `benchmark_models.py` to re-verify the pool live.
- Be polite to the public endpoints (bounded concurrency, short timeouts built in).