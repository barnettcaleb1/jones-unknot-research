# Core (a2 = 0) samples: first nonzero moment k0, its value, and sign patterns (positivity test); span of J; crossings.
import sys, random, collections
import clib, lp
from fractions import Fraction as F
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
rows=[]; seen=set(); tries=0
while len(rows)<N and tries<400000:
    tries+=1
    w,J=clib.randJ(rnd,6,18)
    if w in seen: continue
    seen.add(w)
    if clib.M(J,2)!=0 or J=={0:1}: continue
    V=clib.VK(w)
    if V is None: continue
    ms=[clib.M(J,k) for k in range(0,12)]
    k0=next(k for k in range(1,12) if ms[k]!=0)
    ncross=sum(1 for t in w.split('.') if t[0] in 'xy')
    rows.append((w,k0,ms,lp.span(J),V=={0:1},ncross,clib.j_of(J)))
print('core samples',len(rows),'(tries',tries,')')
print('K unknot (V_K=1) among core samples:',sum(1 for r in rows if r[4]))
print('k0 distribution:',collections.Counter(r[1] for r in rows))
print('M3 sign:',collections.Counter((r[2][3]>0)-(r[2][3]<0) for r in rows))
m4=[r for r in rows if r[2][3]==0]
print('rows with M3=0:',len(m4),' sign of M4 there:',collections.Counter((r[2][4]>0)-(r[2][4]<0) for r in m4))
print('M4 sign overall:',collections.Counter((r[2][4]>0)-(r[2][4]<0) for r in rows))
print('M4/288 integer & = q\'_1+4 q\'_0 form check:',all((r[2][4]-16*r[2][3])%288==0 for r in rows))
print('span(J) min/median:',min(r[3] for r in rows),sorted(r[3] for r in rows)[len(rows)//2])
for r in rows:
    if r[1]>=4: print('  k0>=4 example:',r[0],' moments',r[2][:7],' span',r[3],' crossings',r[5],' j',r[6])
