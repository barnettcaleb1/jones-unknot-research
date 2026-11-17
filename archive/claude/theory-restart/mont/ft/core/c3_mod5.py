# F3's integrality of iota = (M3/36 - 7 v3)/5 is a mod-5 congruence M3/36 = 2 v3 (mod 5). Test it, and look for its source:
# J vs V_K at t = -1 / 5th roots / mod (5, ...).
import sys, random, collections
import clib, lp
from fractions import Fraction as F
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
cnt=collections.Counter(); seen=set(); rows=[]
while len(rows)<N:
    w,J=clib.randJ(rnd,6,16)
    if w in seen: continue
    seen.add(w); V=clib.VK(w)
    if V is None: continue
    a2=clib.a2_of_V(V); v3=clib.v3_of_V(V)
    M3=clib.M(J,3); M4=clib.M(J,4)
    r=(F(M3,36)-7*v3)
    cnt[('iota integer' if r%5==0 else 'iota NOT integer')]+=1
    rows.append((w,J,V,a2,v3,M3,M4))
print(dict(cnt))
# moments of V_K at t=-1 and J: look for congruences  M_k(J) vs N_k(V) := sum V_e (-1)^e e^k
def N(V,k): return sum(c*(-1)**(e%2)*e**k for e,c in V.items())
for k in range(1,5):
    for mod in (2,3,4,5,8,9,16):
        ok=all((clib.M(J,k)-N(V,k))%mod==0 for (w,J,V,a2,v3,M3,M4) in rows)
        if ok: print('  M_%d(J) = N_%d(V_K) mod %d holds on all'%(k,k,mod))
