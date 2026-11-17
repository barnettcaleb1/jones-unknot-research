#!/usr/bin/env python3
"""Exact arithmetic for the projective-span countertest; standard library only.

Jones is computed from all bracket resolutions of the actual braid closure.
Alexander is computed independently from its reduced Burau matrix.
This does not mechanically verify the projective crossing-identity proof.
"""
from itertools import product
import json


def add(a, b):
    out = dict(a)
    for degree, coefficient in b.items():
        out[degree] = out.get(degree, 0) + coefficient
    return {d: c for d, c in out.items() if c}


def mul(a, b):
    out = {}
    for d, c in a.items():
        for e, f in b.items():
            out[d + e] = out.get(d + e, 0) + c * f
    return {d: c for d, c in out.items() if c}


def shift(a, amount, coefficient=1):
    return {d + amount: coefficient * c for d, c in a.items()}


def exact_divide(a, b):
    remainder, quotient = dict(a), {}
    while remainder and max(remainder) >= max(b):
        d = max(remainder) - max(b)
        c, rem = divmod(remainder[max(remainder)], b[max(b)])
        assert rem == 0
        quotient[d] = c
        remainder = add(remainder, shift(b, d, -c))
    assert not remainder
    return quotient


def positive_braid_jones(strands, word):
    """Return normalized Jones in t=A^-4 for a positive braid closure."""
    assert all(1 <= i < strands for i in word)
    crossings = len(word)
    delta = {2: -1, -2: -1}
    answer = {}
    for resolutions in product((0, 1), repeat=crossings):
        parents = list(range(strands * (crossings + 1)))

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(a, b):
            parents[find(a)] = find(b)

        for layer, (generator, cupcap) in enumerate(zip(word, resolutions)):
            a = layer * strands
            b = (layer + 1) * strands
            i = generator - 1
            if cupcap:
                union(a + i, a + i + 1)
                union(b + i, b + i + 1)
            for j in range(strands):
                if not cupcap or j not in (i, i + 1):
                    union(a + j, b + j)
        for j in range(strands):
            union(j, crossings * strands + j)
        loops = len({find(x) for x in range(len(parents))})
        term = {crossings - 2 * sum(resolutions): 1}
        for _ in range(loops - 1):
            term = mul(term, delta)
        answer = add(answer, term)
    normalized = shift(answer, -3 * crossings, (-1) ** crossings)
    assert all(d % 4 == 0 for d in normalized)
    return {-d // 4: c for d, c in normalized.items()}


def matmul(a, b):
    return [[add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


assert positive_braid_jones(2, [1]) == {0: 1}
assert positive_braid_jones(2, [1, 1, 1]) == {1: 1, 3: 1, 4: -1}
word = [1, 2] * 4
jones = positive_braid_jones(3, word)
assert jones == {3: 1, 5: 1, 8: -1}

# Standard reduced Burau generators, with det(sigma_i)=-t.
generators = {
    1: [[{1: -1}, {0: 1}], [{}, {0: 1}]],
    2: [[{0: 1}, {}], [{1: 1}, {1: -1}]],
}
matrix = [[{0: 1}, {}], [{}, {0: 1}]]
for generator in word:
    matrix = matmul(matrix, generators[generator])
determinant = add(
    mul(add({0: 1}, shift(matrix[0][0], 0, -1)),
        add({0: 1}, shift(matrix[1][1], 0, -1))),
    shift(mul(matrix[0][1], matrix[1][0]), 0, -1),
)
# Alexander of a three-strand braid closure is det(I-B)/(1+t+t^2),
# up to a Laurent unit. The shift below makes the answer symmetric.
alexander = shift(exact_divide(determinant, {0: 1, 1: 1, 2: 1}), -3)
assert alexander == {-3: 1, -2: -1, 0: 1, 2: -1, 3: 1}
assert sum(jones.values()) == sum(alexander.values()) == 1
assert max(jones) - min(jones) == 5
assert max(alexander) - min(alexander) == 6

print(json.dumps({
    'knot': 'T(3,4)',
    'actual_braid': word,
    'jones_t_coefficients': jones,
    'alexander_t_coefficients': alexander,
    'jones_span': 5,
    'alexander_span': 6,
    'consequence': 'c(K) >= span Alexander = 6 > span Jones = 5',
    'scope': 'Polynomial certificate only; beta_Re=c(K) has a separate proof.'
}, indent=2, sort_keys=True))
