#!/usr/bin/env python3
"""Test the involution iota(a,b) = (-a, a+b) (swap of u=b and v=a+b; fixes P, sends D to P-D) on the multisets N(T_K) (doubles),
and on all other data (table inversions etc.)."""
import sys,os,glob,collections,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import lattice
D='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'
names=sorted([os.path.basename(p)[:-4] for p in glob.glob(D+'/*.kht') if os.path.exists(os.path.join(p[:-4],'cxBNr-c2-d'))],key=lambda s:[int(x) for x in s[1:].split('_')])
def iota(C): return collections.Counter({(-a,a+b):v for (a,b),v in C.items()})
ok=0
for n in names:
    rho,arc,sq,other=lattice(os.path.join(D,n,'cxBNr-c2-d'))
    P=list(arc)
    for a,b in sq: P+=[(a,b),(a+1,b),(a,b+1),(a+1,b+1)]
    C=collections.Counter(P)
    good=(iota(C)==C); ok+=good
    print('%-8s iota-symmetric: %s'%(n,good))
print('doubles symmetric:',ok,'of',len(names))
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from gtilde import jset,valid
from grid import ab
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
for f in ['k138/k138.jsonl','tilt/run_3_45.jsonl','comp/comp4.jsonl','comp/comp5.jsonl','alex1/runs.jsonl']:
    seen=set(); tot=0; sym=0; ex=[]
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
        seen.add(key); tot+=1
        C=collections.Counter(ab(pts))
        # allow a translation: iota about some centre: test iota(C) == C shifted by any vector
        I=iota(C)
        good=False
        p0=min(C); 
        for q0 in I:
            sh=(p0[0]-q0[0],p0[1]-q0[1])
            if collections.Counter({(a+sh[0],b+sh[1]):v for (a,b),v in I.items()})==C: good=True; break
        sym+=good
        if good and len(ex)<4: ex.append((r.get('file') or r.get('knot') or r.get('word'),len(pts)))
    print(f,'distinct',tot,' iota-symmetric up to translation:',sym,ex)
