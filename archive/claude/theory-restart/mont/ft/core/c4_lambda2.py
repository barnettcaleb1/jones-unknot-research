# Lin-Wang (Geom. Topol. Monogr. 2 (1999), Fermat limit..., Thm 4.3), converted to our (standard-skein) V convention:
#   lambda_1(S^3_{1/n}K) = 6 n a2,   lambda_2(S^3_{1/n}K) = -3 n a2 - 12 n v3 + n^2 (-6 a2 + 60 a2^2 - 60 a4)
# (our v3 = -(V'''(1)+3V''(1))/36; LW's V(K;t) is our V(K;1/t), so v3^{LW} = 36 v3).  Checks: S^3_{+1}(RHT) -> 39 (Poincare),
# S^3_{+1}(LHT) -> 63 (Sigma(2,3,7)), lambda_2(-M) = lambda_2(M) + lambda_1(M).
# Identity to verify:  c2(L_n) = -lambda_2 + 60 lam^2 + 18 sigma lam - 3 lam + (9/8) sigma^2 + n (M3/6 - 12 v3) - 60 n^2 a4.
import clib, lp, alex, sympy as sp
from fractions import Fraction as F
def conway_a4(word):
    t=sp.symbols('t'); D=alex.alex_poly(word)
    D=sp.Poly(sp.expand(D),t); cs=D.all_coeffs()[::-1]
    while cs and cs[0]==0: cs=cs[1:]
    deg=len(cs)-1; assert deg%2==0
    s=sum(cs)
    cs=[c*s for c in cs]           # Delta(1)=1 (s=+-1)
    # symmetric Laurent: Delta = sum_k c_k t^(k - deg/2); expand in z^2 = t - 2 + 1/t
    z2=sp.symbols('z2'); h=deg//2
    expr=sum(sp.Integer(c)*sp.Symbol('T')**(k-h) for k,c in enumerate(cs))
    # use t^m + t^-m = polynomial in u = t + 1/t = z2 + 2 (Chebyshev)
    u=sp.symbols('u'); P={0:sp.Integer(2),1:u}
    for m in range(2,h+1): P[m]=sp.expand(u*P[m-1]-P[m-2])
    poly=sp.Integer(cs[h])+sum(sp.Integer(cs[h+m])*P[m] for m in range(1,h+1))
    poly=sp.expand(poly.subs(u,z2+2))
    pp=sp.Poly(poly,z2)
    return int(pp.coeff_monomial(z2**2)) if pp.degree()>=2 else 0, int(pp.coeff_monomial(z2)), int(pp.coeff_monomial(1))
def lam2(n,a2,v3,a4): return -3*n*a2-12*n*v3+n*n*(-6*a2+60*a2*a2-60*a4)
print('S3_{+1}(RHT):',lam2(1,1,1,0),' S3_{+1}(LHT):',lam2(1,1,-1,0),' S3_{-1}(RHT):',lam2(-1,1,1,0),' S3_{+1}(4_1):',lam2(1,-1,0,0))
cases={'RHT':'s.l1.y0.x1.u2','LHT':'s.l1.x0.y1.u2','4_1 h1':'s.l1.y0.y0.x1.u2','4_1 h2':'s.l1.x0.x0.y1.u2',
       '6_2 h':'s.l1.y0.x1.y0.x1.u2','6_2 h\'':'s.l1.x0.x0.x0.x1.x1.u2'}
for nm,w in cases.items():
    J=lp.J(w); V=clib.VK(w); a2=clib.a2_of_V(V); v3=clib.v3_of_V(V); a4,a2c,one=conway_a4(w)
    assert a2c==a2 and one==1
    j=clib.j_of(J); M3=clib.M(J,3); iota=(F(M3,36)-7*v3)/5
    out=[]
    for n in (1,-1,2,-2,3,-3):
        c=clib.hexp(clib.V_branch(J,n),2)
        sig=-8*j if n%2 else 0; lam=n*a2
        rhs=-lam2(n,a2,v3,a4)+60*lam*lam+18*sig*lam-3*lam+F(9,8)*sig*sig+n*(F(M3,6)-12*v3)-60*n*n*a4
        P=-lam2(n,a2,v3,a4)+60*lam*lam+18*sig*lam-3*lam+F(9,8)*sig*sig
        out.append((n,c[2]==rhs,c[2],P,(c[2]-P)%30))
    print(nm,'a2=%s v3=%s a4=%s j=%d M3=%d iota=%s'%(a2,v3,a4,j,M3,iota))
    for o in out: print('     n=%2d identity %s  c2=%s  P(lam2,lam,sigma)=%s  (c2-P) mod 30 = %s'%o)
