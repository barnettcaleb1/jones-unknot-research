"""tl.py -- exact Temperley-Lieb / Kauffman bracket engine for tangles (GADGET-B, 17 Nov 2026).

Laurent polynomials in A: dict {exponent: int}.  delta = -A^2 - A^-2.
Tangle diagrams are Morse words read bottom -> top on a row of strands:
  ('cap', i)  : create two new strands at positions i, i+1 joined to each other (a "U-turn" opening upwards)
  ('cup', i)  : join the strands at positions i, i+1 (closing; a loop is closed if they were already joined)
  ('x', i)    : crossing of strands i, i+1, the strand going SW -> NE passes OVER
  ('y', i)    : crossing of strands i, i+1, the strand going SE -> NW passes OVER
Kauffman: the A-smoothing of 'x' is the vertical (identity) smoothing, so  x = A*id + A^-1*e_i,  y = A^-1*id + A*e_i.
(Same convention as tools/kauffman.py, checked there to reproduce V(right trefoil) = t + t^3 - t^4 with t = A^-4.)
A tangle has b bottom endpoints and t top endpoints.  Boundary positions in COUNTERCLOCKWISE order:
  bottom points left -> right are positions 0..b-1, top points right -> left are positions b..b+t-1.
br(T) = dict {matching: poly}, a matching = tuple partner[] over boundary positions (planar automatically).
Closed loops are counted with weight delta (UNREDUCED convention); for a closed link divide by delta.
"""
import itertools, cmath, math, random
from functools import lru_cache

# ----------------------------------------------------------------- Laurent polynomials
def padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c * v
        if nv: p[e] = nv
        elif e in p: del p[e]
    return p
def psum(*ps):
    r = {}
    for p in ps: padd(r, p)
    return r
def pneg(p): return {e: -v for e, v in p.items()}
def pshift(p, k, c=1): return {e + k: c * v for e, v in p.items() if c * v}
def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}
def ppow(p, k):
    r = {0: 1}
    for _ in range(k): r = pmul(r, p)
    return r
DELTA = {2: -1, -2: -1}
ONE = {0: 1}
def pdelta(p): return pmul(p, DELTA)
def peval(p, z): return sum(c * z ** e for e, c in p.items())
def pdiv_exact(p, q):
    """exact division of Laurent polys p / q over Z (raises ValueError if not exact)."""
    if not q: raise ZeroDivisionError
    if not p: return {}
    lp, lq = min(p), min(q)
    P = [0] * (max(p) - lp + 1)
    for e, c in p.items(): P[e - lp] = c
    Q = [0] * (max(q) - lq + 1)
    for e, c in q.items(): Q[e - lq] = c
    if len(P) < len(Q): raise ValueError('not exact (degree)')
    out = [0] * (len(P) - len(Q) + 1)
    for k in range(len(P) - len(Q), -1, -1):
        num = P[k + len(Q) - 1]
        if num % Q[-1]: raise ValueError('not exact (coefficient)')
        c = num // Q[-1]; out[k] = c
        if c:
            for j in range(len(Q)): P[k + j] -= c * Q[j]
    if any(P): raise ValueError('not exact (remainder)')
    return {k + lp - lq: c for k, c in enumerate(out) if c}
def pdiv_delta(p): return pdiv_exact(p, DELTA)
def pstr(p, var='A'):
    if not p: return '0'
    out = []
    for e in sorted(p, reverse=True):
        c = p[e]
        s = ('+' if c > 0 else '-') + (str(abs(c)) if abs(c) != 1 or e == 0 else '')
        if e != 0: s += var + ('^%d' % e if e != 1 else '')
        out.append(s)
    s = ''.join(out)
    return s[1:] if s.startswith('+') else s
def pnorm_unit(p):
    """normalise p up to +-A^k: shift min exponent to 0 and make lowest coeff positive. Returns (key, shift, sign)."""
    if not p: return ((), 0, 1)
    lo = min(p); s = 1 if p[lo] > 0 else -1
    return (tuple(sorted((e - lo, s * v) for e, v in p.items())), lo, s)
def ord_at(p, z, tol=1e-9, maxk=60):
    """order of vanishing of Laurent poly p at A = z (numerical, via repeated derivative)."""
    q = dict(p); k = 0
    while k < maxk:
        if abs(peval(q, z)) > tol * (1 + sum(abs(c) for c in q.values()) * max(1, abs(z)) ** 0):
            return k
        q = {e - 1: e * c for e, c in q.items() if e != 0}
        k += 1
    return k

