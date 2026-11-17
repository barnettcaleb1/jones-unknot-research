#!/usr/bin/env python3
"""run kht++ on given words with a time limit; print dim N, END data, L(t), quadruples; HFK^ if cheap. usage: run_one.py TIMEOUT word..."""
import sys,json,re,collections,signal
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from hfk_word import pd_of_word
from quad_scan import squares_of,quads
import run_words,gtilde,grid
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/work'
timeout=int(sys.argv[1])
out=open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts/run_one.jsonl','a')
def handler(s,f): raise Exception('to')
signal.signal(signal.SIGALRM,handler)
for w in sys.argv[2:]:
    hf=None
    try:
        import spherogram
        K=spherogram.Link(pd_of_word(w)); K.simplify('basic')
        signal.alarm(120); h=K.knot_floer_homology(); signal.alarm(0)
        M1=sum((-1)**(M%2)*M*rk for (A,M),rk in h['ranks'].items())
        hf=dict(rank=h['total_rank'],tau=h['tau'],g=h['seifert_genus'],M1=M1,cross=len(K.crossings))
    except Exception as e:
        signal.alarm(0); hf=dict(err=str(e)[:60])
    rec=run_words.run(W,w,timeout); rec['hfk']=hf
    khr=rec.get('khr') or []
    print(w,'HFK',hf,'time',rec['time'],rec.get('error',''),flush=True)
    if khr and gtilde.valid(khr) and gtilde.jset(khr):
        k,j,pts=gtilde.jset(khr); a=gtilde.analyse(pts)
        S=collections.Counter(grid.ab(pts)); L=collections.Counter()
        for (x,y),m in S.items(): L[x+4*y]+=m*(-1)**((x+y)%2)
        L={e:c for e,c in L.items() if c}
        es=[x+4*y for x,y in S]
        sq,other=squares_of(rec.get('bnchains',[])); wp,nq,found=quads(sq)
        rec.update(k=k,j=j,dimN=len(pts),etop=a['etop'],ebot=a['ebot'],quads=nq,wpairs=wp,topgap=max(es)-max(L),botgap=min(L)-min(es))
        print('   dimN',len(pts),'k',k,'j',j,'etop',a['etop'],'ebot',a['ebot'],'squares',len(sq),'other comps',other,'wpairs',wp,'quads',nq,flush=True)
        print('   N e-range',min(es),max(es),' L support',min(L),max(L),' top gap',max(es)-max(L),' bottom gap',min(L)-min(es),flush=True)
        print('   L =',' '.join('%+d t^%d'%(L[e],e) for e in sorted(L)),flush=True)
    out.write(json.dumps(rec,ensure_ascii=False)+'\n'); out.flush()
