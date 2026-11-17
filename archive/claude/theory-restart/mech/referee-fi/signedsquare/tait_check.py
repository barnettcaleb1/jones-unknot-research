#!/usr/bin/env python3
"""Referee script 5: re-derivation of CX-BOX-SQUARE from the matrix-tree theorem, tested corner by corner.
For random connected two-box diagrams: build the black Tait graph of the diagram completed by auxiliary crossings in
the boxes, signs s_e at outside crossings (black-IN smoothing has weight A^{s_e}), signed tree polynomial
T(x,y) = det(M + x pp^T + y qq^T), and compare the PREDICTED corner values
        C_b(zeta_8) = q i^(-b1-b2) tau_b,   q = zeta^(-sum s_e) i^(v-1)
with the actual reduced raw brackets (TL-direct state sum, independent of the Tait construction).
Also checks tau10 tau01 - tau00 tau11 = (p^T adj(M) q)^2."""
import sys, random, collections
sys.dont_write_bytecode = True
import sympy as sp
from twobox import *

def tait_data(word, n, closure):
    b, boxes, free = build(word, n, closure)
    if free:
        return None
    nc = b.ncross
    # connectivity of the projection
    par = list(range(nc))
    def find(u):
        while par[u] != u:
            par[u] = par[par[u]]; u = par[u]
        return u
    for (i, s), (j, t) in b.conn.items():
        par[find(i)] = find(j)
    if len({find(i) for i in range(nc)}) > 1:
        return None
    # faces: corner (i,s) = corner between slots s-1 and s; walking with the face on the left,
    # arriving at port (i,s) we leave by port (i,s-1) and arrive at conn[(i,s-1)].
    face = {}
    nf = 0
    for i in range(nc):
        for s in range(4):
            if (i, s) in face:
                continue
            cur = (i, s)
            while cur not in face:
                face[cur] = nf
                cur = b.conn[(cur[0], (cur[1] - 1) % 4)]
            nf += 1
    # Euler check: V - E + F = 2
    assert nc - 2 * nc + nf == 2, "not planar/connected"
    # checkerboard colouring: corners (i,s) and (i,s+1) are separated by the edge at slot s
    col = {0: 0}
    adj = collections.defaultdict(set)
    for i in range(nc):
        for s in range(4):
            f1, f2 = face[(i, s)], face[(i, (s + 1) % 4)]
            adj[f1].add(f2); adj[f2].add(f1)
    stack = [0]
    while stack:
        f = stack.pop()
        for g in adj[f]:
            if g not in col:
                col[g] = 1 - col[f]; stack.append(g)
            else:
                assert col[g] != col[f], "checkerboard colouring failed"
    black = sorted(f for f in range(nf) if col[f] == 0)
    vid = {f: k for k, f in enumerate(black)}
    v = len(black)
    Lp = sp.zeros(v, v)
    ssum = 0
    marked = {}
    boxc = {c: name for name, c in boxes.items()}
    for i in range(nc):
        if col[face[(i, 0)]] == 0:          # black corners 0,2: A-smoothing (slots 0-1, 2-3 joined) merges them
            f1, f2 = face[(i, 0)], face[(i, 2)]; s_e = 1
        else:                               # black corners 1,3: B-smoothing merges them
            f1, f2 = face[(i, 1)], face[(i, 3)]; s_e = -1
        a, c = vid[f1], vid[f2]
        if i in boxc:
            # box fillings: 0 = id = A-type join, 1 = e = B-type join.  black-IN bit of filling f:
            inbit = {0: 1, 1: 0} if s_e == 1 else {0: 0, 1: 1}
            marked[boxc[i]] = (a, c, inbit)
        else:
            ssum += s_e
            if a != c:
                Lp[a, a] += s_e; Lp[c, c] += s_e; Lp[a, c] -= s_e; Lp[c, a] -= s_e
    def inc(a, c):
        vec = sp.zeros(v, 1)
        if a != c:
            vec[a] = 1; vec[c] = -1
        return vec
    keep = list(range(1, v))
    x, y = sp.symbols('x y')
    p = inc(*marked['B1'][:2]).extract(keep, [0]) if v > 1 else None
    q = inc(*marked['B2'][:2]).extract(keep, [0]) if v > 1 else None
    if v > 1:
        Mr = Lp.extract(keep, keep)
        T = sp.Poly(sp.expand((Mr + x * p * p.T + y * q * q.T).det()), x, y)
        m = (p.T * Mr.adjugate() * q)[0, 0]
    else:
        T = sp.Poly(sp.Integer(1), x, y); m = 0
    tau = {(0, 0): int(T.coeff_monomial(1)), (1, 0): int(T.coeff_monomial(x)), (0, 1): int(T.coeff_monomial(y)), (1, 1): int(T.coeff_monomial(x * y))}
    return v, ssum, tau, int(m), marked['B1'][2], marked['B2'][2]

def z_pow(k):
    k %= 8
    vv = [Fraction(0)] * 4
    if k >= 4:
        vv[k - 4] = Fraction(-1)
    else:
        vv[k] = Fraction(1)
    return tuple(vv)

random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 31)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
st = collections.Counter()
for t in range(N):
    closure = random.choice(["braid", "braid", "plat"])
    n = random.choice([2, 3, 3, 4, 4]) if closure == "braid" else random.choice([2, 4, 4, 6])
    L = random.randint(0, 9)
    word = [(random.randint(1, n - 1), random.choice([1, -1])) for _ in range(L)]
    for name in ('B1', 'B2'):
        word.insert(random.randint(0, len(word)), (random.randint(1, n - 1), name))
    td = tait_data(word, n, closure)
    if td is None:
        st["skipped (disconnected projection)"] += 1
        # disconnected: all corners must vanish at zeta
        C = tl_tensor(word, n, closure)
        if any(not z_iszero(z_eval(C[i][j])) for i in range(2) for j in range(2)):
            st["FAIL: disconnected but nonzero at zeta"] += 1
        continue
    v, ssum, tau, m, in1, in2 = td
    st["connected diagrams"] += 1
    C = tl_tensor(word, n, closure)
    ok = True
    for f1 in range(2):
        for f2 in range(2):
            b1, b2 = in1[f1], in2[f2]
            # predicted: zeta^(-ssum) * i^(v-1) * i^(-b1-b2) * tau ;  i = z^2
            pred = tuple(Fraction(tau[(b1, b2)]) * c for c in z_pow(-ssum + 2 * (v - 1) - 2 * (b1 + b2)))
            if pred != z_eval(C[f1][f2]):
                ok = False
    sq = tau[(1, 0)] * tau[(0, 1)] - tau[(0, 0)] * tau[(1, 1)]
    if sq != m * m:
        ok = False
    k = (1 if in1[1] == 0 else 0) + (1 if in2[1] == 0 else 0)
    st["label reversals k=%d" % k] += 1
    if m != 0:
        st["m != 0"] += 1
    if ok:
        st["phase formula + square identity exact"] += 1
    else:
        st["FAIL"] += 1
        print("FAIL", closure, n, word, td)
for k in sorted(st):
    print("%-45s %d" % (k, st[k]))
