#!/usr/bin/env python3
"""Compare N(T) read from the stored chain files (my parser) with tools/gtilde.py jset on k138.jsonl."""
import json, sys, os, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import gtilde
from chain import b_generators, read_chains, B
SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'
recs = [json.loads(l) for l in open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/k138.jsonl')]
print('records', len(recs))
bad = 0; nonstandard = []
out = {}
for r in recs:
    name = r['file'].replace('^', '-')
    path = os.path.join(SI, name, 'cxBNr-c2-qs')
    if not os.path.exists(path):
        print('missing chain file', name); bad += 1; continue
    bg = b_generators(path)
    khr = r['khr']
    ok_valid = gtilde.valid(khr)
    js = gtilde.jset(khr) if ok_valid else None
    if js is None:
        nonstandard.append((name, len(bg), [(c['type'], c['len'], c['slope']) for c in khr]))
        out[name] = bg
        continue
    k, j, pts = js
    hq = sorted((q // 2 - d, q) for q, d in pts)
    assert all(q % 2 == 0 for q, d in pts)
    if hq != bg:
        bad += 1
        print('MISMATCH', name, 'chain', bg, 'jset', hq)
    out[name] = bg
print('mismatches', bad, ' nonstandard for gtilde:', nonstandard)
json.dump(out, open('N_from_chains.json', 'w'))
dims = collections.Counter(len(v) for v in out.values())
print('dim N distribution', sorted(dims.items()))
