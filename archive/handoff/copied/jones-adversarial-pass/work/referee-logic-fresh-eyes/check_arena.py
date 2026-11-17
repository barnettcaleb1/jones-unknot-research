#!/usr/bin/env python3
# Referee check (own code, exact rationals): W(6,0) Gram form G(delta)_{mn} = delta^{loops(m,n)}.
# (1) det G = delta^5 (delta^2-1)^4 (delta^2-2) at several rational delta.
# (2) exact inertia (Sylvester, symmetric elimination) at delta in (1, sqrt2) and (sqrt2, 2).
# (3) block of G on the 4 one-crossing matchings for c = boundary of {1,2,3}:
#     compare with delta*(G2 (x) G2) and with (G2 (x) G2)/delta, G2 = [[delta,1],[1,delta]].
from fractions import Fraction as F
import itertools

def ncm(pts):
    if not pts: return [[]]
    a = pts[0]; out = []
    for k in range(1, len(pts), 2):
        for mi in ncm(pts[1:k]):
            for mo in ncm(pts[k+1:]):
                out.append([(a, pts[k])] + mi + mo)
    return out

B = [tuple(sorted(m)) for m in ncm([1, 2, 3, 4, 5, 6])]
def part(m):
    p = {}
    for a, b in m: p[a] = b; p[b] = a
    return p
def loops(m, n):
    p, q = part(m), part(n); seen = set(); L = 0
    for s in range(1, 7):
        if s in seen: continue
        L += 1; x = s; use_p = True
        while True:
            seen.add(x); y = p[x] if use_p else q[x]; seen.add(y); x = y; use_p = not use_p
            if x == s and use_p: break
    return L
LO = [[loops(m, n) for n in B] for m in B]

def gram(d): return [[F(d) ** LO[i][j] for j in range(5)] for i in range(5)]
def det_and_pivots(M):
    M = [row[:] for row in M]; n = len(M); piv = []; det = F(1)
    for k in range(n):
        if M[k][k] == 0: return None, None
        piv.append(M[k][k]); det *= M[k][k]
        for i in range(k + 1, n):
            f = M[i][k] / M[k][k]
            for j in range(k, n): M[i][j] -= f * M[k][j]
    return det, piv

print('basis:', B)
for d in [F(3, 2), F(5, 4), F(7, 5), F(2), F(1, 2), F(6, 5), F(13, 10)]:
    det, piv = det_and_pivots(gram(d))
    formula = d**5 * (d*d - 1)**4 * (d*d - 2)
    sig = None if piv is None else (sum(p > 0 for p in piv), sum(p < 0 for p in piv))
    print(f'delta={str(d):6s} det==formula: {det == formula}  inertia(+,-)={sig}')

# (3) block on one-crossing matchings for c = d{1,2,3}
one = [((1, 2), (3, 4), (5, 6)), ((1, 2), (3, 6), (4, 5)), ((1, 4), (2, 3), (5, 6)), ((1, 6), (2, 3), (4, 5))]
I = [B.index(tuple(sorted(m))) for m in one]
ten = [(0, 0), (0, 1), (1, 0), (1, 1)]   # (inside factor, outside factor)
for d in [F(6, 5), F(3, 2)]:
    G = gram(d); G2 = [[d, F(1)], [F(1), d]]
    blk = [[G[I[a]][I[b]] for b in range(4)] for a in range(4)]
    tens = [[G2[ten[a][0]][ten[b][0]] * G2[ten[a][1]][ten[b][1]] for b in range(4)] for a in range(4)]
    print(f'delta={d}: block == delta*(G2xG2): {blk == [[d*x for x in r] for r in tens]};  '
          f'block == (G2xG2)/delta: {blk == [[x/d for x in r] for r in tens]}')
