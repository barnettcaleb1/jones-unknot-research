#!/usr/bin/env python3
"""Horizontal annular closure functor on type D structures over the Bar-Natan algebra B, coefficients F_2, H = 0.

Closure: T(0) = T u Q_0 (two closing arcs running once around the annulus); to get T(n) feed BN~(T sigma^n).
Module (Khovanov TQFT of the closure, split by annular weight k):
  M(b) = V (x) V, basis 11 (j=+2,k=+2), 1x, x1 (j=0,k=0), xx (j=-2,k=-2); first factor = circle through the special end
  M(c) = W, basis 1 (j=+1,k=0), x (j=-1,k=0)
Algebra action (x --a--> y in the type D structure contributes  v (x) x  |->  a.v (x) y):
  D on b (= x_* + x_2):  11 -> 1x + x1, 1x -> xx, x1 -> xx          (lowers k by 2: part of d_-)
  S: b -> c (merge):     11 -> 1 [d_-], 1x -> x, x1 -> x [d_0], xx -> 0
  S: c -> b (split):     1 -> 1x + x1 [d_0], x -> xx [d_-]
  S^2 on b (= split o merge) = D on b;   D on c = 0;  S^2 on c = 0;  all higher powers 0.
Generators carry (h, j, k) with j = q(generator) + shift.
"""
import sys, os
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khparse import *

Bb, Cc = '⬮', '⬯'
BASIS = {Bb: [('11', 2, 2), ('1x', 0, 0), ('x1', 0, 0), ('xx', -2, -2)], Cc: [('1', 1, 0), ('x', -1, 0)]}

def act(kind, power, src, dst, a):
    if kind == 'S' and power == 1:
        if src == Bb and dst == Cc: return {'11': ['1'], '1x': ['x'], 'x1': ['x'], 'xx': []}[a]
        if src == Cc and dst == Bb: return {'1': ['1x', 'x1'], 'x': ['xx']}[a]
        raise ValueError((kind, power, src, dst))
    if (kind == 'D' and power == 1) or (kind == 'S' and power == 2):
        assert src == dst
        if src == Bb: return {'11': ['1x', 'x1'], '1x': ['xx'], 'x1': ['xx'], 'xx': []}[a]
        return []
    return []

def rank_f2(rows):
    piv = {}; r = 0
    for v in rows:
        while v:
            hb = v.bit_length() - 1
            if hb in piv: v ^= piv[hb]
            else: piv[hb] = v; r += 1; break
    return r

def annular_complex(comps):
    gens = []; index = {}
    for ci, comp in enumerate(comps):
        for gi, (idem, h, q) in enumerate(comp['gens']):
            for (lab, dq, k) in BASIS[idem]:
                index[(ci, gi, lab)] = len(gens)
                gens.append((h, q + dq, k, (ci, gi, lab)))
    diff = defaultdict(list)
    for ci, comp in enumerate(comps):
        for (s, d, kind, power) in comp['arrows']:
            si, di = comp['gens'][s][0], comp['gens'][d][0]
            for (lab, dq, k) in BASIS[si]:
                for lab2 in act(kind, power, si, di, lab):
                    diff[index[(ci, s, lab)]].append(index[(ci, d, lab2)])
    for i, tg in diff.items():
        for j in tg:
            assert gens[j][0] == gens[i][0] + 1 and gens[j][1] == gens[i][1] and gens[j][2] in (gens[i][2], gens[i][2] - 2), (gens[i], gens[j])
    return gens, diff

# ---------- linear algebra over F_2 with explicit bases ----------
def mat_cols(src_idx, dst_idx, diff, cond):
    pos = {i: n for n, i in enumerate(dst_idx)}
    cols = []
    for i in src_idx:
        v = 0
        for j in diff.get(i, []):
            if j in pos and cond(i, j): v ^= 1 << pos[j]
        cols.append(v)
    return cols

def homology(gens, diff, mode):
    """mode 'ann': d_0 only, sectors (j,k); mode 'tot': full, sectors j. Counter (h,j[,k]) -> dim"""
    sectors = defaultdict(lambda: defaultdict(list))
    for i, (h, j, k, _) in enumerate(gens):
        key = (j, k) if mode == 'ann' else (j,)
        sectors[key][h].append(i)
    H = Counter()
    for key, byh in sectors.items():
        rk = {}
        for h in sorted(byh):
            cond = (lambda i, jj: gens[jj][2] == gens[i][2]) if mode == 'ann' else (lambda i, jj: True)
            rk[h] = rank_f2(mat_cols(byh[h], byh.get(h + 1, []), diff, cond))
        for h in sorted(byh):
            d = len(byh[h]) - rk[h] - rk.get(h - 1, 0)
            if d: H[(h,) + key] += d
    return H

