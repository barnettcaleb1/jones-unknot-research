#!/usr/bin/env python3
"""First-order (U^2) obstruction theory for extending a type D structure over B to one over the A_infinity algebra B^*[U]
(Kotelskiy-Watson-Zibrowius, arXiv:2202.01460, Definitions 4.2, 4.3 and Theorem 4.4).  Coefficients F_2.

Algebra basis elements: ('id', i), ('D', i, n) = D_i^n, ('S', i, n) = S^n starting at idempotent i  (i in 'b','c').
Path composition a.b (a first): D^n D^m = D^(n+m), S^n S^m = S^(n+m) when composable, D S = S D = 0.
mu_4: (a1,a2,a3,a4 b) -> b and (b a1,a2,a3,a4) -> b for (a1..a4) an alternating composable path S,D,S,D or D,S,D,S of first powers.
mu_6: same rule with the disk sequences of length 6 = cyclic rotations of (D^2,S,D,S^2,D,S)  (only needed when a D^2 arrow is present).
A type D structure: generators (idem, h, q); arrows (src, dst, alg, upow) with h(dst) = h(src) + 1 + upow, q(dst) = q(src) + qdeg(alg) + 3 upow.
"""
import itertools, sys
from collections import defaultdict

OTHER = {'b': 'c', 'c': 'b'}
def start(a): return a[1]
def end(a):
    if a[0] == 'S' and a[2] % 2 == 1: return OTHER[a[1]]
    return a[1]
def qdeg(a):
    return 0 if a[0] == 'id' else (2 * a[2] if a[0] == 'D' else a[2])
def mul(a, b):
    """path product a then b, or None if zero"""
    if end(a) != start(b): return None
    if a[0] == 'id': return b
    if b[0] == 'id': return a
    if a[0] != b[0]: return None
    return (a[0], a[1], a[2] + b[2])
def split_last(a):
    """all ways a = a4 . b with a4 a first power of the same letter; returns list of (a4, b)"""
    if a[0] == 'id': return []
    a4 = (a[0], a[1], 1)
    if a[2] == 1: return [(a4, ('id', end(a)))]
    return [(a4, (a[0], end(a4), a[2] - 1))]
def split_first(a):
    """a = b . a1 with a1 a first power; returns (b, a1)"""
    if a[0] == 'id': return []
    if a[2] == 1: return [(('id', start(a)), a)]
    b = (a[0], a[1], a[2] - 1)
    return [(b, (a[0], end(b), 1))]
def alternating(seq):
    """seq of first powers: alternating S,D and composable"""
    for x in seq:
        if x[0] == 'id' or x[2] != 1: return False
    for x, y in zip(seq, seq[1:]):
        if end(x) != start(y) or x[0] == y[0]: return False
    return True
def mu4(a1, a2, a3, a4):
    """returns set (as dict elem->count mod 2) of results"""
    res = defaultdict(int)
    for (x4, b) in split_last(a4):
        if alternating([a1, a2, a3, x4]): res[b] ^= 1
    for (b, x1) in split_first(a1):
        if b[0] == 'id': continue          # already counted (b = id on both sides is the same term)
        if alternating([x1, a2, a3, a4]): res[b] ^= 1
    return {k: v for k, v in res.items() if v}
def disk6():
    out = set()
    for i in 'bc':
        j = OTHER[i]
        # cyclic word: D_i^2, S(i->j), D_j, S_j^2, D_j, S(j->i)
        w = [('D', i, 2), ('S', i, 1), ('D', j, 1), ('S', j, 2), ('D', j, 1), ('S', j, 1)]
        for r in range(6): out.add(tuple(w[r:] + w[:r]))
    return out
D6 = disk6()
def mu6(seq):
    res = defaultdict(int)
    seq = list(seq)
    # (a1..a5, a6 b)
    a6 = seq[5]
    cands = []
    if a6[0] != 'id':
        for n in range(1, a6[2] + 1):
            x6 = (a6[0], a6[1], n)
            b = ('id', end(a6)) if n == a6[2] else (a6[0], end(x6), a6[2] - n)
            cands.append((tuple(seq[:5] + [x6]), b))
    for s, b in cands:
        if s in D6: res[b] ^= 1
    a1 = seq[0]
    if a1[0] != 'id':
        for n in range(1, a1[2]):          # b nontrivial: b = a1^(a1[2]-n), x1 = power n
            b = (a1[0], a1[1], a1[2] - n)
            x1 = (a1[0], end(b), n)
            if tuple([x1] + seq[1:]) in D6: res[b] ^= 1
    return {k: v for k, v in res.items() if v}

