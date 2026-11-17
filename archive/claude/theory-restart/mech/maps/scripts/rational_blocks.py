import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts')
from typeD import *
from closures import twist, poincare, show

def Qk(k):
    """DD(Q_k), k even, normalized so that the infinity closure is the unknot in bidegree (0,0)."""
    n = abs(k)
    if n == 0: return TD([('b', 0, 0)], {})
    gens = [('b', 0, 0)] + [('c', i, 2 * i - 1) for i in range(1, n + 1)]
    d = {0: [(1, ('S', 'b', 1))]}
    for i in range(1, n):
        d[i] = [(i + 1, ('D', 'c', 1) if i % 2 == 1 else ('S', 'c', 2))]
    X = TD(gens, d); X.check()
    if k > 0: X = X.mirror(); X.check()
    # normalize: BN-type pairing with a_inf : H_* Mor(a_inf, X) should be q^{-1} * (tower generated in (0,0))
    ainf = TD([('c', 0, 0)], {})
    K = cone_H(X)
    t = hom_table(ainf, K, range(-30, 31), range(-80, 81))
    assert len(t) == 1 and list(t.values()) == [1], t
    (h0, q0), = t.keys()
    return X.shift(-h0, -q0)

if __name__ == '__main__':
    ainf = TD([('c', 0, 0)], {}); a0 = TD([('b', 0, 0)], {})
    for k in [0, -4, 4, -8, 8, -12, 12, -2, 2]:
        X = Qk(k); K = cone_H(X)
        qs = [g[2] for g in K.gens]
        print('k =', k, ' r_1(k): mean q =', sum(qs) / len(qs), ' expected k(|k|+2)/(|k|+1) =', k * (abs(k) + 2) / (abs(k) + 1))
        for nu in [2, -2, 4, -4, 6, -6]:
            t = poincare(twist(nu), K)
            s = show(t)
            assert len(s) == 1
            dl, = s.keys()
            lst = s[dl]
            qmin = min(x[1] for x in lst); qmax = max(x[1] for x in lst); dim = sum(x[2] for x in lst)
            print('    nu=%3d  delta=%4.1f  q-range [%d,%d]  dim %d (expected |1-nu k| = %d)' % (nu, dl, qmin, qmax, dim, abs(1 - nu * k)))
