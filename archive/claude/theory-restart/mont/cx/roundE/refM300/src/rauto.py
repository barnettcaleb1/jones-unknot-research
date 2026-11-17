"""refM300: OWN rigorous jet automaton for non-integral rational boxes at t = infinity (written from scratch).
Normal form u(m_0..m_{k-1}) = E Y^{m_{k-1}} ... E Y^{m_0} e_1 (all m_i != 0, m_0 != -1), TH-2BR state r = v_2/v_1:
  Y: r -> t^-3 (1 + r);  Y^-1: r -> t^3 r - 1;  E = [[1, 1-t^4], [-1, -1]]:  r -> -(1+r)/D,  a -> a D,  D = 1 + (1-t^4) r.
q = b/a = 1 + (1-t^3) r.  Series at t = inf with ABSOLUTE precision: Ser(c, fl): coefficients c[e] exact for all e >= fl
(fl None = exact finite Laurent poly).  A state key: 'init' (r = 0), 'tiny' (r = O(t^(-4-K))), or (d, (j0..jK)) with
r = t^d (j0 + j1 u + .. + jK u^K + O(u^(K+1))).  Every transition is computed on the WHOLE class of series with that key
(unknown coefficients below the floor) and asserted to determine D's K-jet and the next key."""
from fractions import Fraction as Fr
import itertools
class Ser:
    __slots__ = ('c', 'fl')
    def __init__(s, c, fl):
        s.c = {e: Fr(v) for e, v in c.items() if v and (fl is None or e >= fl)}; s.fl = fl
    def topdeg(s):
        """highest degree that may be nonzero"""
        if s.c: return max(s.c)
        return None if s.fl is None else s.fl - 1
def sadd(x, y):
    fl = None if (x.fl is None and y.fl is None) else max(v for v in (x.fl, y.fl) if v is not None)
    c = dict(x.c)
    for e, v in y.c.items(): c[e] = c.get(e, 0) + v
    return Ser(c, fl)
def sneg(x): return Ser({e: -v for e, v in x.c.items()}, x.fl)
def sshift(x, k): return Ser({e + k: v for e, v in x.c.items()}, None if x.fl is None else x.fl + k)
def smul(x, y):
    tx, ty = x.topdeg(), y.topdeg()
    if x.fl is None and not x.c: return Ser({}, None)
    if y.fl is None and not y.c: return Ser({}, None)
    cand = []
    if x.fl is not None: cand.append(x.fl + ty)
    if y.fl is not None: cand.append(y.fl + tx)
    fl = max(cand) if cand else None
    c = {}
    for e, v in x.c.items():
        for f, w in y.c.items():
            if fl is None or e + f >= fl: c[e + f] = c.get(e + f, 0) + v * w
    return Ser(c, fl)
def sinv(x, extra=40):
    assert x.c, 'inverse of a series with unknown leading term'
    d = max(x.c); lc = x.c[d]
    rel = (d - x.fl) if x.fl is not None else extra
    h = {k: x.c.get(d - k, 0) / lc for k in range(1, rel + 1)}     # x = lc t^d (1 + sum h_k u^k)
    inv = [Fr(1)] + [Fr(0)] * rel
    for n in range(1, rel + 1):
        inv[n] = -sum(h[k] * inv[n - k] for k in range(1, n + 1))
    return Ser({-d - n: inv[n] / lc for n in range(rel + 1)}, -d - rel)
ONE = Ser({0: 1}, None); MONE = Ser({0: -1}, None)
OMT4 = Ser({0: 1, 4: -1}, None); OMT3 = Ser({0: 1, 3: -1}, None)
def from_key(key, K):
    if key == 'init': return Ser({}, None)
    if key == 'tiny': return Ser({}, -3 - K)
    d, j = key
    return Ser({d - i: v for i, v in enumerate(j)}, d - K)
def jet_of(x, K):
    """(d, lc, relative coefficients x1..xK) of a series; asserts they are KNOWN"""
    assert x.c, 'unknown leading term'
    d = max(x.c)
    assert x.fl is None or d - x.fl >= K, ('precision', d, x.fl, K)
    lc = x.c[d]
    return d, lc, tuple(x.c.get(d - i, 0) / lc for i in range(1, K + 1))
