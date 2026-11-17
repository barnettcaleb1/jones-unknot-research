#!/usr/bin/env python3
"""Exact cabling-coefficient certificate in u=q^(1/4), standard library only."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json


def add(a, b):
    c = defaultdict(int, a)
    for e, v in b.items():
        c[e] += v
    return {e: v for e, v in c.items() if v}


def qdim(n):
    return {e: 1 for e in range(2*(1-n), 2*n, 4)}


def coefficients(r, N):
    rows = []
    for t in range(1-N, N, 2):
        # t=2k, and 4 times the q exponent is integral.
        signed_color = r*t+1
        M = abs(signed_color)
        exponent_u = r*(N*N-1)-t*(r*t+2)
        sign = 1 if signed_color > 0 else -1
        numerator = {e+exponent_u: sign*c for e, c in qdim(M).items()}
        val = Fraction(min(numerator)-min(qdim(N)), 4)
        k = Fraction(t, 2)
        predicted = (Fraction(r*(N*N-1), 4)-k*(r*k+1)
                     -Fraction(M-1, 2)+Fraction(N-1, 2))
        assert val == predicted
        rows.append((M, val, numerator))
    rows.sort()
    assert len({M for M, val, num in rows}) == N
    assert all(rows[i][1] > rows[i+1][1] for i in range(N-1))
    assert rows[-1][0] == r*(N-1)+1
    assert rows[-1][1] == 0
    total = {}
    for M, val, num in rows:
        total = add(total, num)
    assert total == qdim(N), (r, N, total)
    return rows


checks = []
subset_checks = 0
for r in range(2, 10):
    for N in range(2, 21):
        rows = coefficients(r, N)
        if r <= 5 and N <= 8:
            for count in range(1, N+1):
                for selected in combinations(rows, count):
                    total = {}
                    for M, val, num in selected:
                        total = add(total, num)
                    assert total
                    subset_checks += 1
        checks.append({'winding': r, 'color': N,
                       'target_colors': [M for M, val, num in rows],
                       'q_valuations': [str(val) for M, val, num in rows]})

out = {'variable': 'u=q^(1/4)', 'coefficient_checks': checks,
       'nonempty_subset_checks': subset_checks,
       'formula': 'C_r=(one meridian,r longitudes); all framings zero',
       'largest_color_iteration': 'N_a=r^a+1, starting N_0=2'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(f'PASS: {len(checks)} exact cabling coefficient sums and valuation orderings; '
      f'{subset_checks} full nonempty subset sums.')
