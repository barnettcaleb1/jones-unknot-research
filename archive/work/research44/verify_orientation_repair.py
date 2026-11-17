#!/usr/bin/env python3
"""Exact arithmetic for the proposed orientation repair; no knot search.

The finite checks below support the identities, not the all-m proofs.
They do not independently reconstruct the full clasp-machine diagram.
"""
import json
from pathlib import Path


def clean(a):
    return {e: c for e, c in a.items() if c}


def add(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
    return clean(out)


def scale(a, n):
    return clean({e: n*c for e, c in a.items()})


def shift(a, n):
    return {e+n: c for e, c in a.items()}


def mul(a, b):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            out[i+j] = out.get(i+j, 0) + u*v
    return clean(out)


def jvp(poly):
    # Polynomials in p represented with the same integer dictionary type.
    result_a, result_b = {}, {}
    for e, coefficient in poly.items():
        a, b = {0: 1}, {}
        for _ in range(abs(e)):
            if e >= 0:  # multiplication by x, with x^2=px+1
                a, b = b, add(a, shift(b, 1))
            else:       # multiplication by x^-1=x-p
                a, b = add(b, scale(shift(a, 1), -1)), a
        result_a = add(result_a, scale(a, coefficient))
        result_b = add(result_b, scale(b, coefficient))
    return result_a, result_b


def span(a):
    assert a
    return max(a)-min(a)


def at_i(a):
    # Exact image in Z[i]; supports negative Laurent exponents.
    values = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return tuple(sum(c*values[e % 4][j] for e, c in a.items())
                 for j in range(2))


def main():
    one, p = {0: 1}, {1: 1, -1: -1}
    p2 = mul(p, p)
    trefoil = {2: 1, 6: 1, 8: -1}
    hopf = {1: -1, 5: -1}
    unlink = {1: -1, -1: -1}
    f_hopf = shift(hopf, -3)
    assert f_hopf == {-2: -1, 2: -1}

    # Mixed and self crossing skein formulas, on actual links.
    assert add(f_hopf, scale(shift(unlink, 1), -1)) == shift(p, -1)
    assert add(shift(trefoil, -2), {2: -1}) == shift(mul(p, f_hopf), 3)

    zero_layers = []
    for name, f in [('unlink', unlink), ('Hopf', f_hopf)]:
        a, b = jvp(f)
        aa, bb = jvp(mul(f, f))
        assert (aa.get(0, 0), bb.get(0, 0)) == (4, 0)
        zero_layers.append({'link': name, 'F_layer0': [a.get(0, 0), b.get(0, 0)],
                            'F_squared_layer0': [aa.get(0, 0), bb.get(0, 0)]})
    assert zero_layers[0]['F_layer0'] != zero_layers[1]['F_layer0']

    # The product channel created by squaring is genuinely nonzero.
    b = shift(p, -1)
    cross = scale(shift(mul(unlink, b), 1), 2)
    squared_defect = add(add(mul(f_hopf, f_hopf),
                             scale(shift(mul(unlink, unlink), 2), -1)),
                         scale(mul(b, b), -1))
    assert squared_defect == cross and cross

    # Algebraic residues force both machine channels nonzero for EVERY C.
    pole_a = scale(mul(mul(p2, {2: 1}), {4: 1, 0: 1}), -1)
    pole_b = scale(mul(p2, {0: 1, 6: -1}), -1)
    assert at_i(pole_a) == (-8, 0)
    assert at_i(pole_b) == (8, 0)

    # Actual residual twist family from the switched-trefoil unknot host.
    D = {0: -1, 2: 1, 6: 1, 8: -1}
    residual = one
    rows = []
    for m in range(1, 9):
        residual = add(shift(residual, 4), shift(mul(p, hopf), 2))
        closed_form = add(one, mul(D, {4*j: 1 for j in range(m)}))
        assert residual == closed_form
        squared = mul(residual, residual)
        assert span(residual) == 4*m+2
        assert span(squared) == 8*m+4
        aa, bb = jvp(squared)
        degree = max(set(aa) | set(bb))
        assert degree == 8*m+7
        assert span(squared) <= 2*degree+1
        rows.append({'m': m, 'span_residual': span(residual),
                     'span_squared': span(squared), 'squared_JVP_degree': degree})
    result = {'zero_layers': zero_layers, 'cross_term_nonzero': bool(cross),
              'machine_channel_residues_at_i': [-8, 8], 'residual_checks': rows,
              'scope': 'Algebra only; machine geometry inputs stated separately.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print('Verified normalization, both skein types, square cross term, pole residues, and residual growth.')


if __name__ == '__main__':
    main()
