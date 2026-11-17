#!/usr/bin/env python3
"""multiplicity of N in its extreme quantum degrees, over all data files."""
import json,sys,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from gtilde import jset,valid
files=sys.argv[1:]
seen=set(); tot=0; hist=collections.Counter(); bad=[]
for fn in files:
    for line in open(fn):
        try: r=json.loads(line)
        except: continue
        khr=r.get('khr') or []
        if not khr or not valid(khr): continue
        js=jset(khr)
        if js is None: continue
        k,j,pts=js
        if len(pts)==1: continue
        key=(k,j,tuple(sorted(pts)))
        if key in seen: continue
        seen.add(key); tot+=1
        qs=[q for q,d in pts]
        top=[d for q,d in pts if q==max(qs)]; bot=[d for q,d in pts if q==min(qs)]
        hist[(len(top),len(set(top)))]+=1; hist[(len(bot),len(set(bot)))]+=1
        if len(top)>1 or len(bot)>1: bad.append((r.get('file') or r.get('knot') or r.get('word'),len(pts),len(top),len(bot)))
print('distinct tangles',tot)
print('hist (multiplicity, number of delta levels) at extremes:',sorted(hist.items()))
print('examples with extreme multiplicity >1:',bad[:40], len(bad))
