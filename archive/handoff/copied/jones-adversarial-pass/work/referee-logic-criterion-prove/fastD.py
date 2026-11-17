"""Fast (mod p) two-place height D for words in squared 3|3 twists, built on the exact tl6 engine.
D(X) = max A-exponent - min A-exponent over nonzero entries.  Exactness: generators are exact;
products are mod a ~2^26 prime (false zero prob ~1e-7 per coefficient); violations are re-checked exactly."""
import sys, os, cmath, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tl6 import *
import numpy as np

def is_prime(n):
    if n < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0: return n == q
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True
P = 2 ** 26 - 1
while not is_prime(P): P -= 2

vc = [{2: 1, -2: 1}, {0: 1}, {0: 1}, {2: 1, -2: 1}, {4: 1, 0: 1, -4: 1}]
TC = [1, 2] * 3
def inv_word(w): return [-g for g in reversed(w)]
def conj(g, w): return list(g) + list(w) + inv_word(g)
def perm(word):
    p = list(range(6))
    for g in reversed(word):
        i = abs(g) - 1
        p = [(i + 1 if x == i else i if x == i + 1 else x) for x in p]
    return p
def partition(g):
    p = perm(g); S = frozenset(p[i] for i in range(3)); T = frozenset(range(6)) - S
    return min(tuple(sorted(S)), tuple(sorted(T)))

def to_np(M):
    """exact Laurent matrix -> (lo, array[W,5,5]) with exponents lo + 2k (all same parity)."""
    exps = [e for row in M for p in row for e in p]
    lo, hi = min(exps), max(exps)
    assert all((e - lo) % 2 == 0 for e in exps)
    W = (hi - lo) // 2 + 1
    a = np.zeros((W, DIM, DIM), dtype=np.int64)
    for i in range(DIM):
        for j in range(DIM):
            for e, c in M[i][j].items():
                a[(e - lo) // 2, i, j] = c % P
    return lo, a

def mul(X, Y):
    lx, ax = X; ly, ay = Y
    Wx, Wy = ax.shape[0], ay.shape[0]
    z = np.zeros((Wx + Wy - 1, DIM, DIM), dtype=np.int64)
    for b in range(Wy):
        yb = ay[b]
        if not yb.any(): continue
        z[b:b + Wx] = (z[b:b + Wx] + (ax @ yb) % P) % P
    nz = np.nonzero(z.reshape(z.shape[0], -1).any(axis=1))[0]
    s, t = nz[0], nz[-1]
    return (lx + ly + 2 * s, z[s:t + 1])

def Dnp(X):
    return 2 * (X[1].shape[0] - 1)

def gen_mats(conjugators, power=2):
    """dict (name, e) -> np matrix for e in +-1 (power = twist power, 2 = separating twist)."""
    G = {}
    for k, g in conjugators.items():
        w = conj(g, TC * power)
        G[(k, 1)] = to_np(rho_mat(w)); G[(k, -1)] = to_np(rho_mat(inv_word(w)))
    return G

def zeta8_line(g):
    z = cmath.exp(1j * cmath.pi / 4)
    v = rho_vec(g, vc)
    return [sum(c * z ** e for e, c in p.items()) for p in v]
def same_line(u, v, tol=1e-7):
    return all(abs(u[i] * v[j] - u[j] * v[i]) < tol * (1 + abs(u[i]) * abs(v[j])) for i in range(5) for j in range(5))
def Npair(g1, g2):
    """span of N(s,t) = H(v_s, v_t)/(-[3][4])."""
    h = Hform(rho_vec(g1, vc), rho_vec(g2, vc))
    return (max(h) - min(h) - 20) if h else None

def enumerate_words(G, names, Lmax, exps=(1, -1), report=True, keep_worst=3):
    """DFS over reduced syllable words; letters (name, e) with e in exps; consecutive syllables distinct names.
    Returns per-L min of D, and min of D - (24*sum|e| - 16(L-1)) with witnesses."""
    # syllable generators
    S = {}
    for k in names:
        for e in exps:
            M = G[(k, 1 if e > 0 else -1)]
            X = M
            for _ in range(abs(e) - 1): X = mul(X, M)
            S[(k, e)] = X
    best = {}
    stats = {}
    def rec(word, X, sumabs):
        L = len(word)
        d = Dnp(X)
        bound = 24 * sumabs - 16 * (L - 1)
        st = stats.setdefault(L, [10 ** 9, None, 10 ** 9, None, 0])
        if d < st[0]: st[0], st[1] = d, list(word)
        if d - bound < st[2]: st[2], st[3] = d - bound, list(word)
        st[4] += 1
        if L == Lmax: return
        for (k, e), Y in S.items():
            if k == word[-1][0]: continue
            rec(word + [(k, e)], mul(X, Y), sumabs + abs(e))
    t0 = time.time()
    for (k, e), Y in S.items():
        rec([(k, e)], Y, abs(e))
    if report:
        for L in sorted(stats):
            st = stats[L]
            print('  L=%d words=%d minD=%d (8L+16=%d)  min[D-TSI]=%d  argminD=%s  argmin[D-TSI]=%s' % (
                L, st[4], st[0], 8 * L + 16, st[2], st[1], st[3]))
        print('  time %.1fs' % (time.time() - t0))
    return stats

def exact_D(word, conjugators, power=2):
    bw = []
    for (k, e) in word:
        w = conj(conjugators[k], TC * power)
        if e < 0: w = inv_word(w)
        bw += w * abs(e)
    M = rho_mat(bw)
    lo = min(e for row in M for p in row for e in p); hi = max(e for row in M for p in row for e in p)
    return hi - lo

def enumerate_letters(G, names, Lmax, report=True):
    """DFS over freely reduced LETTER words in R_k^{+-1} (repeats allowed), as in the first lemma.
    Tracks min D, min D-(8L+16), and min of D - TSI(syllable form)."""
    stats = {}
    def nsyl(word):
        n = 1
        for a, b in zip(word, word[1:]):
            if a[0] != b[0]: n += 1
        return n
    def rec(word, X):
        L = len(word); d = Dnp(X)
        tsi = 24 * L - 16 * (nsyl(word) - 1)
        st = stats.setdefault(L, [10 ** 9, None, 10 ** 9, None, 0])
        if d < st[0]: st[0], st[1] = d, list(word)
        if d - tsi < st[2]: st[2], st[3] = d - tsi, list(word)
        st[4] += 1
        if L == Lmax: return
        lk, le = word[-1]
        for (k, e), Y in G.items():
            if k not in names: continue
            if k == lk and e == -le: continue
            rec(word + [(k, e)], mul(X, Y))
    t0 = time.time()
    for (k, e), Y in G.items():
        if k in names: rec([(k, e)], Y)
    if report:
        for L in sorted(stats):
            st = stats[L]
            print('  L=%d words=%d minD=%d (8L+16=%d) min[D-TSI]=%d argminD=%s argmin[D-TSI]=%s' % (
                L, st[4], st[0], 8 * L + 16, st[2], st[1], st[3]))
        print('  time %.1fs' % (time.time() - t0))
    return stats
