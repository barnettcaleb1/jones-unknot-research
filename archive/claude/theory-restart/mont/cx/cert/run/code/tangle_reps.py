"""tangle_reps.py -- an INDEPENDENT invariant of trivial tangles rel boundary, to confirm the kernel test's verdicts:
for a tangle T with psi_T : F_10 = pi_1(boundary plane - 10 points) -> pi_1(half-space - T) = F_5 (free on the 5 arc
meridians), the BOUNDARY REPRESENTATION SET  S_T(G) = { (rho(psi_T(a_0)), ..., rho(psi_T(a_9))) : rho in Hom(F_5, G) }.
If T1 = T2 rel boundary then psi_T2 = alpha o psi_T1 for an isomorphism alpha of the complements' groups compatible with the
boundary, hence S_T1(G) = S_T2(G) for every finite group G.  So S_T1(G) != S_T2(G) CERTIFIES T1 != T2 (no kernel lemma needed).
psi_T is computed as in tangle_kernel.py (loop pushed through the braid, then psi_C)."""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tangle_kernel as TK
def pmul(p, q): return tuple(p[i] for i in q)
def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def sym_elements(n): return [tuple(p) for p in itertools.permutations(range(n))]
def psi_words_bottom(U):
    """psi_T(a_j) for j = 0..9 as words in F_5 (symbols 1..5), T = bottom tangle of U"""
    m = TK.psi_C(TK.BOT_PAIRS); out = []
    for j in range(10):
        w = (j + 1,)
        for L in U: w = TK.act(L, w)
        out.append(TK.psi_apply(m, w))
    return out
def boundary_set(words, els):
    """set of 10-tuples of images, over all assignments of the 5 free generators to elements of G (els)"""
    S = set()
    n = len(els[0]); e = tuple(range(n))
    invs = {x: pinv(x) for x in els}
    for combo in itertools.product(els, repeat=5):
        img = []
        for w in words:
            acc = e
            for s in w:
                x = combo[abs(s) - 1]
                acc = pmul(acc, x if s > 0 else invs[x])
            img.append(acc)
        S.add(tuple(img))
    return S
