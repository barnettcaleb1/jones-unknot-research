"""Formal examples for REPORT sections 4.2 and 4.6. Specials as (c'', 2d'')."""
from collections import Counter
def prof(S):
    lv=sorted(set(d for c,d in S)); return [(d,min(c for c,dd in S if dd==d),max(c for c,dd in S if dd==d)) for d in lv]
def tilt(S,step):
    pr=prof(S); return all(pr[i+1][0]-pr[i][0]==step for i in range(len(pr)-1)) and all(pr[i+1][1]<pr[i][1] and pr[i+1][2]<pr[i][2] for i in range(len(pr)-1))
def Jset(S,k):
    J=Counter(); J[(2*k,0)]+=1
    for (c,e),m in S.items(): J[(c+4,(e-1)//2)]+=m; J[(c-4,(e+1)//2)]+=m
    return J
def sumrule(S1,k1,S2,k2):
    S=Counter()
    for (c,e),m in S1.items(): S[(c+2*k2,e)]+=m
    for (c,e),m in S2.items(): S[(c+2*k1,e)]+=m
    for (c1,e1),m1 in S1.items():
        for (c2,e2),m2 in S2.items(): S[(c1+c2+4,e1+e2-1)]+=m1*m2; S[(c1+c2-4,e1+e2+1)]+=m1*m2
    return S
# 4.2
S=Counter({(106,1):1,(100,3):1})
print('4.2 factor: TILT',tilt(S,2),'J-TILT',tilt(Jset(S,0),1),'profile',prof(S))
SS=sumrule(S,0,S,0); print('    sum profile (level=2d\'\'):',prof(SS),'TILT',tilt(SS,2), sorted(SS.items()))
# sign / divisibility check with sympy
import sympy as sp
q=sp.symbols('q')
P=sum(m*(-1)**((c//2-(e+1)//2)%2)*q**c for (c,e),m in S.items())
J=sp.expand(1-(q**4-q**-4)*P)
print('    P =',sp.factor(P),'; (J-1) divisible by (1+q^2)^2:',sp.rem(sp.expand((J-1)*q**4),(1+q**2)**2,q)==0, '; P divisible by 1+q^6:',sp.rem(P,1+q**6,q)==0)
# 4.6: J-TILT without TILT(S)
S2=Counter({(4,-1):1,(14,-1):1,(-4,1):1,(-12,3):1,(-4,3):1})
print('4.6 example: TILT(S)',tilt(S2,2),prof(S2),' J-TILT',tilt(Jset(S2,0),1),prof(Jset(S2,0)))
# B: a(0)+S+hS at Kh level: specials (c+1,d+1/2),(c-1,d+1/2),(c+1,d-1/2),(c-1,d-1/2) with c even -> take c=20,d=3 (centred, j=0,k=0)
c,d2=20,6
B=Counter({(c+1,d2+1-1):1,(c-1,d2+1-1):1,(c+1,d2-1-1):1,(c-1,d2-1-1):1})
print('B specials',sorted(B.items()),'TILT',tilt(B,2))
