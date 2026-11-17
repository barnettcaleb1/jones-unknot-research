#!/usr/bin/env python3
"""Targeted search for violations of END / NP / TILT: random half-diagram words whose knot has thick HFK^ (computed first, cheap),
then kht++ quotient (time-limited) and the END/NP/TILT checks. usage: end_search.py SEED COUNT MAXLEN TIMEOUT MAXRUNS"""
import sys,random,json,signal,collections,re
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from hfk_word import pd_of_word
import alex_search, run_words, gtilde
import spherogram
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/work'
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)
seed,count,maxlen,timeout,maxruns=[int(x) for x in sys.argv[1:6]]
rnd=random.Random(seed); seen=set(); keys=set(); runs=0
out=open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts/end_search.jsonl','a')
for it in range(count):
    if runs>=maxruns: break
    L=rnd.randint(5,maxlen)
    w=alex_search.gen(rnd,L)
    if not w or w in seen: continue
    seen.add(w)
    try:
        pd=pd_of_word(w)
        if pd is None or len(pd)<6: continue
        K=spherogram.Link(pd)
        if len(K.link_components)!=1: continue
        K.simplify('basic')
        n=len(K.crossings)
        if n<8 or n>14: continue
        signal.alarm(20); h=K.knot_floer_homology(); signal.alarm(0)
    except Exception as e:
        signal.alarm(0); continue
    ranks=h['ranks']
    thin=len(set(A-M for (A,M) in ranks))==1
    if thin: continue
    key=tuple(sorted(ranks.items()))
    if key in keys: continue
    keys.add(key)
    M1=sum((-1)**(M%2)*M*rk for (A,M),rk in ranks.items())
    rec=run_words.run(W,w,timeout); runs+=1
    rec['hfk']=dict(rank=h['total_rank'],tau=h['tau'],g=h['seifert_genus'],M1=M1,cross=n)
    khr=rec.get('khr') or []
    res=rec.get('error','?')
    if khr and gtilde.valid(khr):
        js=gtilde.jset(khr)
        if js:
            k,j,pts=js
            a=gtilde.analyse(pts)
            qs=[q for q,d in pts]; top=len(set(d for q,d in pts if q==max(qs))); bot=len(set(d for q,d in pts if q==min(qs)))
            lev=collections.defaultdict(list)
            for c in khr:
                if c['type']=='s': lev[int(round(c['delta']))].append(int(round(c['q'])))
            ds=sorted(lev); tilt=True
            for d1,d2 in zip(ds,ds[1:]):
                if d2!=d1+1 or not (max(lev[d2])<max(lev[d1]) and min(lev[d2])<min(lev[d1])): tilt=False
            nonunit=any(re.search(r'D\^\d',c) for c in rec.get('bnchains',[]))
            rec.update(k=k,j=j,dimN=len(pts),etop=a['etop'],ebot=a['ebot'],toplevels=top,botlevels=bot,tilt=tilt,nonunit=nonunit)
            res='dimN=%d rank=%d %s | k=%d -4M1=%d | END %s NP %s TILT %s | nonunitD %s'%(len(pts),h['total_rank'],'coll' if len(pts)==h['total_rank'] else 'NOCOLL',k,-4*M1,
                 'ok' if a['etop']!=0 and a['ebot']!=0 else 'FAIL','ok' if top==1 and bot==1 else 'FAIL','ok' if tilt else 'FAIL',nonunit)
        else: res='nonstandard'
    out.write(json.dumps(rec,ensure_ascii=False)+'\n'); out.flush()
    print(w,'cross',n,'t=%s'%rec['time'],res,flush=True)
