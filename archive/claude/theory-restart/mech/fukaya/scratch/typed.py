#!/usr/bin/env python3
"""Type D structures over the Bar-Natan/KWZ quiver algebra B, coefficients F_2.

Idempotents: 0 = bullet (kht++ '⬮', the idempotent of a(0) = BN(Q_0)), 1 = circ ('⬯', idempotent of a(inf)).
Algebra basis elements (paths): ('1', i) ; ('D', i, n) n>=1 (loop at i) ; ('S', i, n) n>=1 (starts at i, alternates).
Relations D.S = 0 = S.D.  gr(D^n) = q^{-2n} h^0, gr(S^n) = q^{-n} h^0.  H = D + S^2 (central), gr H = q^{-2}.
A type D structure: generators with idempotent and bigrading (q, h); differential arrows x --a--> y, meaning
delta(x) contains y (x) a, with a a path from idem(x) to idem(y);  q(y) = q(x) - q(a), h(y) = h(x) + 1.
Mor(X, Y): basis (x, y, b), b a path idem(x) -> idem(y); bidegree (q(y) + q(b) - q(x), h(y) - h(x)).
d(x, y, b) = sum_{y --c--> z} (x, z, b c) + sum_{w --a--> x} (w, y, a b).   (char 2)
HF(X, Y) := H_*(Mor(X, Y)) (arXiv:2602.23442 Thm 2.38).
"""
import itertools, random
from collections import defaultdict

def src(b): return b[1]
def tgt(b):
    if b[0] in ('1', 'D'): return b[1]
    return b[1] ^ (b[2] & 1)
def mult(b, c):
    assert tgt(b) == src(c), (b, c)
    if b[0] == '1': return c
    if c[0] == '1': return b
    if b[0] != c[0]: return None
    return (b[0], b[1], b[2] + c[2])
def qgr(b):
    if b[0] == '1': return 0
    return -2 * b[2] if b[0] == 'D' else -b[2]
def paths(i, j, qmin):
    out = []
    if i == j:
        out.append(('1', i))
        n = 1
        while -2 * n >= qmin: out.append(('D', i, n)); n += 1
    n = 1
    while -n >= qmin:
        if (i ^ (n & 1)) == j: out.append(('S', i, n))
        n += 1
    return out
def lab2elt(lab, i):
    if lab == '1': return ('1', i)
    k = lab[0]; n = int(lab[1:] or 1)
    return (k, i, n)
def elt2lab(a):
    if a[0] == '1': return '1'
    return a[0] + (str(a[2]) if a[2] > 1 else '')