def pages(gens, diff):
    """E1 = H(d_0) by (h,j,k); E2 = H(E1, d_-); returns (E1, E2, Etot) as Counters; computed sector-wise in j with a filtered Gaussian elimination."""
    # generic spectral sequence of the filtered complex (filtration by k), per j-sector, via explicit computation of
    # Z_r/B_r dimensions:  E^r_{p} = Z^r_p / (Z^{r-1}_{p-?} + B^{r-1}_p).  We use the standard formulas with ranks.
    byj = defaultdict(list)
    for i, (h, j, k, _) in enumerate(gens): byj[j].append(i)
    E = {1: Counter(), 2: Counter(), 3: Counter()}
    for j, idx in byj.items():
        idx = sorted(idx, key=lambda i: gens[i][0])
        pos = {i: n for n, i in enumerate(idx)}
        n = len(idx)
        # differential as list of column bitsets over the full sector
        col = []
        for i in idx:
            v = 0
            for t in diff.get(i, []): v ^= 1 << pos[t]
            col.append(v)
        ks = sorted(set(gens[i][2] for i in idx), reverse=True)     # filtration: F_p = span of generators with k <= p (d lowers k)
        hs = sorted(set(gens[i][0] for i in idx))
        mask_k_le = {p: sum(1 << pos[i] for i in idx if gens[i][2] <= p) for p in range(-4, 5, 2)}
        mask_h = {h: sum(1 << pos[i] for i in idx if gens[i][0] == h) for h in hs}
        def Fp(p, h):   # indices
            return [i for i in idx if gens[i][2] <= p and gens[i][0] == h]
        # Z^r_{p,h} = {x in F_p C_h : dx in F_{p-2r} }, dimension via kernel of (d mod F_{p-2r})
        def dimZ(r, p, h):
            src = Fp(p, h)
            keep = ~mask_k_le.get(p - 2*r, 0) if (p - 2*r) >= -4 else ~0
            rows = [col[pos[i]] & keep for i in src]
            return len(src) - rank_f2(rows)
        # B^r_{p,h} = d(F_{p+2r} C_{h-1}) cap F_p C_h ; dimension = dim(d(F_{p+2r}C_{h-1})) - rank of its image modulo F_p
        def dimdF(p, h):   # dim of d(F_p C_{h-1}) 
            return rank_f2([col[pos[i]] for i in Fp(p, h - 1)])
        def dimB(r, p, h):
            src = Fp(min(p + 2*r, 4), h - 1)
            rows = [col[pos[i]] for i in src]
            full = rank_f2(rows)
            mod = rank_f2([v & ~mask_k_le[p] for v in rows])
            return full - mod
        # E^r_{p,h} = Z^r_p / (Z^{r-1}_{p-2} + B^{r-1}_p);  dim = dimZ(r,p) - dim(Z^{r-1}_{p-2} + B^{r-1}_p)
        # compute dim(Z^{r-1}_{p-2,h} + B^{r-1}_{p,h}) explicitly by spanning sets
        def kernel_basis(vecs_src, images):
            # returns basis (as bitsets over idx) of {x in span(src) : image(x) = 0}; vecs_src: list of bitsets (unit vectors), images: list of bitsets
            piv = {}; ker = []
            for x, y in zip(vecs_src, images):
                x = x; y = y
                while y:
                    hb = y.bit_length() - 1
                    if hb in piv:
                        px, py = piv[hb]; x ^= px; y ^= py
                    else:
                        piv[hb] = (x, y); break
                if y == 0: ker.append(x)
            return ker
        def Zbasis(r, p, h):
            src = Fp(p, h)
            keep = ~mask_k_le.get(p - 2*r, 0) if (p - 2*r) >= -4 else ~0
            return kernel_basis([1 << pos[i] for i in src], [col[pos[i]] & keep for i in src])
        def Bbasis(r, p, h):
            src = Fp(min(p + 2*r, 4), h - 1)
            # elements d(x), x in F_{p+2r} C_{h-1}, with d(x) in F_p: kernel of (d mod F_p) then apply d
            ker = kernel_basis([1 << pos[i] for i in src], [col[pos[i]] & ~mask_k_le[p] for i in src])
            out = []
            for x in ker:
                y = 0; m = x; b = 0
                while m:
                    if m & 1: y ^= col[b]
                    m >>= 1; b += 1
                out.append(y)
            return out
        for r in (1, 2, 3):
            for p in ks:
                for h in hs:
                    Z = Zbasis(r, p, h)
                    if not Z: continue
                    denom = (Zbasis(r - 1, p - 2, h) if p - 2 >= -4 else []) + Bbasis(r - 1, p, h)
                    d = rank_f2(list(Z) + denom) - rank_f2(denom) if denom else rank_f2(Z)
                    # dim Z/(denominator): denominator is contained in Z
                    if d: E[r][(h, j, p)] += d
    return E

def fmt(H, k=None):
    return ', '.join('(%d,%d):%d' % (key[0], key[1], v) for key, v in sorted(H.items()) if k is None or key[2] == k)

if __name__ == '__main__':
    ROOT = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'
    fn = sys.argv[1]
    comps = parse_file(fn)
    gens, diff = annular_complex(comps)
    Ha = homology(gens, diff, 'ann'); Ht = homology(gens, diff, 'tot')
    E = pages(gens, diff)
    assert E[1] == Ha, (E[1], Ha)
    print('b-generators (N):', sum(1 for c in comps for g in c['gens'] if g[0] == Bb), ' c-generators:', sum(1 for c in comps for g in c['gens'] if g[0] == Cc))
    for r in (1, 2, 3):
        print('E%d dims by weight:' % r, {k: sum(v for key, v in E[r].items() if key[2] == k) for k in (2, 0, -2)}, 'total', sum(E[r].values()))
    print('total Kh rank:', sum(Ht.values()))
    print('E1 k=2 (h,j):', fmt(E[1], 2))
    print('E3 k=2 (h,j):', fmt(E[3], 2))
    print('E3 k=-2 (h,j):', fmt(E[3], -2))
    print('E3 k=0 (h,j):', fmt(E[3], 0))
    print('Kh (h,j):', ', '.join('(%d,%d):%d' % (k[0], k[1], v) for k, v in sorted(Ht.items())))
