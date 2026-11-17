#!/usr/bin/env python3
"""Exact checks of the root-specialization step; standard library only.
The general topological existence theorem is proved separately.
"""
import json
from functools import lru_cache


def add(a, b):
    result = dict(a)
    for k, v in b.items():
        result[k] = result.get(k, 0) + v
    return {k: v for k, v in result.items() if v}


def scale(a, c):
    return {k: c*v for k, v in a.items() if c*v}


def mul(a, b):
    result = {}
    for k, v in a.items():
        for j, w in b.items():
            result[k+j] = result.get(k+j, 0) + v*w
    return {k: v for k, v in result.items() if v}


def divmod_poly(a, b):
    a, quotient = dict(a), {}
    while a and max(a) >= max(b):
        shift = max(a)-max(b)
        c, rem = divmod(a[max(a)], b[max(b)])
        assert rem == 0
        quotient[shift] = quotient.get(shift, 0)+c
        a = add(a, {k+shift: -c*v for k, v in b.items()})
    return quotient, a


@lru_cache(None)
def cyclotomic(n):
    p = {n: 1, 0: -1}
    for d in range(1, n):
        if n % d == 0:
            p, remainder = divmod_poly(p, cyclotomic(d))
            assert not remainder
    return p


def check(order):
    modulus = cyclotomic(order)
    def reduce(a):
        return divmod_poly(a, modulus)[1]
    def monomial(k):
        return reduce({k % order: 1})
    def product(a, b):
        return reduce(mul(a, b))
    delta = scale(add(monomial(2), monomial(-2)), -1)
    def tl_product(x, y):
        a, b = x
        c, d = y
        return (product(a, c), add(add(product(a, d), product(b, c)),
                                  product(product(b, d), delta)))
    identity = (monomial(0), {})
    crossing = (monomial(1), monomial(-1))
    full_twist = tl_product(crossing, crossing)
    assert full_twist == (monomial(2), add(monomial(0), scale(monomial(-4), -1)))
    answer = identity
    for _ in range(order):
        answer = tl_product(answer, full_twist)
    # Writhe normalization for either +/-2*order crossings.
    assert monomial(6*order) == monomial(-6*order) == monomial(0)
    if order == 8:
        assert delta == {}
        assert answer == (monomial(0), scale(monomial(2), -16))
        assert answer != identity
    else:
        assert answer == identity
    return {'primitive_A_order': order,
            'twist_power_is_identity': answer == identity}


results = [check(order) for order in range(1, 49)]
print(json.dumps({'scope': 'Finite exact arithmetic checks; not a substitute for the proof.',
                  'checks': results,
                  'exception': 'A order 8 gives t=-1; handled by Alexander determinant in the proof.',
                  'status': 'passed'}, indent=2))
