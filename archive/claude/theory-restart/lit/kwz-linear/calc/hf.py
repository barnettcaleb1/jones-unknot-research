#!/usr/bin/env python3
"""
Bigraded morphism-space homology for type D structures over the KWZ algebra B (F_2 coefficients).

Conventions (from arXiv:2202.01460v1, Section 2.1 and Figure 15 inset):
  idempotents: 0 = bullet, 1 = circ
  algebra element = path: ('1', i) | ('D', i, k) | ('S', i, k), i = source idempotent
  gr(D) = q^-2 delta^-1, gr(S) = q^-1 delta^-1/2 ; differentials preserve q, lower delta by 1
  h = q/2 - delta.
We store 2*delta as an integer ("d2").
An arrow x --a--> y in a type D structure means d(x) contains y (x) a.
Mor(X,Y) has basis (x, y, b), b a path idem(x) -> idem(y), grading gr(y)+gr(b)-gr(x),
differential D(x,y,b) = sum_{y-c->z} (x,z,bc) + sum_{w-a->x} (w,y,ab).
"""
import sys
from collections import defaultdict
from fractions import Fraction

# ---------- algebra ----------
def src(b): return b[1]
def tgt(b):
    if b[0] in ('1', 'D'): return b[1]
    return b[1] ^ (b[2] & 1)
def mult(b, c):
    """b then c ; None if zero"""
    assert tgt(b) == src(c)
    if b[0] == '1': return c
    if c[0] == '1': return b
    if b[0] != c[0]: return None      # D.S = 0 = S.D
    return (b[0], b[1], b[2] + c[2])
def qgr(b):
    if b[0] == '1': return 0
    return -2 * b[2] if b[0] == 'D' else -b[2]
def d2gr(b):
    if b[0] == '1': return 0
    return -2 * b[2] if b[0] == 'D' else -b[2]

def paths(i, j, qmin):
    """all basis paths from idempotent i to j with q-grading >= qmin"""
    out = []
    if i == j:
        out.append(('1', i))
        k = 1
        while -2 * k >= qmin:
            out.append(('D', i, k)); k += 1
    k = 1
    while -k >= qmin:
        if (i ^ (k & 1)) == j:
            out.append(('S', i, k))
        k += 1
    return out

