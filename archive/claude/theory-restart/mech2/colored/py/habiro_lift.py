#!/usr/bin/env python3
"""sigma=0 two-bridge doubles: test  P(N(T_K)) = 1 + A1*B1 + A2*B2  with
Kh~(K) = 1 + A1*C,  C = h^-2 q^-4 (1+h q^2)(1+h^3 q^6)
B1 = h^-4 q^-6 (1+hq^2)(1+h^5q^8)(1+h^2q^2),  B2 = h^-8 q^-12 (1+hq^2)(1+h^5q^8)(1+h^3q^4)(1+h^7q^10)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import lattice
from habiro import knot_kh,D
import sympy as sp
h,q=sp.symbols('h q')
def lp(expr):
    e=sp.expand(expr); out={}
    for term in sp.Add.make_args(e):
        c=term.as_coeff_Mul()[0]
        ph=sp.degree(term*h**200,h)-200 if term.has(h) else 0
        pq=sp.degree(term*q**400,q)-400 if term.has(q) else 0
        out[(int(ph),int(pq))]=out.get((int(ph),int(pq)),0)+int(c)
    return {k:v for k,v in sorted(out.items()) if v}
def fmt(d): return ' + '.join(('%d·'%v if v!=1 else '')+'h^%d q^%d'%k for k,v in d.items())
def run(name):
    kh=knot_kh(name)
    free=[(a,b) for a,b,k in kh if k=='free'][0]
    Kh=sum(h**(a-free[0])*q**(b-free[1]) for a,b,_ in kh)
    C=h**-2*q**-4*(1+h*q**2)*(1+h**3*q**6)
    A1=sp.cancel((Kh-1)/C)
    rho,arc,sq,other=lattice(os.path.join(D,name,'cxBNr-c2-d'))
    if len(arc)!=1: print(name,'sigma!=0, skip'); return
    Sq=sum(h**(a+5*b)*q**(2*a+8*b) for a,b in sq)
    A2=sp.cancel((Sq-A1*(1+h**2*q**2)*h**-4*q**-6)/((1+h**3*q**4)*(1+h**7*q**10)*h**-8*q**-12))
    print('==',name)
    try:
        d1=lp(A1); print('  A1 =',fmt(d1),'  positive' if all(v>0 for v in d1.values()) else '  NOT positive')
    except Exception as ex: print('  A1 not Laurent',A1)
    try:
        d2=lp(A2); print('  A2 =',fmt(d2),'  positive' if all(v>0 for v in d2.values()) else '  NOT positive', ' dim',sum(d2.values()))
    except Exception as ex: print('  A2 not Laurent:',sp.factor(A2))
for n in sys.argv[1:] or ['k5_2','k9_2','k9_4','k13_2','k13_6','k13_8','k17_2','k17_8']:
    run(n)
