#!/usr/bin/env python3
"""For the zigzag Z_l (chi = sum_{i=0}^{l} t^{3i} - sum_{i=0}^{l-1} t^{3i+4} up to a unit and mirror), find all Laurent polynomials Pi
with  chi(Z_l) + (1-t)(1-t^4) Pi = +- t^m  (flatness of zigzag + squares; Pi = signed generating function of the squares).
Reports Pi, its number of monomials and the minimal number of squares  sum |coefficients|."""
import sympy as sp
t = sp.symbols('t')
def chiZ(l):
    return sum(t**(3*i) for i in range(l + 1)) - sum(t**(3*i + 4) for i in range(l))
for l in range(0, 8):
    c = chiZ(l)
    sols = []
    for m in range(-12, 3*l + 16):
        for s in (1, -1):
            num = sp.expand((s * t**m - c) * t**20)        # shift to make polynomial
            den = sp.expand((1 - t) * (1 - t**4))
            q, r = sp.div(sp.Poly(num, t), sp.Poly(den, t))
            if r.is_zero:
                Pi = sp.expand(q.as_expr() / t**20)
                coeffs = sp.Poly(sp.expand(Pi * t**40), t).coeffs() if Pi != 0 else []
                sols.append((m, s, Pi, sum(abs(int(x)) for x in coeffs)))
    print('l = %d: chi(Z_l) has %d terms; flat solutions:' % (l, 2*l + 1))
    for (m, s, Pi, w) in sols:
        print('     unit %st^%d   Pi = %s   minimal number of squares = %d   -> dim N >= %d' % ('+' if s > 0 else '-', m, Pi, w, 2*l + 1 + 4*w))
