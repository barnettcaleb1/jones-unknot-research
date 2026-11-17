"""refM300: OWN exact Laurent-polynomial and end-series utilities (written from scratch for this referee).
Polys: dict exponent -> int (or Fraction).  End data at t=inf ('top', u = 1/t) and t=0 ('bot', u = t):
f = lc * t^d * (1 + x1 u + x2 u^2 + ...);  log-jet (l1, l2, ...) = coefficients of log(1 + x1 u + ...)."""
from fractions import Fraction as Fr
def pclean(p): return {e: c for e, c in p.items() if c}
def padd(*ps):
    r = {}
    for p in ps:
        for e, c in p.items(): r[e] = r.get(e, 0) + c
    return pclean(r)
def pneg(p): return {e: -c for e, c in p.items()}
def psub(p, q): return padd(p, pneg(q))
def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items(): r[e + f] = r.get(e + f, 0) + c * d
    return pclean(r)
def pshift(p, k): return {e + k: c for e, c in p.items()}
def pdeg(p): return max(p)
def plow(p): return min(p)
def pspan(p): return max(p) - min(p)
def pdivexact(p, d):
    """exact quotient p/d of Laurent polys (None if not exact)"""
    p = dict(p); q = {}
    if not p: return {}
    dt = max(d); dc = d[dt]; lo = min(p) - min(d)
    while p:
        e = max(p); c = p[e]; k = e - dt
        if k < lo or c % dc: return None
        qq = c // dc; q[k] = qq
        for f, g in d.items():
            v = p.get(k + f, 0) - g * qq
            if v: p[k + f] = v
            else: p.pop(k + f, None)
    return q
def enddata(f, end, K):
    """(d, lc, (x1..xK)) normalised expansion of the Laurent poly f at the given end"""
    if end == 'top':
        d = max(f); c = f[d]; xs = tuple(Fr(f.get(d - i, 0), c) for i in range(1, K + 1))
    else:
        d = min(f); c = f[d]; xs = tuple(Fr(f.get(d + i, 0), c) for i in range(1, K + 1))
    return d, c, xs
def logjet(xs):
    """log(1 + x1 u + x2 u^2 + ...) = l1 u + l2 u^2 + ... ; recursion from u (log s)' s = s' """
    K = len(xs); x = [Fr(1)] + [Fr(v) for v in xs]; l = [Fr(0)] * (K + 1)
    for k in range(1, K + 1):
        tot = k * x[k]
        for j in range(1, k): tot -= j * l[j] * x[k - j]
        l[k] = tot / k
    return tuple(l[1:])
def expjet(ls):
    """inverse of logjet: (l1..lK) -> (x1..xK)"""
    K = len(ls); l = [Fr(0)] + [Fr(v) for v in ls]; x = [Fr(1)] + [Fr(0)] * K
    for k in range(1, K + 1):
        # k x_k = sum_{j=1..k} j l_j x_{k-j}
        x[k] = sum(j * l[j] * x[k - j] for j in range(1, k + 1)) / k
    return tuple(x[1:])
def logdata(f, end, K):
    d, c, xs = enddata(f, end, K); return d, c, logjet(xs)
# --- the closure weights (own formulas, from Theorem N / Theorem V as stated in BRIEF / engineA) ---
def tmono(k): return {k: (-1) ** (k % 2)}           # (-t)^k
T2P1 = {0: 1, 2: 1}; PHI3 = {0: 1, 1: 1, 2: 1}; PHI5 = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
def w1(mu): return padd({1: 1}, pmul(T2P1, tmono(mu)))                 # t + (1+t^2)(-t)^mu
def w3(mu): return pmul(T2P1, psub({0: 1}, tmono(mu)))                  # (1+t^2)(1-(-t)^mu)
def wV(a): return padd(pshift(tmono(a), 1), pshift(PHI5, 3 * a - 1))    # (-t)^a t + t^(3a-1) Phi_5
