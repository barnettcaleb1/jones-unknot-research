"""Beam search, syllable words with exponents in EXPS and consecutive letters distinct curves.
Score = D - TSI (TSI = 24 sum|e| - 16 (L-1)). Also reports worst one-step loss vs D(prefix)."""
import sys, os, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
depth = int(sys.argv[1]); K = int(sys.argv[2]); Lmax = int(sys.argv[3]); EXPS = tuple(int(x) for x in sys.argv[4].split(','))
side = sys.argv[5] if len(sys.argv) > 5 else 'right'
curves = pickle.load(open('curves_d4.pkl', 'rb'))
curves = [(g, d, p) for g, d, p in curves if len(g) <= depth]
curves.sort(key=lambda t: (t[1], len(t[0])))
reps = []
for g, d, p in curves:
    l = zeta8_line(g)
    if any(same_line(l, zeta8_line(h)) for h, _, _ in reps): continue
    reps.append((g, d, p))
print('curves (distinct splittings):', len(reps))
conjs = {i: g for i, (g, d, p) in enumerate(reps)}
G = gen_mats(conjs)
S = {}
for k in conjs:
    for e in EXPS:
        M = G[(k, 1 if e > 0 else -1)]; X = M
        for _ in range(abs(e) - 1): X = mul(X, M)
        S[(k, e)] = X
def tsi(word): return 24 * sum(abs(e) for _, e in word) - 16 * (len(word) - 1)
beam = [((k, e),) for (k, e) in S]
mats = {w: S[w[0]] for w in beam}
worst_loss = (-1, None); best = (10 ** 9, None)
t0 = time.time()
for L in range(2, Lmax + 1):
    cand = []
    for w in beam:
        X = mats[w]; dX = Dnp(X)
        for (k, e), Y in S.items():
            if side == 'right':
                if k == w[-1][0]: continue
                Z = mul(X, Y); nw = w + ((k, e),)
            else:
                if k == w[0][0]: continue
                Z = mul(Y, X); nw = ((k, e),) + w
            d = Dnp(Z); loss = dX + 24 * abs(e) - d
            if loss > worst_loss[0]: worst_loss = (loss, nw)
            sl = d - tsi(nw)
            if sl < best[0]: best = (sl, nw)
            cand.append((sl, d, nw, Z))
    cand.sort(key=lambda t: (t[0], t[1]))
    seen = set(); beam = []; mats = {}
    for sl, d, nw, Z in cand:
        if nw in seen: continue
        seen.add(nw); beam.append(nw); mats[nw] = Z
        if len(beam) >= K: break
    print('L=%d  best slack=%d (D=%d, TSI=%d) word=%s | worst loss so far=%d  t=%.0fs' % (
        L, cand[0][0], cand[0][1], tsi(cand[0][2]), cand[0][2], worst_loss[0], time.time() - t0))
print('worst loss:', worst_loss)
print('best slack overall:', best)
