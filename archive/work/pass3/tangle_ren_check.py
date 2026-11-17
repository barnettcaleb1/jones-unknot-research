"""Exact independent state-sum audit of Ren arXiv:2609.11084v2, published PD.

Keeps component 1 as an annular axis; resolves the 12 self-crossings of component 0.
Essential state circles are detected by their linking number with the axis.
"""
from pathlib import Path
import sys, json
from collections import defaultdict
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'braid_classification/packages'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'generic'))
import regina
from spherogram import Link
from tangle_unit_check import add, neg, mul, shift, ONE, DELTA

PD = [(25,5,26,4),(36,11,37,12),(10,35,11,36),(15,34,16,35),
      (28,34,29,33),(17,13,18,12),(14,22,15,21),(1,33,2,40),
      (31,27,32,26),(23,3,24,2),(3,25,4,24),(18,7,19,8),
      (20,9,21,10),(39,1,40,32),(5,30,6,31),(29,22,30,23),
      (8,19,9,20),(6,14,7,13),(37,16,38,17),(38,28,39,27)]
L = Link(PD)
K = L.sublink(0)
self_crossings = [c for c in L.crossings if all(v == 0 for v in c.strand_components)]
cross_index = {c: i for i, c in enumerate(self_crossings)}
nodes = {(c, i) for c in L.crossings for i in range(4) if c.strand_components[i] == 0}
annular = defaultdict(dict)
linking_numbers = set()
state_features = []
for state in range(1 << len(self_crossings)):
    remaining = set(nodes)
    essential = contractible = 0
    while remaining:
        first = next(iter(remaining))
        h = first
        signed_sum = 0
        while True:
            c, i = h
            if c in cross_index:
                bit = (state >> cross_index[c]) & 1
                j = ((i ^ 1) if bit == 0 else (3 - i))
            else:
                j = (i + 2) % 4
                direction = 1 if (i, j) in c.directions else -1
                signed_sum += c.sign * direction
            remaining.discard((c, i))
            remaining.discard((c, j))
            h = c.adjacent[j]
            if h == first:
                break
        assert signed_sum % 2 == 0
        linking = abs(signed_sum // 2)
        linking_numbers.add(linking)
        assert linking in (0, 1)
        essential += linking
        contractible += int(linking == 0)
    state_features.append((contractible, essential))
    coefficient = ONE
    for _ in range(contractible):
        coefficient = mul(coefficient, DELTA)
    coefficient = shift(coefficient, len(self_crossings) - 2 * state.bit_count())
    annular[essential] = add(annular[essential], coefficient)
annular = {k: v for k, v in annular.items() if v}

def jones_A(link):
    pd = link.PD_code()
    r = regina.Link.fromPD([[x + 1 for x in row] for row in pd])
    p = r.jones()
    return {-2 * e: int(str(p[e])) for e in range(p.minExp(), p.maxExp() + 1) if p[e] != 0}

V = jones_A(K)
VL = jones_A(L)
ordinary = {}
for zdegree, coeff in annular.items():
    value = coeff
    for _ in range(zdegree):
        value = mul(value, DELTA)
    ordinary = add(ordinary, value)
expected = shift(mul(DELTA, V), 3 * K.writhe(), (-1) ** K.writhe())
if ordinary != expected:
    # Smoothing conventions differ by A -> A^-1; fix globally, then recheck.
    annular = {k: {-e: c for e, c in v.items()} for k, v in annular.items()}
    ordinary = {-e: c for e, c in ordinary.items()}
assert ordinary == expected
assert set(annular) == {0, 2}
a, b = annular[2], annular[0]
delta2 = mul(DELTA, DELTA)
Delta2 = add(delta2, neg(ONE))
lambda2 = {6: -1, -6: -1}
hopf_value = add(mul(mul(a, Delta2), lambda2), mul(add(a, b), DELTA))
assert hopf_value == shift(mul(DELTA, VL), 3 * L.writhe(), (-1) ** L.writhe())

# C2=(VL-delta*V)/(lambda2-delta); V_n=V+(A^(8n)-1)*C2.
c2_num = add(VL, neg(mul(DELTA, V)))
c2_den = add(lambda2, neg(DELTA))
target_num = add(c2_num, mul(c2_den, add(ONE, neg(V))))
assert max(target_num) == max(c2_num)
assert V != ONE
data = {
    'source': 'https://arxiv.org/pdf/2609.11084v2',
    'PD_source': PD,
    'states': 1 << len(self_crossings),
    'self_crossings': len(self_crossings),
    'writhe_K': K.writhe(),
    'writhe_K_union_axis': L.writhe(),
    'Jones_K_in_A': V,
    'Jones_K_union_axis_in_A': VL,
    'annular_bracket_coefficients': annular,
    'independent_Hopf_pairing_check': True,
    'twist_formula': 'V_n=V_0+(A^(8n)-1)*C2, C2=c2_num/c2_den',
    'c2_num': c2_num,
    'c2_den': c2_den,
    'degree_of_required_A8n': max(target_num) - max(c2_num),
    'only_possible_twist_n': 0,
    'V_at_n0_is_one': False,
    'conclusion': 'No integer meridional twist has Jones polynomial one.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data, indent=2))
print(json.dumps({k: v for k, v in data.items() if k not in ('PD_source',)}, indent=2))
