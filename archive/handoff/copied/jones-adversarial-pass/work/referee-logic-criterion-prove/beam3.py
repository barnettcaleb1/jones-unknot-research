"""Adversarial beam on the first-lemma triple {c, x, y} (and on the round triple), +-1 syllables."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
systems = {'cxy': {'c': [], 'x': [3], 'y': [4, 3, 2, 3]},
           'c,x,c2,z': {'c': [], 'x': [3], 'C': [3, 3], 'z': [2, -3]}}
K = int(sys.argv[1]); Lmax = int(sys.argv[2])
for name, conjs in systems.items():
    G = gen_mats(conjs)
    beam = [((k, e),) for (k, e) in G]; mats = {w: G[w[0]] for w in beam}
    hist = []
    for L in range(2, Lmax + 1):
        cand = []
        for w in beam:
            X = mats[w]
            for (k, e), Y in G.items():
                if k == w[-1][0]: continue
                Z = mul(X, Y); nw = w + ((k, e),)
                cand.append((Dnp(Z) - 8 * L - 16, nw, Z))
        cand.sort(key=lambda t: t[0])
        beam = [c[1] for c in cand[:K]]; mats = {c[1]: c[2] for c in cand[:K]}
        hist.append(cand[0][0])
    print(name, ': min over beam of D-(8L+16) for L=2..%d:' % Lmax, hist)
