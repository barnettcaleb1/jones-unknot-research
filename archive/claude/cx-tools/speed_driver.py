#!/usr/bin/env python3
"""speed_driver.py -- time bracket.py on large diagrams, each in a subprocess
with a timeout.  Writes TIMING.md and timing.json."""
import os, sys, json, time, random, subprocess, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
PY = os.path.join(HERE, "venv", "bin", "python")
import twist as T
from bracket import Diagram, greedy_order

PER_CASE_TIMEOUT = float(os.environ.get("CX_TIMEOUT", "100"))
TOTAL_BUDGET = float(os.environ.get("CX_BUDGET", "480"))
t_start = time.perf_counter()
results = []
tmpdir = os.path.join(HERE, "speed_tmp")
os.makedirs(tmpdir, exist_ok=True)

WORKER = r'''
import sys, json, time
sys.path.insert(0, %r)
from bracket import jones_from_pd, pclean
pd = json.load(open(sys.argv[1]))
stats = {}
t0 = time.perf_counter()
V = jones_from_pd(pd, stats=stats)
dt = time.perf_counter() - t0
print(json.dumps({"seconds": dt, "max_states": stats["max_states"], "max_width": stats["max_width"],
                  "V_is_one": pclean(V) == {0: 1}, "V_terms": len(V), "V_at_1": sum(V.values()),
                  "components": stats["components"]}))
''' % HERE
open(os.path.join(tmpdir, "worker.py"), "w").write(WORKER)


def run_case(family, name, pd):
    if time.perf_counter() - t_start > TOTAL_BUDGET:
        results.append(dict(family=family, name=name, n=len(pd), status="skipped (budget)"))
        return None
    order, width = greedy_order(pd)
    path = os.path.join(tmpdir, "case.json")
    json.dump(pd, open(path, "w"))
    try:
        p = subprocess.run([PY, os.path.join(tmpdir, "worker.py"), path], capture_output=True, text=True,
                           timeout=PER_CASE_TIMEOUT)
        if p.returncode != 0:
            r = dict(family=family, name=name, n=len(pd), status="error", err=p.stderr[-300:], greedy_width=width)
        else:
            r = json.loads(p.stdout.strip().splitlines()[-1])
            r.update(family=family, name=name, n=len(pd), status="ok", greedy_width=width)
    except subprocess.TimeoutExpired:
        r = dict(family=family, name=name, n=len(pd), status="timeout >%ds" % PER_CASE_TIMEOUT, greedy_width=width)
    results.append(r)
    print("%-14s %-48s n=%-4d width=%-3s %s" % (family, name, len(pd), width,
          ("%.2fs states=%s" % (r["seconds"], r["max_states"])) if r["status"] == "ok" else r["status"]), flush=True)
    return r


random.seed(7)
# 1. random braid closures: k strands, m crossings (unsimplified)
for k, m in [(4, 60), (6, 60), (8, 80), (10, 100), (10, 200), (12, 60), (12, 120), (14, 60), (16, 40)]:
    word = [random.choice([1, -1]) * random.randint(1, k - 1) for _ in range(m)]
    try:
        pd = T.braid_closure_pd(word, k)
    except ValueError as ex:
        print("skip", k, m, ex)
        continue
    r = run_case("braid", "random %d-strand braid closure, %d cr." % (k, m), pd)
    if r and r["status"].startswith("timeout"):
        break

# 2. unsimplified random planar diagrams from spherogram (random 4-valent maps)
try:
    import spherogram
    for n in [40, 60, 80, 100, 120, 150, 200]:
        L = None
        for simplify in (None, "basic"):
            try:
                L = spherogram.random_link(n, num_components=1, initial_map_gives_link=True, simplify=simplify)
                break
            except Exception as ex:
                print("random_link(simplify=%r) failed: %s" % (simplify, ex))
        if L is None:
            break
        pd = [list(x) for x in L.PD_code()]
        r = run_case("random-map", "random planar knot diagram (asked %d, got %d cr.)" % (n, len(pd)), pd)
        if r and r["status"].startswith("timeout"):
            break
except Exception as ex:
    print("spherogram random maps unavailable:", ex)

# 3. twist knot family / connected sums: trivial width, large n
pd = T.clasp_unknot_pd()
for n in [25, 50, 100]:
    q = T.insert_full_twists(pd, 2, 4, -n)
    run_case("twist", "clasp unknot + %d full twists (%d cr.)" % (n, len(q)), q)

json.dump(results, open(os.path.join(HERE, "timing.json"), "w"), indent=1)
md = ["# TIMING.md -- bracket.py speed on large diagrams (subprocess per case, timeout %ds)\n" % PER_CASE_TIMEOUT,
      "| family | diagram | crossings | greedy width | max states | seconds | status |", "|---|---|---|---|---|---|---|"]
for r in results:
    md.append("| %s | %s | %d | %s | %s | %s | %s |" % (r["family"], r["name"], r["n"], r.get("greedy_width", ""),
              r.get("max_states", ""), ("%.2f" % r["seconds"]) if "seconds" in r else "", r["status"]))
ok = [r for r in results if r["status"] == "ok" and r["seconds"] < 60]
if ok:
    b = max(ok, key=lambda r: r["n"])
    md.append("\nLargest crossing number finished in under 60 s: **%d** (%s, %.1f s, width %s, %s states)." % (
        b["n"], b["name"], b["seconds"], b["greedy_width"], b["max_states"]))
    for fam in dict.fromkeys(r["family"] for r in results):
        fo = [r for r in ok if r["family"] == fam]
        if fo:
            b = max(fo, key=lambda r: r["n"])
            md.append("- %s: %d crossings in %.1f s (%s)." % (fam, b["n"], b["seconds"], b["name"]))
open(os.path.join(HERE, "TIMING.md"), "w").write("\n".join(md) + "\n")
print("wrote TIMING.md")
