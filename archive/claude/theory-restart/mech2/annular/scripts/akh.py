#!/usr/bin/env python3
"""Direct (annular) Khovanov homology over F_2 of a closure of a kht++ Morse word (one top end).
Independent of kht++ and of the multicurve calculus; used to test the dictionary  AKh_2 = generators of BNr at Q_inf.

Word letters (kht++): r<i>/l<i> cap creating strands i,i+1; u<i> cup; x<i>/y<i> crossing of strands i,i+1
 x: over-strand from top-left  => 0-resolution = horizontal (cup/cap), 1-resolution = vertical
 y: over-strand from top-right => 0-resolution = vertical,             1-resolution = horizontal
(calibrated against lit/kht/REPORT.md 4.4: appended y0 sends e_inf -> e_inf - q e_0.)
Closures: list of (endA, endB, seam) with ends 'top' or bottom index; seam=True if the closing arc crosses the seam once.
Gradings: h = #1-resolutions - n_-, q = (#1 labels - #x labels) + #1-resolutions + n_+ - 2 n_-, k = sum over essential circles (+1 for label 1, -1 for x).
"""
import sys, itertools
from collections import defaultdict, Counter

def build(word, closures):
    letters = [w for w in word.strip().split('.') if w]
    nid = [0]
    def new():
        nid[0] += 1; return nid[0] - 1
    top = new()
    frontier = [top]
    joins = []          # (a, b, seam) arcs joining ids
    crossings = []      # (type, tl, tr, bl, br)
    up_att = {top: ('top',)}; low_att = {}
    for w in letters:
        t, i = w[0], int(w[1:])
        if t in 'rl':
            a, b = new(), new()
            joins.append((a, b, False)); up_att[a] = ('cap', b); up_att[b] = ('cap', a)
            frontier[i:i] = [a, b]
        elif t == 'u':
            a, b = frontier[i], frontier[i+1]
            joins.append((a, b, False)); low_att[a] = ('cup', b); low_att[b] = ('cup', a)
            del frontier[i:i+2]
        elif t in 'xy':
            tl, tr = frontier[i], frontier[i+1]
            bl, br = new(), new()
            c = len(crossings)
            crossings.append((t, tl, tr, bl, br))
            low_att[tl] = ('x', c, 'tl'); low_att[tr] = ('x', c, 'tr')
            up_att[bl] = ('x', c, 'bl'); up_att[br] = ('x', c, 'br')
            frontier[i:i+2] = [bl, br]
        else:
            raise ValueError(w)
    ends = {'top': top}
    for j, f in enumerate(frontier): ends[j] = f
    seam_nodes = []
    for (A, B, seam) in closures:
        a, b = ends[A], ends[B]
        joins.append((a, b, seam))
        if seam: seam_nodes.append(a)
        # attachments for orientation tracing
        for (p, P, q_) in ((a, A, b), (b, B, a)):
            if P == 'top': up_att[p] = ('close', q_)
            else: low_att[p] = ('close', q_)
    used = set(x for cl in closures for x in cl[:2])
    assert used == set(ends), ('all ends must be closed', used, set(ends))
    return dict(n=nid[0], joins=joins, crossings=crossings, seam_nodes=seam_nodes, up=up_att, low=low_att, top=top)

def signs(D):
    """orient the link (each component arbitrarily), return (n_plus, n_minus, ncomponents)"""
    X = D['crossings']; up = D['up']; low = D['low']
    passdir = {}   # (c, strand) -> +1 down / -1 up ; strand 'a' = tl-br, 'b' = tr-bl
    visited = set(); ncomp = 0
    for start in range(D['n']):
        if start in visited: continue
        ncomp += 1
        cur, d = start, +1     # d=+1: travelling downward along id cur (from upper to lower attachment)
        while True:
            if (cur, d) in visited or cur in visited and False: break
            if cur in visited: break
            visited.add(cur)
            att = low[cur] if d == 1 else up[cur]
            if att[0] == 'x':
                c, corner = att[1], att[2]
                t, tl, tr, bl, br = X[c]
                if d == 1:
                    if corner == 'tl': passdir[(c, 'a')] = +1; cur = br
                    else: passdir[(c, 'b')] = +1; cur = bl
                else:
                    if corner == 'br': passdir[(c, 'a')] = -1; cur = tl
                    else: passdir[(c, 'b')] = -1; cur = tr
            elif att[0] in ('cup', 'cap'):
                cur = att[1]; d = -d
            elif att[0] == 'close':
                other = att[1]
                # arriving at a bottom end going down (d=1) or at the top end going up (d=-1)
                # continue on 'other': if other is the top end we travel down, if other is a bottom end we travel up
                d = +1 if other == D['top'] else -1
                cur = other
            elif att[0] == 'top':
                raise RuntimeError('open top end')
    npl = nmi = 0
    for c, (t, tl, tr, bl, br) in enumerate(X):
        co = passdir[(c, 'a')] == passdir[(c, 'b')]
        # oriented smoothing is vertical iff co-directed; crossing is positive iff oriented smoothing = 0-resolution
        zero_is_vertical = (t == 'y')
        pos = (co == zero_is_vertical)
        if pos: npl += 1
        else: nmi += 1
    return npl, nmi, ncomp

class UF:
    def __init__(s, n): s.p = list(range(n))
    def f(s, a):
        while s.p[a] != a:
            s.p[a] = s.p[s.p[a]]; a = s.p[a]
        return a
    def u(s, a, b):
        a, b = s.f(a), s.f(b)
        if a != b: s.p[max(a, b)] = min(a, b)

