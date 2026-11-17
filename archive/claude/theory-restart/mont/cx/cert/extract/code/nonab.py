"""Search for homomorphisms pi_1(S^3 - K) -> G with NONABELIAN image (would certify K nontrivial).  Presentation from
tietze.presentation (optionally partially simplified by tietze.simplify, an isomorphic presentation).  Meridian generators
are conjugate in pi_1, so all images lie in one conjugacy class C; fix g1 -> c0 in C.  G = A5 (classes of 3-cycles, 5-cycles,
double transpositions) and S5 transpositions / 4-cycles; also SL(2,F_p) traceless-free classes are not needed here.
Every relator is checked on the found assignment; nonabelian = two images that do not commute."""
import sys, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import tietze
def comp(p, q): return tuple(q[p[i]] for i in range(len(p)))        # first p then q
def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def perms(n): return list(itertools.permutations(range(n)))
def sign(p):
    s = 1; seen = [False] * len(p)
    for i in range(len(p)):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = p[j]; L += 1
            if L % 2 == 0: s = -s
    return s
def cycle_type(p):
    seen = [False] * len(p); t = []
    for i in range(len(p)):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = p[j]; L += 1
            t.append(L)
    return tuple(sorted(t))
def classes():
    P5 = perms(5); out = {}
    for p in P5:
        ct = cycle_type(p)
        if ct in ((1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (5,), (1, 4)): out.setdefault(ct, []).append(p)
    return out
def evalw(w, img, e):
    r = e
    for a in w:
        r = comp(r, img[a] if a > 0 else pinv(img[-a]))
    return r
def search(word, simplify_first=True, maxcombos=400000):
    ng, rels = tietze.presentation(word)
    gens = list(range(1, ng + 1))
    if simplify_first:
        gs, rs, log = tietze.simplify(ng, rels)
        gens = sorted(gs); rels = [r for r in rs if r]
    if len(gens) == 1: return None, 'cyclic presentation (abelian)'
    e = tuple(range(5)); C = classes()
    for ct, cl in C.items():
        c0 = cl[0]
        n = len(gens) - 1
        if len(cl) ** n > maxcombos: continue
        for rest in itertools.product(cl, repeat=n):
            img = {gens[0]: c0}
            for g, x in zip(gens[1:], rest): img[g] = x
            if all(evalw(r, img, e) == e for r in rels):
                vals = list(img.values())
                if any(comp(a, b) != comp(b, a) for a in vals for b in vals):
                    return {'class': ct, 'images': {g: img[g] for g in gens}, 'gens': gens, 'rels': rels}, 'NONABELIAN'
    return None, 'no nonabelian rep in A5/S5 classes searched'
if __name__ == '__main__':
    for w in sys.argv[1:]: print(w, search(w)[1])
