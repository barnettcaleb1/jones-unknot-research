"""Exact seven-sector coefficients c_ab(U,V) = phi rho(U) E_ab rho(V) v in Q(t) (sympy), E_ab = joint spectral projectors of
the normalised full-twist sites X1^2 (legs 0,1) and X3^2 (legs 2,3).  J_raw(m,n) =. sum_ab c_ab u^(e_a m + e_b n), u = t^2.
Also returns the exact list of identically vanishing c_ab.  (Codex request: record the seven c_ab for promising templates.)"""
import sys, json
import sympy as sp
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import rho2
t = sp.symbols('t')
MT, VT, PHIT = rho2.normalised()
def S(p): return sum(c * t**e for e, c in p.items()) if p else sp.Integer(0)
M = {L: sp.Matrix(9, 9, lambda i, j: S(MT[L][i][j])) for L in MT}
v0 = sp.Matrix(9, 1, lambda i, j: S(VT['l1.l1'][i]))
phi = sp.Matrix(1, 9, lambda i, j: S(PHIT['u2.u2'][j])) * t**2 / (1 + t)**4
lam = [sp.Integer(1), -t, t**3]
I9 = sp.eye(9)
def proj(X, a):
    R = I9
    for b in range(3):
        if b != a: R = R * (X - lam[b] * I9) / (lam[a] - lam[b])
    return R.applyfunc(sp.cancel)
COL = [0, 2, 4]
P1 = [proj(M['x1'], a) for a in range(3)]
P3 = [proj(M['x3'], b) for b in range(3)]
E = {(COL[a], COL[b]): (P1[a] * P3[b]).applyfunc(sp.cancel) for a in range(3) for b in range(3)}
def rho(W):
    R = I9
    for L in W: R = M[L] * R
    return R
def cab(V, U):
    vv = rho(V) * v0; ww = phi * rho(U)
    out = {}
    for k, Ek in E.items():
        if all(x == 0 for x in Ek): continue
        out[k] = sp.factor(sp.cancel((ww * Ek * vv)[0, 0]))
    return out
if __name__ == '__main__':
    import time
    t0 = time.time()
    print('ranks', {k: E[k].rank() for k in E}, round(time.time() - t0, 1))
    templates = [(sys.argv[i], sys.argv[i + 1]) for i in range(1, len(sys.argv) - 1, 2)]
    res = []
    for Vs, Us in templates:
        V = [x for x in Vs.split('.') if x]; U = [x for x in Us.split('.') if x]
        c = cab(V, U)
        zero = [k for k, x in c.items() if x == 0]
        print('TEMPLATE V =', Vs, ' U =', Us); print('  identically zero:', zero)
        for k, x in sorted(c.items()): print('  c%d%d =' % k, x)
        # check: sum of c_ab = J_raw(0,0)
        tot = sp.factor(sp.cancel(sum(c.values())))
        print('  sum c_ab = J_raw(0,0) =', tot)
        res.append({'V': Vs, 'U': Us, 'c': {'%d%d' % k: str(x) for k, x in c.items()}, 'zero': ['%d%d' % k for k in zero], 'Jraw00': str(tot)})
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/exact_sectors.json', 'w'), indent=1)
