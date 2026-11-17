import sys, time, collections
sys.path.insert(0, '.')
from khsplit import *

def analyse(D, name, verbose=True, show_pairs=True):
    assert D.ncomp == 2, D.ncomp
    t0 = time.time()
    C = Complex(D)
    ok = check_d_squared(C)
    E1 = homology_bigraded(C)
    Htot = homology_bigraded(C, True)
    pairs, ess = pages(C)
    lk = D.linking(0, 1)
    print('%s: crossings %d (mixed %d), lk=%s, n+=%d n-=%d, pointed gens %d, d^2=0 %s' % (name, D.n, sum(D.mixed), lk, D.npos, D.nneg, len(C.gens), ok))
    print('   E_1 = H(X1X2 C, d0), by (h,q):', fmt(E1), ' dim', sum(E1.values()))
    print('   H(X1X2 C, d0+d1) by l:', fmt(Htot), ' dim', sum(Htot.values()))
    # components
    comps = []
    for c in range(2):
        S = SubDiagram(D, c)
        assert len(S.marks) == 1, ('each component must carry exactly one mark', S.marks)
        Hc = homology_bigraded(Complex(S, deform=False))
        comps.append(Hc)
        print('   component %d alone: %d crossings, Kh~ (q shifted by -1) = %s' % (c, S.n, fmt(Hc)))
    T = tensor_l(comps[0], comps[1])
    s = shift_equal(Htot, T)
    print('   Kh~(L1) (x) Kh~(L2) by l:', fmt(T), ' dim', sum(T.values()), '  => total homology is a shift of it:', s is not None, '(shift %s; 2 lk = %s)' % (s, 2 * lk))
    k = 1
    while True:
        P = page_poly(C, pairs, ess, k)
        if k == 1: assert P == E1, (fmt(P), fmt(E1))
        if verbose: print('   E_%d by (h,q): %s   dim %d' % (k, fmt(P), sum(P.values())))
        if all(kk < k for _, _, kk in pairs): break
        k += 1
    Pinf = page_poly(C, pairs, ess, None)
    print('   E_infinity by (h,q): %s   dim %d;   pages needed: collapse at E_%d' % (fmt(Pinf), sum(Pinf.values()), k))
    assert lpoly(Pinf) == Htot
    bideg = collections.Counter()
    for i, g, kk in pairs:
        if kk >= 1:
            dh, dq = C.h[i] - C.h[g], C.q[i] - C.q[g]
            assert (dh, dq) == (1 - 2 * kk, -2 * kk), (kk, dh, dq)
            bideg[kk] += 1
            if show_pairs: print('     d_%d: (h,q)=(%d,%d) -> (%d,%d)' % (kk, C.h[g], C.q[g], C.h[i], C.q[i]))
    print('   nonzero higher differentials by page (bidegree (1-2k,-2k) asserted):', dict(bideg), ' time %.1fs' % (time.time() - t0))
    return dict(D=D, C=C, E1=E1, Htot=Htot, comps=comps, tensor=T, shift=s, pairs=pairs, ess=ess)

def closure13(word, marks=('t0', 'b0')):
    """1-3 tangle word (top; b1,b2,b3) -> closure T(0): join b1-b2 and top-b3; marks on the two closing arcs"""
    return Diagram(word, 1, [('b0', 'b1'), ('t0', 'b2')], list(marks))

def quotient_word(half):
    """kht++ Tangle::quotient() without the framing twists; half = half-diagram word without the prefix 's.'"""
    out = ['r1', 'r2']
    for t in half.split('.'):
        typ, j = t[0], int(t[1:])
        if typ in 'xy':
            if j == 0: out += [typ + '0', typ + '1', typ + '1', typ + '0']
            else: out += [typ + str(2 * j), typ + str(2 * j - 1), typ + str(2 * j + 1), typ + str(2 * j)]
        elif typ in 'lr':
            out += [typ + str(2 * j - 1), typ + str(2 * j)]
        elif typ == 'u':
            out += ['u' + str(2 * j), 'u' + str(2 * j - 1)]
    out.append('u0')
    return '.'.join(out)

def cable2(word):
    """blackboard 2-cable of a Morse word (strand j -> strands 2j, 2j+1)"""
    out = []
    for t in word.split('.'):
        typ, i = t[0], int(t[1:])
        if typ in 'lr': out += [typ + str(2 * i), typ + str(2 * i + 1)]
        elif typ == 'u': out += ['u' + str(2 * i + 1), 'u' + str(2 * i)]
        else: out += [typ + str(2 * i + 1), typ + str(2 * i), typ + str(2 * i + 2), typ + str(2 * i + 1)]
    return '.'.join(out)

def double_closure(word11):
    """closed blackboard 2-cable of the knot given as a 1-1 tangle word; marks = two parallel points"""
    return Diagram(cable2(word11), 2, [('t0', 'b0'), ('t1', 'b1')], ['t0', 't1'])