class TypeD:
    def __init__(self, gens, arrows):
        self.gens = gens                      # list of (idem, h, q)
        self.arrows = list(arrows)            # (src, dst, alg, upow)
        for (s, t, a, u) in self.arrows:
            assert start(a) == gens[s][0] and end(a) == gens[t][0], (s, t, a)
            assert gens[t][1] == gens[s][1] + 1 + u and gens[t][2] == gens[s][2] + qdeg(a) + 3 * u, ('grading', s, t, a, u, gens[s], gens[t])
    def out(self, upow=None):
        o = defaultdict(list)
        for (s, t, a, u) in self.arrows:
            if upow is None or u == upow: o[s].append((t, a, u))
        return o
    def relation_terms(self, maxU=2, use6=True):
        """all terms of sum_k mu_k(delta^k) up to U-order maxU: dict (src, dst, alg, upow) -> 0/1"""
        o = self.out()
        terms = defaultdict(int)
        n = len(self.gens)
        for x in range(n):
            # k = 2
            for (y, a, u1) in o[x]:
                for (z, b, u2) in o[y]:
                    c = mul(a, b)
                    if c is not None and u1 + u2 <= maxU: terms[(x, z, c, u1 + u2)] ^= 1
            # k = 4
            for (y1, a1, u1) in o[x]:
                for (y2, a2, u2) in o[y1]:
                    for (y3, a3, u3) in o[y2]:
                        for (y4, a4, u4) in o[y3]:
                            if u1 + u2 + u3 + u4 + 2 > maxU: continue
                            for b, v in mu4(a1, a2, a3, a4).items():
                                terms[(x, y4, b, u1 + u2 + u3 + u4 + 2)] ^= 1
                            if use6 and maxU >= 4:
                                for (y5, a5, u5) in o[y4]:
                                    for (y6, a6, u6) in o[y5]:
                                        if u1 + u2 + u3 + u4 + u5 + u6 + 4 > maxU: continue
                                        for b, v in mu6((a1, a2, a3, a4, a5, a6)).items():
                                            terms[(x, y6, b, u1 + u2 + u3 + u4 + u5 + u6 + 4)] ^= 1
        return {k: v for k, v in terms.items() if v}

