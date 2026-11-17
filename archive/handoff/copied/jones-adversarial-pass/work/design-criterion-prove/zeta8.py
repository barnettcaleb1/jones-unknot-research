"""At delta=0 (A = zeta_8) compare lines [v_c'] with [v_c] and record |N(zeta_8)|.
N = (rho(phi) v_c)_{m0}. Collinearity at zeta_8 <=> same Z-splitting (Kasahara Lemma 2.1 model)."""
import sys, random, cmath
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
z = cmath.exp(2j * cmath.pi / 16)   # A with A^4 = i ... use A^4=-1: A = e^{i pi/4}
z = cmath.exp(1j * cmath.pi / 4)
def ev(p, a): return sum(c * a ** e for e, c in p.items())
def perm(word):
    p = list(range(6))
    for g in reversed(word):
        i = abs(g) - 1
        p = [(i + 1 if x == i else i if x == i + 1 else x) for x in p]
    return p
random.seed(5)
hist = {}; same_line = 0; tot = 0
v0 = [ev(p, z) for p in vc]
for it in range(4000):
    L = random.randint(1, 14)
    w = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(L)]
    if random.random() < 0.5: w = [g for x in w for g in (x, x)]
    v = rho_vec(w, vc)
    vz = [ev(p, z) for p in v]
    N = vz[4]
    key = round(abs(N), 3)
    hist[key] = hist.get(key, 0) + 1
    # collinearity at zeta_8
    col = all(abs(vz[i] * v0[j] - vz[j] * v0[i]) < 1e-6 for i in range(5) for j in range(5))
    tot += 1; same_line += col
print("|N(zeta_8)| histogram (top 12):", sorted(hist.items(), key=lambda t: -t[1])[:12])
print("fraction with [v_c'](zeta_8) = [v_c](zeta_8):", same_line, "/", tot)
