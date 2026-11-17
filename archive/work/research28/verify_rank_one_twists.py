"""Exact fixed-identity checks; no braid-word search.

Uses the previously audited generic TL5 link-state module and standard-library
arithmetic. Checks the rank-one three-strand full-twist projector, its regular
classical specialization, and the ten classical subset projectors.
"""
from pathlib import Path
import sys
from itertools import combinations
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'work/pass2'))
from tl5_block import ident, rho, matmul, lincomb, iszero, trace, mul, add

I = ident()
delta = {2: -1, -2: -1}
den = add(mul(delta, delta), {0: -1})
e1 = lincomb(({1: 1}, rho([1])), ({2: -1}, I))
e2 = lincomb(({1: 1}, rho([2])), ({2: -1}, I))
F = lincomb((den, I), ({k: -v for k, v in delta.items()}, e1),
            ({k: -v for k, v in delta.items()}, e2),
            ({0: 1}, matmul(e1, e2)), ({0: 1}, matmul(e2, e1)))
assert iszero(lincomb(({0: 1}, matmul(F, F)),
                     ({k: -v for k, v in den.items()}, F)))
assert trace(F) == den
D = rho([1, 2] * 3)
assert iszero(lincomb((den, D),
                     ({k - 6: -v for k, v in den.items()}, I),
                     ({6: -1, -6: 1}, F)))
assert sum(den.values()) == 3

edges = list(combinations(range(5), 2))
subsets = list(combinations(range(5), 3))
def shadow(S):
    S = set(S)
    return [(-1 if len(set(e) & S) == 2 else
             1 if len(set(e) & S) == 1 else -3) for e in edges]

counts = {}
for S in subsets:
    v = shadow(S)
    assert sum(x*x for x in v) == 18
    for vertex in range(5):
        assert sum(x for e, x in zip(edges, v) if vertex in e) == 0
    for T in subsets:
        w = shadow(T)
        overlap = Fraction(sum(x*y for x, y in zip(v, w))**2, 18**2)
        assert overlap == (1 if S == T else Fraction(1, 9))
        key = str(overlap)
        counts[key] = counts.get(key, 0) + 1

result = {
    'generic_projector_identity': True,
    'generic_projector_rank': 1,
    'full_twist_eigenvalues': ['A^6 (rank 1)', 'A^-6 (rank 4)'],
    'projector_denominator_at_A1': 3,
    'ordered_classical_subset_pairs': counts,
    'scope': 'Fixed polynomial identities and classical projectors only; no kernel found.'
}
print(json.dumps(result, indent=2))
