"""Bracket-vector algebra for Montesinos-type tangles and the multiplicative invariant J of a strong inversion.

Run with tools/venv/bin/python.  Conventions (pretzel frame):
  basis ([inf],[0]) of the rank-two skein module; delta = -A^2 - A^-2; unknot bracket = delta.
  tangle sum:           [0] is the unit, [inf]+[inf] = delta [inf]
  vertical composition: [inf] is the unit, [0]o[0] = delta [0]
  vert(a) = rational tangle 1/a (a vertical half twists) = A^a [inf] + ((-A^-3)^a - A^a)/delta [0]
  N(p) = numerator-closure bracket = p_inf*delta + p_0*delta^2
Lemma Q frame for a tangle X whose numerator closure is an unknot and whose longitude prototype is vert(lam):
  [X] = x*[0] + y*[1/lam],  u = N(X)/delta,  u_e = N(vert(lam))/delta,  J = y*u_e/u = 1 - delta*x/u.
Checked 2026-11-15: X = 1/2 + (-1/3) (trefoil's inversion), lam = 6: N(X)/delta = -A^-3;
  N(X + 1/(-5))/delta = -(A^24 - A^8 - 1)/A^14  (T(3,5) up to mirror), N(X + 1/(-7)) gives the (-2,3,7) pretzel knot,
  x = unit*(A^16 - 1)(A^8 - A^4 + 1), delta | x, and with t = A^-4:  J = t^7 + t^4 - t^3 = 1 - (1 + t^3)(1 - t^4).
"""
import sympy as sp
A = sp.symbols('A'); d = -A**2 - A**-2
def add(p, q): return (sp.expand(d*p[0]*q[0] + p[0]*q[1] + p[1]*q[0]), sp.expand(p[1]*q[1]))
def comp(p, q): return (sp.expand(p[0]*q[0]), sp.expand(p[0]*q[1] + p[1]*q[0] + d*p[1]*q[1]))
def vert(a): return (A**a, sp.expand(sp.cancel(((-A**-3)**a - A**a)/d)))
def N(p): return sp.expand(p[0]*d + p[1]*d**2)
def lq(X, lam):
    e = vert(lam); y = sp.cancel(X[0]/e[0]); x = sp.cancel(X[1] - y*e[1])
    u = sp.cancel(N(X)/d); ue = sp.cancel(N(e)/d)
    return dict(x=sp.factor(x), y=sp.factor(y), u=sp.factor(u), J=sp.factor(sp.cancel(y*ue/u)))
if __name__ == '__main__':
    X = add(vert(2), vert(-3)); r = lq(X, 6)
    for k, v in r.items(): print(k, '=', v)
    t = sp.symbols('t'); print('J in t:', sp.factor(sp.simplify(r['J'].subs(A, t**sp.Rational(-1, 4)))))
    Y = comp(X, X); r2 = lq(Y, 12); print('composite (vertical composition of two copies): N/delta =', r2['u'])
    print('J(composite) / J(X)^2 =', sp.simplify(r2['J']/r['J']**2))
