from nt import *
from fractions import Fraction
def series(num,den,n=12): return ser_div(num,den,n)
def fmt(s): return ' '.join(f"{c}t^{e}" for e,c in s)
# kappa = -t/(1+t^2); Z_mu = -w1/w3
def w1(mu):
    if mu>=0: tm=P(((-1)**mu,mu))
    else: tm=P(((-1)**(-mu),mu))
    return add(mono(1),mul(P((1,0),(1,2)),tm))
def w3(mu):
    tm=P(((-1)**abs(mu),mu))
    return mul(P((1,0),(1,2)),sub(ONE,tm))
for mu in (1,2,3,-1,-2,-3,-4):
    print('Z',mu, fmt(series(neg(w1(mu)),w3(mu),9)))
print('kappa',fmt(series(mono(1,-1),P((1,0),(1,2)),8)))
for s in [(-2,),(-2,-2,1),(1,),(1,1),(1,1,1),(-2,1),(2,),(1,2),(-2,-1),(-2,-1,-1)]:
    a,b=chan(box(s))
    print(s,'q=',fmt(series(b,a,9)))
