#!/usr/bin/env python3
"""Exact Laurent checks for the linear-size satellite collision certificate.

u=q^(1/2); only integer arithmetic is used. Full determinants, not numerical
samples, are computed for all listed small label sets.
"""
from collections import defaultdict
from itertools import permutations
import json
from pathlib import Path


def add(a, b):
    c = defaultdict(int, a)
    for e, v in b.items():
        c[e] += v
    return {e: v for e, v in c.items() if v}


def mul(a, b):
    c = defaultdict(int)
    for e, v in a.items():
        for f, w in b.items():
            c[e+f] += v*w
    return {e: v for e, v in c.items() if v}


def shift(a, e, sign=1):
    return {f+e: sign*v for f, v in a.items()}


def qdim(n):
    return {e: 1 for e in range(1-n, n, 2)}


def divide(a, b):
    """Exact Laurent division, independently checking the remainder."""
    amin, bmin = min(a), min(b)
    r = shift(a, -amin)
    b = shift(b, -bmin)
    q = {}
    while r and max(r) >= max(b):
        e = max(r)-max(b)
        assert r[max(r)] % b[max(b)] == 0
        c = r[max(r)]//b[max(b)]
        q[e] = q.get(e, 0)+c
        r = add(r, shift(b, e, -c))
    assert not r, r
    return shift(q, amin-bmin)


def torus(j, m):
    p = {}
    for a in range(j+1):
        lam = a*(a+1)-j*(j+2)
        p = add(p, shift(qdim(2*a+1), (2*m+1)*lam, (-1)**(j-a)))
    ans = divide(p, qdim(j+1))
    assert all(e % 2 == 0 for e in ans)
    assert mul(ans, qdim(j+1)) == p
    return ans


def determinant(matrix):
    n = len(matrix)
    ans = {}
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = {0: (-1)**inv}
        for i in range(n):
            term = mul(term, matrix[i][p[i]])
        ans = add(ans, term)
    return ans


valuation_checks = []
for j in range(2, 11):
    for m in range(1, 7):
        h = torus(j, m)
        v = -m*j*(j+2)-j*(j+1)//2
        assert min(h) == 2*v
        assert h[min(h)] == (-1)**j
        valuation_checks.append([j, m, v, h[min(h)]])

determinants = []
for labels in ([2], [3], [2, 4], [3, 5], [2, 4, 6], [3, 5, 7],
               [2, 3, 4], [2, 4, 6, 8], [3, 5, 7, 9]):
    s = len(labels)
    mat = [[torus(j, m) for j in labels] for m in range(1, s+1)]
    d = determinant(mat)
    v = sum(-m*j*(j+2)-j*(j+1)//2 for m, j in enumerate(labels, 1))
    c = (-1)**sum(labels)
    assert min(d) == 2*v
    assert d[min(d)] == c
    # Independent finite check of the strict-rearrangement premise.
    scores = [sum((m+1)*labels[p[m]]*(labels[p[m]]+2) for m in range(s))
              for p in permutations(range(s))]
    assert scores.count(max(scores)) == 1
    determinants.append({'labels': labels, 'sample_m': list(range(1, s+1)),
                         'q_valuation': v, 'leading_coefficient': c,
                         'full_determinant_terms': len(d)})

out = {'variable': 'u=q^(1/2)', 'exact_valuation_checks': valuation_checks,
       'exact_full_determinants': determinants,
       'bound': 's probes, one for each possible higher color label; s<=floor(r/2) by pattern parity'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(f'PASS: {len(valuation_checks)} exact colored-torus valuations and '
      f'{len(determinants)} full Laurent determinants, through size four.')
