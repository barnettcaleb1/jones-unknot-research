#!/usr/bin/env python3
"""From the junction formula: Euler characteristics of d_P and d_D (P at y=-1, at x=-1 are monomials?), and the decomposition
   P = staircase + (1+x)(1+y) Pi with Pi >= 0 (staircase from rho to x_0, either orientation)."""
import sys,os,itertools,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from junction import reduce,junction_poly
maxe=int(sys.argv[1]) if len(sys.argv)>1 else 3
maxn=int(sys.argv[2]) if len(sys.argv)>2 else 3
exps=[e for e in range(-maxe,maxe+1) if e!=0]
def stair(rho,l):
    # l >= 0: rho, rho+D, rho+D-P, ... ending at rho + l(D-P);  l < 0: rho, rho-D? (mirror) rho, rho - D, rho - D + P, ...
    pts=[]
    if l>=0:
        for i in range(l+1): pts.append((rho[0]+i,rho[1]-i))
        for i in range(l): pts.append((rho[0]+i+1,rho[1]-i))
    else:
        m=-l
        for i in range(m+1): pts.append((rho[0]-i,rho[1]+i))
        for i in range(m): pts.append((rho[0]-i-1,rho[1]+i))
    return collections.Counter(pts)
def divide_square(d):
    d=collections.Counter(d)
    if any(v<0 for v in d.values()): return None
    out=collections.Counter()
    for k in sorted(d):
        v=d[k]
        if v==0: continue
        if v<0: return None
        for dk in ((0,0),(1,0),(0,1),(1,1)):
            q=(k[0]+dk[0],k[1]+dk[1])
            if d[q]<v: return None
            d[q]-=v
        out[k]+=v
    return out
seen=set(); bad=collections.Counter(); tot=0
for n in range(1,maxn+1):
    for blocks in itertools.product(itertools.product(exps,repeat=2),repeat=n):
        w=''.join(('Y' if a>0 else 'y')*abs(a)+('X' if b>0 else 'x')*abs(b) for a,b in blocks)
        r=reduce(w)
        if r in seen or not r: continue
        seen.add(r); tot+=1
        Pj=junction_poly(r)
        ey=collections.Counter(); ex=collections.Counter()
        for (a,b),c in Pj.items(): ey[a]+=c*(-1)**b; ex[b]+=c*(-1)**a
        ey={k:v for k,v in ey.items() if v}; ex={k:v for k,v in ex.items() if v}
        if len(ey)!=1 or abs(list(ey.values())[0])!=1: bad['y=-1 not monomial']+=1; continue
        if len(ex)!=1 or abs(list(ex.values())[0])!=1: bad['x=-1 not monomial']+=1; continue
        # rho: the generator surviving at y=-1 has a-coordinate a_r ; x_0 surviving at x=-1 has b-coordinate b_0
        a_r=list(ey)[0]; b_0=list(ex)[0]
        # staircase: rho=(a_r,b_r), x_0=(a_r+l, b_r-l) with b_r - l = b_0 ; try all rho on column a_r
        okk=False
        for (a,b) in Pj:
            if a!=a_r: continue
            l=b-b_0
            d=collections.Counter(Pj); d.subtract(stair((a,b),l))
            if divide_square(d) is not None: okk=True; break
        if not okk: bad['no staircase+squares decomposition']+=1
print('reduced words:',tot,'failures:',dict(bad))
