"""Exact Laurent-polynomial certificate; Python standard library only.

Geometric identifications are proved separately in the accompanying notes.
The optional --diagrams flag regenerates two actual base-knot PD diagrams
and recomputes their Jones polynomials with Spherogram and Regina.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent


def add(*polys):
    result = {}
    for p in polys:
        for e, c in p.items():
            result[e] = result.get(e, 0) + c
    return {e: c for e, c in result.items() if c}


def mul(p, q):
    result = {}
    for e, c in p.items():
        for f, d in q.items():
            result[e + f] = result.get(e + f, 0) + c * d
    return {e: c for e, c in result.items() if c}


def shift(p, e, sign=1):
    return {k + e: sign * c for k, c in p.items()}


def power(p, n):
    result = {0: 1}
    for _ in range(n):
        result = mul(result, p)
    return result


ONE = {0: 1}
DELTA = {2: -1, -2: -1}


def product(x, y):
    a, b = x
    c, d = y
    return mul(a, c), add(mul(a, d), mul(b, c), mul(DELTA, mul(b, d)))


def integer_tangle(n):
    crossing = ({-1: 1}, {1: 1}) if n >= 0 else ({1: 1}, {-1: 1})
    result = (ONE, {})
    for _ in range(abs(n)):
        result = product(result, crossing)
    return result


def numerator(tangle):
    a, b = tangle
    return add(mul(DELTA, a), b)


def denominator(tangle):
    a, b = tangle
    return add(a, mul(DELTA, b))


# R = <-1> + <1/2> + <1/3>; rotation reverses the reciprocal.
r = product(product(integer_tangle(-1), integer_tangle(-2)[::-1]),
            integer_tangle(-3)[::-1])
assert numerator(r) == ONE
t = product(r[::-1], integer_tangle(-6))
assert denominator(t) == {-18: 1}
v_longitude = shift(numerator(t), 18)
assert v_longitude == {2: -1, 6: 1, 22: -1, 30: -1}

x_core = shift(mul(mul({4: 1, 0: -1}, {0: 1, 8: 1}),
                   {0: 1, 12: 1}), 2)
assert add(v_longitude, shift(DELTA, 0, -1)) == mul(
    add(ONE, shift(mul(DELTA, DELTA), 0, -1)), x_core)

d = mul(mul({0: 1, 4: -1}, {0: 1, 8: 1}), {0: 1, 12: 1})
assert x_core == shift(d, 2, -1)
cap = shift(mul({4: 1, 0: -1}, {8: 1, 4: 1, 0: 1}), -10)
base_difference_a = mul(cap, x_core)

# Check the exact base knot by a separate rational cap computation.
cap_tangle = integer_tangle(2)[::-1]
actual_base_v_a = shift(numerator(product(t, cap_tangle)), 12)
assert add(actual_base_v_a, {0: -1}) == base_difference_a

# Independent diagram computations saved by the parent use the mirror
# convention for the Jones variable. Check both half-integral fillings.
rows = json.loads((HERE / 'trefoil_actual_PD_checks.json').read_text())
f0 = mul(mul(mul(power({1: 1, 0: -1}, 2), {2: 1, 1: 1, 0: 1}),
             {2: 1, 0: 1}), {3: 1, 0: 1})
matches = []
for row in rows:
    if row['name'] not in ('minus_half', 'plus_half'):
        continue
    p_x = {int(e): c for e, c in row['Jones_x'].items()}
    assert all(e % 2 == 0 for e in p_x)
    difference = add({e // 2: c for e, c in p_x.items()}, {0: -1})
    offset = min(difference) - min(f0)
    sign = difference[min(difference)] // f0[min(f0)]
    assert sign in (-1, 1)
    assert difference == shift(f0, offset, sign)
    matches.append((row['name'], sign, offset))

if '--diagrams' in sys.argv:
    local = HERE.parents[0] / 'braid_classification' / 'packages'
    if local.exists():
        sys.path.insert(0, str(local))
    from spherogram.links.tangles import RationalTangle as RT
    import regina
    actual_r = RT(-1) + RT(1, 2) + RT(1, 3)
    actual_t = actual_r.rotate(1) + RT(-6)
    for name, cap_sign in [('minus_half', -1), ('plus_half', 1)]:
        link = (actual_t + RT(cap_sign, 2)).numerator_closure()
        reg = regina.Link.fromPD([[e + 1 for e in row] for row in link.PD_code()])
        assert reg.countComponents() == 1
        j = reg.jones()
        p = {e: int(str(j[e])) for e in range(j.minExp(), j.maxExp() + 1)
             if int(str(j[e]))}
        saved = next(row for row in rows if row['name'] == name)
        assert p == {int(e): c for e, c in saved['Jones_x'].items()}
    print('Independent actual base diagrams recomputed successfully.')

print('Trefoil anchor, preferred longitude, exact x, Whitehead factor, and cap verified.')
print('Actual base-knot difference / F_0(t):', matches)
print('For general r, the proof multiplies these exact nonzero factors; no finite enumeration is used.')
