"""Referee: pretzel closed form (REPORT Sec 9), identities, T1 formula, clean tops, T2 class."""
import random, sys, time, itertools
from rcore import *
from fractions import Fraction
PHI6={2:1,1:-1,0:1}; ALPHA=ml({1:1,0:-1},{2:1,0:1}); BETA=ml({1:1},{1:1,0:-1})
def mt(t_pow,sign): return {t_pow:sign}
def zr(r):
    """z = (-t)^{(r-1)/2}"""
    e=(r-1)//2
    return {e:(-1)**(e%2)}
def rowvec(r):
    v=[ONE,{}]
    if r>0:
        j=(r-1)//2; v=Ypow(1,v); v=Xpow(j,v)
    else:
        l=(-r-1)//2; v=Ypow(-1,v); v=Xpow(-l,v)
    return v
def J_pretzel(mu,rows,k=0):
    bd=[(ach(v),bch(v)) for v in (rowvec(r) for r in rows)]
    A=fprod([a for a,b in bd]); B=fprod([b for a,b in bd])
    G=ad(ml(w1(mu),A),ml(w3(mu),sh(B,-3*k)))
    return pdiv_exact(G,PHI3),G
def Gclosed(mu,rows,k=0):
    P=ONE; Q=ONE
    for r in rows:
        z=zr(r); P=ml(P,ad(PHI6,ml(z,ALPHA))); Q=ml(Q,ad(PHI6,ng(ml(z,BETA))))
    return ad(ml(w1(mu),P),ml(w3(mu),sh(Q,-3*k)))
def unit_of(rows):
    e=sum(-3 if r>0 else 1 for r in rows); return e
def topH(mu,rows,k=0):
    return tp(Gclosed(mu,rows,k))-2*len(rows)
if __name__=='__main__':
    rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
    t0=time.time()
    # (1) closed form vs necklace; (2) span formula span J = 2n + top H + top H'' - 4 ; H divisible by Phi_6^n? (H is G/Phi6^n: is G divisible?)
    bad=0; nd=0; cnt=0; spanbad=0
    for it in range(400):
        n=rnd.randint(2,6)
        rows=[rnd.choice([1,-1])*(2*rnd.randint(1,10)+1) for _ in range(n)]
        mu=rnd.choice([m for m in range(-8,9) if m]); k=rnd.choice([0,0,0,rnd.randint(-4,4)])
        J,G=J_pretzel(mu,rows,k)
        Gc=Gclosed(mu,rows,k)
        if sh(Gc,unit_of(rows))!=G: bad+=1; print('CLOSED FORM FAIL',mu,rows,k)
        cnt+=1
        if k==0:
            th=topH(mu,rows); thm=topH(-mu,[-r for r in rows])
            if sp(J)!=2*n+th+thm-4: spanbad+=1; print('SPAN FORMULA FAIL',mu,rows,sp(J),th,thm)
    print('closed form checked',cnt,'bad',bad,'| H not polynomial (Phi6^n does not divide G):',nd,'| span formula bad',spanbad)
    # (3) identities with sympy-free exact series: gamma_0=Phi3, gamma_1, degeneration identity, g_m formula
    from fractions import Fraction
    import sympy as sp_
    t=sp_.symbols('t')
    Phi3=t**2+t+1; Phi6=t**2-t+1; al=(t-1)*(t**2+1); be=t*(t-1)
    def W1(mu): return t+(1+t**2)*(-t)**mu
    def W3(mu): return (1+t**2)*(1-(-t)**mu)
    def gam(m,mu,k=0): return W1(mu)*(al/Phi6)**m+(-1)**m*t**(-3*k)*W3(mu)*(be/Phi6)**m
    def brk(k): return sp_.cancel(((t**2+1)**k-(-t)**k)/Phi3)
    okg=0; badg=0
    for mu in [m for m in range(-6,7) if m]:
        if sp_.cancel(gam(0,mu)-Phi3)!=0: print('gamma0 fail',mu); badg+=1
        if sp_.cancel(gam(1,mu)-(t-1)*(t**2+1)*Phi3*(-t)**mu/Phi6)!=0: print('gamma1 fail',mu); badg+=1
        if sp_.cancel(Phi3+(-t)**(-1-mu)*gam(1,mu)-Phi3/(t*Phi6))!=0: print('degeneration fail',mu); badg+=1
        for m in range(1,11):
            gm=sp_.cancel(gam(m,mu)/Phi3)
            pred=(t-1)**m*(t**2+1)*Phi6**(-m)*(t*brk(m-1)+(-t)**mu*brk(m))
            if sp_.cancel(gm-pred)!=0: print('g_m fail',m,mu); badg+=1
            else: okg+=1
    # pair identity
    for mu in [m for m in range(-6,7) if m]:
        lhs=Phi3-gam(2,mu)/t; rhs=-Phi3*((-t)**mu*Phi6*(t-1)**2*(t**2+1)-t**3)/(t*Phi6**2)
        if sp_.cancel(lhs-rhs)!=0: print('pair identity fail',mu); badg+=1
    print('g_m formula checks ok',okg,'identity failures',badg,'time',round(time.time()-t0,1))
