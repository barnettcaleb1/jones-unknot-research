"""Type D structures over the KWZ quiver algebra B, coefficients F_2.
Idempotents: 'b' (kht++ ⬮, slope 0, KWZ bullet) and 'c' (kht++ ⬯, slope infinity, KWZ circle).
Algebra basis elements (as maps source idempotent -> target idempotent):
   ('1', s)        identity at s
   ('D', s, k)     D_s^k, k>=1 (s -> s)
   ('S', s, k)     S^k starting at s, k>=1 (s -> s if k even, other(s) if k odd)
Relations: D S = S D = 0.  q-degree: D^k -> -2k, S^k -> -k.  All of homological degree 0.
A type D structure: list gens of (idem, h, q); differential dict i -> list of (j, alg) meaning d(x_i) contains alg * x_j,
with h(j) = h(i)+1 and q(j) = q(i) - qdeg(alg)   (arrow x --a--> y:  q(y) = q(x) + |q(a)|).
Morphism (i, j, a): x_i |-> a * y_j, bidegree (h(y_j)-h(x_i), q(y_j)-q(x_i)+qdeg(a)).
"""
import re
from itertools import product
OTHER = {'b': 'c', 'c': 'b'}

def src(a): return a[1]
def tgt(a):
    if a[0] == 'S' and a[2] % 2 == 1: return OTHER[a[1]]
    return a[1]
def qdeg(a):
    if a[0] == '1': return 0
    if a[0] == 'D': return -2 * a[2]
    return -a[2]
def mul(b2, a):
    """b2 after a (a first). returns element or None (zero)."""
    if tgt(a) != src(b2): return None
    if a[0] == '1': return b2
    if b2[0] == '1': return a
    if a[0] != b2[0]: return None
    return (a[0], a[1], a[2] + b2[2])
