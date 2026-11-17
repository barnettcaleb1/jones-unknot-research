# Swap-type equivariant connected sums: half-words with no axis letters (x0,y0). Quotient arc is a locally knotted copy of
# K' = K_out = K_in, axis unentangled; J should be the normalised colour-2 Jones of K'. Test: (i) K = K'#rho K' (V_K = V_K'^2),
# (ii) symmetry J(-t) vs J(t), (iii) moments M_k vs t=1 Taylor coefficients.
import itertools, collections, random
import clib, lp
from c1_constituents import constituents
from fractions import Fraction as F
rnd=random.Random(5); seen=set(); rows=[]
letters=['x1','y1','x2','y2','x3','y3']
tries=0
while len(rows)<40 and tries<200000:
    tries+=1
    L=rnd.randint(3,9)
    body=[rnd.choice(letters) for _ in range(L)]
    cap=rnd.choice(['l1','r1','l2','r2']); cup=rnd.choice(['u1','u2','u3'])
    w='s.'+cap+'.'+'.'.join(body)+'.'+cup
    if w in seen: continue
    seen.add(w)
    J=lp.J(w)
    if J is None or J=={0:1}: continue
    V=clib.VK(w); Vi,Vo=constituents(w)
    if V is None or Vo is None: continue
    rows.append((w,J,V,Vo))
print('swap-sum samples',len(rows))
ok_sq=0; sym=collections.Counter(); 
for w,J,V,Vo in rows:
    if V==lp.mul(Vo,Vo): ok_sq+=1
    Jm={e:c*(-1)**(e%2) for e,c in J.items()}   # J(-t)
    # compare J(-t) with +-t^k J(t)
    k=min(J)-min(Jm); s=J[min(J)]*Jm[min(Jm)]
    same = {e+k:c*s for e,c in Jm.items()}==J
    sym['J(-t) = unit*J(t)' if same else 'no t->-t symmetry']+=1
print('V_K = V_{K_out}^2 (connected sum K # rho K):',ok_sq,'/',len(rows))
print(dict(sym))
w,J,V,Vo=rows[0]; print('example',w,' K_out V=',sorted(Vo.items()),' J=',sorted(J.items()))
