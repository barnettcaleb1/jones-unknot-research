#!/usr/bin/env python3
"""Exact standard-library verification of the pass37 finite certificate."""
from fractions import Fraction
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def clean(p):
    return {e: c for e, c in p.items() if c}

def at_i_over_i(p, euler=0):
    assert all(e % 2 for e in p), "Expected odd Laurent support"
    return sum(c * e ** euler * (1 if e % 4 == 1 else -1)
               for e, c in p.items())

def candidate(d1, d2, a, b):
    c1, c2 = at_i_over_i(d1), at_i_over_i(d2)
    e1, e2 = at_i_over_i(d1, 1), at_i_over_i(d2, 1)
    return -(Fraction(e1, c1) - Fraction(e2, c2)) / (2 * (a + b))

def geometric(r, z_shift=0):
    assert r != 0
    # x*z^z_shift*(z^r-1)/(z-1), z=x^-4; works for signed r.
    js, sign = (range(r), 1) if r > 0 else (range(r, 0), -1)
    return {1-4*(z_shift+j): sign for j in js}

synthetic = []
for a, b in [(1,1), (1,4), (4,1), (4,9)]:
    for k in [-3,-1,1,2]:
        d1 = geometric(b*k, a*k)
        d2 = geometric(a*k)
        recovered = candidate(d1, d2, a, b)
        assert recovered == k
        synthetic.append({'a':a,'b':b,'k':k,'recovered':str(recovered)})

source = ROOT/'work/research34/two_band_family.json'
data = json.loads(source.read_text())
by_active = {tuple(c['active_bands']): c for c in data['cuts']}

def partial_defect(active):
    s = {int(e): c for e,c in by_active[active]['Jones_x_coefficients'].items()}
    s[1] = s.get(1,0)+1
    s[-1] = s.get(-1,0)+1
    return clean(s)

d1 = partial_defect((False,True))
d2 = partial_defect((True,False))
actual = []
for name,d in [('S1_minus_delta',d1),('S2_minus_delta',d2)]:
    jets = [sum(c*e**j for e,c in d.items()) for j in range(5)]
    order = next(j for j,value in enumerate(jets) if value)
    actual.append({'name':name,'value_at_i_over_i':at_i_over_i(d),
                   'euler_derivative_at_i_over_i':at_i_over_i(d,1),
                   'euler_jets_at_1':jets,'order_at_1':order})
assert [r['value_at_i_over_i'] for r in actual] == [144,144]
assert [r['euler_derivative_at_i_over_i'] for r in actual] == [-576,-720]
assert [r['order_at_1'] for r in actual] == [3,2]
kstar = candidate(d1,d2,1,1)
assert kstar == Fraction(-1,4)
def derivative_at_1(p, degree):
    total = 0
    for e,c in p.items():
        falling = 1
        for j in range(degree):
            falling *= e-j
        total += c*falling
    return total

corner_jets = []
for corner in data['corners']:
    m,n = corner['m'],corner['n']
    poly = {int(e): c for e,c in corner['Jones_x_coefficients'].items()}
    third = derivative_at_1(poly,3)
    fourth = derivative_at_1(poly,4)
    assert third == 576*n
    if n == 0:
        assert fourth == 2304*m
    corner_jets.append({'m':m,'n':n,'third_derivative':third,'fourth_derivative':fourth})
report = {'corner_jet_checks':corner_jets, 'synthetic_algebra_checks':synthetic,'actual_partials':actual,
          'actual_k_star':str(kstar),
          'actual_all_integer_conclusion':'Jones=1 iff m=n=0, using rank-one determinant line',
          'scope':'Synthetic pairs are algebra tests, not claimed geometric realizations.'}
(HERE/'verify_isolated_twist_algebra.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: 16 exact signed-parameter algebra checks; actual k_star=-1/4; orders at1 are3 and2.')