# ---------- type D structures ----------
class TypeD:
    def __init__(self, name, idem, arrows, base=0):
        """idem: list of idempotents; arrows: list of (x, y, element-spec) where element-spec is
        'D', 'S', 'S2', 'S3', ... (source idempotent inferred) ; arrows with several labels: list them separately."""
        self.name = name
        self.idem = list(idem)
        self.arrows = []
        for (x, y, lab) in arrows:
            if lab == 'D': a = ('D', self.idem[x], 1)
            elif lab[0] == 'D': a = ('D', self.idem[x], int(lab[1:]))
            elif lab == 'S': a = ('S', self.idem[x], 1)
            else: a = ('S', self.idem[x], int(lab[1:]))
            assert tgt(a) == self.idem[y], (name, x, y, lab)
            self.arrows.append((x, y, a))
        self.grade(base)
        self.check_d2()
    def grade(self, base):
        n = len(self.idem)
        q = [None] * n; d2 = [None] * n
        q[base] = 0; d2[base] = 0
        changed = True
        while changed:
            changed = False
            for (x, y, a) in self.arrows:
                # q(y) = q(x) - q(a) ; delta(y) = delta(x) - 1 - delta(a)
                if q[x] is not None:
                    qq, dd = q[x] - qgr(a), d2[x] - 2 - d2gr(a)
                    if q[y] is None: q[y], d2[y] = qq, dd; changed = True
                    else: assert (q[y], d2[y]) == (qq, dd), ("grading inconsistency", self.name)
                elif q[y] is not None:
                    q[x], d2[x] = q[y] + qgr(a), d2[y] + 2 + d2gr(a); changed = True
        assert all(v is not None for v in q), "disconnected"
        self.q, self.d2 = q, d2
    def check_d2(self):
        acc = defaultdict(int)
        out = defaultdict(list)
        for (x, y, a) in self.arrows: out[x].append((y, a))
        for (x, y, a) in self.arrows:
            for (z, c) in out[y]:
                m = mult(a, c)
                if m is not None: acc[(x, z, m)] ^= 1
        assert not any(acc.values()), ("d^2 != 0", self.name, {k: v for k, v in acc.items() if v})
    def shifted_copy(self):
        return self
    def klass(self):
        """K_0 class: dict idem -> {q: signed count}, sign (-1)^h, h = q/2 - delta (must be integer or uniformly half-integer)"""
        res = {0: defaultdict(int), 1: defaultdict(int)}
        for g in range(len(self.idem)):
            h2 = self.q[g] - self.d2[g]          # 2h
            res[self.idem[g]][(self.q[g])] += (h2,)[0] * 0 + (1 if (h2 // 2) % 2 == 0 else -1) if h2 % 2 == 0 else 0
        return res

def cone_H(X):
    """mapping cone [q^-1 d^1/2 X --H--> q^1 d^1/2 X], H = D + S^2 (both idempotents)"""
    n = len(X.idem)
    idem = X.idem + X.idem
    arrows = []
    lab = lambda a: ('D' + (str(a[2]) if a[2] > 1 else '')) if a[0] == 'D' else ('S' + (str(a[2]) if a[2] > 1 else ''))
    for (x, y, a) in X.arrows:
        arrows.append((x, y, lab(a))); arrows.append((x + n, y + n, lab(a)))
    for x in range(n):
        arrows.append((x, x + n, 'D')); arrows.append((x, x + n, 'S2'))
    return TypeD('Cone_H(' + X.name + ')', idem, arrows)

# ---------- linear algebra over F_2 (bitmask rows) ----------
def rank_f2(rows):
    rows = [r for r in rows if r]
    rank = 0
    piv = {}
    for r in rows:
        while r:
            hb = r.bit_length() - 1
            if hb in piv: r ^= piv[hb]
            else: piv[hb] = r; rank += 1; break
    return rank

def hf(X, Y, depth=None, verbose=False):
    """homology of Mor(X,Y) as dict {(q, d2): dim}. depth: how far below the top q-degree to compute."""
    qtop = max(Y.q) - min(X.q)
    qbot_gen = min(Y.q) - max(X.q)
    if depth is None: depth = (qtop - qbot_gen) + 12
    qmin_alg = (qtop - depth) - qtop - 2   # most negative algebra q needed (generous)
    qmin_alg = -(depth + (qtop - qbot_gen) + 4)
    basis = defaultdict(list)   # (q, d2) -> list of basis elements
    for x in range(len(X.idem)):
        for y in range(len(Y.idem)):
            for b in paths(X.idem[x], Y.idem[y], qmin_alg):
                q = Y.q[y] + qgr(b) - X.q[x]
                d2 = Y.d2[y] + d2gr(b) - X.d2[x]
                basis[(q, d2)].append((x, y, b))
    index = {k: {e: i for i, e in enumerate(v)} for k, v in basis.items()}
    Yout = defaultdict(list)
    for (y, z, c) in Y.arrows: Yout[y].append((z, c))
    Xin = defaultdict(list)
    for (w, x, a) in X.arrows: Xin[x].append((w, a))
    def diff(e):
        x, y, b = e
        out = defaultdict(int)
        for (z, c) in Yout[y]:
            m = mult(b, c)
            if m is not None: out[(x, z, m)] ^= 1
        for (w, a) in Xin[x]:
            m = mult(a, b)
            if m is not None: out[(w, y, m)] ^= 1
        return [k for k, v in out.items() if v]
    res = {}
    for q in range(qtop, qtop - depth - 1, -1):
        d2s = sorted({k[1] for k in basis if k[0] == q})
        ranks = {}
        for d2 in d2s:
            tgt_idx = index.get((q, d2 - 2), {})
            rows = []
            for e in basis[(q, d2)]:
                r = 0
                for f in diff(e):
                    r |= 1 << tgt_idx[f]
                rows.append(r)
            ranks[d2] = rank_f2(rows)
        for d2 in d2s:
            dim = len(basis[(q, d2)]) - ranks[d2] - ranks.get(d2 + 2, 0)
            if dim: res[(q, d2)] = dim
    return res

def report(res, label=''):
    """print generators as (q, h, delta) relative to the lowest-q (then lowest h) generator; Euler char."""
    gens = []
    for (q, d2), dim in sorted(res.items()):
        h2 = q - d2
        gens += [(q, Fraction(h2, 2), Fraction(d2, 2))] * dim
    if not gens:
        print(f"{label}: HF = 0"); return
    gens.sort()
    q0, h0, d0 = gens[0]
    rel = [(q - q0, h - h0, d - d0) for (q, h, d) in gens]
    chi = defaultdict(int)
    for (q, h, d) in rel:
        assert h.denominator == 1
        chi[q] += (-1) ** int(h)
    chis = ' '.join(f"{'+' if c > 0 else '-'}{abs(c) if abs(c) != 1 else ''}q^{q}" for q, c in sorted(chi.items()) if c)
    deltas = sorted({d for (_, _, d) in rel})
    print(f"{label}: dim={len(gens)}  delta-values(rel)={[str(d) for d in deltas]}  thin={len(deltas)==1}")
    print("    (q,h,delta) rel: " + ' '.join(f"({q},{h},{d})" for (q, h, d) in rel))
    print(f"    chi = {chis if chis else '0'}   [#terms abs-sum = {sum(abs(c) for c in chi.values())}]")
    return rel, dict(chi)

# ---------- the curves ----------
def arc0():   return TypeD('a(0)', [0], [])
def arcinf(): return TypeD('a(inf)', [1], [])
def arc_int(n):
    """a(n), n integer != 0, read off in the cover (derived): segment from (0,1) to (1,1+n).
       n<0: [b -S-> c -D-> c -S2-> c ...] (|n| circ's, arrows away from bullet); n>0: all arrows reversed."""
    m = abs(n)
    idem = [0] + [1] * m
    arrows = []
    labs = ['S'] + [('D' if i % 2 == 1 else 'S2') for i in range(1, m)]
    for i in range(m):
        if n < 0: arrows.append((i, i + 1, labs[i]))
        else:     arrows.append((i + 1, i, labs[i]))
    return TypeD(f'a({n})', idem, arrows)
def swap(X, name=None):
    lab = lambda a: ('D' + (str(a[2]) if a[2] > 1 else '')) if a[0] == 'D' else ('S' + (str(a[2]) if a[2] > 1 else ''))
    return TypeD(name or ('swap ' + X.name), [1 - i for i in X.idem], [(x, y, lab(a)) for (x, y, a) in X.arrows])
def arc_inv(n):
    """a(1/n) for n>0 = swap(a(-n)); a(-1/n) = swap(a(n))  (rotation by 90 degrees: slope s -> -1/s)"""
    return swap(arc_int(-n), f'a(1/{n})') if n > 0 else swap(arc_int(-n), f'a(-1/{-n})')

def r_curve(n):
    """r_n(0): Lemma 5.5 of the paper. source 0, sink 2n-1 ... """
    if n == 1:
        return TypeD('r_1(0)', [0, 0], [(0, 1, 'D'), (0, 1, 'S2')])
    idem = [0] * (2 * n)
    # generators: 0 = source, 1..n-1 top chain, n..2n-2 bottom chain, 2n-1 = sink
    top = [0] + list(range(1, n)) + [2 * n - 1]
    bot = [0] + list(range(n, 2 * n - 1)) + [2 * n - 1]
    arrows = []
    for i in range(n):
        arrows.append((top[i], top[i + 1], 'D' if i % 2 == 0 else 'S2'))
        arrows.append((bot[i], bot[i + 1], 'S2' if i % 2 == 0 else 'D'))
    return TypeD(f'r_{n}(0)', idem, arrows)

def s_curve(n):
    """s_2n(0): proof of Theorem 5.1 of the paper. Two rows  c -S-> b -D-> b -S2-> ... -D-> b -S-> c ; D between row ends."""
    L = 2 * n + 2
    idem = ([1] + [0] * (2 * n) + [1]) * 2
    arrows = []
    for r in range(2):
        o = r * L
        arrows.append((o, o + 1, 'S'))
        for i in range(1, 2 * n):
            arrows.append((o + i, o + i + 1, 'D' if i % 2 == 1 else 'S2'))
        arrows.append((o + 2 * n, o + 2 * n + 1, 'S'))
    arrows.append((0, L, 'D'))
    arrows.append((L - 1, 2 * L - 1, 'D'))
    return TypeD(f's_{2*n}(0)', idem, arrows)

if __name__ == '__main__':
    print("== sanity: reduced Khovanov homology of 2-bridge closures via HF(arc, Cone_H(arc)) ==")
    for n in (1, 2, 3, 4, 5):
        for sgn in (-1, 1):
            report(hf(arc0(), cone_H(arc_int(sgn * n))), f"HF(a(0), Kh(Q_{sgn*n}))")
    report(hf(arcinf(), cone_H(arc_int(-3))), "HF(a(inf), Kh(Q_-3))")
    report(hf(arc0(), cone_H(arc0())), "HF(a(0), Kh(Q_0))")
