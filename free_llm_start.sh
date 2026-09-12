#!/usr/bin/env bash
# FREE LLM STACK - zero API keys, zero registration, zero user credentials.
# Starts two local OpenAI-compatible gateways that aggregate no-credential providers.
set -u

FL_PORT=18090
FL_KEY="flmp-KEEP97"
G4_PORT=18091
G4_KEY="g4f-KEEP"

start_freellmpool() {
  if curl -s -m 2 "http://127.0.0.1:${FL_PORT}/v1/models" -H "Authorization: Bearer ${FL_KEY}" >/dev/null 2>&1; then
    echo "[=] freellmpool already up on :${FL_PORT}"; return
  fi
  setsid env FREELLMPOOL_PROXY_KEY="${FL_KEY}" python3 -m freellmpool proxy \
    --host 127.0.0.1 --port "${FL_PORT}" > /tmp/freellmpool-proxy.log 2>&1 < /dev/null &
  echo "[+] freellmpool -> http://127.0.0.1:${FL_PORT}/v1 (key ${FL_KEY})"
}

start_g4f() {
  if curl -s -m 2 "http://127.0.0.1:${G4_PORT}/v1/models" -H "Authorization: Bearer ${G4_KEY}" >/dev/null 2>&1; then
    echo "[=] g4f already up on :${G4_PORT}"; return
  fi
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  setsid env G4F_API_KEY="${G4_KEY}" python3 "${SCRIPT_DIR}/launch_g4f.py" "127.0.0.1:${G4_PORT}" \
    > /tmp/g4f-server.log 2>&1 < /dev/null &
  echo "[+] g4f -> http://127.0.0.1:${G4_PORT}/v1 (key ${G4_KEY})"
}

start_freellmpool
start_g4f
sleep 6

echo
echo "=== endpoint checks ==="
curl -s -m 10 -o /dev/null -w "freellmpool :${FL_PORT} models HTTP:%{http_code}\n" \
  "http://127.0.0.1:${FL_PORT}/v1/models" -H "Authorization: Bearer ${FL_KEY}"
curl -s -m 20 -o /dev/null -w "g4f         :${G4_PORT} models HTTP:%{http_code}\n" \
  "http://127.0.0.1:${G4_PORT}/v1/models" -H "Authorization: Bearer ${G4_KEY}"
echo
echo "=== verified no-credential models ==="
echo "freellmpool : auto | llm7/* | ovh/Qwen3.5-397B-A17B ovh/gpt-oss-120b | kilo/openrouter/free kilo/nvidia/nemotron-3-ultra-550b-a55b:free kilo/stepfun/step-3.7-flash:free"
echo "g4f         : gpt-4 (Yqcloud) | command-r / command-r7b-arabic-02-2025 (HuggingSpace) | gemini-2.5-flash (anon)"
echo "direct      : https://api.kilo.ai/api/gateway/chat/completions (19 ':free' models, NO auth)"
echo
echo "Any OpenAI client: base_url + api_key above. No user keys ever."
