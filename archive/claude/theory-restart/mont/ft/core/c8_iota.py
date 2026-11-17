# (1) f = 0 cases: are they unknots (V_K = 1)?  (2) iota = g(1) - 3 v3 with g = (J(-t)-V_K(t^2))/((t^2-1)(t^3-1)(t^5-1)).
import random, collections
import clib, lp
from fractions import Fraction as F
MOD=lp.mul(lp.mul(lp.P((-1,0),(1,2)),lp.P((-1,0),(1,3))),lp.P((-1,0),(1,5)))
rnd=random.Random(77); seen=set(); st=collections.Counter(); n=0
while n<400:
    w,J=clib.randJ(rnd,6,18)
    if w in seen: continue
    seen.add(w); V=clib.VK(w)
    if V is None: continue
    n+=1
    f=lp.sub({e:c*(-1)**(e%2) for e,c in J.items()},{2*e:c for e,c in V.items()})
    if not f:
        st['f=0, V_K=1' if V=={0:1} else 'f=0 but V_K!=1']+=1
        if V!={0:1}: print('nontrivial exact case:',w,sorted(J.items()))
        continue
    g,r=clib.pdiv(f,MOD)
    if r: st['not divisible']+=1; continue
    v3=clib.v3_of_V(V); M3=clib.M(J,3)
    iota=(F(M3,36)-7*v3)/5
    st['iota == g(1)-3v3' if iota==lp.ev(g,1)-3*v3 else 'iota formula FAILS']+=1
print(dict(st))
