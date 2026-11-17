import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
conjs = {0: [], 1: [3], 7: [3, 3], 10: [2, -3]}
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
inv = lambda W: [(k, -e) for (k, e) in reversed(W)]
B = [(0, 1), (1, 1), (7, 1), (1, -1), (0, -1), (10, 1)]
W23 = [(0, 1), (1, 1), (7, -1), (1, -1), (0, -1), (10, 1)] + B * 2 + [(0, 1), (1, 1), (7, 1), (1, -1), (0, -1)]
X = inv(W23[:-1]); s = inv([W23[-1]])
print('left form: D(X)=%d, D(R_s^e X)=%d -> loss %d (program form D(X)+24-D(R_s^e X))' % (Dex(X), Dex(s + X), Dex(X) + 24 - Dex(s + X)))
print('D((B^-1)^5) =', Dex(inv(B) * 5), ' vs TSI 256')