def canon(r, K):
    if r.fl is None and not r.c: return 'init'
    # nonzero coefficient at degree >= -3-K ?
    big = [e for e in r.c if e >= -3 - K]
    if not big:
        assert r.fl is not None and r.fl <= -3 - K or r.fl is None, ('cannot decide tiny', r.fl)
        return 'tiny'
    d = max(r.c)
    assert r.fl is None or d - r.fl >= K, ('state precision', d, r.fl)
    return (d, tuple(r.c.get(d - i, Fr(0)) for i in range(K + 1)))
def Yact(r, m):
    for _ in range(abs(m)):
        r = sshift(sadd(ONE, r), -3) if m > 0 else sadd(MONE, sshift(r, 3))
    return r
def step(key, m, K):
    r = from_key(key, K)
    rp = Yact(r, m)
    D = sadd(ONE, smul(OMT4, rp))
    num = sadd(ONE, rp)
    if num.fl is None and not num.c: return None          # degenerate (only init with m = -1)
    rn = sneg(smul(num, sinv(D)))
    return jet_of(D, K), canon(rn, K)
def logs(xs):
    K = len(xs); x = [Fr(1)] + list(xs); l = [Fr(0)] * (K + 1)
    for k in range(1, K + 1):
        tot = k * x[k]
        for j in range(1, k): tot -= j * l[j] * x[k - j]
        l[k] = tot / k
    return tuple(l[1:])
def qdata(key, K):
    """(deg q, lc q, log-jet of q to order K) at the state"""
    if key in ('init',): return None
    r = from_key(key, K)
    q = sadd(ONE, smul(OMT3, r))
    d, lc, xs = jet_of(q, K)
    return d, lc, logs(xs)
def build(K, M=None, check_clip=8):
    """states, edges: dict (key, m) -> (Djet logs, next key) for m in [-M, M]\\{0}; clipping checked for M..M+check_clip"""
    if M is None: M = K + 3
    order = ['init']; seen = {'init'}; trans = {}
    i = 0
    while i < len(order):
        key = order[i]; i += 1
        for m in list(range(1, M + 1)) + list(range(-M, 0)):
            if key == 'init' and m == -1: continue
            res = step(key, m, K)
            if res is None: continue
            (d, lc, xs), nk = res
            trans[(key, m)] = (d, lc, logs(xs), nk)
            if nk not in seen: seen.add(nk); order.append(nk)
        for m in (M, -M):
            base = trans[(key, m)]
            for e in range(1, check_clip + 1):
                mm = m + e if m > 0 else m - e
                (d, lc, xs), nk = step(key, mm, K)
                assert (logs(xs), nk) == (base[2], base[3]), ('CLIP FAIL', key, m, mm)
    return order, trans
def edges(order, trans):
    """deduplicated edges (from, to, logjet of D) -- the multigraph used for longest/shortest paths"""
    E = set()
    for (k, m), (d, lc, l, nk) in trans.items(): E.add((k, nk, l))
    return sorted(E, key=repr)
def extremum(order, E, fin, edgew, finw, sense='min'):
    """exact min (or max) over all walks init -> s (s != init, >= 1 step) of sum edgew(l) + finw(fin[s]).
    Returns None if unbounded (negative cycle for min / positive cycle for max reachable)."""
    sg = 1 if sense == 'min' else -1
    best = {k: None for k in order}; best['init'] = Fr(0)
    n = len(order)
    for it in range(n + 1):
        ch = False
        for (a, b, l) in E:
            if best[a] is None: continue
            v = best[a] + sg * edgew(l)
            if best[b] is None or v < best[b]: best[b] = v; ch = True
        if not ch: break
    else:
        return None
    # init is never re-entered (asserted by caller); the empty walk is excluded because init has no incoming edges
    vals = [best[k] + sg * finw(fin[k]) for k in order if k != 'init' and best[k] is not None]
    return sg * min(vals)
