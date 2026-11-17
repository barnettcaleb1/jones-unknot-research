"""F-C core (round G, 17 Nov 2026).  Exact algebra only (Python ints).
Dense Laurent polys: (lo, [c_lo, ..., c_hi]) with nonzero end coefficients; zero poly = (0, []).
Body state in channel coords (a, b) (vc convention); integral state (a, c), b = a + (1-t^3) c;
eigenpair A = a + C c, B = C c, C = (1-t)(1+t^2).  Horizontal closure at twist m: f_m = A - (-t)^-m B  (= a-channel of F_m(body)).
Ideal test: is (a, c) = Lambda = Z[t,1/t]?  Algorithm (justified in REPORT 2.1):
  R = Res(a0, c0) over Z (a0, c0 = a, c shifted to nonzero constant term).  R = 0 -> common factor (proper).  |R| = 1 -> unit ideal.
  Else for every prime p | R decide whether gcd(a0 mod p, c0 mod p) in F_p[t] is a power of t; done without factoring R by a
  Euclid over Z/qZ that splits q whenever a non-invertible leading/constant coefficient appears.  Unit ideal iff all are powers of t.
"""
import sys, math, hashlib
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')

ZERO = (0, [])
def trim(lo, c):
    i = 0; n = len(c)
    while i < n and c[i] == 0: i += 1
    if i == n: return ZERO
    j = n - 1
    while c[j] == 0: j -= 1
    return (lo + i, c[i:j + 1])
def D(d):
    if not d: return ZERO
    lo = min(d); hi = max(d); c = [0] * (hi - lo + 1)
    for e, v in d.items(): c[e - lo] = v
    return trim(lo, c)
def todict(p):
    lo, c = p
    return {lo + i: v for i, v in enumerate(c) if v}
def mul(p, q):
    (l1, a), (l2, b) = p, q
    if not a or not b: return ZERO
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return trim(l1 + l2, r)
def lin(p, q, s=1):
    """p + s*q"""
    (l1, a), (l2, b) = p, q
    if not a: return (l2, [s * y for y in b]) if b else ZERO
    if not b: return p
    lo = min(l1, l2); hi = max(l1 + len(a), l2 + len(b))
    r = [0] * (hi - lo)
    for i, x in enumerate(a): r[l1 - lo + i] += x
    for j, y in enumerate(b): r[l2 - lo + j] += s * y
    return trim(lo, r)
def add(p, q): return lin(p, q, 1)
def sub(p, q): return lin(p, q, -1)
def shift(p, k): return (p[0] + k, p[1]) if p[1] else ZERO
def tmono_mul(m, p):
    """(-t)^m * p"""
    if not p[1]: return ZERO
    s = -1 if m % 2 else 1
    return (p[0] + m, [s * x for x in p[1]] if s < 0 else p[1])
def bot(p): return p[0]
def top(p): return p[0] + len(p[1]) - 1
def span(p): return len(p[1]) - 1
def isunit(p): return len(p[1]) == 1 and abs(p[1][0]) == 1
def ev1(p): return sum(p[1])
def evm1(p):
    lo, c = p
    s = sum(x if i % 2 == 0 else -x for i, x in enumerate(c))
    return s if lo % 2 == 0 else -s

CPOLY = (0, [1, -1, 1, -1])
def div_1mt3(g):
    """exact g / (1 - t^3), or None"""
    lo, gc = g
    if not gc: return ZERO
    n = len(gc)
    if n < 4: return None
    c = [0] * (n - 3)
    for k in range(n - 3):
        c[k] = gc[k] + (c[k - 3] if k >= 3 else 0)
    for k in range(n - 3, n):
        if gc[k] != -(c[k - 3] if 0 <= k - 3 < n - 3 else 0): return None
    return trim(lo, c)
def state_from_channel(a, b):
    c = div_1mt3(sub(b, a))
    assert c is not None, 'not a lattice vector'
    return a, c
def eigen(a, c):
    B = mul(CPOLY, c)
    return add(a, B), B
def chan_from_vc(v):
    return D(v[0]), D(v[1])

def okey(A, B):
    """F-orbit key: common unit removed (A shifted to bot 0, sign by A(1) > 0), twist unit (-t)^k on B removed."""
    s = 1 if ev1(A) > 0 else -1
    Ac = A[1] if s > 0 else [-x for x in A[1]]
    if not B[1]: Bc = []
    else:
        k = B[0] - A[0]
        sg = s * (-1 if k % 2 else 1)
        Bc = B[1] if sg > 0 else [-x for x in B[1]]
    h = hashlib.blake2b(repr((Ac, Bc)).encode(), digest_size=12).digest()
    return h

# ---------------- resultant over Z (modular, Hadamard bound, CRT)
def _primes():
    import sympy
    out = []; p = 2**61
    while len(out) < 400:
        p = sympy.prevprime(p); out.append(p)
    return out
