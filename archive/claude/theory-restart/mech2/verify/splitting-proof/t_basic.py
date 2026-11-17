import sys, collections, time
sys.path.insert(0, '.')
from khsplit import *

def reduced_kh(word, ntop, joins, mark):
    D = Diagram(word, ntop, joins, [mark])
    C = Complex(D, deform=False)
    return D, homology_bigraded(C)

D, H = reduced_kh('r1.y0.y0.y0.u1', 1, [('t0', 'b0')], 't0')
print('RH trefoil r1.y0.y0.y0.u1: n+,n- =', D.npos, D.nneg, ' H(X_p C) =', fmt(H), '  [kht++: q^2 + q^6 h^2 + q^8 h^3, here shifted by q^-1]')
D, H = reduced_kh('', 1, [('t0', 'b0')], 't0')
print('unknot: ', fmt(H))
D, H = reduced_kh('l1.l2.x0.y1.x0.y1.u2.u1', 1, [('t0', 'b0')], 't0')
print('4_1 (3-braid): n+,n- =', D.npos, D.nneg, ' H =', fmt(H))
D, H = reduced_kh('l1.l2.y0.y1.y0.y1.y0.y1.y0.y1.u2.u1', 1, [('t0', 'b0')], 't0')
print('T(3,4): n+,n- =', D.npos, D.nneg, ' H =', fmt(H))

def pointed(word, name, verbose=True):
    """1-3 tangle word; closure T(0) = join b0-b1 and t0-b2; marks on the two closing arcs"""
    D = Diagram(word, 1, [('b0', 'b1'), ('t0', 'b2')], ['t0', 'b0'])
    assert D.ncomp == 2, D.ncomp
    C = Complex(D)
    ok = check_d_squared(C)
    E1 = homology_bigraded(C)
    Htot = homology_bigraded(C, True)
    pairs, ess = pages(C)
    print('%s: crossings %d (mixed %d), lk=%s, pointed gens %d, d^2=0 %s' % (name, D.n, sum(D.mixed), D.linking(0, 1), len(C.gens), ok))
    print('   E_1 = H(X1X2 C, d0), by (h,q):', fmt(E1), ' dim', sum(E1.values()))
    print('   H(X1X2 C, d0+d1) by l:', fmt(Htot), ' dim', sum(Htot.values()))
    k = 1
    while True:
        P = page_poly(C, pairs, ess, k)
        if k == 1: assert P == E1, (fmt(P), fmt(E1))
        print('   E_%d by (h,q): %s   dim %d' % (k, fmt(P), sum(P.values())))
        if all(kk < k for _, _, kk in pairs): break
        k += 1
    for i, g, kk in sorted(pairs, key=lambda t: t[2]):
        if kk >= 1: print('     d_%d: (h,q)=(%d,%d) -> (%d,%d)' % (kk, C.h[g], C.q[g], C.h[i], C.q[i]))
    return D, C, E1, Htot

pointed('l0.x1.x1', 'Hopf = closure of Q_2')
pointed('l0.x1.x1.x1.x1', 'T(2,4) = closure of Q_4')
pointed('l0.y1.y1', 'Hopf mirror')
