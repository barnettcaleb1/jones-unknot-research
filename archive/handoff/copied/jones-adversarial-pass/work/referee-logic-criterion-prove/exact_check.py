import sys, os, pickle
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
for i in (0, 1, 7): print('curve', i, 'conjugator', reps[i][0], 'partition', reps[i][2], 'D(R)=', reps[i][1])
for a, b in ((0, 1), (0, 7), (1, 7)): print('span N(%d,%d) =' % (a, b), Npair(conjs[a], conjs[b]))
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
X = [(1, 1), (7, 1), (1, -1)]
print('exact D(X) =', Dex(X), ' D(X R_0^-1) =', Dex(X + [(0, -1)]), ' D(R_0^-1 X) =', Dex([(0, -1)] + X))
Xi = [(k, -e) for (k, e) in reversed(X)]
print('inverse word: D(X^-1) =', Dex(Xi), ' D(R_0 X^-1) =', Dex([(0, 1)] + Xi))
for w in ([(1, 1), (7, 1)], [(7, 1), (1, -1)], [(1, 1), (7, 1), (1, -1), (0, -1)], [(7, 1), (1, -1), (0, -1)], [(1, -1), (0, -1)]):
    print('  D', w, '=', Dex(w), '  TSI bound =', 24 * len(w) - 16 * (len(w) - 1))
