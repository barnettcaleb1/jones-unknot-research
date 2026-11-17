"""Test 'three-term positivity': for partition-preserving phi, is N = (rho(phi)v_c)_{m0}
(up to sign) a Laurent polynomial with nonnegative coefficients and N(1)=+-3?"""
import sys, random, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
M0 = 4
def perm(word):
    p = list(range(6))
    for g in reversed(word):
        i = abs(g) - 1
        p = [(i + 1 if x == i else i if x == i + 1 else x) for x in p]
    return p
def preserves(word):
    p = perm(word); S = {p[0], p[1], p[2]}
    return S in ({0, 1, 2}, {3, 4, 5})
def proportional(a, b):
    # a, b vectors of Laurent polys; check a_i b_j == a_j b_i
    for i in range(DIM):
        for j in range(i+1, DIM):
            if ladd(lmul(a[i], b[j]), lmul(a[j], b[i]), -1):
                return False
    return True
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
T = float(sys.argv[2]) if len(sys.argv) > 2 else 60
t0 = time.time()
stats = {}
bad = []
n = 0
while time.time() - t0 < T:
    L = random.randint(1, 16)
    w = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(L)]
    if random.random() < 0.5:
        w = [g for x in w for g in (x, x)]
    pres = preserves(w)
    wv = rho_vec(w, vc)
    if proportional(vc, wv):
        continue
    N = wv[M0]
    n += 1
    coeffs = list(N.values())
    pos = all(c > 0 for c in coeffs) or all(c < 0 for c in coeffs)
    val1 = sum(coeffs)
    nterms = sum(abs(c) for c in coeffs)
    key = (pres, pos, val1 if val1 >= 0 else -val1)
    stats[key] = stats.get(key, 0) + 1
    if pres and not pos and len(bad) < 8:
        bad.append((w, lstr(N)))
print("samples", n)
for k in sorted(stats):
    print("  preserving=%s  signcoherent=%s |N(1)|=%s : %d" % (k[0], k[1], k[2], stats[k]))
print("non-sign-coherent preserving examples:")
for b in bad:
    print("  ", b)
