"""refGen (round D referee) -- INDEPENDENT core code (written from scratch; does not import engineC1/engineA code).
 * exact Laurent polynomials in t as {exp: int} dicts
 * exact rational boxes u(m_0..m_{k-1}) = E Y^{m_{k-1}} ... E Y^{m_0} e_1 (TH-2BR vector), channels a = v1, b = v1 + (1-t^3) v2
 * end data of a Laurent polynomial at t = inf ('top') or t = 0 ('bot'): (deg, lc, normalised coefficients x_1..x_K),
   log-jets l_1..l_K of the normalised series
 * precision-tracked truncated Laurent series at t = infinity (class TS) and an independent jet automaton (build_auto)
"""
from fractions import Fraction as Fr
import itertools

# ---------------- exact Laurent polynomials ----------------
def padd(*ps):
    r = {}
    for p in ps:
        for e, c in p.items():
            r[e] = r.get(e, 0) + c
    return {e: c for e, c in r.items() if c}
def pneg(p): return {e: -c for e, c in p.items()}
def psub(p, q): return padd(p, pneg(q))
def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}
def pshift(p, k): return {e + k: c for e, c in p.items()}
ONE = {0: 1}
ONEMT3 = {0: 1, 3: -1}
ONEMT4 = {0: 1, 4: -1}

# matrices acting on TH-2BR vectors (v1, v2)
# Y = [[1,0],[t^-3,t^-3]], Y^-1 = [[1,0],[-1,t^3]], E = Y^-1 X = [[1,1-t^4],[-1,-1]]
def Ymul(v, m):
    v1, v2 = v
    if m > 0:
        for _ in range(m):
            v2 = pshift(padd(v1, v2), -3)
    else:
        for _ in range(-m):
            v2 = padd(pneg(v1), pshift(v2, 3))
    return (v1, v2)
def Emul(v):
    v1, v2 = v
    return (padd(v1, pmul(ONEMT4, v2)), pneg(padd(v1, v2)))
def box(seq):
    """exact TH-2BR vector of u(m_0..m_{k-1}) = E Y^{m_{k-1}} ... E Y^{m_0} e_1"""
    v = (ONE, {})
    for m in seq:
        v = Emul(Ymul(v, m))
    return v
def chans(v):
    return (dict(v[0]), padd(v[0], pmul(ONEMT3, v[1])))

def enddata(p, end, K):
    """(deg, lc, (x_1..x_K)) of Laurent polynomial p at t=inf (top) or t=0 (bot); x_i normalised coefficients"""
    if end == 'top':
        d = max(p); c = p[d]
        return d, c, tuple(Fr(p.get(d - i, 0), c) for i in range(1, K + 1))
    d = min(p); c = p[d]
    return d, c, tuple(Fr(p.get(d + i, 0), c) for i in range(1, K + 1))

def logjet(x):
    """log of 1 + x_1 u + x_2 u^2 + ... : (l_1..l_K); independent recursion via power-series log"""
    K = len(x)
    # log(1+h) = sum_{n>=1} (-1)^{n+1} h^n / n, truncated at u^K
    h = [Fr(0)] + [Fr(v) for v in x]          # h[0] = 0
    res = [Fr(0)] * (K + 1)
    hp = [Fr(1)] + [Fr(0)] * K                # h^0
    for n in range(1, K + 1):
        # hp = hp * h
        new = [Fr(0)] * (K + 1)
        for i in range(K + 1):
            if hp[i]:
                for j in range(1, K + 1 - i):
                    if h[j]:
                        new[i + j] += hp[i] * h[j]
        hp = new
        sgn = 1 if n % 2 == 1 else -1
        for i in range(K + 1):
            res[i] += sgn * hp[i] / n
    return tuple(res[1:])

def sdiv(x, y):
    """normalised series quotient (1+x)/(1+y) coefficients"""
    K = len(x)
    X = [Fr(1)] + list(x); Yv = [Fr(1)] + list(y)
    q = [Fr(0)] * (K + 1)
    for n in range(K + 1):
        s = X[n] - sum(Yv[i] * q[n - i] for i in range(1, n + 1))
        q[n] = s
    return tuple(q[1:])

