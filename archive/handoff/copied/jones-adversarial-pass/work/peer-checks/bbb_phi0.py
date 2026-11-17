# Independent check of the structure chat's BBB example:
# Phi0 = [(s1 s2)^6, [[y1,y2],y3]] in B_4, y_i = A_{i4} (push of p4 around p_i).
# Claims: unreduced Burau(Phi0) = I at t = -1, != I at generic t (so Phi0 != 1).
# Exact Laurent-polynomial arithmetic (dict exponent -> int), no sympy.
n = 4
def ladd(p, q, s=1):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + s * c
        if r[e] == 0: del r[e]
    return r
def lmul(p, q):
    r = {}
    for a, x in p.items():
        for b, y in q.items():
            r[a + b] = r.get(a + b, 0) + x * y
    return {e: c for e, c in r.items() if c}
ONE, ZERO = {0: 1}, {}
def eye():
    return [[dict(ONE) if i == j else {} for j in range(n)] for i in range(n)]
def mmul(A, B):
    C = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]: continue
            for j in range(n):
                if B[k][j]:
                    C[i][j] = ladd(C[i][j], lmul(A[i][k], B[k][j]))
    return C
def gen(i, s):
    M = eye()
    a = i - 1
    if s > 0:   # [[1-t, t],[1, 0]]
        blk = [[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]]
    else:       # [[0, 1],[t^-1, 1-t^-1]]
        blk = [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]
    for r in range(2):
        for c in range(2):
            M[a + r][a + c] = blk[r][c]
    return M
def burau(word):
    M = eye()
    for g in word:
        M = mmul(M, gen(abs(g), 1 if g > 0 else -1))
    return M
def is_eye(M):
    return all((M[i][j] == (ONE if i == j else {})) for i in range(n) for j in range(n))
def ev(p, x):
    from fractions import Fraction
    return sum(c * Fraction(x) ** e for e, c in p.items())
def at(M, x):
    return [[ev(M[i][j], x) for j in range(n)] for i in range(n)]
def is_eye_num(M):
    return all(M[i][j] == (1 if i == j else 0) for i in range(n) for j in range(n))
inv = lambda w: [-g for g in reversed(w)]
comm = lambda a, b: a + b + inv(a) + inv(b)
y1 = [3, 2, 1, 1, -2, -3]
y2 = [3, 2, 2, -3]
y3 = [3, 3]
X = [1, 2] * 6
W = comm(comm(y1, y2), y3)
Phi0 = comm(X, W)
print("length of Phi0 word:", len(Phi0))
assert burau([1, 2, 1]) == burau([2, 1, 2]) and burau([1, 3]) == burau([3, 1])
assert is_eye(burau([1, -1, 2, 3, -3, -2]))
print("Burau((s1s2)^6) at t=-1 is I:", is_eye_num(at(burau(X), -1)))
print("Burau((s1s2)^6) is I generically:", is_eye(burau(X)))
MP = burau(Phi0)
print("Burau(Phi0) is I as Laurent matrix:", is_eye(MP))
print("Burau(Phi0) at t=-1 is I:", is_eye_num(at(MP, -1)))
print("Burau(Phi0) at t=2 is I:", is_eye_num(at(MP, 2)))
# (t+1)-adic depth: smallest k with (MP - I) divisible by (t+1)^k
def divides_tp1(p):  # p Laurent; test p(-1)==0 and return p/(t+1)
    if not p: return True, {}
    lo, hi = min(p), max(p)
    co = [p.get(e, 0) for e in range(lo, hi + 1)]  # low->high
    # synthetic division by (t+1): root -1, on polynomial t^-lo * p
    q = [0] * (len(co) - 1)
    acc = 0
    for k in range(len(co) - 1, 0, -1):
        acc = co[k] + acc * 0 if False else co[k] - (-1) * 0  # placeholder
    # straightforward: evaluate and divide via repeated subtraction
    val = sum(c * (-1) ** (e) for e, c in p.items())
    if val != 0: return False, None
    # divide polynomial P(t) = sum co[k] t^k by (t+1)
    P = co[:]
    Q = [0] * (len(P) - 1)
    for k in range(len(P) - 1, 0, -1):
        Q[k - 1] = P[k]
        P[k - 1] -= P[k]
    return True, {lo + k: c for k, c in enumerate(Q) if c}
D = [[ladd(MP[i][j], ONE if i == j else {}, -1) for j in range(n)] for i in range(n)]
depth = 0
cur = D
while True:
    ok = True; nxt = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            f, q = divides_tp1(cur[i][j])
            if not f: ok = False; break
            nxt[i][j] = q
        if not ok: break
    if not ok: break
    depth += 1; cur = nxt
print("(t+1)-adic depth of Burau(Phi0) - I:", depth)
