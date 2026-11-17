import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
conjs = {0: [], 1: [3], 7: [3, 3], 10: [2, -3]}
for k, g in conjs.items(): print(k, g, partition(g))
print('distinct zeta8 lines (splittings):', all(not same_line(zeta8_line(conjs[a]), zeta8_line(conjs[b])) for a in conjs for b in conjs if a < b))
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
B = [(0, 1), (1, 1), (7, 1), (1, -1), (0, -1), (10, 1)]
for n in (4, 5):
    t0 = time.time(); d = Dex(B * n)
    print('EXACT D(B^%d) = %d, L=%d, TSI = 8L+16 = %d  (%.0fs)' % (n, d, 6 * n, 48 * n + 16, time.time() - t0))
# D-decreasing step from the beam (L=22 -> L=23)
W23 = [(0, 1), (1, 1), (7, -1), (1, -1), (0, -1), (10, 1)] + B * 2 + [(0, 1), (1, 1), (7, 1), (1, -1), (0, -1)]
print('EXACT D(W22) =', Dex(W23[:-1]), ' D(W23) =', Dex(W23))
# pair data for gamma = (T_c^2 T_x^2)(c') and z
g = TC * 2 + conj([3], TC * 2)   # braid of T_c^2 T_x^2 (rightmost applied first)
gam = g + [3, 3]
print('span N(gamma, z) =', Npair(gam, [2, -3]), '  span N(c\', z) =', Npair([3, 3], [2, -3]))
