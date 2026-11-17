import sys, os, pickle, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
curves = pickle.load(open('curves_d4.pkl', 'rb'))
curves = [(g, d, p) for g, d, p in curves if len(g) <= 2]
curves.sort(key=lambda t: (t[1], len(t[0])))
reps = []
for g, d, p in curves:
    l = zeta8_line(g)
    if any(same_line(l, zeta8_line(h)) for h, _, _ in reps): continue
    reps.append((g, d, p))
conjs = {i: g for i, (g, d, p) in enumerate(reps)}
for i, (g, d, p) in enumerate(reps): print(i, 'conj', g, 'partition', p, 'D(R)=', d)
def bw(word):
    out = []
    for (k, e) in word:
        w = conj(conjs[k], TC * 2)
        if e < 0: w = inv_word(w)
        out += w * abs(e)
    return out
def Dex(word):
    M = rho_mat(bw(word))
    return max(e for r in M for p in r for e in p) - min(e for r in M for p in r for e in p)
W14 = [(8, -1), (0, -1), (2, -1), (12, -1), (2, 1), (0, 1), (8, 1), (0, -1), (2, -1), (12, 1), (2, 1), (0, 1), (8, 1), (0, -1)]
W11 = [(0, 1), (1, 1), (7, -1), (1, -1), (0, -1), (10, 1), (0, 1), (1, 1), (7, 1), (1, -1), (0, -1)]
for W in (W11, W14):
    t0 = time.time()
    used = sorted(set(k for k, _ in W))
    print('word uses curves', used, 'partitions', [reps[k][2] for k in used])
    for a in used:
        for b in used:
            if a < b: print('   span N(%d,%d)=%s' % (a, b, Npair(conjs[a], conjs[b])))
    print('  exact D =', Dex(W), ' 8L+16 = TSI =', 8 * len(W) + 16, '  (%.0fs)' % (time.time() - t0))
