#!/usr/bin/env python3
"""Newton polygon of N(T) in lattice coordinates (a,b). Reports primitive edge directions of the convex hull, split by side."""
import json,sys,collections,math
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from gtilde import jset,valid
from grid import ab
def hull(points):
    pts=sorted(set(points))
    if len(pts)<=2: return pts
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0: up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]   # counterclockwise
def edges(h):
    out=[]
    n=len(h)
    for i in range(n):
        p,q=h[i],h[(i+1)%n]
        d=(q[0]-p[0],q[1]-p[1]); g=math.gcd(abs(d[0]),abs(d[1]))
        if g: out.append(((d[0]//g,d[1]//g),g))
    return out
if __name__=='__main__':
    dirs=collections.Counter(); seen=set(); ex={}
    for fn in sys.argv[1:]:
        for line in open(fn):
            try: r=json.loads(line)
            except: continue
            khr=r.get('khr') or []
            if not khr or not valid(khr): continue
            js=jset(khr)
            if js is None: continue
            k,j,pts=js
            if len(pts)<3: continue
            key=(k,j,tuple(sorted(pts)))
            if key in seen: continue
            seen.add(key)
            S=ab(pts); h=hull(S)
            for d,g in edges(h):
                # normalise direction up to sign: make first nonzero coordinate positive
                if d[0]<0 or (d[0]==0 and d[1]<0): d=(-d[0],-d[1])
                dirs[d]+=1; ex.setdefault(d,(r.get('file') or r.get('knot') or r.get('word')))
    print('tangles:',len(seen))
    for d,c in sorted(dirs.items(),key=lambda kv:-kv[1]):
        print('  direction (da,db)=%s  count %d   (h,q)=(%d,%d)   example %s'%(d,c,d[0]+5*d[1],2*d[0]+8*d[1],str(ex[d]).split('/')[-1]))
