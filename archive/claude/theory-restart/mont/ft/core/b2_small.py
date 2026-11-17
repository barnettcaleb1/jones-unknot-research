# Enumerate short TH-2BR-type words s.l1.W.u2 (W over y0,x0,x1,y1) and record (V_K, J, j, M_k) for small knots.
import sys, itertools, collections
import clib, lp
from fractions import Fraction as F
targets={'RHT':{1:1,3:1,4:-1},'LHT':{-1:1,-3:1,-4:-1},'4_1':{-2:1,-1:-1,0:1,1:-1,2:1}}
def key(V): return tuple(sorted(V.items()))
found=collections.defaultdict(dict)
letters=['y0','x0','x1','y1']
for L in range(1,7):
    for W in itertools.product(letters,repeat=L):
        # skip immediately cancelling pairs
        if any(W[i][1:]==W[i+1][1:] and W[i][0]!=W[i+1][0] for i in range(L-1)): continue
        for cap,cup in (('l1','u2'),('r1','u1'),('l1','u1'),('r1','u2')):
            w='s.'+cap+'.'+'.'.join(W)+'.'+cup
            J=lp.J(w)
            if J is None: continue
            V=clib.VK(w)
            if V is None: continue
            for name,T in targets.items():
                if key(V)==key(T):
                    found[name].setdefault(key(J),w)
for name in targets:
    print(name, len(found[name]),'distinct J')
    for kJ,w in sorted(found[name].items(),key=lambda kv:len(kv[1]))[:8]:
        J=dict(kJ)
        print('   ',w,' J=',kJ,' J\'(1)=',clib.der(J,1,1),' M2..M4=',[clib.M(J,k) for k in (2,3,4)])