class TypeD:
    def __init__(self, name, idem, arrows, q=None, h=None, base=0, baseq=0, baseh=0):
        """arrows: list of (x, y, label) with label 'D','D2','S','S2',...  If q,h not given, they are propagated from
        generator `base` placed at (baseq, baseh); components not connected to base get (0,0) at their first generator."""
        self.name = name; self.idem = list(idem)
        self.arrows = []
        for (x, y, lab) in arrows:
            a = lab2elt(lab, self.idem[x]) if isinstance(lab, str) else lab
            assert src(a) == self.idem[x] and tgt(a) == self.idem[y], (name, x, y, lab)
            self.arrows.append((x, y, a))
        n = len(self.idem)
        if q is not None:
            self.q = list(q); self.h = list(h)
        else:
            self.q = [None] * n; self.h = [None] * n
            self.q[base] = baseq; self.h[base] = baseh
            self._propagate()
        self.check()
    def _propagate(self):
        n = len(self.idem)
        while True:
            changed = True
            while changed:
                changed = False
                for (x, y, a) in self.arrows:
                    if self.q[x] is not None and self.q[y] is None:
                        self.q[y] = self.q[x] - qgr(a); self.h[y] = self.h[x] + 1; changed = True
                    elif self.q[y] is not None and self.q[x] is None:
                        self.q[x] = self.q[y] + qgr(a); self.h[x] = self.h[y] - 1; changed = True
            rest = [i for i in range(n) if self.q[i] is None]
            if not rest: break
            self.q[rest[0]] = 0; self.h[rest[0]] = 0
    def check(self):
        for (x, y, a) in self.arrows:
            assert self.q[y] == self.q[x] - qgr(a) and self.h[y] == self.h[x] + 1, ('grading', self.name, x, y, a)
        acc = defaultdict(int); out = defaultdict(list)
        for (x, y, a) in self.arrows: out[x].append((y, a))
        for (x, y, a) in self.arrows:
            for (z, c) in out[y]:
                m = mult(a, c)
                if m is not None: acc[(x, z, m)] ^= 1
        bad = {k: v for k, v in acc.items() if v}
        assert not bad, ('d^2 != 0', self.name, bad)
    def shift(self, dq, dh, name=None):
        return TypeD(name or f'q^{dq}h^{dh} {self.name}', self.idem, self.arrows, [x + dq for x in self.q], [x + dh for x in self.h])
    def __len__(self): return len(self.idem)
    def klass(self):
        """K_0 class: (poly_bullet, poly_circ), each dict q -> coefficient, sum (-1)^h q^q."""
        res = [defaultdict(int), defaultdict(int)]
        for g in range(len(self.idem)):
            res[self.idem[g]][self.q[g]] += -1 if self.h[g] % 2 else 1
        return tuple({k: v for k, v in sorted(r.items()) if v} for r in res)
    def meanq(self):
        from fractions import Fraction
        return Fraction(sum(self.q), len(self.q))
    def show(self):
        s = self.name + ': ' + ' '.join(f"{i}{'bc'[self.idem[i]]}(q{self.q[i]},h{self.h[i]})" for i in range(len(self.idem)))
        s += ' | ' + ' '.join(f"{x}-{elt2lab(a)}>{y}" for (x, y, a) in self.arrows)
        return s

def dsum(name, *Xs):
    idem = []; arrows = []; q = []; h = []
    for X in Xs:
        o = len(idem)
        idem += X.idem; q += X.q; h += X.h
        arrows += [(x + o, y + o, a) for (x, y, a) in X.arrows]
    return TypeD(name, idem, arrows, q, h)

def cone_H(X, name=None):
    """Cone(H.1_X) = [q^-1 h^-1 X --H--> q^1 h^0 X]"""
    n = len(X.idem)
    idem = X.idem + X.idem
    q = [v - 1 for v in X.q] + [v + 1 for v in X.q]
    h = [v - 1 for v in X.h] + [v for v in X.h]
    arrows = []
    for (x, y, a) in X.arrows:
        arrows.append((x, y, a)); arrows.append((x + n, y + n, a))
    for x in range(n):
        arrows.append((x, x + n, ('D', X.idem[x], 1))); arrows.append((x, x + n, ('S', X.idem[x], 2)))
    return TypeD(name or f'Cone_H({X.name})', idem, arrows, q, h)

def cone(f_arrows, X, Y, name=None):
    """Cone of a morphism given by arrows (x in X, y in Y, label/elt): complex X' (+) Y with extra arrows x -> y.
    X is taken with the gradings it has; the caller must have shifted X so that the arrows have degree (0, +1)."""
    n = len(X.idem)
    idem = X.idem + Y.idem
    arrows = list(X.arrows) + [(x + n, y + n, a) for (x, y, a) in Y.arrows]
    for (x, y, a) in f_arrows:
        a = lab2elt(a, X.idem[x]) if isinstance(a, str) else a
        arrows.append((x, y + n, a))
    return TypeD(name or 'Cone', idem, arrows, X.q + Y.q, X.h + Y.h)

