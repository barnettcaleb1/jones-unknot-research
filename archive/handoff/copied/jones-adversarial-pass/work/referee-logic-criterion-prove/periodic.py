import sys, os, pickle, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
conjs = {0: [], 2: [-3], 8: [-2, 3], 12: [-3, -3], 1: [3], 7: [3, 3], 10: [2, -3]}
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
def tsi(word):
    # syllable form
    syl = 1 + sum(1 for a, b in zip(word, word[1:]) if a[0] != b[0])
    return 24 * len(word) - 16 * (syl - 1)
for W in ([(0, -1), (2, -1), (12, -1), (2, 1), (0, 1)],
          [(0, -1), (2, -1), (12, 1), (2, 1), (0, 1)],
          [(1, 1), (7, -1), (1, -1)], [(0, 1), (1, 1), (7, -1), (1, -1), (0, -1)]):
    print('conjugate-type word', W, ' L=%d  exact D=%d  TSI=%d' % (len(W), Dex(W), tsi(W)))
u = [(0, -1), (2, -1), (12, -1), (2, 1), (0, 1), (8, 1)]
G = gen_mats(conjs)
X = None
for n in range(1, 9):
    for (k, e) in u:
        Y = G[(k, e)]
        X = Y if X is None else mul(X, Y)
    print('u^%d: L=%d  D=%d  TSI=8L+16=%d  slack=%d' % (n, 6 * n, Dnp(X), 8 * 6 * n + 16, Dnp(X) - 8 * 6 * n - 16))
print('exact D(u^3) =', Dex(u * 3))
