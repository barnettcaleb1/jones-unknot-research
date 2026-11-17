"""Exact Temperley-Lieb / Kauffman-bracket action on W(6,0) over Z[A,A^-1].

Self-contained (no imports from the read-only workspace).
Conventions:
  delta = -A^2 - A^-2
  sigma_i  -> A*1 + A^-1*e_i ,  sigma_i^-1 -> A^-1*1 + A*e_i   (i = 1..5)
  Words are lists of nonzero ints (+i = sigma_i, -i = sigma_i^-1); rho(w) v applies the
  RIGHTMOST letter first, so rho is a homomorphism and v_{phi(c)} = rho(phi) v_c.
  G(m,n) = delta^{#loops(m u n)}  (bilinear Gram form, e_i-symmetric, NOT braid invariant)
  H(a,b) = sum bar(a_m) G(m,n) b_n, bar: A -> A^-1   (sesquilinear, braid INVARIANT)
"""
from fractions import Fraction
from itertools import combinations
import math

# ---------------- Laurent polynomials: dict exp -> int ----------------
def L(d=None):
    return {k: v for k, v in (d or {}).items() if v}
ONE = {0: 1}
def ladd(p, q, s=1):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + s * c
        if r[e] == 0:
            del r[e]
    return r
def lmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}
def lscale(p, c, shift=0):
    return {e + shift: c * v for e, v in p.items() if c * v}
def lbar(p):
    return {-e: c for e, c in p.items()}
def mono(e, c=1):
    return {e: c}
DELTA = {2: -1, -2: -1}
def lpow(p, k):
    r = ONE
    for _ in range(k):
        r = lmul(r, p)
    return r
def span(p):
    if not p:
        return None
    return (min(p), max(p))
def lstr(p):
    if not p:
        return "0"
    terms = []
    for e in sorted(p, reverse=True):
        c = p[e]
        terms.append(f"{c:+d}*A^{e}")
    return " ".join(terms)
def leval(p, x):
    # x: complex or Fraction
    return sum(c * x ** e for e, c in p.items())

# ---------------- matchings of 6 points ----------------
N = 6
def noncrossing_matchings(pts):
    if not pts:
        return [[]]
    out = []
    a = pts[0]
    for k in range(1, len(pts), 2):
        b = pts[k]
        inner = pts[1:k]
        outer = pts[k + 1:]
        for mi in noncrossing_matchings(inner):
            for mo in noncrossing_matchings(outer):
                out.append([(a, b)] + mi + mo)
    return out
def to_partner(pairs):
    p = [None] * N
    for a, b in pairs:
        p[a] = b
        p[b] = a
    return tuple(p)
BASIS = [to_partner(m) for m in noncrossing_matchings(list(range(N)))]
IDX = {m: i for i, m in enumerate(BASIS)}
DIM = len(BASIS)

def e_act(i, m):
    """e_i on matching m (points i-1,i in 0-index). returns (coef_is_delta, new_matching)"""
    a, b = i - 1, i
    if m[a] == b:
        return True, m
    p = list(m)
    x, y = p[a], p[b]
    p[a], p[b] = b, a
    p[x], p[y] = y, x
    return False, tuple(p)

def loops(m, n):
    seen = [False] * N
    cnt = 0
    for s in range(N):
        if seen[s]:
            continue
        cnt += 1
        cur = s
        use_m = True
        while True:
            seen[cur] = True
            nxt = m[cur] if use_m else n[cur]
            seen[nxt] = True
            cur = n[nxt] if use_m else m[nxt]
            # walk: cur -m-> nxt -n-> cur2
            if cur == s:
                break
        # (alternation handled by stepping m then n each loop)
    return cnt

