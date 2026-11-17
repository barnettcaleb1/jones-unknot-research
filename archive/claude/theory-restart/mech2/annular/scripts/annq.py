#!/usr/bin/env python3
"""Characteristic zero check of the annular dictionary on the standard pieces (unit square with local system lam, zigzags).
Type D structure over B_Z (relations DS = SD = 0); module M: M(b) = V(x)V, M(c) = W with
 D_b = 1(x)X - X(x)1, S_b = merge, S_c = split, S_c S_b = split.merge on b, S_b S_c = merge.split (= 2X) on c, D_c = 0.
sl_2: f = D_b on V(x)V, e = Theta f Theta, zero on W.
"""
import sys, itertools
from fractions import Fraction as Fr
import sympy as sp

VV = ['11', '1x', 'x1', 'xx']; WW = ['1', 'x']
JK = {'11': (2, 2), '1x': (0, 0), 'x1': (0, 0), 'xx': (-2, -2), '1': (1, 0), 'x': (-1, 0)}
def lin(d):  # dict basis->coeff
    return {k: v for k, v in d.items() if v != 0}
Db = {'11': {'1x': 1, 'x1': -1}, '1x': {'xx': -1}, 'x1': {'xx': 1}, 'xx': {}}
Sb = {'11': {'1': 1}, '1x': {'x': 1}, 'x1': {'x': 1}, 'xx': {}}           # b -> c
Sc = {'1': {'1x': 1, 'x1': 1}, 'x': {'xx': 1}}                              # c -> b
def comp(f, g):  # apply f then g
    out = {}
    for a, im in f.items():
        o = {}
        for b, c in im.items():
            for d, e in g[b].items(): o[d] = o.get(d, 0) + c * e
        out[a] = lin(o)
    return out
S2b = comp(Sb, Sc); S2c = comp(Sc, Sb)
Dc = {'1': {}, 'x': {}}
ACT = {('D', 1, 'b', 'b'): Db, ('S', 1, 'b', 'c'): Sb, ('S', 1, 'c', 'b'): Sc, ('S', 2, 'b', 'b'): S2b, ('S', 2, 'c', 'c'): S2c, ('D', 1, 'c', 'c'): Dc}
THETA = {'1': 'x', 'x': '1'}
def theta(lab): return THETA[lab[0]] + THETA[lab[1]]
Fop = Db
Eop = {a: lin({theta(b): c for b, c in Fop[theta(a)].items()}) for a in VV}

def build(gens, arrows):
    """gens: list of (idem, h, q); arrows: list of (src, dst, kind, power, coeff). returns basis list and matrices d0, dm (sympy), e, f"""
    basis = []
    for gi, (idem, h, q) in enumerate(gens):
        for lab in (VV if idem == 'b' else WW):
            j, k = JK[lab]
            basis.append((gi, lab, h, q + j, k))
    pos = {(b[0], b[1]): n for n, b in enumerate(basis)}
    n = len(basis)
    d0 = sp.zeros(n, n); dm = sp.zeros(n, n); dother = sp.zeros(n, n)
    for (s, t, kind, power, coeff) in arrows:
        A = ACT[(kind, power, gens[s][0], gens[t][0])]
        for a, im in A.items():
            for b, c in im.items():
                i, o = pos[(s, a)], pos[(t, b)]
                dk = basis[o][4] - basis[i][4]
                assert basis[o][3] == basis[i][3], ('j not preserved', kind, power, a, b)
                if dk == 0: d0[o, i] += coeff * c
                elif dk == -2: dm[o, i] += coeff * c
                else: dother[o, i] += coeff * c
    E = sp.zeros(n, n); F = sp.zeros(n, n)
    for gi, (idem, h, q) in enumerate(gens):
        if idem != 'b': continue
        for a in VV:
            for b, c in Eop[a].items(): E[pos[(gi, b)], pos[(gi, a)]] += c
            for b, c in Fop[a].items(): F[pos[(gi, b)], pos[(gi, a)]] += c
    return basis, d0, dm, dother, E, F

