#!/usr/bin/env python3
"""Check the two closed formulas for N(T_K):
 (T) K = T(2,2n+1):  staircase(4n+1) from rho + squares at (m-3s, -m+s), 1<=m<=2n-1, 1<=s<=min(m,2n-m).
 (W) K = twist knot K_p (two-bridge (4p+1)/2):  point + squares at (2s+1,-1),(2s-2,0) (s<p) and
      (2(s+s')-3c+2, c-2) + {(0,0),(-2,1),(-3,2),(-5,3)},  c = 2min(s,s')+[s>s'].   Mirror: (a,b)->(-a,-b) with squares' corners adjusted."""
import sys,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import lattice
D='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'
def pts_of(arc,sq):
    P=list(arc)
    for a,b in sq: P+=[(a,b),(a+1,b),(a,b+1),(a+1,b+1)]
    return collections.Counter(P)
def torus(n):
    arc=[]
    for i in range(2*n): arc+=[(i,-i),(i+1,-i)]
    arc.append((2*n,-2*n))
    sq=[(m-3*s,-m+s) for m in range(1,2*n) for s in range(1,min(m,2*n-m)+1)]
    return pts_of(arc,sq)
def twist(p):
    sq=[]
    for s in range(p): sq+=[(2*s+1,-1),(2*s-2,0)]
    for s in range(p):
        for t in range(p):
            c=2*min(s,t)+(1 if s>t else 0)
            base=(2*(s+t)-3*c+2,c-2)
            for d in [(0,0),(-2,1),(-3,2),(-5,3)]: sq.append((base[0]+d[0],base[1]+d[1]))
    return pts_of([(0,0)],sq)
def mirror(C): return collections.Counter({(-a,-b):v for (a,b),v in C.items()})
def actual(name):
    rho,arc,sq,other=lattice(os.path.join(D,name,'cxBNr-c2-d'))
    return pts_of(arc,sq)
for n,name in [(1,'k3_2'),(2,'k5_4'),(3,'k7_6'),(4,'k9_8'),(5,'k11_10'),(6,'k13_12')]:
    print('torus T(2,%d) %-7s formula==data: %s'%(2*n+1,name,torus(n)==actual(name)))
for p,name in [(1,'k5_2'),(2,'k9_2'),(3,'k13_2'),(4,'k17_2')]:
    A=actual(name)
    print('twist K_%d %-7s formula==data: %s   (mirror: %s)'%(p,name,twist(p)==A,mirror(twist(p))==A))
for p,name in [(2,'k9_4'),(3,'k13_6'),(4,'k17_8')]:
    A=actual(name)
    print('twist K_%d mirror %-7s formula==data: %s'%(p,name,mirror(twist(p))==A))
