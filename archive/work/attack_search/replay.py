#!/usr/bin/env python3
"""Recheck the saved bounded search without rerunning unknot simplification."""
import json
from search import ROOT, bracket, jones_a, knot, validate
from certify import verify
from alexander import alexander

validate()
counts=json.loads((ROOT/'search_counts.json').read_text())
rows=json.loads((ROOT/'exact_hits.json').read_text())
certs=json.loads((ROOT/'unknot_certificates.json').read_text())
words=[list(map(int,x.split())) for x in (ROOT/'modular_hits.txt').read_text().splitlines()]
assert len(words)==sum(x['modular_hits'] for x in counts['lengths'])
assert len(rows)==len(words)==len(certs)
assert alexander([1,2,3])=={0:1}
assert alexander([1,1,1,2,3])=={0:1,1:-1,2:1}
assert alexander([1,-2,1,-2,3])=={0:1,1:-3,2:1}
for i,(w,r,c) in enumerate(zip(words,rows,certs)):
    assert w==r['word']==c['word']
    assert knot(w) and r['knot']
    v=jones_a(w)
    assert v=={int(k):x for k,x in r['jones_A'].items()}=={0:1}
    assert alexander(w)=={0:1}
    if c['certified_unknot']:verify(4,w,c['certificate'])
    else:assert c['certificate'] is None
checks=0
for line in (ROOT/'modular_checks.txt').read_text().splitlines():
    value,*w=map(int,line.split());p=counts['prime'];a=counts['A']
    assert sum(c*pow(a,e,p) for e,c in bracket(w).items())%p==value
    checks+=1
print('Recomputed exactly:',len(rows),'Jones=1 and Alexander=1 polynomials.')
print('Replayed unknot certificates:',sum(r['certified_unknot'] for r in certs))
print('Unresolved by this bounded simplifier:',sum(not r['certified_unknot'] for r in certs))
print('Exact vs. finite-field cross-checks:',checks)
