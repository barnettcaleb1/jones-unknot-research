#!/usr/bin/env python3
"""PARALLELOGRAM LAW test: N(T) lies in the parallelogram with sides of slopes 1 and 2 in the (h,q) plane whose opposite vertices are
the bottom and top generators, i.e. for every generator g and the top-q generators y: q(g)/2 - h(g) >= q(y)/2 - h(y) (delta minimal at the top)
and h(g) - q(g) >= h(y) - q(y) (l minimal at the top); dually at the bottom."""
import json,sys,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from gtilde import jset,valid
def check(pts):
    g=[(q//2-d,q) for q,d in pts]          # (h,q)
    qmax=max(q for h,q in g); qmin=min(q for h,q in g)
    top=[x for x in g if x[1]==qmax]; bot=[x for x in g if x[1]==qmin]
    ok_top=all(len(set(top))==1 and (q/2-h)>=(top[0][1]/2-top[0][0]) and (h-q)>=(top[0][0]-top[0][1]) for h,q in g)
    ok_bot=all(len(set(bot))==1 and (q/2-h)<=(bot[0][1]/2-bot[0][0]) and (h-q)<=(bot[0][0]-bot[0][1]) for h,q in g)
    return ok_top,ok_bot,len(top),len(bot),len(set(top)),len(set(bot))
if __name__=='__main__':
    seen=set(); n=0; bad=[]; mult=collections.Counter()
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
            seen.add(key); n+=1
            a,b,nt,nb,dt,db=check(pts)
            mult[(nt,nb)]+=1
            if not (a and b): bad.append(((r.get('file') or r.get('knot') or r.get('word')),a,b,nt,nb,dt,db))
    print('distinct tangles:',n,' parallelogram law fails:',len(bad))
    for x in bad[:20]: print('   ',x)
    print('multiplicities (top,bottom) of the extreme quantum degree:',sorted(mult.items()))
