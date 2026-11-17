import json, cmath, sys
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/tools')
import alex
from fractions import Fraction
from math import gcd
data=json.load(open(sys.argv[1]))
def P(d): return {int(Fraction(k)):v for k,v in d.items()}
data=[(w,P(J),P(V)) for w,J,V in data][:120]
def ev(Pd,z): return sum(c*z**e for e,c in Pd.items())
def normV(Pd,m):
    pr=1
    for k in range(1,m+1):
        if gcd(k,m)==1: pr*=ev(Pd,cmath.exp(2j*cmath.pi*k/m))
    return abs(pr)
def normA(word,m):
    pr=1
    for k in range(1,m+1):
        if gcd(k,m)==1:
            v=alex.alex_eval(word,cmath.exp(2j*cmath.pi*k/m))
            if v is None: return None
            pr*=v
    return abs(pr)
w3=cmath.exp(2j*cmath.pi/3)
hitsV={m:0 for m in range(2,31)}; hitsA={m:0 for m in range(2,31)}
hitsA2={}
n=0
for w,J,V in data:
    NJ=round(abs(ev(J,w3))**2)
    n+=1
    for m in range(2,31):
        if round(normV(V,m))==NJ: hitsV[m]+=1
        a=normA(w,m)
        if a is not None and round(a)==NJ: hitsA[m]+=1
print('samples',n)
print('N(J(w)) == N(V(zeta_m)) counts:',{m:c for m,c in hitsV.items() if c})
print('N(J(w)) == N(Delta(zeta_m)) counts:',{m:c for m,c in hitsA.items() if c})
