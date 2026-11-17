#!/usr/bin/env python3
"""Ranges of the four edge functionals of the Newton polygon of N(T_K) in lattice coordinates, with knot data."""
import sys,os,glob,collections,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import lattice
from lgrade import data
D='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'
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
def crossings(name):
    w=open(os.path.join(D,name+'.kht')).read().splitlines()[1]
    return sum(1 for t in w.split('.') if t[0] in 'xy')
names=sorted([os.path.basename(p)[:-4] for p in glob.glob(D+'/*.kht') if os.path.exists(os.path.join(p[:-4],'cxBNr-c2-d'))],key=lambda s:[int(x) for x in s[1:].split('_')])
print('name     c  |arc| hs(min,max)   b-range     a-range     (a+b)-range  (a+2b)-range (a+3b)-range (a+4b)-range  hull vertices (ccw)')
for n in names:
    hs,deltas,arc,sq,pts=data(n)
    c=crossings(n)
    f=lambda g:(min(g(a,b) for a,b in pts),max(g(a,b) for a,b in pts))
    H=hull(pts)
    print('%-8s %2d %3d   (%3d,%3d)   %-11s %-11s %-12s %-12s %-12s %-12s %s'%(n,c,len(arc),hs[0],hs[-1],f(lambda a,b:b),f(lambda a,b:a),f(lambda a,b:a+b),f(lambda a,b:a+2*b),f(lambda a,b:a+3*b),f(lambda a,b:a+4*b),H))