def elems(s, t, qd):
    """basis of iota_t B iota_s in q-degree qd (qd <= 0)."""
    out = []
    if qd > 0: return out
    if s == t:
        if qd == 0: out.append(('1', s))
        elif qd % 2 == 0:
            out.append(('D', s, -qd // 2)); out.append(('S', s, -qd))
    else:
        if qd % 2 == 1 or (-qd) % 2 == 1: out.append(('S', s, -qd))
    return out

class TD:
    def __init__(self, gens, d):
        self.gens = list(gens)           # (idem, h, q)
        self.d = {i: list(d.get(i, [])) for i in range(len(self.gens))}
    def check(self):
        for i, lst in self.d.items():
            for (j, a) in lst:
                assert src(a) == self.gens[i][0] and tgt(a) == self.gens[j][0], (i, j, a)
                assert self.gens[j][1] == self.gens[i][1] + 1, ('h', i, j)
                assert self.gens[j][2] == self.gens[i][2] - qdeg(a), ('q', i, j, a)
        # d^2 = 0
        for i, lst in self.d.items():
            acc = {}
            for (j, a) in lst:
                for (k, b2) in self.d[j]:
                    m = mul(b2, a)
                    if m is not None:
                        acc[(k, m)] = acc.get((k, m), 0) ^ 1
            assert not any(acc.values()), ('d^2', i, acc)
        return True
    def shift(self, dh=0, dq=0):
        return TD([(g[0], g[1] + dh, g[2] + dq) for g in self.gens], self.d)
    def mirror(self):
        """KWZ mirror: reverse arrows, negate gradings, exchange S_b and S_c (i.e. keep the idempotents, reverse paths)."""
        gens = [(g[0], -g[1], -g[2]) for g in self.gens]
        d = {}
        for i, lst in self.d.items():
            for (j, a) in lst:
                if a[0] == '1': ra = a
                elif a[0] == 'D': ra = a
                else: ra = ('S', tgt(a), a[2])
                d.setdefault(j, []).append((i, ra))
        return TD(gens, d)

def dsum(*tds):
    gens = []; d = {}; off = 0
    for t in tds:
        for i, g in enumerate(t.gens): gens.append(g)
        for i, lst in t.d.items():
            d[i + off] = [(j + off, a) for (j, a) in lst]
        off += len(t.gens)
    return TD(gens, d)

def cone_H(X):
    """Kh-type complex: [h^-1 q^-1 X --H--> q^{+1} X], H = D + S^2 (char 2) on each generator."""
    n = len(X.gens)
    gens = [(g[0], g[1] - 1, g[2] - 1) for g in X.gens] + [(g[0], g[1], g[2] + 1) for g in X.gens]
    d = {}
    for i, lst in X.d.items():
        d[i] = [(j, a) for (j, a) in lst] + [(i + n, ('D', X.gens[i][0], 1)), (i + n, ('S', X.gens[i][0], 2))]
        d[i + n] = [(j + n, a) for (j, a) in lst]
    return TD(gens, d)

# ---------- morphism complexes ----------
def mor_basis(X, Y, hh, qq):
    out = []
    for i, gx in enumerate(X.gens):
        for j, gy in enumerate(Y.gens):
            if gy[1] - gx[1] != hh: continue
            qd = qq - (gy[2] - gx[2])
            for a in elems(gx[0], gy[0], qd):
                out.append((i, j, a))
    return out

def mor_diff(X, Y, f):
    """boundary of basis morphism f=(i,j,a): d_Y o f + f o d_X ; returns dict of basis elts -> 1 (mod 2)."""
    i, j, a = f
    acc = {}
    for (j2, b2) in Y.d[j]:
        m = mul(b2, a)
        if m is not None:
            key = (i, j2, m); acc[key] = acc.get(key, 0) ^ 1
    for i0, lst in X.d.items():
        for (i1, b2) in lst:
            if i1 == i:
                m = mul(a, b2)
                if m is not None:
                    key = (i0, j, m); acc[key] = acc.get(key, 0) ^ 1
    return {k for k, v in acc.items() if v}

def compose(X, Y, Z, g, f):
    """g o f for chains (sets of basis morphisms) f: X->Y, g: Y->Z (mod 2). returns set."""
    acc = {}
    for (i, j, a) in f:
        for (j2, k, b2) in g:
            if j2 != j: continue
            m = mul(b2, a)
            if m is not None:
                key = (i, k, m); acc[key] = acc.get(key, 0) ^ 1
    return {k for k, v in acc.items() if v}

# ---------- F_2 linear algebra with python ints ----------
def rref(rows):
    """rows: list of ints (bit vectors). returns list of (pivot_bit, row) reduced."""
    piv = {}
    for r in rows:
        while r:
            p = r.bit_length() - 1
            if p in piv: r ^= piv[p]
            else: piv[p] = r; break
    return piv
def reduce(piv, r):
    while r:
        p = r.bit_length() - 1
        if p in piv: r ^= piv[p]
        else: return r
    return 0

class MorSpace:
    """graded piece (hh,qq) of Mor(X,Y) with cycles, boundaries, homology."""
    def __init__(self, X, Y, hh, qq):
        self.X, self.Y, self.hh, self.qq = X, Y, hh, qq
        self.B0 = mor_basis(X, Y, hh, qq)
        self.Bm = mor_basis(X, Y, hh - 1, qq)
        self.Bp = mor_basis(X, Y, hh + 1, qq)
        self.i0 = {b: n for n, b in enumerate(self.B0)}
        self.ip = {b: n for n, b in enumerate(self.Bp)}
        # boundaries: images of Bm
        self.bd_rows = [self.vec(mor_diff(X, Y, f)) for f in self.Bm]
        self.bd = rref(self.bd_rows)
        # cycles: kernel of d on B0
        self._cycles = None
    def vec(self, s):
        v = 0
        for b in s: v |= 1 << self.i0[b]
        return v
    def vecp(self, s):
        v = 0
        for b in s: v |= 1 << self.ip[b]
        return v
    def unvec(self, v):
        return {self.B0[n] for n in range(len(self.B0)) if (v >> n) & 1}
    def cycles(self):
        if self._cycles is None:
            # kernel computation: augment
            n = len(self.B0)
            piv = {}
            ker = []
            for idx, f in enumerate(self.B0):
                img = self.vecp(mor_diff(self.X, self.Y, f))
                tag = 1 << idx
                r = img
                while r:
                    p = r.bit_length() - 1
                    if p in piv:
                        r ^= piv[p][0]; tag ^= piv[p][1]
                    else:
                        piv[p] = (r, tag); break
                if r == 0: ker.append(tag)
            self._cycles = ker
        return self._cycles
    def is_boundary(self, s):
        return reduce(self.bd, self.vec(s)) == 0
    def homology_basis(self):
        """list of cycle vectors (ints) representing a basis of homology."""
        piv = dict(self.bd)
        out = []
        for c in self.cycles():
            r = reduce(piv, c)
            if r:
                piv[r.bit_length() - 1] = r
                out.append(c)
        return out
    def dim(self):
        return len(self.homology_basis())

def hom_table(X, Y, hrange, qrange):
    t = {}
    for hh in hrange:
        for qq in qrange:
            dm = MorSpace(X, Y, hh, qq).dim()
            if dm: t[(hh, qq)] = dm
    return t

def central(X, name):
    """c * id_X for central c in {'Db','Dc','S2','H'} as a set of basis morphisms."""
    s = set()
    for i, g in enumerate(X.gens):
        if name in ('Db', 'H') and g[0] == 'b': s ^= {(i, i, ('D', 'b', 1))}
        if name in ('Dc', 'H') and g[0] == 'c': s ^= {(i, i, ('D', 'c', 1))}
        if name in ('S2', 'H'): s ^= {(i, i, ('S', g[0], 2))}
    return s

# ---------- parsing kht++ chains ----------
SYM = {'⬮': 'b', '⬯': 'c'}
def parse_chain(h, q, chain, swap=False):
    """chain string like '⬮~~S~>⬯—>⬯~>⬯...' ; cyclic if number of arrows == number of generators.
    swap=True exchanges idempotent symbols (old website convention)."""
    toks = re.findall(r'[⬮⬯]|[^⬮⬯]+', chain)
    gs = [t for t in toks if t in SYM]; ar = [t for t in toks if t not in SYM]
    idem = [SYM[g] for g in gs]
    if swap: idem = [OTHER[x] for x in idem]
    n = len(gs)
    hq = [(h, q)]
    arrows = []
    for i, a in enumerate(ar):
        l = i; r = (i + 1) % n
        direction = +1 if a.endswith('>') else -1
        m = re.search(r'([SDH])(?:\^(\d+))?', a)
        if m: kind = m.group(1); p = int(m.group(2) or 1)
        else:
            kind = 'S' if '~' in a else 'D'; p = 1
            if kind == 'S' and idem[l] == idem[r]: p = 2
        deg = p if kind == 'S' else 2 * p
        if i < n - 1:
            hq.append((hq[-1][0] + direction, hq[-1][1] + direction * deg))
        else:
            assert (hq[-1][0] + direction, hq[-1][1] + direction * deg) == hq[0], 'cyclic chain does not close'
        s_, t_ = (l, r) if direction == 1 else (r, l)
        if kind == 'D': alg = ('D', idem[s_], p)
        else: alg = ('S', idem[s_], p)
        arrows.append((s_, t_, alg))
    gens = [(idem[i], hq[i][0], hq[i][1]) for i in range(n)]
    d = {}
    for (s_, t_, alg) in arrows: d.setdefault(s_, []).append((t_, alg))
    X = TD(gens, d); X.check()
    return X
