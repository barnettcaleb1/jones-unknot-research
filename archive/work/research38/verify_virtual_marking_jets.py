"""Standard-library exact checks accompanying virtual_marking_jets.txt.

The universal integer reduction is proved in the text, not inferred from
this script's finite checks. Laurent polynomials are exponent->integer maps.
"""
from collections import defaultdict
from fractions import Fraction
from math import factorial
import json
from pathlib import Path


def add(*polys):
    out = defaultdict(int)
    for p in polys:
        for exponent, coefficient in p.items():
            out[exponent] += coefficient
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: c * a for e, a in p.items() if c * a}


def shift(p, k):
    return {e + k: c for e, c in p.items()}


def multiply(p, q):
    out = defaultdict(int)
    for e, c in p.items():
        for f, d in q.items():
            out[e + f] += c * d
    return {e: c for e, c in out.items() if c}


def quantum_integer(n):
    if n < 0:
        return scale(quantum_integer(-n), -1)
    return {2 * (n - 1 - 2 * j): 1 for j in range(n)}


def E2(p, q):
    return add({0: 2}, shift(quantum_integer(2 * p + 1), 4 * q * (p + 1)),
               scale(shift(quantum_integer(2 * p - 1), 4 * q * (p - 1)), -1))


def jet(poly, k):
    return Fraction(sum(c * e ** k for e, c in poly.items()), factorial(k))


delta = {2: -1, -2: -1}
C = {-7: 1, 1: -2, 5: -1}
delta2 = multiply(delta, delta)
assert E2(1, 0) == delta2
assert E2(1, 1) == {0: 1, 4: 1, 8: 1, 12: 1}

jet_checks = 0
for p in range(-3, 4):
    for q in range(-3, 4):
        X, U = p * q, p * p + q * q
        actual = [jet(E2(p, q), k) for k in range(4)]
        expected = [4, 24 * X, 80 * X * X + 16 * U,
                    Fraction(448 * X ** 3 + 320 * X * U + 64 * X, 3)]
        assert actual == expected, (p, q, actual, expected)
        jet_checks += 1

survivor_checks = []
for Y, Ev in [(0, delta2), (-1, {0: 1, -4: 1, -8: 1, -12: 1})]:
    actual = add(C, multiply({1: 1, -3: -1}, delta2), shift(Ev, 1))
    target = scale(shift(delta, 3 + 12 * Y), -1)
    assert actual == target
    survivor_checks.append({"rs": Y, "framing": 1 + 4 * Y,
                            "exact_bracket": actual})

# This list follows from the proved inequalities, not a numerical search.
positive_cases = []
for Y, X in [(1, 1), (1, 2), (2, 3), (2, 4), (3, 6)]:
    V = 4 * Y * Y + 3 * Y + 1 - 6 * X
    U = Fraction(-10 * X * X + 20 * X * Y + 6 * X - Y * Y - Y + 2, 2)
    positive_cases.append({"Y": Y, "X": X, "U": str(U), "V": V,
                           "required_cross_square": 1 + 4 * X * Y})

result = {"status": "passed", "exact_E2_jet_checks": jet_checks,
          "survivor_full_polynomial_checks": survivor_checks,
          "positive_cases_from_proof": positive_cases,
          "scope": "Universal marking elimination is the accompanying written proof."}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
