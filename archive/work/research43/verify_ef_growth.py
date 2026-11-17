#!/usr/bin/env python3
"""Exact integer Laurent calculations for Eliahou--Fromentin's family.

The finite checks validate the seeds; the all-r statements follow by the
induction given in divisibility.txt.  No knot enumeration is performed.
"""
from collections import defaultdict
from functools import reduce
from math import gcd
from pathlib import Path
import json

def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for e, a in p.items(): out[e] += a
    return {e: a for e, a in out.items() if a}

def mul(p, q):
    out = defaultdict(int)
    for e, a in p.items():
        for f, b in q.items(): out[e + f] += a * b
    return {e: a for e, a in out.items() if a}

def shift(p, k, c=1): return {e + k: c*a for e, a in p.items()}
def mirror(p): return {-e: a for e, a in p.items()}

# Equations in Section 4.1 of https://arxiv.org/pdf/1610.05560v2,
# with the paper's bracket variable renamed A.
delta = {2: -1, -2: -1}
f10 = {-10: 2, -6: -2, -2: 2, 6: -2, 10: 2, 14: -2, 18: 1}
g10 = {-8: 2, -4: -5, 0: 7, 4: -7, 8: 5, 12: -3, 16: 1}
f = mul(f10, mirror(f10))
g = add(mul(f10, mirror(g10)), mul(g10, mirror(f10)), mul(delta, mul(g10, mirror(g10))))
rows = []
stable_residue = None
for r in range(1, 7):
    N = 2**(r - 1)
    assert min(f) == -28*N and max(f) == 28*N
    assert min(g) == -28*N+2 and max(g) == 28*N-2
    assert f[min(f)] == f[max(f)] == g[min(g)] == g[max(g)] == 2**N
    chi = add(f, shift(g, -6))
    error = add(chi, {0: -1})
    content = reduce(gcd, error.values(), 0)
    assert all(e % 4 == 0 for e in chi)
    assert min(chi) == -28*N-4 and max(chi) == 28*N
    assert content == 2**r
    residue = sorted(e for e, a in error.items() if (a // (2**r)) % 2)
    if r == 2: stable_residue = residue
    if r >= 2:
        assert residue == stable_residue
        assert 56 in residue
    rows.append({
        'r': r, 'N': N, 'diagram_crossings': 20*N+1,
        'min_A': min(chi), 'max_A': max(chi),
        'min_Jones': -7*N, 'max_Jones': 7*N+1, 'span_Jones': 14*N+1,
        'extreme_coefficients': 2**N, 'content_of_V_minus_1': content,
        'height_bits': max(abs(a) for a in error.values()).bit_length(),
    })
    f, g = mul(f, f), add(shift(mul(f, g), 0, 2), mul(delta, mul(g, g)))

result = {'checked_rows': rows, 'stable_mod2_exponents_for_r_at_least_2': stable_residue}
Path(__file__).with_name('ef_quantitative_check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
