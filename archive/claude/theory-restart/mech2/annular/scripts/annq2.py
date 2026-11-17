#!/usr/bin/env python3
"""Characteristic zero: induced operators on AKh for the standard pieces; checks of v_0 = [e, d_-] = +-2 d_D on N,
of the quiver relations, and of Kh = H(AKh, v_-2)."""
import sys
import sympy as sp
from annq import *

def hom_basis(d0):
    """returns (Zb, Bb, Hb): matrices whose columns are bases of cycles, boundaries, and a complement of B in Z; and a projector"""
    n = d0.shape[0]
    Z = d0.nullspace()
    Bcols = d0.columnspace()
    Bm = sp.Matrix.hstack(*Bcols) if Bcols else sp.zeros(n, 0)
    Hcols = []
    cur = Bm
    for z in Z:
        test = sp.Matrix.hstack(cur, z)
        if test.rank() > cur.rank():
            Hcols.append(z); cur = test
    Hm = sp.Matrix.hstack(*Hcols) if Hcols else sp.zeros(n, 0)
    return Bm, Hm

def induced(op, Bm, Hm):
    """matrix of op on homology in basis Hm (op must be a chain map up to sign)"""
    nb = Bm.shape[1]; nh = Hm.shape[1]
    M = sp.Matrix.hstack(Bm, Hm)
    out = sp.zeros(nh, nh)
    for c in range(nh):
        v = op * Hm[:, c]
        sol, params = M.gauss_jordan_solve(v)
        # unique since columns independent
        out[:, c] = sol[nb:, 0]
    return out

def analyse(name, gens, arrows):
    basis, d0, dm, do, E, F = build(gens, arrows)
    n = len(basis)
    assert do.is_zero_matrix
    d = d0 + dm
    assert (d*d).is_zero_matrix and (d0*d0).is_zero_matrix and (dm*dm).is_zero_matrix and (d0*dm + dm*d0).is_zero_matrix
    Bm, Hm = hom_basis(d0)
    nh = Hm.shape[1]
    e = induced(E, Bm, Hm); f = induced(F, Bm, Hm); vm = induced(dm, Bm, Hm)
    h = e*f - f*e
    v0 = e*vm - vm*e
    print('==', name, ': chain dim', n, ' dim AKh =', nh, ' dim Kh(Q) =', n - 2*d.rank())
    # weights of the homology basis: eigenvalues of h
    print('   h eigenvalues:', sorted(h.eigenvals().items()))
    print('   v_-2^2 = 0:', (vm*vm).is_zero_matrix, ' v0^2 = 0:', (v0*v0).is_zero_matrix, ' [v0, v_-2]_+ = 0:', (v0*vm + vm*v0).is_zero_matrix,
          ' [f, v_-2] = 0:', (f*vm - vm*f).is_zero_matrix, ' [h,v0]=0:', (h*v0 - v0*h).is_zero_matrix)
    print('   dim H(AKh, v_-2) =', nh - 2*vm.rank(), ' dim H(AKh, v_0) =', nh - 2*v0.rank())
    # restrict v0 to weight 2: N = b-generators (x) 11. compare with d_D
    idxN = [i for i, b in enumerate(basis) if b[1] == '11']
    # the homology basis vectors of weight 2 are exactly the chains g(x)11 (no differential in weight 2)
    # express v0 on N in the generator basis
    gensN = [basis[i][0] for i in idxN]
    V0chain = E*dm - dm*E
    M = sp.zeros(len(idxN), len(idxN))
    for a, i in enumerate(idxN):
        for b, j in enumerate(idxN):
            M[b, a] = V0chain[j, i]
    DD = sp.zeros(len(idxN), len(idxN))
    for (s, t, kind, power, coeff) in arrows:
        if kind == 'D' and gens[s][0] == 'b':
            DD[gensN.index(t), gensN.index(s)] += coeff
    print('   chain level v0 on N equals -2 d_D:', (M + 2*DD).is_zero_matrix, ' equals +2 d_D:', (M - 2*DD).is_zero_matrix)
    return basis, e, f, vm, v0, h

if __name__ == '__main__':
    g, a = close_cycle(*chain(['+P', '+D', '-P', '-D'], lam=1)); analyse('unit square, lam=1', g, a)
    g, a = close_cycle(*chain(['+P', '+D', '-P', '-D'], lam=-1)); analyse('unit square, lam=-1', g, a)
    g, a = chain(['+P', '-D']); analyse('zigzag l=1 (x0 -P-> x1 <-D- x2), no tail', g, a)
    g, a = chain(['+P', '-D', '+P', '-D']); analyse('zigzag l=2, no tail (4_1 type)', g, a)
    g, a = chain([]); analyse('point a(0)', g, a)
