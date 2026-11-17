"""Pretzel closed form: J*Phi3 = unit * [w1 prod(Phi6 + z_i alpha) + w3 t^{-3k} prod(Phi6 - z_i beta)],  z_i = (-t)^{(r_i-1)/2}."""
from nt import *
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from lp import apply
PHI6=P((1,0),(-1,1),(1,2)); ALPHA=P((-1,0),(1,1),(-1,2),(1,3)); BETA=P((-1,1),(1,2))
def w1(mu): return add(mono(1),mul(P((1,0),(1,2)),mono(mu,(-1)**abs(mu))))
def w3(mu): return mul(P((1,0),(1,2)),sub(ONE,mono(mu,(-1)**abs(mu))))
def zz(r):
    e=(r-1)//2; return mono(e,(-1)**abs(e))
def G(mu,rows,k=0):
    A=ONE; B=ONE
    for r in rows:
        A=mul(A,add(PHI6,mul(zz(r),ALPHA))); B=mul(B,sub(PHI6,mul(zz(r),BETA)))
    return add(mul(w1(mu),A),shift(mul(w3(mu),B),-3*k))
def vrow(r):
    j=(abs(r)-1)//2
    return apply(('X'*j+'Y') if r>0 else ('x'*j+'y'))
def Jdirect(mu,rows,k=0):
    p=vrow(rows[0])
    for r in rows[1:]: p=star(p,vrow(r))
    p=Ypow(k,p); return Xpow(mu,p)[0]
if __name__=='__main__':
    PHI3=P((1,0),(1,1),(1,2))
    import random
    rnd=random.Random(3); bad=0
    for _ in range(300):
        n=rnd.randint(2,4); rows=[rnd.choice([3,5,7,9,-3,-5,-7,-9]) for _ in range(n)]
        mu=rnd.choice([m for m in range(-5,6) if m]); k=rnd.randint(-2,2)
        lhs=mul(Jdirect(mu,rows,k),PHI3); rhs=G(mu,rows,k)
        # compare up to unit: ratio must be a monomial
        e1,e2=top(lhs),top(rhs); c=Fraction(lhs[e1],rhs[e2]) if False else None
        sh=e1-e2; s=lhs[e1]//rhs[e2]
        if {e+sh:s*c_ for e,c_ in rhs.items()}!=lhs: bad+=1; print('BAD',mu,rows,k)
    print('closed form checked 300, bad',bad)
