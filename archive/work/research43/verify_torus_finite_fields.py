#!/usr/bin/env python3
"""Elementary finite-field false positives; exact standard-library check.

V_{T(2,2m+1)}(t)=t^m(1+t+t^2-t^(2m+2))/(1+t).
This is equality of evaluation functions on specified finite fields, NOT
coefficientwise equality of Laurent polynomials, nor Jones-one over Z.
"""
import json
from math import lcm
from pathlib import Path


def polynomial(m):
    assert m >= 0
    return {m: 1, **{m+j: (-1)**j for j in range(2, 2*m+2)}}


def add(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
    return {e: c for e, c in r.items() if c}


def shifted(p, n):
    return {e+n: c for e, c in p.items()}


def check_formula(m):
    v = polynomial(m)
    numerator = add({m: 1, m+1: 1, m+2: 1}, {3*m+2: -1})
    assert add(v, shifted(v, 1)) == numerator
    assert sum(v.values()) == 1
    assert sum(c*e for e, c in v.items()) == 0
    determinant_value = sum(c*(-1)**e for e, c in v.items())
    assert determinant_value == (-1)**m*(2*m+1)
    return v


def remainder(p, q, characteristic):
    # Exact remainder in F_p[t]/(t^(q-1)-1); roots are ALL F_q^*.
    r = {}
    for e, c in p.items():
        j = e % (q-1)
        r[j] = (r.get(j, 0)+c) % characteristic
    return {e: c for e, c in r.items() if c}


def main():
    for m in (0, 1, 2, 3):
        check_formula(m)
    assert polynomial(1) == {1: 1, 3: 1, 4: -1}
    fields = [(2, 2), (3, 3), (4, 2), (5, 5), (8, 2), (9, 3)]
    m = lcm(*(p*(q-1) for q, p in fields))
    assert m % 2 == 0 and m > 0
    v = check_formula(m)
    defect = add(v, {0: -1})
    checks = []
    for q, p in fields:
        assert m % (p*(q-1)) == 0
        r = remainder(defect, q, p)
        assert not r
        checks.append({"q": q, "characteristic": p, "defect_remainder": r})
    result = {
        "family": "T(2,2m+1)", "m": m,
        "determinant": 2*m+1,
        "integer_polynomial_is_one": v == {0: 1},
        "all_nonzero_finite_field_evaluations_are_one": True,
        "checks": checks,
        "scope": "Evaluation functions only; not coefficientwise polynomial equality.",
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
