import json, collections
import clib, lp
from fractions import Fraction as F
for w in ('s.l1.y0.x1.y0.x1.u2','s.l1.x0.x0.x0.x1.x1.u2'):
    J=lp.J(w); j=clib.j_of(J); a2=lp.a2(J)
    print(w,' J=',sorted(J.items()),' j=',j,' a2=',a2,' M3=',clib.M(J,3),' V_K=',sorted(clib.VK(w).items()))
    for n in (1,-1,2):
        V=clib.V_branch(J,n); c=clib.hexp(V,2)
        sig=-8*j if n%2 else 0
        print('   n=%d V(L_n)=%s det=%d c1=%s c2=%s sigma=%d lambda(Mullins)=%s'%(n,sorted(V.items()),lp.ev(V,-1),c[1],c[2],sig,-c[1]/12-F(sig,8)))
# pattern of M3 differences between the two inversions, all V-classes with >= 2 inversions (length <= 7 enumeration)
import itertools, alex
groups=collections.defaultdict(dict)
letters=['y0','x0','x1','y1']
for L in range(1,8):
    for W in itertools.product(letters,repeat=L):
        if any(W[i][1:]==W[i+1][1:] and W[i][0]!=W[i+1][0] for i in range(L-1)): continue
        w='s.l1.'+'.'.join(W)+'.u2'
        J=lp.J(w)
        if J is None or J=={0:1}: continue
        V=clib.VK(w)
        if V is None or V=={0:1}: continue
        key=tuple(sorted(V.items()))
        groups[key].setdefault(tuple(sorted(J.items())),w)
tab=collections.Counter(); multi=0
for key,d in groups.items():
    if len(d)<2: continue
    if len(d)>2: multi+=1
    rows=[(clib.j_of(dict(k)),clib.M(dict(k),3)) for k in d]
    for (j1,m1),(j2,m2) in itertools.combinations(rows,2):
        if (j1,m1)>(j2,m2): j1,m1,j2,m2=j2,m2,j1,m1
        tab[(j2-j1,(m2-m1))]+=1
print('classes with >2 distinct J (should be 0 for 2-bridge):',multi)
print('(Delta j, Delta M3) over pairs of inversions of the same 2-bridge K:')
for k,v in sorted(tab.items()): print('   ',k,v, '  Delta M3/36 =',F(k[1],36))
