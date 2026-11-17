# Independent check of Theorem A: for 3|3 curves c, c' = phi(c), |N(zeta8)| is an odd integer,
# where N = (rho(phi) v_c)_{m0}, m0 = (16)(25)(34), so H(v_c, rho(phi) v_c) = -[3][4] N.
import sys, random
sys.path.insert(0, sys.argv[1])
from tl6 import *
def m_of(pairs):
    return to_partner([(a - 1, b - 1) for a, b in pairs])
order = [m_of([(1,2),(3,4),(5,6)]), m_of([(1,2),(3,6),(4,5)]), m_of([(1,4),(2,3),(5,6)]),
         m_of([(1,6),(2,3),(4,5)]), m_of([(1,6),(2,5),(3,4)])]
TWO = {2: 1, -2: 1}; THREE = {4: 1, 0: 1, -4: 1}
Tc = [1, 2] * 3
found = None
for s2 in (1, -1):
    v = vzero()
    for m, val in zip(order, [lscale(TWO, s2), ONE, ONE, lscale(TWO, s2), THREE]):
        v[IDX[m]] = dict(val)
    w = rho_vec(Tc, v)
    if vec_eq(w, [lscale(x, 1, 6) for x in v]) or vec_eq(w, [lscale(x, 1, -6) for x in v]):
        found = (s2, v)
print("eigenvector sign choice for [2]:", found[0] if found else None)
vc = found[1]
m0 = IDX[order[4]]
# check H(v_c, w) = -[3][4] w_m0 on a random vector-ish image
FOUR = {6: 1, 2: 1, -2: 1, -6: 1}
w = rho_vec([1, -3, 2, 5, -4], vc)
lhs = Hform(vc, w); rhs = lscale(lmul(lmul(THREE, FOUR), w[m0]), -1)
print("H(v_c,w) = -[3][4] w_m0 :", ladd(lhs, rhs, -1) == {} , "| alt sign:", ladd(lhs, rhs, 1) == {})
def red8(p):  # Laurent poly -> Z[zeta8] coords a0..a3 with zeta^4 = -1
    a = [0, 0, 0, 0]
    for e, c in p.items():
        r = e % 8
        if r < 4: a[r] += c
        else: a[r - 4] -= c
    return a
def norm8(a):  # N * conj(N) in Z[zeta8], conj(zeta) = zeta^-1 = -zeta^3
    # multiply polynomials then reduce
    ab = [0] * 4
    conj = [a[0], -a[3], -a[2], -a[1]]  # zeta^-1=-z^3, zeta^-2=-z^2, zeta^-3=-z
    prod = [0] * 7
    for i in range(4):
        for j in range(4):
            prod[i + j] += a[i] * conj[j]
    for k in range(7):
        if k < 4: ab[k] += prod[k]
        else: ab[k - 4] -= prod[k]
    return ab
random.seed(7)
hist = {}; bad = 0; tot = 0
for _ in range(3000):
    L = random.randint(1, 14)
    word = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(L)]
    N = rho_vec(word, vc)[m0]
    nn = norm8(red8(N))
    tot += 1
    if nn[1] or nn[2] or nn[3]:
        bad += 1; continue
    val = nn[0]; r = int(round(val ** 0.5))
    if r * r != val or r % 2 == 0:
        bad += 1; print("violation", word, val); continue
    hist[r] = hist.get(r, 0) + 1
print("samples:", tot, " violations:", bad, " |N(zeta8)| histogram:", dict(sorted(hist.items())))
