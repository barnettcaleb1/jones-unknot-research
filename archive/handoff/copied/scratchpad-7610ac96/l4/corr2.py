import json, cmath, sys
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/tools')
import alex
import sympy as sp
from fractions import Fraction
from math import gcd
data=json.load(open(sys.argv[1]))
def P(d): return {int(Fraction(k)):v for k,v in d.items()}
data=[(w,P(J),P(V)) for w,J,V in data][:80]
def ev(Pd,z): return sum(c*z**e for e,c in Pd.items())
def normP(Pd,m):
    pr=1
    for k in range(1,m+1):
        if gcd(k,m)==1: pr*=ev(Pd,cmath.exp(2j*cmath.pi*k/m))
    return abs(pr)
t=sp.symbols('t')
w3=cmath.exp(2j*cmath.pi/3)
hitsV={}; hitsA={}; rows=[]
for w,J,V in data:
    NJ=round(abs(ev(J,w3))**2)
    D=sp.Poly(sp.expand(alex.alex_poly(w)*t**60),t)
    Dd={}
    for (e,),c in D.terms(): Dd[e]=int(c)
    for m in range(2,31):
        if round(normP(V,m))==NJ: hitsV[m]=hitsV.get(m,0)+1
        if round(normP(Dd,m))==NJ: hitsA[m]=hitsA.get(m,0)+1
    rows.append((NJ, round(normP(Dd,2)), round(normP(Dd,3)), round(normP(Dd,6)), round(normP(V,2))))
print('N(J(w)) == N(V(zeta_m)):',hitsV)
print('N(J(w)) == N(Delta(zeta_m)):',hitsA)
print('(NJ, |D(-1)|, N D(w), N D(z6), detV) first 25:',rows[:25])