def resolution(D, s):
    uf = UF(D['n'])
    for a, b, seam in D['joins']: uf.u(a, b)
    for bit, (t, tl, tr, bl, br) in zip(s, D['crossings']):
        vertical = (bit == 0) == (t == 'y')
        if vertical: uf.u(tl, bl); uf.u(tr, br)
        else: uf.u(tl, tr); uf.u(bl, br)
    comp = [uf.f(a) for a in range(D['n'])]
    reps = sorted(set(comp))
    ess = Counter()
    for a in D['seam_nodes']: ess[comp[a]] += 1
    essential = {r: (ess[r] % 2 == 1) for r in reps}
    return comp, reps, essential

def rank_f2(rows):
    """rows: list of python ints (bitsets). returns rank"""
    piv = {}
    r = 0
    for v in rows:
        while v:
            hb = v.bit_length() - 1
            if hb in piv: v ^= piv[hb]
            else: piv[hb] = v; r += 1; break
    return r

def khovanov(word, closures, annular=True, verbose=False):
    D = build(word, closures)
    n = len(D['crossings'])
    npl, nmi, ncomp = signs(D)
    res = {}
    for s in itertools.product((0, 1), repeat=n):
        res[s] = resolution(D, s)
    # generators: (s, labels tuple aligned with reps) ; label 0 = '1', 1 = 'x'
    # sectors: total complex keyed (q) -> h -> list ; annular keyed (q,k)
    gens_tot = defaultdict(lambda: defaultdict(dict))   # q -> h -> {gen: index}
    gens_ann = defaultdict(lambda: defaultdict(dict))   # (q,k) -> h -> {gen: index}
    info = {}
    for s, (comp, reps, essential) in res.items():
        r = sum(s); h = r - nmi
        for lab in itertools.product((0, 1), repeat=len(reps)):
            q = sum(1 - 2*l for l in lab) + r + npl - 2*nmi
            k = sum((1 - 2*l) for l, rp in zip(lab, reps) if essential[rp])
            g = (s, lab)
            d = gens_tot[q][h]; d[g] = len(d)
            d = gens_ann[(q, k)][h]; d[g] = len(d)
            info[g] = (h, q, k)
    def images(g):
        s, lab = g
        comp, reps, essential = res[s]
        labd = dict(zip(reps, lab))
        out = []
        for c in range(n):
            if s[c] == 1: continue
            s2 = s[:c] + (1,) + s[c+1:]
            comp2, reps2, ess2 = res[s2]
            t, tl, tr, bl, br = D['crossings'][c]
            old = sorted(set(comp[a] for a in (tl, tr, bl, br)))
            new = sorted(set(comp2[a] for a in (tl, tr, bl, br)))
            base = {}
            for rp in reps:
                if rp not in old: base[rp] = labd[rp]
            # untouched circles keep their representative (same node sets) 
            if len(old) == 2 and len(new) == 1:
                a, b = labd[old[0]], labd[old[1]]
                if a == 1 and b == 1: continue
                l2 = dict(base); l2[new[0]] = a | b
                out.append((s2, tuple(l2[rp] for rp in reps2)))
            elif len(old) == 1 and len(new) == 2:
                a = labd[old[0]]
                if a == 0:
                    for (u, v) in ((0, 1), (1, 0)):
                        l2 = dict(base); l2[new[0]] = u; l2[new[1]] = v
                        out.append((s2, tuple(l2[rp] for rp in reps2)))
                else:
                    l2 = dict(base); l2[new[0]] = 1; l2[new[1]] = 1
                    out.append((s2, tuple(l2[rp] for rp in reps2)))
            else:
                raise RuntimeError('bad edge')
        return out
    img = {g: images(g) for g in info}
    def homology(sectors, same_k):
        H = Counter()
        for key, byh in sectors.items():
            hs = sorted(byh)
            rk = {}
            for h in hs:
                tgt = byh.get(h + 1, {})
                rows = []
                for g in byh[h]:
                    v = 0
                    for g2 in img[g]:
                        if same_k and info[g2][2] != info[g][2]: continue
                        if not same_k or True:
                            v ^= (1 << tgt[g2]) if g2 in tgt else 0
                    rows.append(v)
                rk[h] = rank_f2(rows)
            for h in hs:
                dim = len(byh[h]) - rk[h] - rk.get(h - 1, 0)
                if dim: H[(h,) + (key if isinstance(key, tuple) else (key,))] += dim
        return H
    Htot = homology(gens_tot, False)
    Hann = homology(gens_ann, True) if annular else None
    return dict(n=n, npl=npl, nmi=nmi, ncomp=ncomp, Kh=Htot, AKh=Hann)

def fmt(H):
    return ', '.join('%s:%d' % (k, v) for k, v in sorted(H.items()))

if __name__ == '__main__':
    # sanity: right-handed trefoil as a 1-1 tangle (kht++: r1.y0.y0.y0.u1 is the positive trefoil)
    r = khovanov('r1.y0.y0.y0.u1', [('top', 0, False)], annular=False)
    print('trefoil r1.y0.y0.y0.u1: n+,n-,comps', r['npl'], r['nmi'], r['ncomp'], 'Kh (h,q):', fmt(r['Kh']))
    r = khovanov('r1.u1', [('top', 0, False)], annular=False)
    print('unknot:', fmt(r['Kh']))
    # annular: Q_inf (l1 in 1-3 form): two essential circles
    r = khovanov('l1', [('top', 0, True), (1, 2, True)])
    print('Q_inf annular closure: Kh', fmt(r['Kh']), '| AKh (h,q,k):', fmt(r['AKh']))
    r = khovanov('l0', [('top', 0, True), (1, 2, True)])
    print('Q_0 annular closure: Kh', fmt(r['Kh']), '| AKh (h,q,k):', fmt(r['AKh']))
