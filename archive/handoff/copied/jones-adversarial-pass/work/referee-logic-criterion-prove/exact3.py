import sys, os, time, ast
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
import pickle
curves = pickle.load(open('curves_d4.pkl', 'rb'))
curves = [(g, d, p) for g, d, p in curves if len(g) <= 2]
curves.sort(key=lambda t: (t[1], len(t[0])))
reps = []
for g, d, p in curves:
    l = zeta8_line(g)
    if any(same_line(l, zeta8_line(h)) for h, _, _ in reps): continue
    reps.append((g, d, p))
conjs = {i: g for i, (g, d, p) in enumerate(reps)}
line = open('best25.txt').read()
W = list(ast.literal_eval(line.split(':', 1)[1].strip())[1])
print('word (L=%d):' % len(W), W)
print('curves used:', sorted(set(k for k, _ in W)), [ (k, conjs[k], reps[k][2]) for k in sorted(set(k for k, _ in W))])
def bw(word):
    out = []
    for (k, e) in word:
        w = conj(conjs[k], TC * 2)
        if e < 0: w = inv_word(w)
        out += w * abs(e)
    return out
t0 = time.time()
M = rho_mat(bw(W))
D = max(e for r in M for p in r for e in p) - min(e for r in M for p in r for e in p)
print('braid length', len(bw(W)), ' EXACT D =', D, ' TSI = 8L+16 =', 8 * len(W) + 16, ' time %.0fs' % (time.time() - t0))
# also check: is rho(W) v_c proportional to v_c?  (collision test)
v = mat_vec(M, vc)
def proportional(a, b):
    for i in range(DIM):
        for j in range(i + 1, DIM):
            if ladd(lmul(a[i], b[j]), lmul(a[j], b[i]), -1): return False
    return True
print('rho(W) v_c proportional to v_c?', proportional(vc, v))
