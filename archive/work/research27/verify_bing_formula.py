#!/usr/bin/env python3
"""Stdlib checks of identities used in the Bing-pattern proof.

This verifies finite Laurent algebra, not Suzuki's theorem or knot geometry.
Variables: x=q^(1/2), Y=fundamental representation, H=H3(C), J=H3(companion).
"""
from collections import defaultdict


def mono(c=1, x=0, y=0, h=0, j=0):
    return {(x, y, h, j): c} if c else {}


def add(*polys):
    out = defaultdict(int)
    for poly in polys:
        for key, coefficient in poly.items():
            out[key] += coefficient
    return {key: value for key, value in out.items() if value}


def scale(poly, coefficient):
    return {key: coefficient * value for key, value in poly.items() if coefficient * value}


def mul(*polys):
    out = mono()
    for poly in polys:
        new = defaultdict(int)
        for left, lc in out.items():
            for right, rc in poly.items():
                new[tuple(a + b for a, b in zip(left, right))] += lc * rc
        out = {key: value for key, value in new.items() if value}
    return out


def sub(left, right):
    return add(left, scale(right, -1))


one = mono()
a = sub(mono(x=1), mono(x=-1))
s = add(mono(x=1), mono(x=-1))
r = add(mono(x=3), mono(x=-3))
q4 = sub(mono(x=4), mono(x=-4))
Y, H, J = mono(y=1), mono(h=1), mono(j=1)
d2 = sub(mul(s, s), one)

assert q4 == mul(a, add(r, s)), "{4}/{1}=r+s"
assert sub(r, s) == mul(s, a, a), "r-s=s{1}^2"
assert d2 == add(mono(x=2), one, mono(x=-2)), "[3]=s^2-1"

# Clear the sole denominator {1} from the low-color Suzuki combination.
lhs = add(scale(mul(q4, sub(Y, s)), -1),
          scale(mul(a, sub(Y, s), sub(Y, r)), -1))
rhs = scale(mul(a, sub(mul(Y, Y), mul(s, s))), -1)
assert lhs == rhs, "Suzuki combination = -(Y^2-s^2)"

# The j=1 fundamental-pattern probe has an EXTRA factor {1}.
# Claimed z^2 coefficient b=(1-H)/s has Hopf probe b*[3]*(r-s)/a.
# Clear s*a to compare against -a*[3]*(H-1).
lhs = mul(sub(one, H), d2, sub(r, s))
rhs = scale(mul(s, a, a, d2, sub(H, one)), -1)
assert lhs == rhs, "fundamental probe and annular z^2 coefficient agree"

# The positive-convention annular expression is s*H+(1-H)z^2/s.
# Satellite evaluation z^2 -> 1+[3]*J, then divide by s.
# Clear s^2. This is unchanged by s=-delta in the Kauffman convention.
satellite_numerator = add(mul(s, s, H), mul(sub(one, H), add(one, mul(d2, J))))
factorized_numerator = sub(mul(s, s), mul(d2, sub(H, one), sub(J, one)))
assert satellite_numerator == factorized_numerator, "full product identity"

# Setting either input to 1 gives the unknot value; this is visible in
# the factorization, whose nonzero prefactor cannot produce cancellation.
assert a and s and d2
print("PASS: Suzuki low-color identity, Hopf normalization, and exact satellite product identity.")
print("Scope: Laurent identities only; published inputs and topology require the accompanying proof.")
