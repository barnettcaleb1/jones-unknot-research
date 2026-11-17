#!/usr/bin/env python3
"""Print N(T_K) in hexagon coordinates u=b, v=a+b (rows u from top, columns v)."""
import sys,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lgrade import data
def show(name):
    hs,deltas,arc,sq,pts=data(name)
    S=collections.Counter((b,a+b) for a,b in pts)
    U=[u for u,v in S]; V=[v for u,v in S]
    print('==',name,' Kh~ h (rel free gen):',hs)
    print('      v: '+' '.join('%2d'%v for v in range(min(V),max(V)+1)))
    for u in range(max(U),min(U)-1,-1):
        print('  u=%3d  '%u+' '.join(('%2d'%S[(u,v)] if S[(u,v)] else ' .') for v in range(min(V),max(V)+1)))
for n in sys.argv[1:]: show(n)
