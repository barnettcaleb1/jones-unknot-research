"""Exact checks of the three published unknot braid polynomials."""
from collections import Counter
import json
from pathlib import Path


def add(*polys):
    out = Counter()
    for p in polys:
        for m, c in p.items():
            out[m] += c
    return {m: c for m, c in out.items() if c}


def mul(p, q):
    out = Counter()
    for (a, b), c in p.items():
        for (e, f), g in q.items():
            out[a + e, b + f] += c * g
    return {m: c for m, c in out.items() if c}


def neg(p):
    return {m: -c for m, c in p.items()}


def specialize(p, jones=False):
    out = Counter()
    for (a, b), c in p.items():
        out[a - b if jones else a] += c * (
            (-1 if b % 2 else 1) if jones else 1
        )
    return {e: c for e, c in out.items() if c}


A = {(1, 2): 1, (1, 1): -1, (0, 1): 1}
B = {(2, 4): 1, (2, 3): -1, (1, 3): 1, (1, 1): -1, (0, 1): 1}
factor = {(0, 0): 1, (0, 1): -1, (-1, 0): -1}
C = mul({(2, 2): 1}, mul(factor, factor))
ideal = mul({(0, 1): 1, (0, 0): -1}, {(1, 1): 1, (0, 0): 1})
assert add(B, neg(A)) == mul({(1, 2): 1}, ideal)
assert add(C, neg(B)) == mul({(1, 1): -1, (0, 1): 1}, ideal)
out = []
for name, p in zip(("sigma_1", "sigma_1 sigma_2", "conjugate"), (A, B, C)):
    assert specialize(p) == specialize(p, True) == {0: 1}
    out.append({
        "braid": name,
        "terms": [[a, b, c] for (a, b), c in sorted(p.items())],
        "rank_lower_bound": sum(map(abs, p.values())),
        "Alexander": "1", "Jones": "1",
    })
assert [r["rank_lower_bound"] for r in out] == [3, 5, 9]
Path(__file__).with_name("quantum_floer_polynomial_checks.json").write_text(
    json.dumps(out, indent=2)
)
print("Verified both factorizations, both specializations, and rank bounds 3,5,9.")
