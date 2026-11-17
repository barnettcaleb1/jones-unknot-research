"""symbolic check of the matrix identities behind R0 (normal forms) and R2 (mirror) -- sympy"""
import sympy as sp
t = sp.symbols('t')
Y = sp.Matrix([[1, 0], [t**-3, t**-3]]); X = sp.Matrix([[1, 1 - t**4], [0, -t]])
E = Y.inv() * X; D = sp.diag(1, -t**3); e1 = sp.Matrix([1, 0])
bar = lambda M: M.subs(t, 1 / t)
chk = {
 'E = [[1,1-t^4],[-1,-1]]': sp.simplify(E - sp.Matrix([[1, 1 - t**4], [-1, -1]])) == sp.zeros(2),
 'E^2 = t^4 I': sp.simplify(E * E - t**4 * sp.eye(2)) == sp.zeros(2),
 'E e1 = Y^-1 e1': sp.simplify(E * e1 - Y.inv() * e1) == sp.zeros(2, 1),
 'X = Y E': sp.simplify(X - Y * E) == sp.zeros(2),
 'X^-1 = t^-4 E Y^-1': sp.simplify(X.inv() - t**-4 * E * Y.inv()) == sp.zeros(2),
 'bar Y = D Y^-1 D^-1': sp.simplify(bar(Y) - D * Y.inv() * D.inv()) == sp.zeros(2),
 'bar X = D X^-1 D^-1': sp.simplify(bar(X) - D * X.inv() * D.inv()) == sp.zeros(2),
 'bar E = t^-4 D Y E Y^-1 D^-1': sp.simplify(bar(E) - t**-4 * D * Y * E * Y.inv() * D.inv()) == sp.zeros(2),
 'D^-1 e1 = e1': D.inv() * e1 == e1,
}
# channels of D Y w: a = w1, b(bar) = t^-3 b(w)
w1, w2 = sp.symbols('w1 w2')
v = D * Y * sp.Matrix([w1, w2])
chk['a(DYw) = a(w)'] = sp.simplify(v[0] - w1) == 0
chk['bar-b: v1 + (1-t^-3) v2 = t^-3 (w1 + (1-t^3) w2)'] = sp.simplify(v[0] + (1 - t**-3) * v[1] - t**-3 * (w1 + (1 - t**3) * w2)) == 0
for k, val in chk.items(): print(('OK  ' if val else 'FAIL'), k)
