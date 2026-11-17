"""Exact algebra checks for pass 25; no knot-construction certificate."""
from collections import defaultdict
import json


def multiply(p, q):
    result = defaultdict(int)
    for (a, b), c in p.items():
        for (d, e), f in q.items():
            result[a + d, b + e] += c * f
    return {key: value for key, value in result.items() if value}


# Work over Z[x^+-1,y^+-1], then substitute x=t^(3k), y=t.
# This is an identity for all parameters, not polynomial interpolation.
torus = {(1, 0): 1, (1, 2): 1, (2, 2): -1}
reciprocal = {(-a, -b): c for (a, b), c in torus.items()}
double = multiply(torus, reciprocal)
expected = {(0, 0): 3, (0, 2): 1, (0, -2): 1,
            (1, 0): -1, (-1, 0): -1, (1, 2): -1, (-1, -2): -1}
assert double == expected
for parity, determinant in ((1, 9), (0, 1)):
    value = sum(c * (-1 if (a * parity + b) % 2 else 1)
                for (a, b), c in double.items())
    assert abs(value) == determinant


def content_exponent(partition):
    n = sum(partition)
    content = sum(j - i for i, row in enumerate(partition, 1)
                  for j in range(1, row + 1))
    return 4 * content - n * (n - 1)


blocks6 = [(6,), (5, 1), (4, 2), (3, 3)]
blocks5 = [(5,), (4, 1), (3, 2)]
assert list(map(content_exponent, blocks6)) == [30, 6, -10, -18]
assert list(map(content_exponent, blocks5)) == [20, 0, -12]
assert content_exponent((3, 3)) - content_exponent((3, 2)) == -6
assert content_exponent((4, 2)) - content_exponent((3, 2)) == 2
assert content_exponent((4, 2)) - content_exponent((4, 1)) == -10
for partition in blocks6 + blocks5:
    n = sum(partition)
    k = partition[0] - (partition[1] if len(partition) == 2 else 0)
    assert content_exponent(partition) == k * (k + 2) - 3 * n

print(json.dumps({
    "two_variable_reciprocal_product": "passed exactly",
    "determinant_parity": "passed exactly",
    "full_twist_content_and_through_label_formulas": "agree",
    "limitation": "Does not prove published inputs, a bounded Jones fiber, or a nontrivial braid kernel."
}, indent=2))