# ----------------------------------------------------------------- matchings / TL basis
def nc_matchings(n):
    """all non-crossing perfect matchings of 0..n-1 (n even) as partner tuples."""
    @lru_cache(None)
    def rec(lo, hi):
        if lo > hi: return [()]
        res = []
        for k in range(lo + 1, hi + 1, 2):
            for left in rec(lo + 1, k - 1):
                for right in rec(k + 1, hi):
                    res.append(((lo, k),) + left + right)
        return res
    out = []
    for pairs in rec(0, n - 1):
        m = [None] * n
        for a, b in pairs: m[a] = b; m[b] = a
        out.append(tuple(m))
    return sorted(out)
def pairs_of(m): return tuple(sorted((a, b) for a, b in enumerate(m) if a < b))
def is_noncrossing(m):
    pr = pairs_of(m)
    for (a, b), (c, d) in itertools.combinations(pr, 2):
        if a < c < b < d or c < a < d < b: return False
    return True

# ----------------------------------------------------------------- Morse word evaluation
def _relabel_join(row, i):
    """join current strands i, i+1 (cup). returns (newrow, closed_loop:bool, bottom_pair or None)"""
    a, c = row[i], row[i + 1]
    row = list(row)
    loop = False; bpair = None
    if a == ('S', i + 1):          # they are joined to each other -> closed loop
        loop = True
    elif a[0] == 'B' and c[0] == 'B':
        bpair = (a[1], c[1])
    elif a[0] == 'B' and c[0] == 'S':
        row[c[1]] = a
    elif a[0] == 'S' and c[0] == 'B':
        row[a[1]] = c
    else:
        row[a[1]] = ('S', c[1]); row[c[1]] = ('S', a[1])
    del row[i:i + 2]
    # reindex S-references
    def fix(e):
        if e[0] == 'S':
            j = e[1]
            return ('S', j - 2 if j > i + 1 else j)
        return e
    row = [fix(e) for e in row]
    return row, loop, bpair

def _apply(row, op, i, p):
    """yield (newrow, poly) ; bottom-bottom pairs are stored as ('P', k) markers appended? -- we handle them by
    keeping a separate canonical record inside the row as trailing tuple."""
    # row is a tuple; bottom-bottom pairs are stored at the end as ('BB', a, b) entries (not strands)
    strands = [e for e in row if e[0] in ('B', 'S')]
    extra = [e for e in row if e[0] == 'BB']
    w = len(strands)
    def pack(st, ex): return tuple(st) + tuple(sorted(ex))
    if op == 'cap':
        if i > w: raise ValueError('cap index')
        def fix(e):
            if e[0] == 'S':
                j = e[1]; return ('S', j + 2 if j >= i else j)
            return e
        st = [fix(e) for e in strands]
        st[i:i] = [('S', i + 1), ('S', i)]
        yield pack(st, extra), p
    elif op == 'cup':
        if i + 1 >= w: raise ValueError('cup index')
        st, loop, bp = _relabel_join(strands, i)
        ex = list(extra)
        if bp: ex.append(('BB',) + tuple(sorted(bp)))
        yield pack(st, ex), (pdelta(p) if loop else p)
    elif op in ('x', 'y'):
        if i + 1 >= w: raise ValueError('crossing index')
        aid, ae = (1, -1) if op == 'x' else (-1, 1)
        yield pack(strands, extra), pshift(p, aid)
        st, loop, bp = _relabel_join(strands, i)
        ex = list(extra)
        if bp: ex.append(('BB',) + tuple(sorted(bp)))
        q = pdelta(p) if loop else p
        # cap at i
        def fix(e):
            if e[0] == 'S':
                j = e[1]; return ('S', j + 2 if j >= i else j)
            return e
        st = [fix(e) for e in st]
        st[i:i] = [('S', i + 1), ('S', i)]
        yield pack(st, ex), pshift(q, ae)
    else:
        raise ValueError(op)

