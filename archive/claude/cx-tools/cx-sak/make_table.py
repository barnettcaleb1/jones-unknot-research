#!/usr/bin/env python3
"""Collect the pilot results into out/RESULTS.md."""
import json, glob, os, sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import kb
OUT = '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak/out'
rows = []
for f in sorted(glob.glob(os.path.join(OUT, 'pilot_n*_summary.json'))):
    d = json.load(open(f))
    for tag, r in d.items():
        VS = {int(k): v for k, v in r['VS'].items()}
        JS = {int(k): v for k, v in r['JS'].items()}
        rows.append((tag, r, VS, JS))
lines = ["# Pilot results (zero-framed Sakuma links S = U ∪ c of κ_n = [2,−4n,2,2n])", "",
         "| run | det(K) | writhe x | K = ref 2-bridge | crossings of S (raw proj.) | lk(c,U) | V_S = unlink? |",
         "|---|---|---|---|---|---|---|"]
for tag, r, VS, JS in rows:
    lines.append("| %s | %s | %d | %s | %d | %g | %s |" % (tag, r['detK'], r['x'], ','.join(r['match']), r['ncrossS'], r['lkBL'], 'YES' if r['unlink'] else 'NO'))
lines.append("")
for tag, r, VS, JS in rows:
    lines.append("## %s" % tag)
    lines.append("PD files: out/%s_sakuma_proj0.json, out/%s_sakuma_proj1.json; knot: out/%s_knot.json; log: out/%s_log.txt" % (tag, tag, tag, tag))
    lines.append("")
    lines.append("V_S(t) = " + kb.jones_str(VS))
    lines.append("")
    lines.append("J_S(q) [t^(1/2) = −q] = " + kb.poly_str_q(JS))
    lines.append("")
    lines.append("V_S(1) with t^(1/2)=1: %d ; number of terms: %d ; span in t^(1/2): %d..%d" % (sum(VS.values()), len(VS), min(VS), max(VS)))
    lines.append("")
open(os.path.join(OUT, 'RESULTS.md'), 'w').write('\n'.join(lines) + '\n')
print('\n'.join(lines))
