#!/usr/bin/env python3
"""Referee tool: pointed, deformed (Batson-Seed) Khovanov complex over F_2, written from scratch.

Diagram input: a kht++-style Morse word (top to bottom): x<i>/y<i> crossings (x: over-strand from top-left to
bottom-right; y: over-strand from top-right to bottom-left), l<i>/r<i> caps, u<i> cups; i = position of the left strand.
ntop = number of top ends; after the word some bottom ends remain; `joins` closes the diagram up:
a list of pairs of end names 't0','t1',... (top ends, left to right) and 'b0','b1',... (bottom ends left to right).
Marked points: end names (the edge through that end carries the marked point).

Conventions (standard Khovanov/Bar-Natan):
  0-smoothing = A-smoothing; for x it joins top-left to top-right ("horizontal"), for y top-left to bottom-left ("vertical").
  h = r - n_-,  q = (#1 - #x) + r + n_+ - 2 n_-,  l = h - q.   d_0: forward saddles; d_1: backward saddles at mixed crossings.
"""
import sys, collections

SLOTPOS = {'NW': (-1, 1), 'NE': (1, 1), 'SW': (-1, -1), 'SE': (1, -1)}
OPP = {'NW': 'SE', 'SE': 'NW', 'NE': 'SW', 'SW': 'NE'}


class UF:
    def __init__(self):
        self.p = {}
    def new(self, x):
        self.p[x] = x
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if a > b: a, b = b, a
            self.p[b] = a


