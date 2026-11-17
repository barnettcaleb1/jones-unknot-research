# Copied helper functions (same conventions as phi0_check.py), no top-level checks.
from fractions import Fraction
from functools import reduce
def inv(w): return [-a for a in reversed(w)]
def comm(x, y): return x + y + inv(x) + inv(y)
def red(w):
    s = []
    for a in w: s.pop() if s and s[-1] == -a else s.append(a)
    return s
def artin(w, n, start=None):
    img = {j: [j] for j in range(1, n + 1)} if start is None else {j: list(v) for j, v in start.items()}
    for a in w:
        i = abs(a)
        sub = {i: [i, i + 1, -i], i + 1: [i]} if a > 0 else {i: [i + 1], i + 1: [-i - 1, i, i + 1]}
        for j in img:
            out = []
            for c in img[j]:
                s = sub.get(abs(c), [abs(c)])
                out += s if c > 0 else inv(s)
            img[j] = red(out)
    return img
def trivial(w, n): return all(v == [j] for j, v in artin(w, n).items())
def commute(u, v, n): return artin(u + v, n) == artin(v + u, n)
def pure(w, n):
    p = list(range(n))
    for a in w: k = abs(a); p[k - 1], p[k] = p[k], p[k - 1]
    return p == list(range(n))
def delete(w, n, d):
    p, out = list(range(1, n + 1)), []
    for a in w:
        k = abs(a)
        if d not in (p[k - 1], p[k]):
            kk = k - 1 if p.index(d) < k - 1 else k
            out.append(kk if a > 0 else -kk)
        p[k - 1], p[k] = p[k], p[k - 1]
    return out
def padd(a, b):
    r = dict(a)
    for e, c in b.items(): r[e] = r.get(e, 0) + c
    return {e: c for e, c in r.items() if c}
def pmul(a, b):
    r = {}
    for e, c in a.items():
        for f, d in b.items(): r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}
def ident(m): return [[{0: 1} if i == j else {} for j in range(m)] for i in range(m)]
def mmul(A, B):
    m = len(A)
    return [[reduce(padd, (pmul(A[i][k], B[k][j]) for k in range(m)), {}) for j in range(m)] for i in range(m)]
def gen(n, a):
    i = abs(a); M = ident(n)
    blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]] if a > 0 else [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2): M[i - 1 + r][i - 1 + c] = blk[r][c]
    return M
def burau(w, n): return reduce(mmul, (gen(n, a) for a in w), ident(n))
def mult(p):
    c, k = [p.get(e, 0) for e in range(min(p), max(p) + 1)], 0
    while sum(x * (-1) ** i for i, x in enumerate(c)) == 0:
        q, acc = [], 0
        for x in reversed(c): acc = x - acc; q.append(acc)
        c, k = q[:-1][::-1], k + 1
    return k
def depth(M):
    D = [[padd(p, {0: -1} if i == j else {}) for j, p in enumerate(row)] for i, row in enumerate(M)]
    return min((mult(p) for row in D for p in row if p), default=float('inf'))
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
X = [1, 2] * 6
b = comm(comm(A14, A24), A34)
Phi0 = comm(X, b)
