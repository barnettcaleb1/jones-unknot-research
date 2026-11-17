"""Adversarial beam search for small D - TSI and for small one-step increments, over many
squared 3|3 twists with pairwise distinct Z-splittings (distinct zeta_8 lines)."""
import sys, os, pickle, heapq
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
depth = int(sys.argv[1]); K = int(sys.argv[2]); Lmax = int(sys.argv[3]); maxD = int(sys.argv[4]) if len(sys.argv) > 4 else 99
curves = pickle.load(open('curves_d4.pkl', 'rb'))
curves = [(g, d, p) for g, d, p in curves if len(g) <= depth and d <= maxD]
curves.sort(key=lambda t: (t[1], len(t[0])))
reps = []
for g, d, p in curves:
    l = zeta8_line(g)
    if any(same_line(l, zeta8_line(h)) for h, _, _ in reps): continue
    reps.append((g, d, p))
print('curves kept (distinct splittings):', len(reps), ' D values:', sorted(set(d for _, d, _ in reps)))
from collections import Counter
print('partitions used:', len(set(p for _, _, p in reps)), Counter(p for _, _, p in reps).most_common(4))
conjs = {i: g for i, (g, d, p) in enumerate(reps)}
G = gen_mats(conjs)
gens = list(G.keys())
def nsyl(word):
    return 1 + sum(1 for a, b in zip(word, word[1:]) if a[0] != b[0])
def tsi(word): return 24 * len(word) - 16 * (nsyl(word) - 1)
beam = [((k, e),) for (k, e) in gens]
mats = {w: G[w[0]] for w in beam}
worst_inc = (10 ** 9, None); worst_slack = (10 ** 9, None)
t0 = time.time()
for L in range(2, Lmax + 1):
    cand = []
    for w in beam:
        X = mats[w]; dX = Dnp(X)
        lk, le = w[-1]
        for (k, e) in gens:
            if k == lk and e == -le: continue
            Y = mul(X, G[(k, e)]); d = Dnp(Y)
            nw = w + ((k, e),)
            inc = d - dX
            if inc < worst_inc[0]: worst_inc = (inc, nw)
            sl = d - tsi(nw)
            if sl < worst_slack[0]: worst_slack = (sl, nw)
            cand.append((sl, d, nw, Y))
    cand.sort(key=lambda t: (t[0], t[1]))
    beam = []; mats = {}
    for sl, d, nw, Y in cand[:K]:
        beam.append(nw); mats[nw] = Y
    print('L=%d cand=%d best slack=%d (D=%d) worst increment so far=%d  t=%.0fs' % (L, len(cand), cand[0][0], cand[0][1], worst_inc[0], time.time() - t0))
print('worst one-step increment:', worst_inc)
print('worst slack D-TSI:', worst_slack)