class Diagram:
    def __init__(self, word, ntop, joins, marks):
        toks = [t for t in word.strip().split('.') if t]
        uf = UF(); nseg = 0
        strands = []
        for i in range(ntop):
            uf.new(nseg); strands.append(nseg); nseg += 1
        top = list(strands)
        cr = []  # (type, segNW, segNE, segSW, segSE)
        for t in toks:
            typ, i = t[0], int(t[1:])
            if typ in 'lr':
                assert 0 <= i <= len(strands), (t, len(strands))
                uf.new(nseg); strands[i:i] = [nseg, nseg]; nseg += 1
            elif typ == 'u':
                assert i + 1 < len(strands), (t, len(strands))
                uf.union(strands[i], strands[i + 1]); del strands[i:i + 2]
            elif typ in 'xy':
                assert i + 1 < len(strands), (t, len(strands))
                a, b = strands[i], strands[i + 1]
                uf.new(nseg); c = nseg; nseg += 1
                uf.new(nseg); d = nseg; nseg += 1
                strands[i], strands[i + 1] = c, d
                cr.append((typ, a, b, c, d))
            else:
                raise ValueError(t)
        bottom = list(strands)
        ends = {('t%d' % i): s for i, s in enumerate(top)}
        ends.update({('b%d' % i): s for i, s in enumerate(bottom)})
        used = set()
        for a, b in joins:
            uf.union(ends[a], ends[b]); used.add(a); used.add(b)
        assert used == set(ends), ('open ends left', set(ends) - used)
        # canonical edge ids
        roots = sorted({uf.find(s) for s in range(nseg)})
        eid = {r: k for k, r in enumerate(roots)}
        E = lambda s: eid[uf.find(s)]
        self.nedges = len(roots)
        self.n = len(cr)
        self.ctype = [c[0] for c in cr]
        self.slots = [dict(NW=E(c[1]), NE=E(c[2]), SW=E(c[3]), SE=E(c[4])) for c in cr]
        self.marks = [E(ends[m]) for m in marks]
        # ends of each edge
        eends = collections.defaultdict(list)
        for k, sl in enumerate(self.slots):
            for s, e in sl.items():
                eends[e].append((k, s))
        for e in range(self.nedges):
            assert len(eends[e]) in (0, 2), (e, eends[e])
        # components and orientations
        comp = [None] * self.nedges
        indir = {}  # (k, slot) -> True if a strand enters crossing k at this slot
        ncomp = 0
        for e0 in range(self.nedges):
            if comp[e0] is not None: continue
            if not eends[e0]:
                comp[e0] = ncomp; ncomp += 1; continue
            e = e0; exit_end = eends[e][0]
            while True:
                comp[e] = ncomp
                other = [x for x in eends[e] if x != exit_end]
                assert len(other) == 1
                k, s = other[0]          # we arrive at crossing k through slot s
                indir[(k, s)] = True
                exit_end = (k, OPP[s])   # leave through the opposite slot
                e = self.slots[k][OPP[s]]
                if e == e0 and exit_end == eends[e0][0]:
                    break
            ncomp += 1
        self.comp = comp; self.ncomp = ncomp
        self.sign = []; self.mixed = []
        for k in range(self.n):
            def direction(sa, sb):  # strand on slots sa-sb
                if indir.get((k, sa)): p = SLOTPOS[sa]
                else:
                    assert indir.get((k, sb)), (k, sa, sb); p = SLOTPOS[sb]
                return (-p[0], -p[1])
            d1 = direction('NW', 'SE'); d2 = direction('NE', 'SW')
            over, under = (d1, d2) if self.ctype[k] == 'x' else (d2, d1)
            z = over[0] * under[1] - over[1] * under[0]
            self.sign.append(1 if z > 0 else -1)
            self.mixed.append(comp[self.slots[k]['NW']] != comp[self.slots[k]['NE']])
        self.npos = sum(1 for s in self.sign if s > 0); self.nneg = self.n - self.npos
        # smoothings as pairs of edges
        self.sm = []
        for k in range(self.n):
            sl = self.slots[k]
            H = ((sl['NW'], sl['NE']), (sl['SW'], sl['SE']))
            V = ((sl['NW'], sl['SW']), (sl['NE'], sl['SE']))
            self.sm.append((H, V) if self.ctype[k] == 'x' else (V, H))

    def linking(self, c1, c2):
        tot = 0
        for k in range(self.n):
            a, b = self.comp[self.slots[k]['NW']], self.comp[self.slots[k]['NE']]
            if {a, b} == {c1, c2}: tot += self.sign[k]
        return tot // 2 if tot % 2 == 0 else tot / 2

    def circles(self, s):
        """return list rep[e] = smallest edge of the circle through e in state s"""
        p = list(range(self.nedges))
        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]; x = p[x]
            return x
        for k in range(self.n):
            for a, b in self.sm[k][(s >> k) & 1]:
                a, b = find(a), find(b)
                if a != b:
                    if a > b: a, b = b, a
                    p[b] = a
        return [find(e) for e in range(self.nedges)]


