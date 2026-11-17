"""Check the retained table data and displayed Euler-cancellation examples.

Standard library only. This verifies arithmetic, not a fresh computation of
Khovanov homology. The graph theorem is proved in spanning_tree_mechanism.txt.
"""
from collections import defaultdict
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
record = json.loads((HERE / "knotinfo_10_132_subset.json").read_text())
claims = json.loads((HERE / "spanning_tree_checks.json").read_text())
vector = json.loads(record["khovanov_reduced_rational_vector"])
assert vector == claims["10_132"]["reduced_rational_vector"]
assert all(field == 1 and rank > 0 for field, rank, h, q in vector)

def euler(terms):
    polynomial = defaultdict(int)
    for h, q, rank in terms:
        polynomial[q] += rank * (-1 if h % 2 else 1)
    return {q: c for q, c in polynomial.items() if c}

poly = euler([(h, q, rank) for _, rank, h, q in vector])
raw_jones = [int(x) for x in record["jones_polynomial_vector"].strip("{}").split(",")]
lo, hi, *coeffs = raw_jones
assert len(coeffs) == hi - lo + 1
jones = {2 * (lo + i): c for i, c in enumerate(coeffs) if c}
assert poly == jones
assert poly == {int(q): c for q, c in claims["10_132"]["euler_q_polynomial"].items()}
homology_max = max(q for _, _, _, q in vector)
assert homology_max == -2 and max(jones) == -4
assert sum(rank for _, rank, _, _ in vector) == 11
# Tensor products and products of nonzero Laurent polynomials add maxima.
# The arbitrary-m assertion uses these identities, not finite extrapolation.
assert homology_max - max(jones) == 2

torus_terms = claims["T(3,4)"]["reduced_P_terms"]
assert euler(torus_terms) == {6: 1, 10: 1, 16: -1}
assert sum(rank for h, q, rank in torus_terms if q == 12) == 2
assert sum(rank for h, q, rank in torus_terms) == 5
print("Verified table-vector provenance, Jones/Euler equality, rank 11 and exterior gap 2 for 10_132.")
print("Verified T(3,4)'s two hidden q=12 classes and three-term Euler polynomial.")
