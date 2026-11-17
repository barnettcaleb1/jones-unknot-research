"""Step 1a: exact seven-sector coefficients of Codex's template (V = x2.x1, U = x1) with engineB's OWN exact_sectors module
(imported read-only from engineB; nothing written there).  Also checks Codex's three matrix identities and J along the
diagonal with lp.J."""
import sys, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
t0 = time.time()
import exact_sectors as ES       # module-level code builds M, v0, phi, projectors E (no file writes at import)
import sympy as sp
import lp
t = ES.t
print('import/projectors', round(time.time() - t0, 1), 's')
V = ['x2', 'x1']; U = ['x1']
c = ES.cab(V, U)
for k in sorted(c): print('  c%d%d =' % k, c[k])
tot = sp.factor(sp.cancel(sum(c.values())))
print('  sum c_ab =', tot)
# Codex's coefficients
codex = {(0, 0): t**5 / (t**2 + t + 1), (2, 2): -t**5, (4, 4): t**6 * (t**4 + t**3 + t**2 + t + 1) / (t**2 + t + 1),
         (0, 2): 0, (2, 0): 0, (2, 4): 0, (4, 2): 0}
ratio = None
for k in codex:
    ours = c.get(k, sp.Integer(0))
    if codex[k] == 0:
        print('  sector', k, 'zero in ours?', sp.simplify(ours) == 0)
    else:
        r = sp.factor(sp.cancel(ours / codex[k]))
        print('  sector', k, 'ours/codex =', r)
# Codex's matrix identities in engineB's normalised t-form
M = ES.M; v0 = ES.v0
f = [sp.Matrix(9, 1, lambda i, j: 1 if i == k else 0) for k in range(9)]
X1, X2, X3 = M['x1'], M['x2'], M['x3']
a = (X1 * X2 * v0).applyfunc(sp.expand)
print('X1 X2 f0 =', list(a), ' == t^4 f2 ?', a == t**4 * f[2])
b1 = (X1 * f[2]).applyfunc(sp.expand); b3 = (X3 * f[2]).applyfunc(sp.expand)
print('X1 f2 =', list(b1)); print('X3 f2 =', list(b3), ' equal:', b1 == b3)
phiX1w = sp.factor(sp.cancel((ES.phi * X1 * f[2])[0, 0]))
print('phi X1 f2 =', phiX1w)
# is f2 / phi X1 an eigen(co)vector of X1 or X3?
for nm, X in (('X1', X1), ('X3', X3)):
    w = X * f[2]
    print(nm, 'f2 eigen?', sp.Matrix.hstack(w, f[2]).rank() == 1)
    cov = ES.phi * X1
    print(nm, 'phi.X1 eigen-covector?', sp.Matrix.vstack(cov * X, cov).applyfunc(sp.cancel).rank() == 1)
# lp.J along the diagonal
for m in range(0, 4):
    hw = 's.l1.l1.x2.x1.' + '.'.join(['x1'] * (2 * m) + ['y3'] * (2 * m) + ['x1']) + '.u2.u2'
    hw = hw.replace('..', '.')
    print('m =', m, hw, 'lp.J =', lp.J(hw))
for (m, n) in [(1, 0), (0, 1), (2, 0), (0, -1)]:
    W = ['x2', 'x1'] + (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n)) + ['x1']
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    print((m, n), hw, 'lp.J =', lp.J(hw))
json.dump({'%d%d' % k: str(v) for k, v in c.items()}, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/step1_exact.json', 'w'), indent=1)
print('time', round(time.time() - t0, 1))
