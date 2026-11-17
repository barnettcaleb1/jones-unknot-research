#!/usr/bin/env python3
"""Exact independent closed-form/binomial verification. Standard library only."""
from math import comb
import json
from pathlib import Path

def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}

def shift(p, k):
    return {n+k: v for n, v in p.items()}

def mul(p, q):
    return add(*({a+b: x*y} for a, x in p.items() for b, y in q.items()))

def scale(p, v):
    return {k: c*v for k, c in p.items() if c*v}

def closed(L):
    assert L > 0 and L % 2 == 1
    m = (L-1)//2
    seed = {2: 1, 6: 1, 8: -1}
    defect = {2: 1, 4: -1, 6: 1, 8: -1}
    return add(shift(seed, 4*m), *(shift(defect, 4*j) for j in range(m)))

def fibpoly(n):
    if n == 0:
        return {}
    return {n-1-2*j: comb(n-1-j, j) for j in range((n-1)//2+1)}

def basis_from_binomials(v):
    a, b = {}, {}
    for n, c in v.items():
        assert n >= 1
        a = add(a, scale(fibpoly(n-1), c))
        b = add(b, scale(fibpoly(n), c))
    return a, b

def power(p, n):
    out = {0: 1}
    for _ in range(n):
        out = mul(out, p)
    return out

def reconstruct(a, b):
    p = {1: 1, -1: -1}
    return add(
        *(scale(power(p, n), c) for n, c in a.items()),
        *(shift(scale(power(p, n), c), 1) for n, c in b.items())
    )

def latex(p, var="x"):
    out = ""
    for n in sorted(p):
        c = p[n]
        sign = "-" if c < 0 else ("+" if out else "")
        term = str(abs(c)) if n == 0 or abs(c) != 1 else ""
        if n:
            term += var if n == 1 else var+"^{"+str(n)+"}"
        out += sign+term
    return out or "0"

def main():
    records = []
    h = {1: -1, 5: -1}
    p = {1: 1, -1: -1}
    for L in (1, 3, 5, 7, 23):
        v = closed(L)
        a, b = basis_from_binomials(v)
        assert reconstruct(a, b) == v
        assert max(v) == 2*L+6 and v[2*L+6] == -1
        assert max(set(a) | set(b)) == 2*L+5
        assert b[2*L+5] == -1
        assert sum(v.values()) == 1
        prev = {0: 1} if L == 1 else closed(L-2)
        assert add(shift(v, -2), scale(shift(prev, 2), -1)) == mul(p, h)
        records.append({"L": L, "V": v, "a": a, "b": b,
                        "top_x": max(v), "degree_p": 2*L+5,
                        "leading_b": -1, "latex": latex(v)})
        print(L, latex(v), "degree_p", 2*L+5, "leading_b", -1)
    assert records[-1]["b"][51] == -1
    output = {"method": "closed geometric sum + independent binomial basis + exact substitution",
              "cap": 3*3+11+2, "records": records, "all_checks_passed": True}
    Path(__file__).with_name("verification.json").write_text(json.dumps(output, indent=2)+"\n")

if __name__ == "__main__":
    main()
