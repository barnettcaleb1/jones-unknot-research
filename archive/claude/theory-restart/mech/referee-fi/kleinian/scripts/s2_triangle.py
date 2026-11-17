# Numeric (50 digits) check: at A_n the fixed points of [J],[JM],[M] in the G-negative (and G-positive) disc
# form a hyperbolic triangle with angles pi/2, pi/3, pi/n, for every n>=7 (odd AND even).
# Also: signature of G(A_n), order of [M_n], E_n fixes fix(J), fix(JM) and swaps sides.
from mpmath import mp, mpf, mpc, matrix, exp, pi, sin, cos, acos, acosh, sqrt, eig, cosh, sinh, fabs
mp.dps = 50
def mats(n):
    A = exp(1j*pi/4 - 1j*pi/(2*n))
    d = (-A**2 - A**-2).real
    G = matrix([[d,1],[1,d]])
    M = matrix([[A,0],[1/A,-A**-3]])
    J = matrix([[0,1],[1,0]])
    E = matrix([[d,1],[-1,-d]])
    return A,d,G,M,J,E
def herm(G,v,w):  # <v,w> = v^* G w
    return (v.H*G*w)[0,0]
def fixed(G,X,sign):
    ev, V = eig(X)
    out=[]
    for k in range(2):
        v = V[:,k]
        nv = herm(G,v,v).real
        if nv*sign>0: out.append((v, ev[k], ev[1-k]))
    assert len(out)==1, (len(out))
    return out[0]
def dist(G,v,w):
    c2 = (herm(G,v,w)*herm(G,w,v)).real/(herm(G,v,v).real*herm(G,w,w).real)
    return 2*acosh(sqrt(c2))
def angle(a,b,c):  # angle opposite side c
    return acos((cosh(a)*cosh(b)-cosh(c))/(sinh(a)*sinh(b)))
worst = 0
for n in list(range(2,61))+[101,200,1001]:
    A,d,G,M,J,E = mats(n)
    detG = d*d-1
    sig = 'degenerate' if fabs(detG)<mpf(10)**-40 else ('indefinite' if detG<0 else 'definite')
    if n<7:
        print(n, 'delta=%.6f'%float(d), sig); continue
    assert sig=='indefinite'
    # unitarity
    assert max(abs(x) for x in (M.H*G*M-G)) < mpf(10)**-40
    for sign in (-1,+1):
        p,_,_ = fixed(G,J,sign); q,_,_ = fixed(G,J*M,sign); r,l1,l2 = fixed(G,M,sign)
        a = dist(G,q,r); b = dist(G,p,r); c = dist(G,p,q)
        angP = angle(b,c,a); angQ = angle(a,c,b); angR = angle(a,b,c)
        err = max(fabs(angP-pi/2), fabs(angQ-pi/3), fabs(angR-pi/n))
        worst = max(worst, err)
        assert err < mpf(10)**-35, (n, sign, angP, angQ, angR)
        # E swaps the two discs.  Under the identification of the two discs by the inversion
        # iota: [v] -> [v]^perp (G-orthogonal line), E fixes p and q: E p is G-orthogonal to p, same for q.
        for v in (p,q):
            w = E*v
            assert herm(G,w,w).real*sign < 0          # E v lies in the other disc
            assert abs(herm(G,v,w)) < mpf(10)**-40     # and is the mirror image iota(v)
        # E does NOT fix r in that sense (it is the reflection in the side pq)
        w = E*r; assert abs(herm(G,r,w)) > mpf(10)**-10
    # eigenvalue ratio of M_n is exp(-2 pi i/n) : rotation by exactly 2pi/n, order n
    rat = A/(-A**-3)
    assert abs(rat - exp(-2j*pi/n)) < mpf(10)**-40
    # multiplier of E negative
    assert (d*d-1) < 0
    if n in (7,8,12,30,31,33,1001): print(n, 'delta=%.6f'%float(d), sig, 'triangle angles = pi/2, pi/3, pi/%d verified on both discs'%n)
print('max angle error over n in 7..60,101,200,1001 :', worst)