def chain(spec, lam=1, h0=0, q0=0):
    """spec: list of moves along a curve starting at a b-generator: '+P', '-P', '+D', '-D', tail 'T<n>' ; closed=True if cyclic.
    +P: x -S-> c -D-> c -S2-> c -D-> c -S-> y ; -P reversed arrows. lam on the first D arrow encountered."""
    gens = [('b', h0, q0)]; arrows = []; cur = 0; used_lam = [False]
    def add(idem, dh, dq):
        h, q = gens[cur_holder[0]][1] + dh, gens[cur_holder[0]][2] + dq
        gens.append((idem, h, q)); return len(gens) - 1
    cur_holder = [0]
    def step(kind, power, idem_next, sign, coeff=1):
        deg = power if kind == 'S' else 2 * power
        a = cur_holder[0]
        b = add(idem_next, sign, sign * deg)
        arrows.append((a, b, kind, power, coeff) if sign == 1 else (b, a, kind, power, coeff))
        cur_holder[0] = b
    for mv in spec:
        s = 1 if mv[0] == '+' else -1
        if mv[1] == 'P':
            seq = [('S', 1, 'c'), ('D', 1, 'c'), ('S', 2, 'c'), ('D', 1, 'c'), ('S', 1, 'b')]
            if s == -1: seq = [('S', 1, 'c'), ('D', 1, 'c'), ('S', 2, 'c'), ('D', 1, 'c'), ('S', 1, 'b')]
            for (kind, power, nxt) in seq: step(kind, power, nxt, s)
        elif mv[1] == 'D':
            c = 1
            if not used_lam[0]: c = lam; used_lam[0] = True
            step('D', 1, 'b', s, c)
    return gens, arrows

def close_cycle(gens, arrows):
    """identify last generator with first (must have equal idempotent and grading)"""
    last = len(gens) - 1
    assert gens[last] == gens[0], (gens[last], gens[0])
    arrows = [(0 if s == last else s, 0 if t == last else t, k, p, c) for (s, t, k, p, c) in arrows]
    return gens[:-1], arrows

def homology_dims(d, basis, grade):
    """d: matrix with d^2=0; returns Counter grade->dim of homology"""
    from collections import Counter, defaultdict
    n = len(basis)
    H = Counter()
    sect = defaultdict(list)
    for i, b in enumerate(basis): sect[grade(b)].append(i)
    rk_out = {}
    # ranks between sectors
    def sub(rows, cols): return d.extract(rows, cols) if rows and cols else sp.zeros(len(rows), len(cols))
    keys = list(sect)
    rank_from = {}
    for a in keys:
        # image of sector a lies in sectors with h+1; compute rank of d restricted to columns in a
        rank_from[a] = sp.Matrix(d[:, sect[a]]).rank() if sect[a] else 0
    return sect, rank_from

if __name__ == '__main__':
    for lam in (1, -1):
        gens, arrows = chain(['+P', '+D', '-P', '-D'], lam=lam)
        gens, arrows = close_cycle(gens, arrows)
        basis, d0, dm, do, E, F = build(gens, arrows)
        n = len(basis)
        d = d0 + dm + do
        print('square, lam =', lam, ': gens', len(gens), 'dim', n)
        print('  (d0+dm+dother)^2 = 0:', (d*d).is_zero_matrix, ' d0^2=0:', (d0*d0).is_zero_matrix, ' dother nonzero:', not do.is_zero_matrix)
        print('  [e,d0]=0:', (E*d0 - d0*E).is_zero_matrix, ' [f,d0]=0:', (F*d0 - d0*F).is_zero_matrix, ' [f,dm]=0:', (F*dm - dm*F).is_zero_matrix)
        Hh = E*F - F*E
        rk0 = d0.rank()
        print('  dim AKh =', n - 2*rk0, ' rank total d:', d.rank(), ' dim Kh(Q) =', n - 2*d.rank())
        # by weight
        for k in (2, 0, -2):
            idx = [i for i, b in enumerate(basis) if b[4] == k]
            sub = d0.extract(idx, idx)
            print('    weight', k, 'dim', len(idx), 'AKh dim', len(idx) - 2*sub.rank())
