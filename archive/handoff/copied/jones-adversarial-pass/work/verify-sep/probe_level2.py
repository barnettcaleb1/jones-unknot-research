"""Level-2 check: among random partition-PRESERVING phi with phi(c) != c, record min span(N)
(N = [3] H(v_c,v_c')/H(v_c,v_c), span(N) = span(H) - 20). Collision needs span(N)=8."""
import sys, random, time, json
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
from intersect import curve, count_crossings, Ribbon, cyc_reduce
from probe_collision import proportional, same_curve, vc, c0, R
def perm(word):
    p = list(range(6))
    for g in reversed(word):
        i = abs(g) - 1
        p = [(i + 1 if x == i else i if x == i + 1 else x) for x in p]
    return p
def preserves(word):
    p = perm(word); S = {p[0], p[1], p[2]}
    return S in ({0, 1, 2}, {3, 4, 5})
random.seed(23)
t0 = time.time(); hist = {}; low = []; n = 0
while time.time() - t0 < 100:
    L = random.randint(1, 18)
    w = [random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(L)]
    if random.random() < 0.6:
        w = [g for x in w for g in (x, x)]
    if not preserves(w):
        continue
    wv = rho_vec(w, vc)
    if proportional(vc, wv):
        continue
    h = Hform(vc, wv); sN = max(h) - min(h) - 20
    n += 1
    hist[sN] = hist.get(sN, 0) + 1
    if sN <= 12 and len(low) < 30:
        cw = curve(w); low.append((w, sN, count_crossings(c0, cw, R)))
print("partition-preserving, phi(c)!=c samples:", n)
print("span(N) histogram:", dict(sorted(hist.items())))
print("low-span examples (word, spanN, i):", low[:6])
print("i values among span(N)=12:", sorted({x[2] for x in low if x[1] == 12}))
