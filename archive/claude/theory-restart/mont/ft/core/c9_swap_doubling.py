import random, collections
import clib, lp
from c1_constituents import constituents
MOD=lp.mul(lp.mul(lp.P((-1,0),(1,2)),lp.P((-1,0),(1,3))),lp.P((-1,0),(1,5)))
PHI7={i:1 for i in range(7)}
rnd=random.Random(9); seen=set(); st=collections.Counter(); n=0
letters=['x1','y1','x2','y2','x3','y3']
while n<60:
    body=[rnd.choice(letters) for _ in range(rnd.randint(3,10))]
    w='s.'+rnd.choice(['l1','r1','l2','r2'])+'.'+'.'.join(body)+'.'+rnd.choice(['u1','u2','u3'])
    if w in seen: continue
    seen.add(w); J=lp.J(w)
    if J is None or J=={0:1}: continue
    Vi,Vo=constituents(w)
    if Vo is None or Vo=={0:1}: continue
    n+=1
    V2=lp.mul(Vo,Vo); f=lp.sub({e:c*(-1)**(e%2) for e,c in J.items()},{2*e:c for e,c in V2.items()})
    g,r=clib.pdiv(f,MOD)
    st['I(-t) = V_K\'(t^2)^2 mod (t^2-1)(t^3-1)(t^5-1)' if not r else 'FAIL']+=1
    lo=min(f); q7,r7=clib.pdiv_poly(lp.shift(f,-lo),PHI7)
    st['also Phi_7' if not r7 else 'not Phi_7']+=1
print('swap sums with nontrivial K\':',n,dict(st))
