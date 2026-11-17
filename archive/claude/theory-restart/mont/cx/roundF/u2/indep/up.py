"""u2/indep/up.py -- UPSTAIRS (full symmetric picture) global-disc test, written from scratch for U2.
Full picture of K (cert/run convention, = alex.symmetrize): positions 0..9 = L4..L0 R0..R4; caps (0,9),(1,2),(3,4),(5,6),(7,8);
braid W with x0 -> s4, x_i -> s_(4-i) s_(4+i) (i=1..3), y = inverse; cups (0,1),(2,3),(4,5),(6,7),(8,9).
Positions 0, 9 never cross anything, so the OUTER ARC  cup(0,1) + strand 0 + cap(0,9) + strand 9 + cup(8,9)  is isotopic (sweep across
the outer face of the projection sphere) to a big cup (1,8) below everything.  Let B_H = regular nbhd of (big cup u centre cup (4,5) u
a planar arc joining them below the cups (2,3),(6,7)): a ball meeting K in two trivial arcs; B' = S^3 - B_H is a ball and
T' = K n B' = caps (1,2),(3,4),(5,6),(7,8) + braid + cups (2,3),(6,7).  Van Kampen (top half-space: F_4 on the cap meridians;
shell between the bottom level and dB_H: F_8/<<a2a3, a6a7>>, the planar tree adds nothing):
      pi_1(B' - T') = F_4 / << psi_V(U^-1(a2 a3)), psi_V(U^-1(a6 a7)) >>,   psi_V = psi_0 o (pull up through V).
A twist site (X3 = x3x3 -> circles C around (1,2) and C' around (7,8); X1 = x1x1 -> (3,4) and (5,6)) at the cut V|U: push the
circle down through U to the bottom level: C'' = U_*(C) (a simple closed curve, class = Artin image).  CUP-AVOIDING iff its
cyclic word in the basis {a1, a2a3, a3, a4, a5, a6a7, a7, a8} uses neither a3 nor a7 (free factor = pi_1 of the level plane
minus the two cup shadows; geometric intersection argument); then C'' is isotopic (in S^3 - K, disjoint from the other site
circles) onto dB' - K.  If moreover C (= C'' in pi_1) is trivial in pi_1(B' - T') then by DEHN'S LEMMA C'' bounds an embedded
disc in B' - N(T') whose interior misses dB' (hence misses K and every other site circle on dB').  Twisting along circles that
bound such discs is trivial: every member of the twist family is isotopic to the base knot (surgery induction, see REPORT).
Word problem: Whitehead reduction of the relator pair (fg.free_quotient_solver); only a reduction to single letters is accepted.
Conventions (Artin push-down, pull-up, adjacent caps/cups only) are those VALIDATED by cert/run (tangle_kernel) and are
re-validated here independently (validate_up.py)."""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fg import red, inv, cyc, subst, free_quotient_solver, in_free_factor

def sym(p): return p + 1          # position p -> generator symbol

def sigma(j, s):
    """push-down automorphism of the crossing of positions j, j+1 (sign s)"""
    a, b = sym(j), sym(j + 1)
    if s > 0: return {a: (a, b, -a), b: (a,)}
    return {a: (b,), b: (-b, a, b)}

def letter_sigmas(L):
    i = int(L[1:]); s = 1 if L[0] == 'x' else -1
    return [(4, s)] if i == 0 else [(4 - i, s), (4 + i, s)]

INVL = {('x%d' % i): ('y%d' % i) for i in range(4)}
INVL.update({('y%d' % i): ('x%d' % i) for i in range(4)})

def push_down(word_letters, w):
    for L in word_letters:
        for j, s in letter_sigmas(L): w = subst(sigma(j, s), w)
    return w

def pull_up(word_letters, w):
    for L in reversed(word_letters):
        for j, s in letter_sigmas(INVL[L]): w = subst(sigma(j, s), w)
    return w

PSI0 = {sym(1): (1,), sym(2): (-1,), sym(3): (2,), sym(4): (-2,), sym(5): (3,), sym(6): (-3,), sym(7): (4,), sym(8): (-4,)}

def psi_top(V, w):
    """class in pi_1(upper half-space - (caps + V)) = F_4 of a loop w at the level just below V"""
    x = pull_up(V, w)
    for a in x:
        if abs(a) not in PSI0: raise ValueError('loop involves position 0/9')
    return subst(PSI0, x)

CUP23 = (sym(2), sym(3)); CUP67 = (sym(6), sym(7))
SITE = {'X3': [(sym(1), sym(2)), (sym(7), sym(8))], 'X1': [(sym(3), sym(4)), (sym(5), sym(6))]}

def cup_avoiding(c2):
    """c2 at the bottom level; rewrite a2 = h23 a3^-1, a6 = h67 a7^-1 (h23 -> symbol 91, h67 -> 92)"""
    out = []
    for a in c2:
        g = abs(a)
        if g == sym(2): out.extend([91, -sym(3)] if a > 0 else [sym(3), -91])
        elif g == sym(6): out.extend([92, -sym(7)] if a > 0 else [sym(7), -92])
        else: out.append(a)
    return in_free_factor(tuple(out), {sym(1), 91, sym(4), sym(5), 92, sym(8)})

_solver_cache = {}
def site_test(V, U, site):
    """returns (verdict, detail) for the site circles at cut V|U; verdict True iff BOTH circles pass (cup-avoiding + trivial)"""
    r1 = psi_top(V, pull_up(U, CUP23)); r2 = psi_top(V, pull_up(U, CUP67))
    key = (r1, r2)
    if key not in _solver_cache: _solver_cache[key] = free_quotient_solver(4, [r1, r2])
    triv, info = _solver_cache[key]
    det = []
    ok = True
    for c in SITE[site]:
        c2 = push_down(U, c)
        if not cup_avoiding(c2): det.append('not-cup-avoiding'); ok = False; continue
        if triv is None: det.append('relators-not-reduced'); ok = False; continue
        if not triv(psi_top(V, c)): det.append('not-null'); ok = False; continue
        det.append('disc')
    return ok, det

def family_test(W, j0, site, comm):
    """try every cut reachable from j0 by sliding the site through letters in comm; returns (cut, detail) or (None, details)"""
    lo = j0
    while lo > 0 and W[lo - 1] in comm: lo -= 1
    hi = j0
    while hi < len(W) and W[hi] in comm: hi += 1
    seen = []
    for i in range(lo, hi + 1):
        ok, det = site_test(W[:i], W[i:], site)
        seen.append((i, det))
        if ok: return i, seen
    return None, seen

COMM = {'X1': {'x1', 'y1', 'x3', 'y3'}, 'X3': {'x0', 'y0', 'x1', 'y1', 'x3', 'y3'}}
