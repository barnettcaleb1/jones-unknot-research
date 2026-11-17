#!/usr/bin/env python3
"""From the junction formula: Newton polygon directions, NP (unique top/bottom t-degree monomial), dimension = |p|,
   for all reduced words with block exponents in a range."""
import sys,os,itertools,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from junction import reduce,junction_poly
from hull_formula import hull,edges
from jmatrix import cf_num,Jw
maxe=int(sys.argv[1]) if len(sys.argv)>1 else 3
maxn=int(sys.argv[2]) if len(sys.argv)>2 else 3
exps=[e for e in range(-maxe,maxe+1) if e!=0]
seen=set(); dirs=collections.Counter(); ex={}; bad=collections.Counter(); tot=0
for n in range(1,maxn+1):
    for blocks in itertools.product(itertools.product(exps,repeat=2),repeat=n):
        w=''.join(('Y' if a>0 else 'y')*abs(a)+('X' if b>0 else 'x')*abs(b) for a,b in blocks)
        r=reduce(w)
        if r in seen or not r: continue
        seen.add(r); tot+=1
        Pj=junction_poly(r)
        p,q=cf_num(blocks)
        if sum(Pj.values())!=abs(p): bad['dim!=p']+=1
        # J check
        J=collections.Counter()
        for (a,b),c in Pj.items(): J[a+4*b]+=c*(-1)**(a+b)
        J={e:c for e,c in J.items() if c}
        Jm=Jw(blocks)
        lo=min(J); lo2=min(Jm)
        A={e-lo:c for e,c in J.items()}; B={e-lo2:c for e,c in Jm.items()}; Bn={e:-c for e,c in B.items()}
        if A!=B and A!=Bn: bad['J']+=1
        td=[k[0]+4*k[1] for k in Pj.elements()]
        if td.count(max(td))!=1 or td.count(min(td))!=1: bad['NP']+=1
        if len(Pj)>2:
            for e in set(e[0] for e in edges(hull(list(Pj)))):
                dirs[e]+=1; ex.setdefault(e,r)
print('reduced words:',tot,' failures:',dict(bad))
for d,c in sorted(dirs.items(),key=lambda kv:-kv[1]): print('  direction',d,c,'e.g.',ex[d])
