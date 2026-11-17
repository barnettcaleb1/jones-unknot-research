import sys
sys.path.insert(0, sys.argv[1])
from bracket import *
def analyse(a, b, m0, label):
    X = hsum(column(a), column(b))
    T = stack(X, column(m0))
    v, eta = T
    print('==', label, ': T = P(%d,%d) o c^%d' % (a, b, m0))
    print(' N-closure bracket (unknot, unit):', show(Ncl(T)))
    print(' coefficient of V :', show(v))
    print(' coefficient of H (eta, the defect):', show(eta))
    for name, q in (('1-A^16', P((1,0),(-1,16))), ('1-A^8', P((1,0),(-1,8))), ('1+A^8', P((1,0),(1,8))), ('1-A^4',P((1,0),(-1,4))), ('1+A^4',P((1,0),(1,4)))):
        r = divide(eta, q)
        print('  eta /(%s):' % name, show(r) if r is not None else 'not divisible')
    Dc = Dcl(T)
    print(' D-closure bracket (tau(0)):', show(Dc))
    # tau(0)-contribution of the defect: eta*(1-d^2)
    print(' eta*(1-d^2):', show(mul(eta, add(ONE, neg(mul(d, d))))))
    print(' unit*d part: ', show(mul(Ncl(T), d)))
    return T
T = analyse(-2, 3, 6, 'trefoil A')
T2 = analyse(2, -3, -6, 'trefoil B (mirror)')