def alg_elements(i, j, maxdeg=12):
    """basis elements from idempotent i to j with q-degree <= maxdeg"""
    out = []
    if i == j:
        out.append(('id', i))
        for n in range(1, maxdeg // 2 + 1): out.append(('D', i, n))
        for n in range(2, maxdeg + 1, 2): out.append(('S', i, n))
    else:
        for n in range(1, maxdeg + 1, 2): out.append(('S', i, n))
    return out

def first_order(td, verbose=False):
    """Is there delta_2 (arrows carrying U^2) with  mu_2(d0,d2) + mu_2(d2,d0) + [mu_4(d0^4)]_{U^2} = 0 ?  returns (ok, solution arrows)"""
    assert all(u == 0 for (_, _, _, u) in td.arrows)
    base = td.relation_terms(maxU=2)
    assert all(k[3] == 2 for k in base), ('d0^2 != 0', [k for k in base if k[3] != 2])
    n = len(td.gens)
    # unknowns: (x, y, a) with gradings h(y) = h(x)+3, q(y) = q(x) + qdeg(a) + 6
    unknowns = []
    for x in range(n):
        for y in range(n):
            if td.gens[y][1] != td.gens[x][1] + 3: continue
            dq = td.gens[y][2] - td.gens[x][2] - 6
            if dq < 0: continue
            for a in alg_elements(td.gens[x][0], td.gens[y][0], dq):
                if qdeg(a) == dq: unknowns.append((x, y, a))
    idx = {u: i for i, u in enumerate(unknowns)}
    o0 = td.out(0)
    inc = defaultdict(list)
    for (s, t, a, u) in td.arrows: inc[t].append((s, a))
    rows = defaultdict(int)     # equation key -> bitmask of unknowns
    for (x, y, a) in unknowns:
        i = idx[(x, y, a)]
        # d2 then d0:  x -a U^2-> y -b-> z
        for (z, b, _) in o0[y]:
            c = mul(a, b)
            if c is not None: rows[(x, z, c)] ^= 1 << i
        # d0 then d2:  w -b-> x -a U^2-> y
        for (w, b) in inc[x]:
            c = mul(b, a)
            if c is not None: rows[(w, y, c)] ^= 1 << i
    rhs = {(k[0], k[1], k[2]): 1 for k in base}
    keys = set(rows) | set(rhs)
    # Gaussian elimination over F_2 on augmented rows
    N = len(unknowns)
    piv = {}
    ok = True
    for k in keys:
        v = rows.get(k, 0) | ((rhs.get(k, 0)) << N)
        while v:
            hb = (v & ((1 << N) - 1)).bit_length() - 1
            if hb < 0:
                ok = False; break         # 0 = 1
            if hb in piv: v ^= piv[hb]
            else: piv[hb] = v; break
        if not ok: break
    sol = None
    if ok:
        # back substitution: set free variables to 0
        val = {}
        for hb in sorted(piv):
            v = piv[hb]
            s = (v >> N) & 1
            m = v & ((1 << hb) - 1)
            b = 0
            while m:
                if m & 1: s ^= val.get(b, 0)
                m >>= 1; b += 1
            val[hb] = s
        sol = [unknowns[i] for i, s in val.items() if s]
    return ok, sol, len(unknowns), len(base)

# ---------- curves from move sequences ----------
def curve(moves, closed, h0=0, q0=0):
    """moves: list of ('D', a, s) | ('P', n, s) | ('T', m, s); returns TypeD (order 0)"""
    gens = [('b', h0, q0)]; arrows = []
    cur = 0
    def step(alg_first, nxt_idem, s):
        nonlocal cur
        # alg_first: the label written from the generator at which the ARROW starts
        _, h, q = gens[cur]
        a = alg_first
        gens.append((nxt_idem, h + s, q + s * qdeg(a)))
        new = len(gens) - 1
        if s == 1: arrows.append((cur, new, a, 0))
        else: arrows.append((new, cur, a, 0))
        cur = new
    for mv in moves:
        kind, n, s = mv
        if kind == 'D':
            step(('D', 'b', n), 'b', s)
        elif kind in ('P', 'T'):
            labels = ['S'] + ['D', 'S2'] * (n - 1) + ['D'] + (['S'] if kind == 'P' else [])
            idem = 'b'
            for L in labels:
                # determine label element as it starts from the tail of the arrow
                if L == 'S':
                    nxt = OTHER[idem]
                    a = ('S', idem, 1) if s == 1 else ('S', nxt, 1)
                elif L == 'D':
                    nxt = idem; a = ('D', idem, 1)
                else:
                    nxt = idem; a = ('S', idem, 2)
                step(a, nxt, s); idem = nxt
    if closed:
        last = len(gens) - 1
        if gens[last] != gens[0]: return None
        arrows = [(0 if s == last else s, 0 if t == last else t, a, u) for (s, t, a, u) in arrows]
        gens = gens[:-1]
    return TypeD(gens, arrows)

if __name__ == '__main__':
    # sanity: mu_4 values quoted in KWZ
    D, S = (lambda i, n=1: ('D', i, n)), (lambda i, n=1: ('S', i, n))
    print('mu4(D,S,D,S^2) =', mu4(D('b'), S('b'), D('c'), S('c', 2)), ' expect S')
    print('mu4(S^2,D,S,D) =', mu4(S('c', 2), D('c'), S('c'), D('b')), ' expect S (c->b ... first S from c to c? )')
    print('mu4(S,D,S,D)   =', mu4(S('b'), D('c'), S('c'), D('b')), ' expect id')
    print('mu4(S,D,S^2,D) =', mu4(S('b'), D('c'), S('c', 2), D('c')), ' expect 0')
    sq = curve([('P', 2, 1), ('D', 1, 1), ('P', 2, -1), ('D', 1, -1)], True)
    print('unit square: gens', len(sq.gens), ' first-order extension:', first_order(sq))
    ok, sol, _, _ = first_order(sq)
    ext = TypeD(sq.gens, sq.arrows + [(x, y, a, 2) for (x, y, a) in sol])
    print('  extended square satisfies the full relation up to U^4:', ext.relation_terms(maxU=4) == {})
    for name, mv, cl in [('zigzag l=2', [('P', 2, 1), ('D', 1, -1), ('P', 2, 1), ('D', 1, -1)], False),
                         ('3_1 arc with tail', [('P', 2, 1), ('D', 1, -1), ('T', 2, 1)], False),
                         ('arc D then P (composable)', [('D', 1, 1), ('P', 2, 1)], False),
                         ('arc P then D (composable)', [('P', 2, 1), ('D', 1, 1)], False),
                         ('arc D then tail (composable)', [('D', 1, 1), ('T', 2, 1)], False),
                         ('s2 square (P_1 legs)', [('P', 1, 1), ('D', 1, 1), ('P', 1, -1), ('D', 1, -1)], True),
                         ('s6 square (P_3 legs)', [('P', 3, 1), ('D', 1, 1), ('P', 3, -1), ('D', 1, -1)], True)]:
        td = curve(mv, cl)
        print(name, ':', None if td is None else first_order(td)[:2])
