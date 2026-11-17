#!/usr/bin/env python3
"""Referee script 6 (side exploration, adversarial): among random actual two-box patterns, which have S = G^-1 C a
G-similitude (the regime in which TH-FI-EXT / TH-PATTERN-FI speak)?  For those, record the multiplier, the zeta_8
ratios and the A=1 values, looking for anything with the OUTER-coset signature (negative diagonal ratio, zero entry at
A=1, multiplier (delta^2-1)*norm).
Similitude test without division: N = bar(C)^T adj(G) C = (delta^2-1) S*GS must equal c' G, i.e.
N00 = N11, N01 = N10, N00 = delta*N01."""
import sys, random, collections
sys.dont_write_bytecode = True
from twobox import *

def pbar(p):
    return {-e: c for e, c in p.items()}
def psub(p, q):
    return padd(p, pscale(q, -1))
def mmul(X, Y):
    return [[padd(pmul(X[i][0], Y[0][j]), pmul(X[i][1], Y[1][j])) for j in range(2)] for i in range(2)]
ADJG = [[dict(DELTA), {0: -1}], [{0: -1}, dict(DELTA)]]
D2M1 = psub(pmul(DELTA, DELTA), {0: 1})

random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
st = collections.Counter()
mult = collections.Counter()
shown = 0
for t in range(N):
    closure = random.choice(["braid", "braid", "plat"])
    n = random.choice([2, 3, 3, 4, 4, 5]) if closure == "braid" else random.choice([2, 4, 4, 6])
    L = random.randint(0, 8)
    word = [(random.randint(1, n - 1), random.choice([1, -1])) for _ in range(L)]
    for name in ('B1', 'B2'):
        word.insert(random.randint(0, len(word)), (random.randint(1, n - 1), name))
    C = tl_tensor(word, n, closure)
    st["patterns"] += 1
    det = psub(pmul(C[0][0], C[1][1]), pmul(C[0][1], C[1][0]))
    if not pclean(det):
        st["det C = 0"] += 1
        continue
    Cst = [[pbar(C[j][i]) for j in range(2)] for i in range(2)]
    Nm = mmul(mmul(Cst, ADJG), C)
    sim = (pclean(psub(Nm[0][0], Nm[1][1])) == {} and pclean(psub(Nm[0][1], Nm[1][0])) == {}
           and pclean(psub(Nm[0][0], pmul(DELTA, Nm[0][1]))) == {})
    if not sim:
        st["det != 0, not a similitude"] += 1
        continue
    st["similitude"] += 1
    c1 = pclean(Nm[0][1])                 # = (delta^2-1) * multiplier
    is_unitary = (c1 == pclean(D2M1))
    mult["multiplier 1 (G-unitary S)" if is_unitary else "multiplier " + pstr(c1) + " / (delta^2-1)"] += 1
    res = analyse(C)
    a1 = [[sum(C[i][j].values()) for j in range(2)] for i in range(2)]
    neg = any(d["rational"] and d["ratio"][0] * (-1) ** (i + j) < 0 for (i, j), d in res["anchors"].items())
    if neg:
        st["SIMILITUDE WITH OUTER SIGN"] += 1
    if any(a1[i][j] == 0 for i in range(2) for j in range(2)):
        st["SIMILITUDE WITH ZERO AT A=1"] += 1
    if not res["nonzero"]:
        st["similitude with C(zeta)=0"] += 1
    if not is_unitary and shown < 6:
        shown += 1
        print("non-unitary similitude example:", closure, n, word, " multiplier*(d^2-1) =", pstr(c1), " C(1) =", a1)
for k in sorted(st):
    print("%-40s %d" % (k, st[k]))
for k, v in mult.most_common(12):
    print("   %-60s %d" % (k, v))
