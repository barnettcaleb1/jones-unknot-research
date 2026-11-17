#!/usr/bin/env python3
"""Formal annular homology of B0 = a(0) + S + hS (and of a ladder) in characteristic 0: module relations, ranks, Euler characteristics."""
import sympy as sp
from collections import Counter
from annq import *
from annq2 import hom_basis, induced

def union(parts):
    gens = []; arrows = []
    for (g, a) in parts:
        off = len(gens)
        gens += g
        arrows += [(s + off, t + off, k, p, c) for (s, t, k, p, c) in a]
    return gens, arrows
def square(h0, q0, lam=1):
    g, a = close_cycle(*chain(['+P', '+D', '-P', '-D'], lam=lam, h0=h0, q0=q0)); return g, a
def report(name, gens, arrows):
    basis, d0, dm, do, E, F = build(gens, arrows)
    n = len(basis); d = d0 + dm
    Bm, Hm = hom_basis(d0)
    e = induced(E, Bm, Hm); f = induced(F, Bm, Hm); vm = induced(dm, Bm, Hm)
    h = e*f - f*e; v0 = e*vm - vm*e; v2c = None
    wts = Counter(sp.Integer(x) for x in h.eigenvals(multiple=True))
    nb = sum(1 for g in gens if g[0] == 'b')
    # Euler characteristics of N in q (by h parity)
    chi = Counter()
    for (idem, hh, q) in gens:
        if idem == 'b': chi[q] += (-1) ** (hh % 2)
    chi = {q: c for q, c in sorted(chi.items()) if c}
    ok = (vm*vm).is_zero_matrix and (v0*v0).is_zero_matrix and (v0*vm + vm*v0).is_zero_matrix and (f*vm - vm*f).is_zero_matrix and (h*e - e*h - 2*e).is_zero_matrix
    print('==', name)
    print('   dim N =', nb, ' chi_q(N) =', chi)
    print('   dim AKh =', Hm.shape[1], ' weights:', dict(wts), ' => dim M_0 =', wts[0] - wts[2])
    print('   sl_2(wedge) relations on homology:', ok, ';  dim H(AKh, v_-2) =', Hm.shape[1] - 2*vm.rank(), ' = dim Kh(Q) =', n - 2*d.rank(),
          ';  dim H(AKh, v_0) =', Hm.shape[1] - 2*v0.rank())
if __name__ == '__main__':
    pt = ([('b', 0, 0)], [])
    report('point a(0)', *union([pt]))
    report('B0 = a(0) + S + hS  (S at (1,2), hS at (2,2))', *union([pt, square(1, 2), square(2, 2)]))
    # 9_42 for comparison: point + squares at h^5 q^8 and h^1 q^2
    report('9_42 (actual): point + squares at (5,8), (1,2)', *union([pt, square(5, 8), square(1, 2)]))