def loops2(m, n):
    # robust union-find count
    parent = list(range(N))
    def f(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for x in range(N):
        for y in (m[x], n[x]):
            rx, ry = f(x), f(y)
            if rx != ry:
                parent[rx] = ry
    return len({f(x) for x in range(N)})

GRAM = [[lpow(DELTA, loops2(m, n)) for n in BASIS] for m in BASIS]

# vectors: list of Laurent polys length DIM
def vzero():
    return [{} for _ in range(DIM)]
def e_vec(i, v):
    out = vzero()
    for j, c in enumerate(v):
        if not c:
            continue
        isd, m2 = e_act(i, BASIS[j])
        k = IDX[m2]
        out[k] = ladd(out[k], lmul(c, DELTA) if isd else c)
    return out
def sigma_vec(g, v):
    i = abs(g)
    ev = e_vec(i, v)
    if g > 0:
        a, b = 1, -1
    else:
        a, b = -1, 1
    return [ladd(lscale(v[j], 1, a), lscale(ev[j], 1, b)) for j in range(DIM)]
def rho_vec(word, v):
    for g in reversed(word):
        v = sigma_vec(g, v)
    return v
def rho_mat(word):
    cols = []
    for j in range(DIM):
        ej = vzero(); ej[j] = dict(ONE)
        cols.append(rho_vec(word, ej))
    # matrix M[i][j] = cols[j][i]
    return [[cols[j][i] for j in range(DIM)] for i in range(DIM)]
def mat_vec(M, v):
    out = vzero()
    for i in range(DIM):
        acc = {}
        for j in range(DIM):
            if M[i][j] and v[j]:
                acc = ladd(acc, lmul(M[i][j], v[j]))
        out[i] = acc
    return out
def Gform(a, b):
    acc = {}
    for i in range(DIM):
        if not a[i]:
            continue
        for j in range(DIM):
            if b[j]:
                acc = ladd(acc, lmul(lmul(a[i], GRAM[i][j]), b[j]))
    return acc
def Hform(a, b):
    return Gform([lbar(x) for x in a], b)
def vec_eq(a, b):
    return all(ladd(x, y, -1) == {} for x, y in zip(a, b))

# ---------------- integer polynomial helpers (for gcd / reduction) ----------------
def to_poly(p):
    """Laurent -> (shift, list of int coeffs low->high)"""
    if not p:
        return 0, []
    lo, hi = min(p), max(p)
    return lo, [p.get(e, 0) for e in range(lo, hi + 1)]
def poly_trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a
def poly_divmod_Q(a, b):
    a = [Fraction(x) for x in a]
    b = [Fraction(x) for x in b]
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(poly_trim(a)) >= len(b) and poly_trim(a):
        a = poly_trim(a)
        d = len(a) - len(b)
        c = a[-1] / b[-1]
        q[d] = c
        for k in range(len(b)):
            a[d + k] -= c * b[k]
        a = poly_trim(a)
    return q, poly_trim(a)
def poly_gcd(a, b):
    a, b = poly_trim(a), poly_trim(b)
    while b:
        _, r = poly_divmod_Q(a, b)
        a, b = b, r
    # make primitive integer
    if not a:
        return [1]
    den = 1
    for x in a:
        den = den * Fraction(x).denominator // math.gcd(den, Fraction(x).denominator)
    a = [int(Fraction(x) * den) for x in a]
    g = 0
    for x in a:
        g = math.gcd(g, x)
    a = [x // g for x in a]
    if a[-1] < 0:
        a = [-x for x in a]
    return a
def poly_exact_div(a, b):
    q, r = poly_divmod_Q(a, b)
    assert not r, "not exact"
    q = poly_trim(q)
    assert all(x.denominator == 1 for x in q)
    return [int(x) for x in q]
def content(p):
    g = 0
    for c in p.values():
        g = math.gcd(g, c)
    return g

def cyclotomic(n):
    # Phi_n(x) integer coeffs via division of x^n - 1 by Phi_d, d|n, d<n
    num = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            num = poly_exact_div(num, cyclotomic(d))
    return num
_CYC = {}
def cyc(n):
    if n not in _CYC:
        _CYC[n] = cyclotomic(n)
    return _CYC[n]
def factor_cyclo(p, maxn=80):
    """Laurent poly -> (unit_shift, sign*content, {n: mult}, rest_poly)"""
    if not p:
        return None
    shift, a = to_poly(p)
    c = 0
    for x in a:
        c = math.gcd(c, x)
    a = [x // c for x in a]
    if a[-1] < 0:
        a = [-x for x in a]; c = -c
    mult = {}
    for n in range(1, maxn + 1):
        f = cyc(n)
        while len(a) >= len(f):
            q, r = poly_divmod_Q(a, f)
            if r:
                break
            if not all(x.denominator == 1 for x in q):
                break
            a = [int(x) for x in poly_trim(q)]
            mult[n] = mult.get(n, 0) + 1
    return shift, c, mult, a
def fstr(fc):
    if fc is None:
        return "0"
    shift, c, mult, rest = fc
    parts = [f"{c}*A^{shift}"]
    for n in sorted(mult):
        parts.append(f"Phi{n}(A)" + (f"^{mult[n]}" if mult[n] > 1 else ""))
    if rest != [1]:
        parts.append("R(A)=" + str(rest))
    return " * ".join(parts)
