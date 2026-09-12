#!/usr/bin/env python3
"""Real benchmark of every no-credential model across the local gateways."""
import json, time, urllib.request, urllib.error, concurrent.futures as cf, random, os, sys

PROMPT = "What is 7+8? Reply with only the number."
EXPECT = "15"
OUT = "/content/model_benchmark.jsonl"
PROG = "/tmp/bench.progress"

def targets():
    T = []
    # g4f
    try:
        req = urllib.request.Request("http://127.0.0.1:18091/v1/models",
                                     headers={"Authorization": "Bearer g4f-KEEP"})
        for m in json.load(urllib.request.urlopen(req, timeout=20))["data"]:
            T.append(("g4f", m["id"], "http://127.0.0.1:18091/v1/chat/completions", "g4f-KEEP"))
    except Exception as e:
        print("g4f enumerate failed:", e)
    # freellmpool
    try:
        req = urllib.request.Request("http://127.0.0.1:18090/v1/models",
                                     headers={"Authorization": "Bearer flmp-KEEP97"})
        for m in json.load(urllib.request.urlopen(req, timeout=20))["data"]:
            T.append(("freellmpool", m["id"], "http://127.0.0.1:18090/v1/chat/completions", "flmp-KEEP97"))
    except Exception as e:
        print("freellmpool enumerate failed:", e)
    # kilo direct
    try:
        d = json.load(open("/tmp/kilomodels.txt"))
        ids = [m.get("id") for m in (d if isinstance(d, list) else d.get("data", []))]
        for i in ids:
            if i and ":free" in i:
                T.append(("kilo-direct", i, "https://api.kilo.ai/api/gateway/chat/completions", None))
    except Exception as e:
        print("kilo enumerate failed:", e)
    return T

def call(kind, model, url, key, timeout=75):
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": PROMPT}],
                       "max_tokens": 40, "temperature": 0}).encode()
    h = {"Content-Type": "application/json"}
    if key:
        h["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(url, data=body, headers=h)
    t = time.time()
    try:
        d = json.load(urllib.request.urlopen(req, timeout=timeout))
        lat = time.time() - t
        txt = (d["choices"][0]["message"].get("content") or "").strip()
        usage = d.get("usage") or {}
        return {"target": kind, "model": model, "ok": True, "latency_s": round(lat, 2),
                "correct": EXPECT in txt, "answer": " ".join(txt.split())[:80],
                "completion_tokens": usage.get("completion_tokens"),
                "total_tokens": usage.get("total_tokens")}
    except urllib.error.HTTPError as e:
        lat = time.time() - t
        try: msg = e.read().decode()[:150]
        except Exception: msg = str(e)
        return {"target": kind, "model": model, "ok": False, "latency_s": round(lat, 2),
                "correct": False, "answer": "", "error": f"HTTP {e.code}: {' '.join(msg.split())[:120]}"}
    except Exception as e:
        lat = time.time() - t
        return {"target": kind, "model": model, "ok": False, "latency_s": round(lat, 2),
                "correct": False, "answer": "", "error": " ".join(str(e).split())[:120]}

def main():
    T = targets()
    total = len(T)
    open(PROG, "w").write(f"0/{total}")
    done = 0
    results = []
    with open(OUT, "w") as f:
        with cf.ThreadPoolExecutor(max_workers=4) as ex:
            futs = {ex.submit(call, *t): t for t in T}
            for fut in cf.as_completed(futs):
                r = fut.result()
                results.append(r)
                f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
                done += 1
                if done % 5 == 0 or done == total:
                    open(PROG, "w").write(f"{done}/{total}")
    # summary
    ok = [r for r in results if r["ok"]]
    cor = [r for r in ok if r["correct"]]
    ok_sorted = sorted(ok, key=lambda r: r["latency_s"])
    lines = [f"# Benchmark: {total} endpoints", "",
             f"- responded OK: {len(ok)}",
             f"- correct (7+8=15): {len(cor)}",
             f"- failed: {total - len(ok)}", "",
             "## Fastest correct", ""]
    for r in [x for x in ok_sorted if x["correct"]][:40]:
        lines.append(f"- {r['latency_s']:>6.2f}s  {r['target']}  {r['model']}")
    lines += ["", "## All failures", ""]
    for r in results:
        if not r["ok"]:
            lines.append(f"- {r['target']}  {r['model']}  ->  {r.get('error','')}")
    open("/content/model_benchmark_summary.md", "w").write("\n".join(lines))
    open(PROG, "w").write(f"DONE {done}/{total}")

if __name__ == "__main__":
    main()
