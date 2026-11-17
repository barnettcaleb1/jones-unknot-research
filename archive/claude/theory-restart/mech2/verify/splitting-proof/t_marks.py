# does the total homology H(X_p X_q C, d0+d1) depend on where the marked points sit on their components?
from t_common import *
half = sys.argv[1] if len(sys.argv) > 1 else 'l1.y0.y0.y1.u2'
w = quotient_word(half)
D = closure13(w)
c1, c2 = D.comp[D.marks[0]], D.comp[D.marks[1]]
E1s = collections.Counter(); Hs = collections.Counter()
edges1 = [e for e in range(D.nedges) if D.comp[e] == c1]; edges2 = [e for e in range(D.nedges) if D.comp[e] == c2]
orig = tuple(D.marks)
res = {}
for e1 in edges1:
    for e2 in edges2:
        D.marks = [e1, e2]
        C = Complex(D)
        dE1 = sum(homology_bigraded(C).values()); dH = sum(homology_bigraded(C, True).values())
        res[(e1, e2)] = (dE1, dH)
        E1s[dE1] += 1; Hs[dH] += 1
print('word', w, ' original marks', orig, '->', res[orig])
print('all placements of (p on L1, q on L2): dim E_1 distribution', dict(E1s), '; dim H(X_pX_q C, d) distribution', dict(Hs))
