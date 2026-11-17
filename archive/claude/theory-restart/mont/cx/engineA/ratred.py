"""Greedy rationality test: try to reduce v to an integral vector by X^{+-1}, Y^k steps decreasing span(a)+span(b)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc
from vc import span
def size(v): return span(v[0])+span(v[1])
def reduce(v, maxsteps=200):
    path=[]
    for _ in range(maxsteps):
        if len(v[0])==1: return True,path
        best=None
        for mu in (1,-1):
            for k in range(-6,7):
                w=vc.nv(vc.Xpow(mu,vc.Ypow(k,v)))
                if w is None: continue
                s=size(w)
                if best is None or s<best[0]: best=(s,mu,k,w)
        if best[0]>=size(v): return False,path
        path.append(best[1:3]); v=best[3]
    return False,path