def cancel(X, name=None):
    """Cancel all identity-labelled arrows (Gaussian elimination, char 2). Returns a reduced TypeD (may be non-curve-like)."""
    idem = list(X.idem); q = list(X.q); h = list(X.h)
    arr = defaultdict(int)
    for (x, y, a) in X.arrows: arr[(x, y, a)] ^= 1
    alive = set(range(len(idem)))
    while True:
        piv = None
        for (x, y, a), v in arr.items():
            if v and a[0] == '1': piv = (x, y); break
        if piv is None: break
        x0, y0 = piv
        ins = [(w, a) for (w, y, a), v in arr.items() if v and y == y0 and w != x0]
        outs = [(z, c) for (x, z, c), v in arr.items() if v and x == x0 and z != y0]
        for (w, a) in ins:
            for (z, c) in outs:
                m = mult(a, c)
                if m is not None: arr[(w, z, m)] ^= 1
        for k in list(arr.keys()):
            if k[0] in (x0, y0) or k[1] in (x0, y0): del arr[k]
        alive -= {x0, y0}
    keep = sorted(alive); idx = {g: i for i, g in enumerate(keep)}
    arrows = [(idx[x], idx[y], a) for (x, y, a), v in arr.items() if v]
    return TypeD(name or X.name + '~', [idem[g] for g in keep], arrows, [q[g] for g in keep], [h[g] for g in keep])

# ---------------- linear algebra over F_2 ----------------
def rank_f2(rows):
    piv = {}; rank = 0
    for r in rows:
        while r:
            hb = r.bit_length() - 1
            if hb in piv: r ^= piv[hb]
            else: piv[hb] = r; rank += 1; break
    return rank

def mor_basis(X, Y, qlo, qhi):
    """basis of Mor(X,Y) with q-degree in [qlo, qhi], grouped by (q, h)."""
    basis = defaultdict(list)
    for x in range(len(X.idem)):
        for y in range(len(Y.idem)):
            base = Y.q[y] - X.q[x]
            if base < qlo: continue
            for b in paths(X.idem[x], Y.idem[y], qlo - base):
                qq = base + qgr(b)
                if qlo <= qq <= qhi: basis[(qq, Y.h[y] - X.h[x])].append((x, y, b))
    return basis

def mor_diff(X, Y):
    Yout = defaultdict(list); Xin = defaultdict(list)
    for (y, z, c) in Y.arrows: Yout[y].append((z, c))
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
    return diff

def hf(X, Y, qlo=None, qhi=None):
    """dict (q, h) -> dim of H_*(Mor(X,Y)) for q in [qlo, qhi] (exact in that window: the differential preserves q)."""
    top = max(Y.q) - min(X.q)
    if qhi is None: qhi = top
    if qlo is None: qlo = min(Y.q) - max(X.q) - 14
    basis = mor_basis(X, Y, qlo, qhi)
    index = {k: {e: i for i, e in enumerate(v)} for k, v in basis.items()}
    diff = mor_diff(X, Y)
    rk = {}
    for (qq, hh), els in basis.items():
        tidx = index.get((qq, hh + 1), {})
        rows = []
        for e in els:
            r = 0
            for f in diff(e): r |= 1 << tidx[f]
            rows.append(r)
        rk[(qq, hh)] = rank_f2(rows)
    res = {}
    for (qq, hh), els in basis.items():
        d = len(els) - rk[(qq, hh)] - rk.get((qq, hh - 1), 0)
        if d: res[(qq, hh)] = d
    return res

def chain_maps(X, Y, dq=0, dh=0):
    """basis of the space of cycles in Mor(X,Y) of bidegree (dq, dh) (list of lists of basis elements)."""
    basis = mor_basis(X, Y, dq, dq)
    els = basis.get((dq, dh), [])
    tels = basis.get((dq, dh + 1), [])
    tidx = {e: i for i, e in enumerate(tels)}
    diff = mor_diff(X, Y)
    # kernel computation: rows = (image bits, identity bits)
    rows = []
    for i, e in enumerate(els):
        r = 0
        for f in diff(e): r |= 1 << tidx[f]
        rows.append((r, 1 << i))
    piv = {}; ker = []
    for r, tag in rows:
        while r:
            hb = r.bit_length() - 1
            if hb in piv:
                pr, pt = piv[hb]; r ^= pr; tag ^= pt
            else:
                piv[hb] = (r, tag); break
        if not r: ker.append(tag)
    return els, ker

