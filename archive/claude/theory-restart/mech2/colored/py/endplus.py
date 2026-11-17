#!/usr/bin/env python3
"""dimension of N in top and bottom q-degree, over all data files (from khr records via gtilde.jset)."""
import json,sys,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from gtilde import jset,valid
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
files=['k138/k138.jsonl','tilt/run_3_45.jsonl','dbl/doubles.jsonl','comp/comp4.jsonl','comp/comp5.jsonl','alex1/runs.jsonl']
tot=collections.Counter(); seen=set(); bad=[]
for f in files:
    try: lines=open(base+f).read().splitlines()
    except Exception as e: print('missing',f); continue
    for line in lines:
        try: r=json.loads(line)
        except: continue
        khr=r.get('khr') or []
        if not khr or not valid(khr): continue
        js=jset(khr)
        if js is None: continue
        k,j,pts=js
        key=(k,j,tuple(sorted(pts)))
        if key in seen: continue
        seen.add(key)
        qs=collections.Counter(q for q,d in pts)
        top=qs[max(qs)]; bot=qs[min(qs)]
        tot[(top,bot)]+=1
        if top!=1 or bot!=1: bad.append((f,r.get('file') or r.get('knot') or r.get('word'),top,bot,len(pts)))
print('distinct tangles',len(seen)); print('(dim top q, dim bottom q) counts:',dict(tot))
for b in bad[:40]: print('  ',b)
