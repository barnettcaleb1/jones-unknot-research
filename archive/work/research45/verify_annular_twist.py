"""Exact Laurent arithmetic for the two-channel obstruction; stdlib only."""
from fractions import Fraction
import json

def add(p, q):
    r = p.copy()
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}

def mul(p, q):
    r = {}
    for i, x in p.items():
        for j, y in q.items():
            r[i+j] = r.get(i+j, 0) + x*y
    return {k: v for k, v in r.items() if v}

def ev1(p):
    return sum(p.values())

def derivative1(p):
    return sum(k*v for k, v in p.items())

lam0 = {2: -1, -2: -1}
lam2 = {6: -1, -6: -1}
diff = add(lam2, {k: -v for k, v in lam0.items()})
factor = mul({-6: -1}, mul(mul({4: 1, 0: -1}, {4: 1, 0: -1}), {4: 1, 0: 1}))
assert diff == factor
assert mul({4: 1, 0: -1}, {4: 1, 0: 1}) == {8: 1, 0: -1}
normalized_meridian = {4: 1, 0: -1, -4: 1}
assert mul(normalized_meridian, lam0) == lam2
assert ev1(lam0) == ev1(lam2) == -2
assert derivative1(lam0) == derivative1(lam2) == 0
assert derivative1(normalized_meridian) == 0
assert derivative1({8: 1}) == 8
assert derivative1({-8: 1}) == -8
# Exact check of the first formal interpolation coefficient:
# (lambda2-lambda0)*(-A^6)/(A^4-1) = A^8-1.
assert mul(diff, {6: -1}) == mul({8: 1, 0: -1}, {4: 1, 0: -1})
print(json.dumps({
    'lambda_difference_factorization': True,
    'first_interpolation_coefficient': '-A^6/(A^4-1)',
    'normalized_actual_meridian': 'A^4-1+A^-4',
    'meridian_derivative_at_A1': 0,
    'required_twist_derivatives_at_A1': [8, -8],
    'scope': 'Exact small-object arithmetic; general obstruction proved in accompanying note.'
}, indent=2))
