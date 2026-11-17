#!/usr/bin/env python3
"""Referee script 2: the rank-two determinant identity and the signed matrix-tree model.
 (a) symbolic: for generic symmetric M (sizes 1..4) and vectors p,q:
       det(M + x pp^T + y qq^T) = t00 + t10 x + t01 y + t11 xy,
       t10 t01 - t00 t11 = (p^T adj(M) q)^2     (polynomial identity, so valid for singular M).
 (b) brute force: random signed multigraphs (loops, bridges, parallel edges allowed) with two marked edges;
     enumerate spanning trees directly, compare tree counts tau_b with the determinant coefficients,
     and check tau10 tau01 - tau00 tau11 is a perfect square.
"""
import itertools, random, math
import sympy as sp

x, y = sp.symbols('x y')
print("== (a) symbolic identity ==")
for n in range(1, 5):
    syms = {}
    Mm = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            s = sp.Symbol('m%d%d' % (i, j))
            Mm[i, j] = s; Mm[j, i] = s
    p = sp.Matrix([sp.Symbol('p%d' % i) for i in range(n)])
    q = sp.Matrix([sp.Symbol('q%d' % i) for i in range(n)])
    T = sp.expand((Mm + x*p*p.T + y*q*q.T).det())
    P = sp.Poly(T, x, y)
    t00 = P.coeff_monomial(1); t10 = P.coeff_monomial(x); t01 = P.coeff_monomial(y); t11 = P.coeff_monomial(x*y)
    hi = [m for m in P.monoms() if m[0] > 1 or m[1] > 1]
    lhs = sp.expand(t10*t01 - t00*t11)
    rhs = sp.expand(((p.T*Mm.adjugate()*q)[0, 0])**2)
    print("n=%d: bilinear in (x,y): %s ; identity holds: %s" % (n, not hi, sp.expand(lhs - rhs) == 0))

print("\n== (b) brute-force signed spanning trees ==")
random.seed(7)
def trees(nv, edges):
    """yield subsets (tuples of edge indices) forming spanning trees"""
    for sub in itertools.combinations(range(len(edges)), nv - 1):
        parent = list(range(nv))
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]; u = parent[u]
            return u
        ok = True
        for k in sub:
            a, b, _ = edges[k]
            ra, rb = find(a), find(b)
            if ra == rb:
                ok = False; break
            parent[ra] = rb
        if ok:
            yield sub
nbad = 0; ntests = 0; nsing = 0
for trial in range(400):
    nv = random.randint(1, 6)
    ne = random.randint(0, 9)
    edges = [(random.randrange(nv), random.randrange(nv), random.choice([1, -1])) for _ in range(ne)]
    # two marked edges (weights x,y) appended; may be loops, parallel, bridges
    m1 = (random.randrange(nv), random.randrange(nv))
    m2 = (random.randrange(nv), random.randrange(nv))
    alle = edges + [(m1[0], m1[1], 'x'), (m2[0], m2[1], 'y')]
    tau = {(0, 0): 0, (1, 0): 0, (0, 1): 0, (1, 1): 0}
    for sub in trees(nv, alle):
        b1 = int(ne in sub); b2 = int(ne + 1 in sub)
        w = 1
        for k in sub:
            if k < ne:
                w *= alle[k][2]
        tau[(b1, b2)] += w
    # reduced Laplacian (delete vertex 0)
    Lr = sp.zeros(nv, nv)
    for a, b, s in edges:
        if a != b:
            Lr[a, a] += s; Lr[b, b] += s; Lr[a, b] -= s; Lr[b, a] -= s
    def inc(e):
        v = sp.zeros(nv, 1)
        if e[0] != e[1]:
            v[e[0]] = 1; v[e[1]] = -1
        return v
    pv, qv = inc(m1), inc(m2)
    keep = list(range(1, nv))
    Mr = Lr.extract(keep, keep); pr = pv.extract(keep, [0]); qr = qv.extract(keep, [0])
    if nv == 1:
        Tdet = sp.Integer(1)
    else:
        Tdet = sp.expand((Mr + x*pr*pr.T + y*qr*qr.T).det())
    P = sp.Poly(Tdet, x, y)
    co = {(0, 0): P.coeff_monomial(1), (1, 0): P.coeff_monomial(x), (0, 1): P.coeff_monomial(y), (1, 1): P.coeff_monomial(x*y)}
    ntests += 1
    val = tau[(1, 0)]*tau[(0, 1)] - tau[(0, 0)]*tau[(1, 1)]
    if nv > 1 and Mr.det() == 0:
        nsing += 1
    if any(co[k] != tau[k] for k in tau) or val < 0 or math.isqrt(val)**2 != val:
        nbad += 1
        print("BAD", nv, edges, m1, m2, tau, co)
print("graphs tested:", ntests, " with singular reduced outside Laplacian:", nsing, " failures:", nbad)