PRIMES = None
def res_mod(f, g, p):
    """Res(f, g) mod p; f, g coefficient lists low->high with lc nonzero mod p (caller ensures)."""
    f = [x % p for x in f]; g = [x % p for x in g]
    res = 1
    while True:
        df = len(f) - 1; dg = len(g) - 1
        if dg == 0:
            return res * pow(g[0], df, p) % p
        r = f[:]
        inv = pow(g[-1], p - 2, p)
        for i in range(df - dg, -1, -1):
            co = r[i + dg] * inv % p
            if co:
                for j in range(dg + 1):
                    r[i + j] = (r[i + j] - co * g[j]) % p
        r = r[:dg]
        while r and r[-1] == 0: r.pop()
        if not r: return 0
        dr = len(r) - 1
        if (df * dg) & 1: res = -res
        res = res * pow(g[-1], df - dr, p) % p
        f, g = g, r
def resultant(f, g):
    global PRIMES
    if PRIMES is None: PRIMES = _primes()
    df = len(f) - 1; dg = len(g) - 1
    if df == 0 and dg == 0: return 1
    nf = math.sqrt(sum(x * x for x in f)); ng = math.sqrt(sum(x * x for x in g))
    bits = dg * math.log2(nf) + df * math.log2(ng) + 3
    mods = []; res = []; M = 1
    for p in PRIMES:
        if f[-1] % p == 0 or g[-1] % p == 0: continue
        mods.append(p); res.append(res_mod(f, g, p)); M *= p
        if math.log2(M) > bits: break
    else:
        raise RuntimeError('ran out of primes')
    # CRT
    x = 0
    for p, r in zip(mods, res):
        Mi = M // p
        x = (x + r * Mi * pow(Mi, -1, p)) % M
    if x > M // 2: x -= M
    return x

# ---------------- gcd over Z/qZ with splitting (q possibly composite)
class Split(Exception):
    def __init__(self, d): self.d = d
def _norm(f, q):
    f = [x % q for x in f]
    while f and f[-1] == 0: f.pop()
    if f:
        d = math.gcd(f[-1], q)
        if d != 1: raise Split(d)
    return f
def gcd_modq(f, g, q):
    f = _norm(f, q); g = _norm(g, q)
    while g:
        inv = pow(g[-1], -1, q)
        r = f[:]
        dg = len(g) - 1
        for i in range(len(f) - 1 - dg, -1, -1):
            co = r[i + dg] * inv % q
            if co:
                for j in range(dg + 1):
                    r[i + j] = (r[i + j] - co * g[j]) % q
        r = r[:dg] if dg > 0 else []
        f, g = g, _norm(r, q)
    if not f: return f
    inv = pow(f[-1], -1, q)
    f = [x * inv % q for x in f]
    # strip powers of t (they are units in Lambda); a nonzero non-unit lowest coefficient splits q
    while f and f[0] == 0: f.pop(0)
    if f:
        d = math.gcd(f[0], q)
        if d != 1: raise Split(d)
    return f
def ideal_test(a, c):
    """(a, c) dense Laurent.  Returns (status, info): status 'UNIT' | 'CONTENT' (common factor over Q) | 'PROPER' (witness (q, G):
    for every prime p | q, a and c vanish at the roots of G mod p, G not a power of t) | 'SCALAR_UNIT' / 'SCALAR_PROPER' (c = 0)."""
    if not c[1]:
        return ('SCALAR_UNIT' if isunit(a) else 'SCALAR_PROPER'), None
    if not a[1]:
        return ('UNIT' if isunit(c) else 'PROPER'), ('a=0',)
    if isunit(a) or isunit(c): return 'UNIT', 1
    f = a[1]; g = c[1]
    if len(f) == 1 and len(g) == 1:
        return ('UNIT' if math.gcd(f[0], g[0]) == 1 else 'PROPER'), ('consts', f[0], g[0])
    R = resultant(f, g)
    if R == 0: return 'CONTENT', 0
    if abs(R) == 1: return 'UNIT', R
    work = [abs(R)]; done = []
    while work:
        q = work.pop()
        if q == 1: continue
        try:
            G = gcd_modq(f, g, q)
        except Split as s:
            d = s.d
            work.append(d); work.append(q // d)
            continue
        if len(G) > 1:
            return 'PROPER', (q, G, R)
        done.append(q)
    return 'UNIT', R

# ---------------- candidate analysis
def analyze(A, B):
    """B nonzero.  Returns (kappa, H_assuming_primitive, [cand records]); cand = (m, unit, spanf, tau0, tauinf, r0, rinf, D, Delta)."""
    nu0 = bot(B) - bot(A); ninf = top(A) - top(B)
    kappa = nu0 + ninf
    H = span(A)
    out = []
    for m in sorted({nu0, -ninf}):
        f = sub(A, tmono_mul(-m, B))
        if not f[1]:
            out.append((m, False, None, None, None, None, None, None, None)); continue
        tau0 = max(bot(f) - bot(A), 0); tauinf = max(top(A) - top(f), 0)
        r0 = nu0 - m; rinf = ninf + m
        sf = span(f)
        Dd = H - tau0 - tauinf
        Delta = H + max(-r0, 0) + max(-rinf, 0) - tau0 - tauinf
        out.append((m, isunit(f), sf, tau0, tauinf, r0, rinf, Dd, Delta))
    return kappa, H, out