def evaluate_tangle(word, b, t):
    """wrapper returning dict {matching(partner tuple over 0..b+t-1): poly}."""
    states = {tuple(('B', k) for k in range(b)): {0: 1}}
    for op, i in word:
        new = {}
        for row, p in states.items():
            for r2, q in _apply(row, op, i, p):
                if q: padd(new.setdefault(r2, {}), q)
        states = {r: p for r, p in new.items() if p}
    out = {}
    n = b + t
    for row, p in states.items():
        strands = [e for e in row if e[0] in ('B', 'S')]
        extra = [e for e in row if e[0] == 'BB']
        if len(strands) != t: raise ValueError('ends with %d strands, expected %d' % (len(strands), t))
        m = [None] * n
        def pos_top(j): return b + (t - 1 - j)
        for j, e in enumerate(strands):
            if e[0] == 'B': a, c = e[1], pos_top(j)
            else: a, c = pos_top(j), pos_top(e[1])
            m[a] = c; m[c] = a
        for _, a, c in extra: m[a] = c; m[c] = a
        assert None not in m
        padd(out.setdefault(tuple(m), {}), p)
    return {m: p for m, p in out.items() if p}

# ----------------------------------------------------------------- operations on TL vectors
def rotate(br, n, r):
    """rotate boundary positions by r (position p -> p + r mod n)."""
    out = {}
    for m, p in br.items():
        mm = [None] * n
        for a in range(n): mm[(a + r) % n] = (m[a] + r) % n
        padd(out.setdefault(tuple(mm), {}), p)
    return out
def loops_of_union(m1, m2):
    """number of cycles of the union of two perfect matchings on the same point set."""
    n = len(m1); seen = [False] * n; c = 0
    for s in range(n):
        if seen[s]: continue
        c += 1; x = s
        while True:
            seen[x] = True; y = m1[x]; seen[y] = True; x = m2[y]
            if x == s: break
    return c
def pair_with(br, m_out):
    """close the tangle with the crossingless matching m_out (outside); returns UNREDUCED poly (each loop = delta)."""
    tot = {}
    for m, p in br.items():
        L = loops_of_union(m, m_out)
        padd(tot, pmul(p, ppow(DELTA, L)))
    return tot
def bilinear(br1, br2):
    """<T1, T2>: glue T1 (positions 0..n-1 ccw) to the MIRROR-POSITIONED T2: point k of T1 glued to point (n-1-k)
    of T2 (so that gluing two disks along their boundary circle is planar). Returns UNREDUCED poly."""
    tot = {}
    for m1, p1 in br1.items():
        for m2, p2 in br2.items():
            n = len(m1)
            m2r = tuple(n - 1 - m2[n - 1 - k] for k in range(n))
            L = loops_of_union(m1, m2r)
            padd(tot, pmul(pmul(p1, p2), ppow(DELTA, L)))
    return tot
def vec(br, basis):
    return [br.get(m, {}) for m in basis]
def is_zero_vec(v): return all(not p for p in v)

# ----------------------------------------------------------------- exact cyclotomic reduction
@lru_cache(None)
def cyclotomic(N):
    """integer coefficient list (low -> high) of Phi_N."""
    # x^N - 1 = prod_{d|N} Phi_d
    num = [-1] + [0] * (N - 1) + [1]
    for d in range(1, N):
        if N % d == 0:
            num = _polydiv(num, list(cyclotomic(d)))
    return tuple(num)
def _polydiv(a, b):
    a = list(a); out = [0] * (len(a) - len(b) + 1)
    for k in range(len(a) - len(b), -1, -1):
        c = a[k + len(b) - 1] // b[-1]
        out[k] = c
        for j in range(len(b)): a[k + j] -= c * b[j]
    assert all(v == 0 for v in a[:len(b) - 1]), 'nonexact'
    return out
def red_cyclo(p, N):
    """reduce Laurent poly p(A) modulo Phi_N(A): returns tuple of length phi(N) (coefficients of 1, A, ...)."""
    ph = list(cyclotomic(N)); d = len(ph) - 1
    v = [0] * N
    for e, c in p.items(): v[e % N] += c
    # reduce v (degree < N) mod Phi_N (monic)
    for k in range(N - 1, d - 1, -1):
        c = v[k]
        if c:
            for j in range(d + 1): v[k - d + j] -= c * ph[j]
    return tuple(v[:d])

# ----------------------------------------------------------------- standard pieces
def crossing_br(kind='x'):
    """4-ended tangle (b=2,t=2) for a single crossing."""
    return evaluate_tangle([(kind, 0)], 2, 2)
if __name__ == '__main__':
    B4 = nc_matchings(4); print('TL(4) basis', B4)
    print('x:', {m: pstr(p) for m, p in crossing_br('x').items()})
    print('y:', {m: pstr(p) for m, p in crossing_br('y').items()})
    # trefoil as closure: braid x^3 on 2 strands, trace closure via caps/cups
    print(len(nc_matchings(6)), len(nc_matchings(8)))
