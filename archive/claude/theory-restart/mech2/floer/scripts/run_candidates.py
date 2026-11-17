#!/usr/bin/env python3
"""Run kht++ (quotient mode) on candidate words; compare dim N, k with HFK data. usage: run_candidates.py CAND.json OUT.jsonl TIMEOUT [which]"""
import sys,json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import run_words
from gtilde import valid,jset
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/work'
cands=json.load(open(sys.argv[1])); outp=sys.argv[2]; timeout=int(sys.argv[3]); which=sys.argv[4] if len(sys.argv)>4 else 'disc'
if which=='disc': sel=[x for x in cands if abs(x['M1'])!=abs(x['tau'])]
elif which=='thick': sel=[x for x in cands if not x['thin'] and abs(x['M1'])==abs(x['tau'])]
else: sel=cands
sel=sorted(sel,key=lambda x:(x['half'],x['rank']))
fo=open(outp,'a')
for x in sel:
    rec=run_words.run(W,x['word'],timeout)
    rec['hfk']=x
    khr=rec.get('khr') or []
    res='?'
    if khr and valid(khr):
        js=jset(khr)
        if js:
            k,j,pts=js
            rec['k']=k; rec['j']=j; rec['dimN']=len(pts)
            res='dimN=%d rank=%d %s | k=%d  -4M1=%d  4tau=%d %s | j=%d'%(len(pts),x['rank'],'COLLAPSE' if len(pts)==x['rank'] else 'NO-COLLAPSE',k,-4*x['M1'],4*x['tau'],'OK' if k==-4*x['M1'] else 'FAIL',j)
        else: res='nonstandard specials'
    elif khr: res='not valid: '+str([(c['type'],c['len'],c['slope']) for c in khr][:6])
    else: res=rec.get('error','no khr')
    fo.write(json.dumps(rec,ensure_ascii=False)+'\n'); fo.flush()
    print(x['word'],'t=%s'%rec['time'],res,flush=True)
