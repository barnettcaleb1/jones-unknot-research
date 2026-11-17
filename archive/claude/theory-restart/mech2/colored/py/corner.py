#!/usr/bin/env python3
"""Double extremality: do the top-q generators minimise delta (max b) and minimise l (max a+3b)?  Same at the bottom.  Over all data files."""
import json,sys,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from gtilde import jset,valid
from grid import ab
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
files=['k138/k138.jsonl','tilt/run_3_45.jsonl','dbl/doubles.jsonl','comp/comp4.jsonl','comp/comp5.jsonl','alex1/runs.jsonl']
seen=set(); bad=[]; n=0
for f in files:
    try: lines=open(base+f).read().splitlines()
    except Exception: continue
    for line in lines:
        try: r=json.loads(line)
        except: continue
        khr=r.get('khr') or []
        if not khr or not valid(khr): continue
        js=jset(khr)
        if js is None: continue
        k,j,pts=js
        key=(k,j,tuple(sorted(pts)))
        if key in seen or len(pts)<2: continue
        seen.add(key); n+=1
        S=ab(pts)
        q=lambda p:2*p[0]+8*p[1]
        qmax=max(q(p) for p in S); qmin=min(q(p) for p in S)
        top=[p for p in S if q(p)==qmax]; bot=[p for p in S if q(p)==qmin]
        bmax=max(b for a,b in S); bmin=min(b for a,b in S)
        lmax=max(a+3*b for a,b in S); lmin=min(a+3*b for a,b in S)
        ok=all(p[1]==bmax and p[0]+3*p[1]==lmax for p in top) and all(p[1]==bmin and p[0]+3*p[1]==lmin for p in bot)
        if not ok: bad.append((f,r.get('file') or r.get('knot') or r.get('word'),top,bmax,lmax,bot,bmin,lmin))
print('tangles',n,' failures of double extremality:',len(bad))
for b in bad[:20]: print('  ',b)
