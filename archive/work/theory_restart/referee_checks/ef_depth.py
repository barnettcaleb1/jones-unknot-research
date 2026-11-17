"""Exact check of the published Eliahou--Fromentin seed at A = exp(x).

Inputs: arXiv:1610.05560v2, Lemma 4.2.
Normalization: Proposition 5.2, chi(K_r) = f_r + A^-6 g_r.
Only rational arithmetic; no dependencies, diagram enumeration, or fitted data.
The all-r conclusion uses the doubling recurrence explained in the proof note.
"""

from fractions import Fraction
from math import factorial

ORDER = 4


def jet(terms):
    return tuple(
        Fraction(sum(coef * exponent**k for exponent, coef in terms.items()),
                 factorial(k))
        for k in range(ORDER + 1)
    )


def add(*series):
    return tuple(sum(parts) for parts in zip(*series))


def mul(left, right):
    return tuple(sum(left[i] * right[k - i] for i in range(k + 1))
                 for k in range(ORDER + 1))


def scale(series, scalar):
    return tuple(scalar * value for value in series)


def mirror(series):
    return tuple((-1)**k * value for k, value in enumerate(series))


def star(left, right):
    f, g = left
    ff, gg = right
    return mul(f, ff), add(mul(f, gg), mul(g, ff), mul(delta, mul(g, gg)))


f10 = jet({-10: 2, -6: -2, -2: 2, 6: -2, 10: 2, 14: -2, 18: 1})
g10 = jet({-8: 2, -4: -5, 0: 7, 4: -7, 8: 5, 12: -3, 16: 1})
delta = jet({2: -1, -2: -1})
f20, g20 = star((f10, g10), (mirror(f10), mirror(g10)))
assert f20 == (1, 0, 0, 0, 16384)
assert g20 == (0, 0, 0, 0, 8192)

# Products of the seed defects start at order eight. Therefore every doubling
# multiplies both order-four coefficients by two, without creating lower jets.
ff, gg = star((f20, g20), (f20, g20))
assert ff == add((1, 0, 0, 0, 0), scale(add(f20, (-1, 0, 0, 0, 0)), 2))
assert gg == scale(g20, 2)

chi = add(f20, mul(jet({-6: 1}), g20))
assert chi == (1, 0, 0, 0, 24576)
ordinary = tuple(value * Fraction(-1, 4)**k for k, value in enumerate(chi))
assert ordinary == (1, 0, 0, 0, 96)

print("Published seed: V_K1(exp(h)) = 1 + 96 h^4 + O(h^5).")
print("Doubling recurrence: coefficient = 96 * 2^(r-1), exact depth four for every r >= 1.")
