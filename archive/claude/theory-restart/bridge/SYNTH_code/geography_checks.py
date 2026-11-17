#!/usr/bin/env python3
"""Synthesizer checks (17 Nov 2026) on all kht++ records under theory-restart/ with exactly one rational component.
(1) delta-window: offsets of special delta-gradings from the rational component's delta.
(2) |k| <= 4 * sum_s n_s = dim_F2 kappa  (consequence of P(-1) = -k/4, law (b) of L1, under KWZ geography).
Run: tools/venv/bin/python bridge/SYNTH_code/geography_checks.py  (from theory-restart/)."""
import json, glob, collections, os
os.chdir('/Users/calebbarnett/jones-lanes/theory-restart')
seen = set(); rows = []; offs = collections.Counter()
for f in glob.glob('**/*.jsonl', recursive=True):
    for line in open(f):
        try: r = json.loads(line)
        except Exception: continue
        kh = r.get('khr')
        if not isinstance(kh, list) or not kh: continue
        w = r.get('word')
        if w in seen: continue
        seen.add(w)
        rs = [c for c in kh if isinstance(c, dict) and c.get('type') == 'r']
        ss = [c for c in kh if isinstance(c, dict) and c.get('type') == 's']
        if len(rs) != 1: continue
        dr = float(rs[0]['delta']); k = int(rs[0]['slope'])
        o = [round(float(c['delta']) - dr, 2) for c in ss]
        for x in o: offs[x] += 1
        rows.append((w, k, sum(int(c['len'])//4 for c in ss), o))
print('records:', len(rows))
print('special delta offsets:', sorted(offs.items()))
print('records with a special beyond +-1/2:', sum(1 for r in rows if any(abs(x) > 0.6 for x in r[3])))
print('violations of |k| <= 4*sum n:', sum(1 for r in rows if abs(r[1]) > 4*r[2]))
print('equality cases with specials:', sum(1 for r in rows if r[2] > 0 and abs(r[1]) == 4*r[2]))
