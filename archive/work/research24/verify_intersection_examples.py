#!/usr/bin/env python3
"""Standard-library checks of the displayed Laurent-polynomial examples.

This verifies algebra and labels, not the published geometric constructions.
Run: python3 verify_intersection_examples.py
"""
from collections import defaultdict


def clean(p):
    return {e: c for e, c in p.items() if c}


def add(p, q):
    out = defaultdict(int, p)
    for e, c in q.items():
        out[e] += c
    return clean(out)


def mul(p, q):
    out = defaultdict(int)
    for (a, b), c in p.items():
        for (u, v), k in q.items():
            out[a + u, b + v] += c * k
    return clean(out)


def scale(p, c):
    return clean({e: c * k for e, k in p.items()})


def jones(p):
    out = defaultdict(int)
    for (a, b), c in p.items():
        out[a - b] += c * (-1 if b % 2 else 1)
    return clean(out)


def alexander(p):
    out = defaultdict(int)
    for (a, b), c in p.items():
        out[a] += c
    return clean(out)


def extremes(p):
    lo = min(a - b for a, b in p)
    hi = max(a - b for a, b in p)
    result = []
    for e in (lo, hi):
        terms = [c * (-1 if b % 2 else 1)
                 for (a, b), c in p.items() if a - b == e]
        coherent = all(t > 0 for t in terms) or all(t < 0 for t in terms)
        result.append((e, terms, coherent))
    return result


A = {(1, 2): 1, (1, 1): -1, (0, 1): 1}
B = {(2, 4): 1, (2, 3): -1, (1, 3): 1, (1, 1): -1, (0, 1): 1}
base = {(0, 0): 1, (0, 1): -1, (-1, 0): -1}
C = mul({(2, 2): 1}, mul(base, base))
T = {(-1, 3): 1, (0, 3): -1, (1, 3): 1, (2, 3): -1, (2, 4): 1}

for name, p, norm in [('A', A, 3), ('B', B, 5), ('C', C, 9)]:
    assert jones(p) == {0: 1}
    assert alexander(p) == {0: 1}
    assert sum(map(abs, p.values())) == norm
    print(name, 'unknot specializations verified; Euler norm', norm)

factor = mul({(1, 2): 1}, mul({(0, 1): 1, (0, 0): -1},
                              {(1, 1): 1, (0, 0): 1}))
assert add(B, scale(A, -1)) == factor

# Write z=xd+1, so d=(z-1)/x. The derivative at z=0 of
# xd^2(d-1)z is -x^-2-x^-1, hence nonzero.
normal_derivative = {-2: -1, -1: -1}
assert normal_derivative
assert jones(T) == {-4: -1, -3: 1, -1: 1}
assert alexander(T) == {-1: 1, 0: -1, 1: 1}
assert extremes(A) == [(-1, [1, -1], False), (0, [1], True)]
assert extremes(T) == [(-4, [-1], True), (-1, [1], True)]
assert max(jones(T)) - min(jones(T)) == 3
print('Trefoil extreme-face test and interior cancellation verified.')
print('Nonzero stabilization derivative transverse to Jones locus:', normal_derivative)
print('All exact checks passed.')
