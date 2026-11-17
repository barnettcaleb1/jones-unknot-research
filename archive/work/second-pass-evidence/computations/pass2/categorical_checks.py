"""Exact checks of published actual Khovanov data and a curve-block criterion.

Data sources:
  Bar-Natan, AGT 2 (2002), p. 356, Out[21] and Out[22].
  Kotelskiy-Watson-Zibrowius, OBS 5 (2022), p. 238, figure-eight formula.
These computations check consequences of published data; they do not compute
homology from a knot diagram or establish knot-realizability of new data.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json


def euler(terms):
    result = Counter()
    for h, q, dimension in terms:
        assert h == int(h)
        result[int(q)] += (-1 if int(h) % 2 else 1) * dimension
    return dict(sorted((q, n) for q, n in result.items() if n))


def vkappa(h_shift, delta_shift):
    # Base V has delta=0, q=-5,-1,1,5, so h=q/2.
    return [(F(q, 2) + h_shift, q + 2 * (h_shift + delta_shift), 1)
            for q in [-5, -1, 1, 5]]


cinquefoil = [(0, -5, 1), (0, -3, 1), (-5, -15, 1),
              (-4, -11, 1), (-3, -11, 1), (-2, -7, 1)]
knot_10132 = [(0, -3, 1), (0, -1, 1), (-7, -15, 1),
              (-6, -11, 1), (-5, -11, 1), (-4, -9, 1),
              (-4, -7, 1), (-3, -9, 1), (-3, -5, 1),
              (-2, -5, 2), (-1, -1, 1)]
assert euler(cinquefoil) == euler(knot_10132)
assert euler([term for term in knot_10132 if term[1] == -1]) == {}

fig8_blocks = [vkappa(F(5, 2), F(11, 2)), vkappa(F(13, 2), F(9, 2))]
fig8 = sum(fig8_blocks, [])
assert euler(fig8) == {11: 1, 15: 1, 23: -1, 27: -1}
assert euler([term for term in fig8 if term[1] in [17, 21]]) == {}

# Derivation of the exact signed-center certificate for sums of V blocks.
# E(V shifted by h=a,delta=b) =
# (-1)^(a-5/2) q^(2(a+b)-5) (1+q^4)(1-q^6).
def certificate(block_shifts):
    result = Counter()
    for a, b in block_shifts:
        exponent = 2 * (a + b) - 5
        parity = a - F(5, 2)
        assert parity.denominator == 1 and exponent.denominator == 1
        result[int(exponent)] += (-1 if int(parity) % 2 else 1)
    return dict(sorted((q, n) for q, n in result.items() if n))


assert certificate([(F(5, 2), F(11, 2)), (F(13, 2), F(9, 2))]) == {11: 1, 17: 1}
results = {
    "common_unreduced_jones": euler(cinquefoil),
    "cinquefoil_rational_Kh_rank": sum(x[2] for x in cinquefoil),
    "10_132_rational_Kh_rank": sum(x[2] for x in knot_10132),
    "10_132_cancelled_top_quantum_grade": -1,
    "figure8_kappa_blocks": [[[str(v) for v in term] for term in block] for block in fig8_blocks],
    "figure8_kappa_euler": euler(fig8),
    "figure8_kappa_cancelled_quantum_grades": [17, 21],
    "figure8_signed_center_certificate": certificate([(F(5, 2), F(11, 2)), (F(13, 2), F(9, 2))]),
    "scope": "Exact algebra on published actual invariants; no new knot or universal noncancellation theorem."
}
destination = Path(__file__).with_suffix('.json')
destination.write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