def boxdata(seq, K=4):
    """exact end data of a, b, q for box u(seq) at both ends.
       returns {end: dict(da, lca, la, db, lcb, lb, dq, lcq, lq)} with la/lb/lq log-jets to order K"""
    a, b = chans(box(seq))
    out = {}
    for end in ('top', 'bot'):
        da, ca, xa = enddata(a, end, K); db, cb, xb = enddata(b, end, K)
        xq = sdiv(xb, xa)
        out[end] = dict(da=da, lca=ca, la=logjet(xa), db=db, lcb=cb, lb=logjet(xb),
                        dq=db - da, lcq=Fr(cb, ca), lq=logjet(xq))
    return out

def normal_forms_size(S):
    """all normal forms (m_0..m_{k-1}), k>=1, m_0 not in {0,-1}, interior m_i != 0, with size k + sum|m_i| <= S"""
    out = []
    def rec(prefix, size):
        if prefix:
            out.append(tuple(prefix))
        for p in range(2, S - size + 1):   # part size |m|+1
            for m in (p - 1, -(p - 1)):
                if not prefix and m == -1:
                    continue
                prefix.append(m); rec(prefix, size + p); prefix.pop()
    rec([], 0)
    return out

def mirror(seq):
    """u'' = u(-m_0-1, -m_1, ..., -m_{k-1})"""
    return (-seq[0] - 1,) + tuple(-m for m in seq[1:])

# ---------------- precision-tracked truncated Laurent series at t = infinity ----------------
class TS:
    """f = sum_e c[e] t^e, with c[e] KNOWN (possibly 0) for every e >= lo; lo = None means exact (all degrees known)."""
    __slots__ = ('c', 'lo')
    def __init__(self, c, lo):
        self.lo = lo
        self.c = {e: Fr(v) for e, v in c.items() if v != 0 and (lo is None or e >= lo)}
    def top(self):
        return max(self.c) if self.c else None
    def tbound(self):
        """an upper bound for the true top degree: known top if the known part is nonzero, else lo-1 (None if exact zero)"""
        if self.c: return max(self.c)
        if self.lo is None: return None
        return self.lo - 1
def ts_add(f, g):
    if f.lo is None: lo = g.lo
    elif g.lo is None: lo = f.lo
    else: lo = max(f.lo, g.lo)
    c = dict(f.c)
    for e, v in g.c.items(): c[e] = c.get(e, 0) + v
    return TS(c, lo)
def ts_neg(f): return TS({e: -v for e, v in f.c.items()}, f.lo)
def ts_shift(f, k): return TS({e + k: v for e, v in f.c.items()}, None if f.lo is None else f.lo + k)
def ts_mul(f, g):
    Tf, Tg = f.tbound(), g.tbound()
    if Tf is None or Tg is None:      # an exact zero factor
        return TS({}, None)
    cands = []
    if f.lo is not None: cands.append(f.lo + Tg)
    if g.lo is not None: cands.append(g.lo + Tf)
    lo = max(cands) if cands else None
    c = {}
    for e, v in f.c.items():
        for e2, w in g.c.items():
            if lo is None or e + e2 >= lo:
                c[e + e2] = c.get(e + e2, 0) + v * w
    return TS(c, lo)
def ts_inv(f, work=80):
    d = f.top()
    assert d is not None, 'inverse of a series with unknown leading term'
    lc = f.c[d]
    R = work if f.lo is None else d - f.lo        # relative precision of f (number of known orders below the lead)
    # f = lc t^d (1 + h(u)), h_i = c[d-i]/lc, i = 1..R
    h = [Fr(0)] + [f.c.get(d - i, Fr(0)) / lc for i in range(1, R + 1)]
    g = [Fr(1)] + [Fr(0)] * R
    for n in range(1, R + 1):
        g[n] = -sum(h[i] * g[n - i] for i in range(1, n + 1))
    return TS({-d - i: g[i] / lc for i in range(R + 1)}, -d - R)
TONE = TS({0: 1}, None)
T1MT4 = TS({0: 1, 4: -1}, None)
T1MT3 = TS({0: 1, 3: -1}, None)

def ts_jet(f, K):
    """(deg, lc, (x_1..x_K)) requiring relative precision K"""
    d = f.top()
    assert d is not None, 'unknown leading term'
    assert f.lo is None or d - f.lo >= K, ('insufficient precision', d, f.lo, K)
    lc = f.c[d]
    return d, lc, tuple(f.c.get(d - i, Fr(0)) / lc for i in range(1, K + 1))

