"""Margin test for the A-adic ping-pong on squared 3|3 twists (separating twists in genus 2).
For curves c, x, y, z (images of c=d{123} under braids), generators R = rho(T^2) (ratio A^24)
and Q = rho(T) (ratio A^12).  For every freely reduced word w of length L, compute
D(w) = (max exponent - min exponent) over all matrix entries of rho(w).  A scalar matrix has D = 0.
Report min D over words of each length; also check collisions rho(w) v_c ~ v_c for w not in <T_c>."""
import sys, itertools, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *
vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
def inv_word(w): return [-g for g in reversed(w)]
TC = [1, 2] * 3                      # T_c, c = d{123}
def conj(g, w): return g + w + inv_word(g)
def mmul(X, Y):
    Z = [[{} for _ in range(DIM)] for _ in range(DIM)]
    for i in range(DIM):
        for k in range(DIM):
            if not X[i][k]: continue
            for j in range(DIM):
                if Y[k][j]:
                    Z[i][j] = ladd(Z[i][j], lmul(X[i][k], Y[k][j]))
    return Z
def Dspan(M):
    lo, hi = None, None
    for row in M:
        for p in row:
            if p:
                a, b = min(p), max(p)
                lo = a if lo is None else min(lo, a); hi = b if hi is None else max(hi, b)
    return hi - lo
def proportional(a, b):
    for i in range(DIM):
        for j in range(i + 1, DIM):
            if ladd(lmul(a[i], b[j]), lmul(a[j], b[i]), -1): return False
    return True
def perm(word):
    p = list(range(6))
    for g in reversed(word):
        i = abs(g) - 1
        p = [(i + 1 if x == i else i if x == i + 1 else x) for x in p]
    return p
conjs = {'c': [], 'x': [-3, 2, -4], 'y': [5, -3, 4, 2, -3], 'z': [2, 2, -4, 3, 5]}
for k, g in conjs.items():
    p = perm(g); print(k, 'g =', g, ' encloses', sorted(p[i] + 1 for i in range(3)))
power = int(sys.argv[1]) if len(sys.argv) > 1 else 2
names = sys.argv[2] if len(sys.argv) > 2 else 'cxy'
Lmax = int(sys.argv[3]) if len(sys.argv) > 3 else 4
gens = {}
for k in names:
    w = conj(conjs[k], TC * power)
    gens[(k, 1)] = rho_mat(w); gens[(k, -1)] = rho_mat(inv_word(w))
print('power', power, 'curves', names)
for k in names:
    h = Hform(vc, rho_vec(conjs[k], vc)); 
    print('  span N(c,%s) =' % k, (max(h) - min(h) - 20) if h else None)
t0 = time.time()
layer = {((k, s),): gens[(k, s)] for (k, s) in gens}
for L in range(1, Lmax + 1):
    if L > 1:
        new = {}
        for w, M in layer.items():
            last = w[-1]
            for (k, s) in gens:
                if k == last[0] and s == -last[1]: continue
                new[w + ((k, s),)] = mmul(M, gens[(k, s)])
        layer = new
    Ds = []; coll = 0; worst = None
    for w, M in layer.items():
        d = Dspan(M); Ds.append(d)
        if worst is None or d < worst[0]: worst = (d, w)
        if any(k != 'c' for k, s in w):
            v = mat_vec(M, vc)
            if proportional(vc, v): coll += 1
    print('L=%d words=%d minD=%d maxD=%d collisions(w not in <T_c>)=%d worst=%s  t=%.1fs' % (L, len(Ds), min(Ds), max(Ds), coll, worst[1], time.time() - t0))
