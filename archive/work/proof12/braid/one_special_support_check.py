#!/usr/bin/env python3
"""Exact support checks; the proof, not the finite ranges, gives all n/shifts."""
from collections import defaultdict
from pathlib import Path
import json


def euler(points):
    out = defaultdict(int)
    for q, h in points:
        out[q] += (-1)**h
    return {q: int(c) for q, c in out.items() if c}


def shift(poly, a, sign):
    return {q+a: sign*c for q, c in poly.items()}


def add(a, b):
    out = defaultdict(int, a)
    for q, c in b.items():
        out[q] += c
    return {q: c for q, c in out.items() if c}


rows = []
for n in range(1, 9):
    k = 4*n
    r = [(2*j+1, j) for j in list(range(k-1))+[k]]
    eq = [8*i+d for i in range(n) for d in (-1, 3, 5, 9)]
    e = [(q, (q-k+1)//2) for q in eq]
    R, E = euler(r), euler(e)
    assert len(r) == len(e) == k
    assert len(R) == len(E) == k
    assert add(R, E) == {-1: 1, 1: 1}
    solutions = []
    for a in range(-2*k-4, 5):
        for b in range(-2*k-4, 5):
            for er in (-1, 1):
                for ee in (-1, 1):
                    if add(shift(R, a, er), shift(E, b, ee)) == {-1: 1, 1: 1}:
                        solutions.append([a, b, er, ee])
    assert solutions == [[0, 0, 1, 1]]
    supports = 0
    for ar in range(-2*k, 2*k+1, 2):
        for ae in range(-2*k, 2*k+1, 2):
            points = [(q, h+ar) for q, h in r]+[(q, h+ae) for q, h in e]
            H = max(h for q, h in points)
            top = [(q, h) for q, h in points if h == H]
            assert len(top) == 1
            tq = top[0][0]
            # Every d_r has dh=1,dq=2r>0. Check all potential incoming supports.
            assert not [(q, h) for q, h in points
                        if h == H-1 and tq > q and (tq-q) % 2 == 0]
            supports += 1
    rows.append({'n': n, 'sector_rank': k, 'unique_euler_alignment': solutions[0],
                 'independent_h_shift_cases': supports})

Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n')
print('PASS: eight exact Euler identities and shift-alignment searches; '
      f'{sum(row["independent_h_shift_cases"] for row in rows)} top-class support checks.')