class Complex:
    """generators: (state, xmask) with all marked circles distinct and labelled x; xmask = bitmask of representatives
    of the circles labelled x."""
    def __init__(self, D, deform=True, mixed_only=True):
        self.D = D
        n = D.n
        reps = {}; ncirc = {}
        for s in range(1 << n):
            r = D.circles(s); reps[s] = r; ncirc[s] = len(set(r))
        self.reps = reps
        gens = []; index = {}
        for s in range(1 << n):
            r = reps[s]
            mk = [r[e] for e in D.marks]
            if len(set(mk)) < len(mk): continue
            free = sorted(set(r) - set(mk))
            base = 0
            for c in mk: base |= 1 << c
            for sub in range(1 << len(free)):
                m = base
                for j, c in enumerate(free):
                    if (sub >> j) & 1: m |= 1 << c
                index[(s, m)] = len(gens); gens.append((s, m))
        self.gens = gens; self.index = index
        self.h = []; self.q = []
        for s, m in gens:
            r = bin(s).count('1'); nx = bin(m).count('1')
            self.h.append(r - D.nneg)
            self.q.append(ncirc[s] - 2 * nx + r + D.npos - 2 * D.nneg)
        self.l = [a - b for a, b in zip(self.h, self.q)]
        # differentials as lists of target indices
        self.d0 = [[] for _ in gens]; self.d1 = [[] for _ in gens]
        for g, (s, m) in enumerate(gens):
            r = reps[s]
            for k in range(n):
                bit = (s >> k) & 1
                if bit == 1 and not (deform and (D.mixed[k] or not mixed_only)): continue
                s2 = s ^ (1 << k)
                r2 = reps[s2]
                (e1, e2), (e3, e4) = D.sm[k][bit]
                A, B = r[e1], r[e3]
                out = []
                if A != B:      # merge
                    C = r2[e1]
                    xa, xb = (m >> A) & 1, (m >> B) & 1
                    if xa and xb: continue
                    m2 = m & ~(1 << A) & ~(1 << B)
                    if xa or xb: m2 |= 1 << C
                    out.append(m2)
                else:           # split of the circle A into the circles through e1 and e3 in s2
                    (f1, f2), (f3, f4) = D.sm[k][1 - bit]
                    A2, B2 = r2[f1], r2[f3]
                    assert A2 != B2
                    m2 = m & ~(1 << A)
                    if (m >> A) & 1:
                        out.append(m2 | (1 << A2) | (1 << B2))
                    else:
                        out.append(m2 | (1 << A2)); out.append(m2 | (1 << B2))
                tgt = self.d0[g] if bit == 0 else self.d1[g]
                for m2 in out:
                    key = (s2, m2)
                    if key in index:
                        tgt.append(index[key])
                    else:
                        # must only happen if a marked circle lost its x or two marked points share a circle
                        rr = reps[s2]; mk = [rr[e] for e in D.marks]
                        ok = len(set(mk)) == len(mk) and all((m2 >> c) & 1 for c in mk)
                        assert not ok, 'missing pointed generator'
                        raise AssertionError('image left the pointed subcomplex: %r -> %r' % ((s, m), key))


def rank_cols(cols):
    piv = {}
    for v in cols:
        while v:
            p = v.bit_length() - 1
            w = piv.get(p)
            if w is None:
                piv[p] = v; break
            v ^= w
    return len(piv)


def homology_bigraded(C, use_d1=False):
    """H(d_0) by (h,q) (use_d1=False), or H(d_0+d_1) by l (use_d1=True). returns Counter key -> dim"""
    key = (lambda g: C.l[g]) if use_d1 else (lambda g: (C.h[g], C.q[g]))
    nxt = (lambda k: k + 1) if use_d1 else (lambda k: (k[0] + 1, k[1]))
    groups = collections.defaultdict(list)
    for g in range(len(C.gens)): groups[key(g)].append(g)
    pos = {}
    for k, L in groups.items():
        for i, g in enumerate(L): pos[g] = i
    rk = {}
    for k, L in groups.items():
        cols = []
        for g in L:
            v = 0
            for t in C.d0[g]: v ^= 1 << pos[t]
            if use_d1:
                for t in C.d1[g]: v ^= 1 << pos[t]
            cols.append(v)
        rk[k] = rank_cols(cols)
    out = collections.Counter()
    prev = {nxt(k): k for k in groups}
    for k, L in groups.items():
        d = len(L) - rk[k] - (rk[prev[k]] if k in prev else 0)
        if d: out[k] = d
    return out


def check_d_squared(C):
    for g in range(len(C.gens)):
        acc = collections.Counter()
        for t in C.d0[g] + C.d1[g]:
            for u in C.d0[t] + C.d1[t]: acc[u] ^= 1
        if any(acc.values()): return False
    return True


