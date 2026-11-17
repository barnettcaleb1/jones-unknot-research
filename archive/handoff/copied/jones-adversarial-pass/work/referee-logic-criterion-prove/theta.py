import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
from curves import ldiv_exact, T34
conjs = {0: [], 1: [3], 7: [3, 3], 10: [2, -3]}
v = {k: rho_vec(g, vc) for k, g in conjs.items()}
def N(s, t):
    return ldiv_exact(lscale(Hform(v[s], v[t]), -1), T34)
TH3 = {4: 1, 0: 1, -4: 1}
def theta(t, s, y):
    # theta = N(t,y) - N(t,s)N(s,y)/[3]  -> return numerator N(t,y)[3] - N(t,s)N(s,y)
    return ladd(lmul(N(t, y), TH3), lmul(N(t, s), N(s, y)), -1)
B = [0, 1, 7, 1, 0, 10]
seq = B * 3
seen = set()
for y, s, t in zip(seq, seq[1:], seq[2:]):
    if (y, s, t) in seen: continue
    seen.add((y, s, t))
    th = theta(t, s, y)
    at_i = sum(c * (1j) ** e for e, c in th.items())
    print('junction (y=%d; s=%d; t=%d): N(s,y) span=%s, [3]*theta span=%s, nonzero=%s, theta(i)*[3](i)=%s, partitions %s %s %s' % (
        y, s, t, (max(N(s, y)) - min(N(s, y))), (max(th) - min(th)) if th else None, bool(th), at_i,
        partition(conjs[y]), partition(conjs[s]), partition(conjs[t])))
