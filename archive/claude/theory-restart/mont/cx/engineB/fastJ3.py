"""Width THREE: rho_3 on Hom(V_1, V_1 x V_2^{x6}) (dim 51), integral t-form, fast exact J for s.l1.l1.l1.W.u2.u2.u2,
W over x0,y0,x1..x5,y1..y5.  Same construction as rho2 (Ball(3)); gauge found by 2-colouring; X_i = t^2 M[x_i], Y = t^-2 M[y0].
J_raw =. t^3 PHI . rho(W) V / (1+t)^6."""
import sys, pickle, os
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rho2, lp
from fastJ import tolist, norm, mul, addto, todict
B = rho2.Ball(3)
n = B.dim
LET = B.letters
V0 = B.vec_of_prefix('l1.l1.l1')
NPHI, _ = B.covec_of_suffix('u2.u2.u2')
# gauge: c_i in {0,1} with exps(M_ij) = 2(c_i - c_j) mod 4
adj = {}
for L, M in B.M.items():
    for i in range(n):
        for j in range(n):
            if M[i][j]:
                r = {e % 4 for e in M[i][j]}
                assert len(r) == 1
                adj.setdefault(i, []).append((j, (r.pop() // 2) % 2))   # c_i - c_j = r/2 mod 2
c = [None] * n; c[0] = 0; stack = [0]
while stack:
    i = stack.pop()
    for j, d in adj.get(i, []):
        cj = (c[i] - d) % 2
        if c[j] is None: c[j] = cj; stack.append(j)
        else: assert c[j] == cj, 'gauge inconsistent'
c = [x if x is not None else 0 for x in c]
def gt(p, shift):
    out = {}
    for e, v in p.items():
        f = e - shift; assert f % 4 == 0
        out[f // 4] = out.get(f // 4, 0) + v
    return {e: v for e, v in out.items() if v}
MT = {}
for L, M in B.M.items():
    unit = 8 if L[0] == 'x' else -8
    MT[L] = [[gt(rho2.pshift(M[i][j], unit), -2 * (c[i] - c[j])) if M[i][j] else {} for j in range(n)] for i in range(n)]
VT = [gt(rho2.pshift(V0[i], 2 * c[i]), 0) if V0[i] else {} for i in range(n)]
# NPHI = delta^6 PHI ; delta^6 = A^-12 (A^4+1)^6 -> exponents: keep A-form then gauge
PT = [gt(rho2.pshift(NPHI[j], -2 * c[j]), 0) if NPHI[j] else {} for j in range(n)]
SM = {L: [[(j, tolist(MT[L][i][j])) for j in range(n) if MT[L][i][j]] for i in range(n)] for L in LET}
VL = [tolist(x) for x in VT]; PL = [tolist(x) for x in PT]
def step(L, v):
    out = []
    for row in SM[L]:
        acc = None
        for j, m in row:
            if v[j] is not None: acc = addto(acc, mul(m, v[j]))
        out.append(norm(acc))
    return out
def J(W):
    v = VL
    for L in W: v = step(L, v)
    acc = None
    for j in range(n):
        if v[j] is not None and PL[j] is not None: acc = addto(acc, mul(PL[j], v[j]))
    acc = norm(acc)
    if acc is None: return None
    y = rho2.tdiv_1pt(todict(acc), 6)
    return lp.normalize(y)
TOP = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
CUPS = {1: 2, 2: 1, 3: 4, 4: 3}; CLEG = 5; BLEG = 0
def is_knot(W):
    pos = list(range(6))
    for L in W:
        i = int(L[1:])
        if i == 0: continue
        a, b = i - 1, i
        for p in range(6):
            if pos[p] == a: pos[p] = b
            elif pos[p] == b: pos[p] = a
    inv = {pos[p]: p for p in range(6)}
    j = CLEG; seen = 0
    while True:
        p = inv[j]; q = TOP[p]; seen += 2; j = pos[q]
        if j == BLEG: return seen == 6
        if j not in CUPS: return False
        j = CUPS[j]
        if seen > 12: return False
def halfword(W): return 's.l1.l1.l1.' + '.'.join(W) + '.u2.u2.u2'
if __name__ == '__main__':
    import random, time
    rnd = random.Random(3); ok = 0; t0 = time.time(); km = 0
    for it in range(300):
        W = [rnd.choice(LET) for _ in range(rnd.randint(1, 16))]
        hw = halfword(W); Jl = lp.J(hw)
        if (Jl is not None) != is_knot(W): km += 1
        if Jl is None: continue
        assert J(W) == Jl, (hw, J(W), Jl)
        ok += 1
    print('fastJ3 == lp.J on', ok, 'width-three knots; knot-test mismatches', km, 'time', round(time.time() - t0, 1))
