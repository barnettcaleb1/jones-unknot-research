"""C1's automaton lemmas (v3lemmas.py: P1 Psi monotone = BX3, P2 max rho_a by final class, P3 q-data by class,
P6 = Lemma T2 max(lambda_q + rho_a) by class, P4/P5 = BX4' Psi-preserving walks) recomputed on MY K=3 automaton."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_core as C
from fractions import Fraction as Fr
K = 3
st, T = C.build_auto(K)
def cls(s):
    if s == 'init': return 'init'
    if s == 'tiny': return 'S3+'
    d, j = s
    if d == -1: return 'R1' if j[1] == 1 else 'R0'      # j = (lc, x1, x2, x3): x1 = c of R_c
    return 'S%d' % (-4 - d)
phi = lambda s: 1 if cls(s).startswith('R') else 0
E = [(s, m, ns, C.logjet(Dj[2])) for (s, m), (Dj, ns) in T.items()]
bad = [(s, m) for s, m, ns, l in E if l[0] + phi(ns) - phi(s) > 0]
print('P1 (BX3) Psi = rho_a + phi non-increasing on all %d edges: %s' % (len(E), not bad))
def longest(f, allowed=lambda e: True):
    best = {s: None for s in st}; best['init'] = Fr(0)
    for it in range(len(st) + 1):
        ch = False
        for e in E:
            if not allowed(e) or best[e[0]] is None: continue
            v = best[e[0]] + f(e)
            if best[e[2]] is None or v > best[e[2]]: best[e[2]] = v; ch = True
        if not ch: return best
    raise RuntimeError('positive cycle')
rmax = longest(lambda e: e[3][0])
by = {}
for s in st:
    if s != 'init': by.setdefault(cls(s), []).append(rmax[s])
print('P2 max rho_a by final class:', {c: str(max(v)) for c, v in sorted(by.items())})
qd = {}
for s in st:
    if s == 'init': continue
    dq, lc, x = C.q_end(s, K); l = C.logjet(x)
    qd.setdefault(cls(s), set()).add((dq, lc, l[0], l[1]))
print('P3 q-data (deg, lc, rho_q, lambda_q) by class:', {c: sorted((a, str(b), str(c_), str(d)) for a, b, c_, d in v) for c, v in sorted(qd.items())})
t2 = {}
for s in st:
    if s == 'init': continue
    l = C.logjet(C.q_end(s, K)[2]); v = l[1] + rmax[s]; c = cls(s)
    t2[c] = max(t2.get(c, v), v)
print('P6 (Lemma T2) max (lambda_q + rho_a) by class:', {c: str(v) for c, v in sorted(t2.items())})
pres = lambda e: e[3][0] + phi(e[2]) - phi(e[0]) == 0
l2max = longest(lambda e: e[3][1], pres)
for c in ('R1', 'R0', 'S0', 'S1', 'S2', 'S3+'):
    vals = [(l2max[s], C.logjet(C.q_end(s, K)[2])[1]) for s in st if s != 'init' and cls(s) == c and l2max[s] is not None]
    if vals: print('P4/P5 (BX4\') Psi-preserving walks ending in %s: max l2(a) = %s, max l2(b) = %s' % (c, max(v[0] for v in vals), max(v[0] + v[1] for v in vals)))
    else: print('P4/P5 no Psi-preserving walk ends in', c)
