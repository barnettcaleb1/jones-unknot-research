# Validate the curve model: Lemma 3.1 / simplicity of every disk, Lemma 6.1 (n=4), Lemma 4.2/note Lemma 1,
# planar M vs homological pairing, and note Lemma 2 (M_{YX}(-1) = +-M_X(-1) when rho(Y)=I at t=-1).
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lp import *
from curves import *

random.seed(12345)
def rand_braid(n, L):
    return [random.choice([1, -1]) * random.randint(1, n - 1) for _ in range(L)]
def rand_pure(n, L):
    # random product of conjugated pure generators
    def A(i, j):
        up = list(range(j - 1, i, -1)); return up + [i, i] + finv(up)
    out = []
    for _ in range(L):
        i = random.randint(1, n - 1); j = random.randint(i + 1, n)
        g = A(i, j)
        if random.random() < .5: g = finv(g)
        c = rand_braid(n, random.randint(0, 3))
        out += c + g + finv(c)
    return out

n = 4
stats = dict(arcs=0, disks=0, nonsimple=0, lemma61_fail=0, lemma1_fail=0, pairing_fail=0, l31_fail=0)
types = {}
for trial in range(400):
    br = rand_pure(n, random.randint(1, 4))
    if perm(br, n) != [1, 2, 3, 4]: continue
    try:
        A_ = analyse(br, n)
    except AssertionError as e:
        print("analyse failed", e); continue
    stats['arcs'] += 1
    terms, disks = A_['terms'], A_['disks']
    # Lemma 3.1 : k_{i+1}-k_i = W_i ;  disks simple
    for i, d in enumerate(disks):
        stats['disks'] += 1
        if not d['simple']: stats['nonsimple'] += 1
        if terms[i + 1][1] - terms[i][1] != d['W']: stats['l31_fail'] += 1
        P = d['P']
        one_endpoint = len(P & {1, 2}) == 1
        if (not d['changing']) != one_endpoint or (P and P <= {1, 2}): stats['lemma61_fail'] += 1
        key = (tuple(sorted(P)), 'chg' if d['changing'] else 'pres')
        types[key] = types.get(key, 0) + 1
    # note Lemma 1: parity => |M(-1)| = m
    if parity_ok(disks) and abs(M_at_minus1(terms)) != len(terms): stats['lemma1_fail'] += 1
    # planar M vs homological pairing of the boundary loop: pairing = (1 - t^s) * M for a fixed s
    M = moody_poly([(e, k) for e, k in terms])
    Pr = homological_pairing(A_['loop'], n)
    # undo normalisation: planar terms are shifted by k0; compare up to monomial
    ok = False
    for s in (1, -1):
        prod = lmul(lp({0: 1, s: -1}), M)
        for sh in range(-60, 61):
            if lmul(prod, lmono(1, sh)) == Pr or lmul(prod, lmono(-1, sh)) == Pr:
                ok = True; break
        if ok: break
    if not ok and terms: stats['pairing_fail'] += 1
print(stats)
print("disk types seen (P, sign behaviour): count")
for k in sorted(types, key=lambda x: (len(x[0]), x)): print("  ", k, types[k])

# ---- note Lemma 2 in the planar model: Y = Phi0 (rho=I at t=-1), X random pure braid
def A(i, j):
    up = list(range(j - 1, i, -1)); return up + [i, i] + finv(up)
b = fcomm(fcomm(A(1, 4), A(2, 4)), A(3, 4))
# use a smaller Torelli-at-(-1) element to keep words short: Y = [Delta_3^4, A_34]  (also trivial at t=-1)
Y = fcomm([1, 2] * 6, A(3, 4))
assert meval(burau(4, Y), -1) == [[int(i == j) for j in range(4)] for i in range(4)]
print("Y=[Delta_3^4, A34]: rho_4(Y)=I at t=-1, nontrivial at t=2:", meval(burau(4, Y), 2) != [[int(i == j) for j in range(4)] for i in range(4)])
bad = 0; tot = 0
for trial in range(60):
    X = rand_pure(4, random.randint(1, 3))
    try:
        AX = analyse(X, 4); AYX = analyse(Y + X, 4); AXY = analyse(X + Y, 4)
    except AssertionError:
        continue
    tot += 1
    mx = M_at_minus1(AX['terms']); myx = M_at_minus1(AYX['terms']); mxy = M_at_minus1(AXY['terms'])
    if abs(mx) != abs(myx) or abs(mx) != abs(mxy): bad += 1
    if trial < 6:
        print(f"  |M_X(-1)|={abs(mx)}  |M_YX(-1)|={abs(myx)}  |M_XY(-1)|={abs(mxy)}   iota(X)={len(AX['terms'])} iota(YX)={len(AYX['terms'])}")
print(f"Lemma 2 planar test: {tot} pairs, failures {bad}")
