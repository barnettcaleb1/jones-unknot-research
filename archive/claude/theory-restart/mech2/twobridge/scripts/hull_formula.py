#!/usr/bin/env python3
"""Newton polygons of the conjectured closed formula P_w for positive two-bridge words (no kht++), edge directions in (a,b)."""
import sys,os,itertools,collections,math
def mulX(v,b):
    # v = (v1,v2) Counters over (a,b);  M_X = [[1,1+y],[0,x]] applied b times
    v1,v2=v
    for _ in range(b):
        n1=collections.Counter(v1)
        for (a,bb),c in v2.items():
            n1[(a,bb)]+=c; n1[(a,bb+1)]+=c
        n2=collections.Counter({(a+1,bb):c for (a,bb),c in v2.items()})
        v1,v2=n1,n2
    return v1,v2
def mulY(v,a_):
    # M_Y = [[1,0],[u,u]], u = x/y = (1,-1)
    v1,v2=v
    for _ in range(a_):
        n2=collections.Counter()
        for (a,bb),c in v1.items(): n2[(a+1,bb-1)]+=c
        for (a,bb),c in v2.items(): n2[(a+1,bb-1)]+=c
        v1,v2=collections.Counter(v1),n2
    return v1,v2
def P(word):
    """word = list of (a_i,b_i) positive"""
    v=(collections.Counter({(0,0):1}),collections.Counter())
    for a_,b_ in word:
        v=mulY(v,a_); v=mulX(v,b_)
    return v[0]
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
    return lo[:-1]+up[:-1]
def edges(h):
    out=[]; n=len(h)
    for i in range(n):
        p,q=h[i],h[(i+1)%n]
        d=(q[0]-p[0],q[1]-p[1]); g=math.gcd(abs(d[0]),abs(d[1]))
        if g:
            d=(d[0]//g,d[1]//g)
            if d[0]<0 or (d[0]==0 and d[1]<0): d=(-d[0],-d[1])
            out.append((d,g,p,q))
    return out
if __name__=='__main__':
    maxe=int(sys.argv[1]) if len(sys.argv)>1 else 4
    dirs=collections.Counter(); ex={}
    for n in (1,2,3):
        for word in itertools.product(itertools.product(range(1,maxe+1),repeat=2),repeat=n):
            S=P(word)
            for d,g,p,q in edges(hull(list(S))):
                dirs[d]+=1; ex.setdefault(d,word)
    for d,c in sorted(dirs.items(),key=lambda kv:-kv[1]): print(d,c,'example',ex[d])