def key_of(r, K):
    if r.lo is None and not r.c:
        return 'init'
    d = r.top()
    if d is None or d <= -4 - K:
        # need: every degree >= -3-K known (and zero)
        assert r.lo is None or r.lo <= -3 - K, ('tiny undetermined', d, r.lo)
        return 'tiny'
    dd, lc, x = ts_jet(r, K)
    return (dd, (lc,) + x)          # raw (unnormalised) coefficients via lc and ratios
def from_key(key, K):
    if key == 'init': return TS({}, None)
    if key == 'tiny': return TS({}, -3 - K)
    d, (lc, *x) = key
    c = {d: lc}
    for i, v in enumerate(x, 1): c[d - i] = lc * v
    return TS(c, d - K)

def ts_Ypow(r, m):
    if m > 0:
        for _ in range(m): r = ts_shift(ts_add(TONE, r), -3)
    else:
        for _ in range(-m): r = ts_add(ts_neg(TONE), ts_shift(r, 3))
    return r

def trans(key, m, K):
    """returns (Djet=(deg,lc,x), next key) or None for the degenerate exact-zero numerator"""
    r = from_key(key, K)
    rp = ts_Ypow(r, m)
    D = ts_add(TONE, ts_mul(T1MT4, rp))
    num = ts_add(TONE, rp)
    if num.lo is None and not num.c:
        return None
    rn = ts_neg(ts_mul(num, ts_inv(D)))
    return ts_jet(D, K), key_of(rn, K)

def q_end(key, K):
    """(deg, lc, x_1..x_K) of q = 1 + (1-t^3) r at the top"""
    if key == 'init':
        return (0, Fr(1), tuple([Fr(0)] * K))
    r = from_key(key, K)
    q = ts_add(TONE, ts_mul(T1MT3, r))
    return ts_jet(q, K)

def build_auto(K, M=None):
    if M is None: M = K + 3
    states = ['init']; idx = {'init': 0}; T = {}
    i = 0
    while i < len(states):
        s = states[i]; i += 1
        for m in list(range(1, M + 1)) + list(range(-M, 0)):
            if s == 'init' and m == -1: continue
            res = trans(s, m, K)
            if res is None: continue
            Dj, ns = res
            if ns not in idx:
                idx[ns] = len(states); states.append(ns)
            T[(s, m)] = (Dj, ns)
        if len(states) > 10000: raise RuntimeError('state explosion')
    return states, T

def clip(m, M):
    return max(-M, min(M, m))

def run_auto(seq, K, T, M=None):
    """walk the automaton; returns (final key, log-jet of a (sum of log-jets of D), list of states)"""
    if M is None: M = K + 3
    s = 'init'; la = [Fr(0)] * K; path = [s]
    for m in seq:
        Dj, ns = T[(s, clip(m, M))]
        l = logjet(Dj[2])
        la = [x + y for x, y in zip(la, l)]
        s = ns; path.append(s)
    return s, tuple(la), path

# R0 rewriting (copied from rg_q1_exact.py, same author)
def normal_form(word):
    """R0 rewriting: X = Y E, x = t^-4 E Y^-1.  Returns (n_k, (m_0..m_{k-1})) with v(word) = unit * Y^{n_k} u(m)."""
    groups = [0]          # Y-exponent groups, left to right; E separates groups
    for ch in word:
        if ch == 'Y': groups[-1] += 1
        elif ch == 'y': groups[-1] -= 1
        elif ch == 'X': groups[-1] += 1; groups.append(0)          # Y E
        elif ch == 'x': groups.append(-1)                           # E Y^-1   (unit t^-4)
    g = groups[::-1]      # g[0] = m_0 (acts first), ..., g[k] = n_k
    changed = True
    while changed:
        changed = False
        k = len(g) - 1
        for i in range(1, k):          # interior zero: E Y^0 E = t^4
            if g[i] == 0:
                g = g[:i - 1] + [g[i - 1] + g[i + 1]] + g[i + 2:]
                changed = True; break
        if changed: continue
        if k >= 1 and g[0] == 0:       # E e_1 = Y^-1 e_1
            g = [g[1] - 1] + g[2:]; changed = True; continue
        if k >= 1 and g[0] == -1:      # E Y^-1 e_1 = t^4 e_1
            g = [g[1]] + g[2:]; changed = True; continue
    return g[-1], tuple(g[:-1])

