#!/usr/bin/env python3
"""Variants of the 9_46 second-inversion word: HFK^ first, then kht++ (time-limited). Looks for more non-collapsing tangles / non-unit D arrows."""
import sys,json,re,signal
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from hfk_word import pd_of_word
import run_words
from gtilde import valid,jset
import spherogram
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/work'
base='s.l1.y0.y2.r1.{A}.u3.{B}.u1'
words=[]
for A in ['y2.y2.y2','y2','y2.y2.y2.y2.y2','x2.x2.x2','x2','y2.y2']:
    for B in ['x0','y0','x0.x0.x0','y0.y0.y0','x0.x0','y0.y0']:
        for pre in ['y0.y2','x0.y2','y0.x2','x0.x2','y0.y0.y0.y2','y0.y2.y2.y2']:
            words.append('s.l1.%s.r1.%s.u3.%s.u1'%(pre,A,B))
out=open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts/variants.jsonl','a')
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)
seen=set(); n=0
for w in words:
    try:
        pd=pd_of_word(w)
        if pd is None: continue
        K=spherogram.Link(pd)
        if len(K.link_components)!=1: continue
        K.simplify('basic')
        if len(K.crossings)<3: continue
        signal.alarm(20); h=K.knot_floer_homology(); signal.alarm(0)
    except Exception as e:
        signal.alarm(0); continue
    key=tuple(sorted(h['ranks'].items()))
    if key in seen: continue
    seen.add(key)
    M1=sum((-1)**(M%2)*M*rk for (A,M),rk in h['ranks'].items())
    rec=run_words.run(W,w,90)
    khr=rec.get('khr') or []
    res=rec.get('error','?')
    nonunit=[c for c in rec.get('bnchains',[]) if re.search(r'D\^\d',c)]
    if khr and valid(khr):
        js=jset(khr)
        if js:
            k,j,pts=js
            res='dimN=%d rank=%d %s | k=%d -4M1=%d %s | j=%d | nonunitD=%d'%(len(pts),h['total_rank'],'COLLAPSE' if len(pts)==h['total_rank'] else 'NO-COLLAPSE',k,-4*M1,'OK' if k==-4*M1 else 'FAIL',j,len(nonunit))
            rec.update(k=k,j=j,dimN=len(pts))
    rec['hfk']=dict(rank=h['total_rank'],tau=h['tau'],g=h['seifert_genus'],M1=M1,cross=len(K.crossings))
    out.write(json.dumps(rec,ensure_ascii=False)+'\n'); out.flush()
    print(w,'cross',len(K.crossings),'t=%s'%rec['time'],res,flush=True)
    n+=1
    if n>=40: break