def is_isomorphic(X, Y, tries=400, seed=1):
    """Search for an isomorphism of reduced type D structures X -> Y: a degree (0,0) cycle f in Mor(X,Y) whose
    identity-labelled part f_0 is invertible. Returns (True, f) or (False, None). Randomised over the cycle space."""
    if len(X) != len(Y): return False, None
    if sorted(zip(X.idem, X.q, X.h)) != sorted(zip(Y.idem, Y.q, Y.h)): return False, None
    els, ker = chain_maps(X, Y, 0, 0)
    if not ker: return False, None
    rnd = random.Random(seed)
    n = len(X)
    def f0_rank(tag):
        rows = [0] * n
        for i, e in enumerate(els):
            if (tag >> i) & 1 and e[2][0] == '1': rows[e[0]] |= 1 << e[1]
        return rank_f2(rows)
    cands = [0]
    for t in range(tries):
        tag = 0
        for k in ker:
            if rnd.random() < 0.5: tag ^= k
        if f0_rank(tag) == n:
            return True, [els[i] for i in range(len(els)) if (tag >> i) & 1]
    # try also the sum of all
    tag = 0
    for k in ker: tag ^= k
    if f0_rank(tag) == n: return True, [els[i] for i in range(len(els)) if (tag >> i) & 1]
    return False, None

# ---------------- standard objects (current kht++ conventions) ----------------
def chain(name, word, baseq=0, baseh=0, base=0, cyclic=False):
    """word like 'b-S>c-D>c-S2>c<D-c' ; cyclic words end with an arrow token."""
    import re
    toks = re.findall(r'[bc]|-[SD]\d*>|<[SD]\d*-', word)
    idem = [0 if t == 'b' else 1 for t in toks if t in 'bc']
    arrs = [t for t in toks if t not in 'bc']
    n = len(idem); arrows = []
    assert len(arrs) == (n if cyclic else n - 1), (word, len(arrs), n)
    for i, t in enumerate(arrs):
        j = (i + 1) % n
        if t.startswith('-'): arrows.append((i, j, t[1:-1]))
        else: arrows.append((j, i, t[1:-1]))
    return TypeD(name, idem, arrows, base=base, baseq=baseq, baseh=baseh)

ROW = 'b-S>c-D>c-S2>c-D>c-S>b'
def row(m=2):
    """special row arc R_m: b S c D c (S2 c D c)^{m-1} S b  (from a lift of the BL puncture to the next-but-(m-1) one along the special line of slope infinity)"""
    w = 'b-S>c-D>c' + '-S2>c-D>c' * (m - 1) + '-S>b'
    return chain(f'R_{m}', w)
def special(m=2):
    """s_{2m}(infinity) in kht++/2602.23442 indexing: two rows joined by D's (cyclic). m=2: the 12-generator s4."""
    fwd = 'b-S>c-D>c' + '-S2>c-D>c' * (m - 1) + '-S>b'
    bwd = 'b<S-c<D-c' + '<S2-c<D-c' * (m - 1) + '<S-b'
    return chain(f's{2*m}(inf)', fwd + '-D>' + bwd + '<D-', cyclic=True)
def arc(k):
    """a(k), k integer: k<0: b-S>c-D>c-S2>c-...(|k| c's); k>0: arrows reversed (pointing to b); generator 0 is b."""
    if k == 0: return chain('a(0)', 'b')
    m = abs(k)
    labs = ['S'] + [('D' if i % 2 == 1 else 'S2') for i in range(1, m)]
    w = 'b'
    for l in labs:
        w += (f'-{l}>c' if k < 0 else f'<{l}-c')
    return chain(f'a({k})', w)
def rat(k):
    return cone_H(arc(k), f'r1({k})')

if __name__ == '__main__':
    S = special(2); print(S.show()); print(len(S))
    R = row(2); print(R.show())
    for k in (-4, 0, 4): print(arc(k).show())
    print(cone_H(arc(0)).show())
