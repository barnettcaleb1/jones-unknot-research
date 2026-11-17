"""Lean numeric sanity check at A = 3/7 (exact rationals): foreign line (e1 v_c = 0) <=> collision [v_{s1 c}] = [v_c],
on words psi where psi(c0) crosses d12; plus Gram definiteness for delta near 2 (A near i on the unit circle)."""
import random, math
import sympy as sp
a = sp.Rational(3, 7); dl = -a**2 - a**-2
def matchings(pts):
    if not pts: return [()]
    x0, out = pts[0], []
    for k in range(1, len(pts), 2):
        for x in matchings(pts[1:k]):
            for y in matchings(pts[k+1:]): out.append(((x0, pts[k]),) + x + y)
    return out
B = [tuple(sorted(m)) for m in matchings(list(range(1, 7)))]; idx = {m: i for i, m in enumerate(B)}
def e(i, dval):
    M = sp.zeros(5, 5)
    for j, m in enumerate(B):
        P = {}
        for p, q in m: P[p] = q; P[q] = p
        if P[i] == i + 1: M[j, j] += dval
        else:
            p, q = P[i], P[i+1]
            n = [r for r in m if i not in r and i+1 not in r] + [(i, i+1), tuple(sorted((p, q)))]
            M[idx[tuple(sorted(n))], j] += 1
    return M
E = {i: e(i, dl) for i in range(1, 6)}
S = {i: a*sp.eye(5) + E[i]/a for i in range(1, 6)}; Si = {i: S[i].inv() for i in range(1, 6)}
br = lambda n: (a**(2*n) - a**(-2*n)) / (a**2 - a**-2)
v0 = sp.Matrix([br(2), 1, 1, br(2), br(3)])
T = (S[1]*S[2])**3
assert T*v0 == a**6*v0 and E[1]*v0 == sp.zeros(5, 1)
def wm(wd):
    M = sp.eye(5)
    for g in wd: M = M*(S[g] if g > 0 else Si[-g])
    return M
random.seed(7)
tests = [[2, 3], [2, -3], [-2, 3, 3], [3, 2, 4, 3], [2, 3, 3, 2], [-2, -3, 4, 3, 2]]
for _ in range(6): tests.append([random.choice([2, 3, 4, -2, -3, -4, 1, 5]) for _ in range(7)] + [3])
for wd in tests:
    w = wm(wd)*v0
    coll = sp.Matrix.hstack(w, S[1]*w).rank() == 1
    fl = E[1]*w == sp.zeros(5, 1)
    print('psi', wd, ' collision(c, s1 c):', coll, ' e1 v_c = 0:', fl, flush=True)
def loops(m, n):
    adj = {}
    for p, q in list(m) + list(n):
        adj.setdefault(p, []).append(q); adj.setdefault(q, []).append(p)
    seen, c = set(), 0
    for p in adj:
        if p in seen: continue
        c += 1; st = [p]
        while st:
            q = st.pop()
            if q in seen: continue
            seen.add(q); st.extend(adj[q])
    return c
for eps in [0.05, 0.2, 0.6]:
    dv = 2*math.cos(2*eps)
    G = sp.Matrix(5, 5, lambda i, j: sp.Float(dv, 30)**loops(B[i], B[j]))
    print('A = i*exp(i*%.2f), delta = %.4f, leading minors:' % (eps, dv), [float(G[:k, :k].det()) for k in range(1, 6)], flush=True)
