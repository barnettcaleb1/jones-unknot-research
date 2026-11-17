"""u2/indep/down.py -- DOWNSTAIRS (quotient picture) re-implementation of regress's global T-disc test, written from scratch
(no import from regress).  Quotient picture: punctures 0 = axis, 1..4 = legs L0..L3 (symbols 1..5); x_i -> s_i on punctures
(i, i+1) (i = 1..3), x0 -> s_0^2 (leg L0 once around the axis), y = inverses (a global mirror is harmless: every criterion is
mirror invariant).  Top half: axis + caps (L0 L1), (L2 L3), then V: psi_0 = (A, B, B^-1, C, C^-1) on F_3 = <A,B,C>.
Closure: H-tree on punctures 0, 1, 4 and E + cup on punctures (2,3) (legs L1, L2).
Site circle c (X1: punctures (1,2); X3: (3,4)) at the cut V|U; c'' = U_*(c) at the closure level; cup-avoiding iff the cyclic
word in the basis {g0, g1, h = g2 g3, g3, g4} has no g3; then c'' lies on S' = dB_H (B_H = nbhd of the H-tree) and the classes:
  S-trivial: c'' -> 1 on S' (h deleted);  H-vertex: c'' ~ (g0 g1)^{+-1} on S';  T-disc: c = 1 in pi_1(B'-T') = F_3/<<psi_V(U^-1(g2 g3))>>."""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fg import red, inv, cyc, subst, free_quotient_solver, in_free_factor, cyc_equal

def sig(j, s):
    a, b = j + 1, j + 2
    if s > 0: return {a: (a, b, -a), b: (a,)}
    return {a: (b,), b: (-b, a, b)}

def L_sig(L):
    i = int(L[1:]); s = 1 if L[0] == 'x' else -1
    return [(0, s), (0, s)] if i == 0 else [(i, s)]

INVL = {('x%d' % i): ('y%d' % i) for i in range(4)}
INVL.update({('y%d' % i): ('x%d' % i) for i in range(4)})

def push_down(Ls, w):
    for L in Ls:
        for j, s in L_sig(L): w = subst(sig(j, s), w)
    return w

def pull_up(Ls, w):
    for L in reversed(Ls):
        for j, s in L_sig(INVL[L]): w = subst(sig(j, s), w)
    return w

PSI0 = {1: (1,), 2: (2,), 3: (-2,), 4: (3,), 5: (-3,)}
def psi_top(V, w): return subst(PSI0, pull_up(V, w))
CUP = (3, 4)
SITE = {'X1': (2, 3), 'X3': (4, 5)}

_cache = {}
def site_test(V, U, site):
    c = SITE[site]
    c2 = push_down(U, c)
    out = []
    for a in c2:                      # g2 = h g3^-1 ; h -> symbol 9
        if abs(a) == 3: out.extend([9, -4] if a > 0 else [4, -9])
        else: out.append(a)
    hb = cyc(tuple(out))
    if any(abs(a) == 4 for a in hb): return 'not-cup-avoiding'
    sp = cyc(tuple(a for a in hb if abs(a) != 9))
    if not sp: return 'S-trivial'
    if cyc_equal(sp, (1, 2)) or cyc_equal(sp, (-2, -1)): return 'H-vertex'
    r = psi_top(V, pull_up(U, CUP))
    if r not in _cache: _cache[r] = free_quotient_solver(3, [r])
    triv, info = _cache[r]
    if triv is None: return 'r-not-reduced'
    return 'T-disc' if triv(psi_top(V, c)) else 'not-null'

GOOD = ('T-disc', 'S-trivial', 'H-vertex')
COMM = {'X1': {'x1', 'y1', 'x3', 'y3'}, 'X3': {'x0', 'y0', 'x1', 'y1', 'x3', 'y3'}}
def family_test(W, j0, site):
    comm = COMM[site]
    lo = j0
    while lo > 0 and W[lo - 1] in comm: lo -= 1
    hi = j0
    while hi < len(W) and W[hi] in comm: hi += 1
    seen = []
    for i in range(lo, hi + 1):
        r = site_test(W[:i], W[i:], site); seen.append((i, r))
        if r in GOOD: return i, r, seen
    return None, None, seen
