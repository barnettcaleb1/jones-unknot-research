# Smallest case of the foreign-line hunt, mod p at random A (p = 2^61-1).
# Length-2 words g = T_V^a T_W^b, c_V = u(c0), c_W = k(c_V).
# Claim 1 (general): e1 rho(g) v0 lies in span(e1 v_V, e1 v_W) with nonzero e1 v_W-coefficient -> needs [e1 v_V] = [e1 v_W].
# Claim 2 (N-family, k in ker(B_4 -> B_3) on strands 3..6): e1 v_W = e1 v_V exactly, so (S1,S2) is proportional
#          to e1 v_V and vanishing is ONE scalar identity.  We test that identity.
import random, itertools
p = (1 << 61) - 1
inv = lambda x: pow(x % p, p - 2, p)

def ncm(q):
    if not q: return [()]
    a = q[0]; out = []
    for k in range(1, len(q), 2):
        for x in ncm(q[1:k]):
            for y in ncm(q[k+1:]): out.append(((a, q[k]),) + x + y)
    return out
B = [tuple(sorted(m)) for m in ncm(list(range(6)))]
B.sort(key=lambda m: [x for pr in m for x in pr]); IDX = {m: i for i, m in enumerate(B)}
def partner(m):
    P = {}
    for a, b in m: P[a] = b; P[b] = a
    return P
def Epat(i):  # list of (row, col, is_delta)
    out = []
    for j, m in enumerate(B):
        P = partner(m)
        if P[i] == i + 1: out.append((j, j, 1))
        else:
            a, b = P[i], P[i+1]
            n = [q for q in m if i not in q and i+1 not in q] + [(i, i+1), tuple(sorted((a, b)))]
            out.append((IDX[tuple(sorted(n))], j, 0))
    return out
EP = [Epat(i) for i in range(5)]

def mm(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(5)) % p for j in range(5)] for i in range(5)]
def mv(X, v): return [sum(X[i][k] * v[k] for k in range(5)) % p for i in range(5)]
def eye(): return [[int(i == j) for j in range(5)] for i in range(5)]

class Rep:
    def __init__(s, Aval):
        s.A = Aval; Ai = inv(Aval); s.d = (-Aval * Aval - Ai * Ai) % p
        s.E = []
        for pat in EP:
            M = [[0] * 5 for _ in range(5)]
            for r, c, isd in pat: M[r][c] = (M[r][c] + (s.d if isd else 1)) % p
            s.E.append(M)
        s.S = [[[((Aval if i == j else 0) + Ai * s.E[t][i][j]) % p for j in range(5)] for i in range(5)] for t in range(5)]
        s.Si = [[[((Ai if i == j else 0) + Aval * s.E[t][i][j]) % p for j in range(5)] for i in range(5)] for t in range(5)]
        q2 = lambda n: (pow(Aval, 2*n, p) - pow(Ai, 2*n, p)) * inv(Aval*Aval - Ai*Ai) % p
        s.v0 = [q2(2), 1, 1, q2(2), q2(3)]
        s.T0 = s.word([1, 2] * 3)
    def word(s, w):
        M = eye()
        for x in w: M = mm(M, s.S[x-1] if x > 0 else s.Si[-x-1])
        return M
    def winv(s, w): return s.word([-x for x in reversed(w)])

def mpow(M, k, Minv):
    R = eye(); base = M if k > 0 else Minv
    for _ in range(abs(k)): R = mm(R, base)
    return R

random.seed(7)
R1, R2 = Rep(random.randrange(2, p)), Rep(random.randrange(2, p))
# sanity: e1 v0 = 0, T0 v0 = A^6 v0
assert mv(R1.E[0], R1.v0) == [0]*5
assert mv(R1.T0, R1.v0) == [pow(R1.A, 6, p) * x % p for x in R1.v0]

gens = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
def rand_word(L):
    w = []
    while len(w) < L:
        x = random.choice(gens)
        if w and w[-1] == -x: continue
        w.append(x)
    return w
aN, bN = [3, -5], [4, 3, -5, -4]                     # free generators of ker(B_4 -> B_3), strands 3..6
Nwords = [aN, bN, [-x for x in reversed(aN)], aN + aN, aN + bN, bN + [-x for x in reversed(aN)], [2] + aN + [-2]][:6]

def powers(R, M, Mi, rng):
    out = {0: eye()}
    P = eye()
    for e in range(1, max(rng) + 1): P = mm(P, M); out[e] = P
    P = eye()
    for e in range(1, -min(rng) + 1): P = mm(P, Mi); out[-e] = P
    return out

EXPS = [-4, -3, -2, -1, 1, 2, 3, 4]
def run_uk(R, u, k):
    U, Ui = R.word(u), R.winv(u)
    Tu = mm(mm(U, R.T0), Ui); Tui = mm(mm(U, R.word([-2, -1] * 3)), Ui)
    Pw = powers(R, Tu, Tui, EXPS)
    Kw, Kwi = R.word(k), R.winv(k)
    y = mv(Kwi, R.v0)
    res = {}
    for b in EXPS:
        xb = mv(Kw, mv(Pw[b], y))
        for a in EXPS:
            res[(a, b)] = mv(R.E[0], mv(Pw[a], xb))
    eV = mv(R.E[0], mv(U, R.v0))
    return res, eV

def proj_eq(x, y):
    # projective equality of vectors mod p
    i = next((j for j in range(5) if x[j]), None)
    if i is None or y[i] == 0: return x == y
    r = y[i] * inv(x[i]) % p
    return all((r * x[j] - y[j]) % p == 0 for j in range(5))

stats = dict(pairs=0, skipped_same_curve=0, tried=0, eV_zero=0, vanish=0, prop_fail=0)
cands = []
seen_u = set()
for L in range(2, 10):
    for _ in range(40):
        u = rand_word(L)
        vV = mv(R1.word(u), R1.v0)
        eV = mv(R1.E[0], vV)
        if eV == [0]*5: stats['eV_zero'] += 1; continue
        for k in Nwords:
            vW = mv(R1.word(k), vV)
            stats['pairs'] += 1
            if proj_eq(vV, vW): stats['skipped_same_curve'] += 1; continue
            res, eV = run_uk(R1, u, k)
            for (a, b), w in res.items():
                stats['tried'] += 1
                if (w[0] * eV[1] - w[1] * eV[0]) % p: stats['prop_fail'] += 1
                if w == [0]*5:
                    res2, _ = run_uk(R2, u, k)
                    if res2[(a, b)] == [0]*5: stats['vanish'] += 1; cands.append((u, k, a, b))
print(stats)
print('candidates (vanish at two random A):', cands[:10])

# Generic pairs of DISTINCT curves (distinct lines [v]): how often is [e1 v_V] = [e1 v_W]?
curves = []
for _ in range(4000):
    u = rand_word(random.randint(1, 8))
    v = mv(R1.word(u), R1.v0); e = mv(R1.E[0], v)
    if e == [0]*5: continue
    if any(proj_eq(v, c[1]) for c in curves): continue
    curves.append((u, v, e))
    if len(curves) >= 250: break
tot = coinc = 0
for i in range(len(curves)):
    for j in range(i+1, len(curves)):
        tot += 1
        e1, e2 = curves[i][2], curves[j][2]
        if (e1[0]*e2[1] - e1[1]*e2[0]) % p == 0: coinc += 1
print('distinct non-native curves:', len(curves), ' pairs:', tot, ' with [e1 v_V]=[e1 v_W]:', coinc)