def pages(C):
    """Barannikov / persistence normal form of the q-filtered complex (C, d_0+d_1) over F_2.
    returns (pairs, essential): pairs = list of (gen_killed, gen_killer, k) with q(killer) - q(killed) = 2k;
    essential = list of unpaired generators (E_infinity)."""
    N = len(C.gens)
    byl = collections.defaultdict(list)
    for g in range(N): byl[C.l[g]].append(g)
    for L in byl.values(): L.sort(key=lambda g: (C.q[g], g))   # filtration order: increasing q
    pos = {}
    for L in byl.values():
        for i, g in enumerate(L): pos[g] = i
    paired_as_pivot = {}; killer = {}
    for l, L in sorted(byl.items()):
        rows = byl.get(l + 1, [])
        piv = {}
        for g in L:
            v = 0
            for t in C.d0[g] + C.d1[g]: v ^= 1 << pos[t]
            while v:
                p = v.bit_length() - 1
                if p in piv: v ^= piv[p][0]
                else:
                    piv[p] = (v, g); break
        for p, (v, g) in piv.items():
            i = rows[p]
            k2 = C.q[g] - C.q[i]
            assert k2 >= 0 and k2 % 2 == 0
            paired_as_pivot[i] = g; killer[g] = (i, k2 // 2)
    pairs = [(i, g, k) for g, (i, k) in killer.items()]
    ess = [g for g in range(N) if g not in killer and g not in paired_as_pivot]
    return pairs, ess


def page_poly(C, pairs, ess, k):
    """Counter of (h,q) on the page E_k (k >= 1), or E_infinity if k is None"""
    out = collections.Counter()
    for g in ess: out[(C.h[g], C.q[g])] += 1
    if k is not None:
        for i, g, kk in pairs:
            if kk >= k:
                out[(C.h[i], C.q[i])] += 1; out[(C.h[g], C.q[g])] += 1
    return out


def fmt(cnt):
    return ' '.join('%s:%d' % (str(k).replace(' ', ''), v) for k, v in sorted(cnt.items()))


def lpoly(cnt_hq):
    out = collections.Counter()
    for (h, q), v in cnt_hq.items(): out[h - q] += v
    return out


class SubDiagram(Diagram):
    """the diagram of one component c of D (all other components deleted), marked at the image of D's marked edge on c"""
    def __init__(self, D, c):
        uf = UF()
        for e in range(D.nedges):
            if D.comp[e] == c: uf.new(e)
        keep = []
        for k in range(D.n):
            sl = D.slots[k]
            a, b = D.comp[sl['NW']], D.comp[sl['NE']]   # components of the strands NW-SE and NE-SW
            if a == c and b == c:
                keep.append(k)
            elif a == c:
                uf.union(sl['NW'], sl['SE'])
            elif b == c:
                uf.union(sl['NE'], sl['SW'])
        roots = sorted({uf.find(e) for e in uf.p})
        eid = {r: i for i, r in enumerate(roots)}
        E = lambda e: eid[uf.find(e)]
        self.nedges = len(roots)
        self.n = len(keep)
        self.ctype = [D.ctype[k] for k in keep]
        self.slots = [{s: E(e) for s, e in D.slots[k].items()} for k in keep]
        self.marks = [E(m) for m in D.marks if D.comp[m] == c]
        self.comp = [0] * self.nedges; self.ncomp = 1
        self.sign = [D.sign[k] for k in keep]
        self.mixed = [False] * self.n
        self.npos = sum(1 for s in self.sign if s > 0); self.nneg = self.n - self.npos
        self.sm = []
        for k in range(self.n):
            sl = self.slots[k]
            H = ((sl['NW'], sl['NE']), (sl['SW'], sl['SE']))
            V = ((sl['NW'], sl['SW']), (sl['NE'], sl['SE']))
            self.sm.append((H, V) if self.ctype[k] == 'x' else (V, H))


def tensor_l(H1, H2):
    out = collections.Counter()
    for (h1, q1), v1 in H1.items():
        for (h2, q2), v2 in H2.items():
            out[(h1 - q1) + (h2 - q2)] += v1 * v2
    return out


def shift_equal(A, B):
    """is Counter A a shift of Counter B (integer keys)? return the shift s with A[k] = B[k - s] or None"""
    if sum(A.values()) != sum(B.values()): return None
    if not A: return 0
    s = min(A) - min(B)
    return s if all(A[k] == B[k - s] for k in set(A) | {k + s for k in B}) else None
