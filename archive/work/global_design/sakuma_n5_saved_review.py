"""Review the saved first n=5 diagrams; never rerun the spatial generator."""
import json
from pathlib import Path
from sakuma_control_review import check_projection, SOURCE
import regina

PREFIX = 'n5_inv1_I1_2_2_m10_5'
records = [check_projection(i, PREFIX) for i in (0, 1)]
assert records[0]['jones_dictionary'] == records[1]['jones_dictionary']
terms = {int(e): c for e, c in records[0]['jones_dictionary'].items() if c}
data = json.loads((SOURCE / f'{PREFIX}_sakuma_proj0.json').read_text())
link = regina.Link.fromPD(data['pd']['pd'])  # Saved PD is already one-based.
link.simplify()
jones = link.jones()
independent = {e: int(str(jones[e]))
               for e in range(jones.minExp(), jones.maxExp() + 1)
               if jones[e] != 0}
assert independent == terms
assert terms != {-1: -1, 1: -1}

# GF(16) in the basis 1,q,q^2,q^3, q^4+q^3+q^2+q+1=0.
def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        if a & 16:
            a ^= 31
        b >>= 1
    return out

qpowers = [1]
for _ in range(4):
    qpowers.append(mul(qpowers[-1], 2))

def evaluate_half_exponents(polynomial):
    out = 0
    for e, c in polynomial.items():
        if c % 2:
            out ^= qpowers[(3 * int(e)) % 5]
    return out

knot = json.loads((SOURCE / f'{PREFIX}_knot.json').read_text())
kp = {int(e): c for e, c in knot['jones'].items()}  # This file also uses half-exponents.
assert all(e % 2 == 0 for e in kp)
v1 = sum(kp.values())
derivative = sum((e // 2) * c for e, c in kp.items())
second_derivative = sum((e // 2) * (e // 2 - 1) * c for e, c in kp.items())
det_signed = sum((-1 if (e // 2) % 2 else 1) * c for e, c in kp.items())
vs, vk, d = evaluate_half_exponents(terms), evaluate_half_exponents(kp), 12
assert (v1, derivative, second_derivative, det_signed) == (1, 0, 0, -799)
assert (vs, vk) == (d, 1)
assert mul(vs, vs) == (1 ^ mul(d, vk))

result = {
    'scope': 'saved n5 first-inversion diagrams; independent Regina Jones and component isotopies; spatial generator not rerun or certified',
    'projections': records,
    'extrema_half_t': [min(terms), max(terms)],
    'equals_unlink': False,
    'regina_independent_jones': {
        'version': regina.versionString(), 'projection': 0,
        'simplified_crossings': link.size(), 'dictionary': independent,
        'agrees_exactly': True},
    'source_knot_checks': {'value_at_1': v1, 'derivative_at_1': derivative,
                           'second_derivative_at_1': second_derivative,
                           'value_at_minus_1': det_signed},
    'frob5': {'VS_basis_bits': vs, 'Vkappa_basis_bits': vk,
              'd_basis_bits': d, 'identity_passes': True}
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
print('Saved n5-A: exact Regina match; both components isotopically U; nonunlink Jones; FROB5 passes.')
