#!/usr/bin/env python3
"""Variants of the END-violating word s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1: HFK^ first, then kht++ (time limit), END/NP/TILT, quadruples."""
import sys,json,re,signal,collections,itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from hfk_word import pd_of_word
from quad_scan import squares_of,quads
import run_words,gtilde
import spherogram
W='/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/work'
base=['r1','x2','y1','y0','r2','y0','y1','y0','y1','x2','u3','u1']
words=[]
def flip(t): return ('y' if t[0]=='x' else 'x')+t[1:]
# single-token modifications: flip a crossing, triple a crossing, delete a crossing
idx=[i for i,t in enumerate(base) if t[0] in 'xy']
for i in idx:
    w=list(base); w[i]=flip(w[i]); words.append(w)
    w=list(base); w[i:i+1]=[base[i]]*3; words.append(w)
    w=list(base); del w[i]; words.append(w)
for i,j in itertools.combinations(idx,2):
    w=list(base); w[i]=flip(w[i]); w[j]=flip(w[j]); words.append(w)
for i,j in itertools.combinations(idx,2):
    w=list(base); w[i:i+1]=[base[i]]*3; w[j]=flip(w[j]); words.append(w)
words=['s.'+'.'.join(w) for w in words]
out=open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts/ce_variants.jsonl','a')
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)
seen=set(); n=0
maxruns=int(sys.argv[1]); timeout=int(sys.argv[2])
for w in words:
    if n>=maxruns: break
    try:
        pd=pd_of_word(w)
        if pd is None: continue
        K=spherogram.Link(pd)
        if len(K.link_components)!=1: continue
        K.simplify('basic')
        if len(K.crossings)<6: continue
        signal.alarm(20); h=K.knot_floer_homology(); signal.alarm(0)
    except Exception as e:
        signal.alarm(0); continue
    key=tuple(sorted(h['ranks'].items()))
    if key in seen: continue
    seen.add(key)
    thin=len(set(A-M for (A,M) in h['ranks']))==1
    if thin: continue
    M1=sum((-1)**(M%2)*M*rk for (A,M),rk in h['ranks'].items())
    rec=run_words.run(W,w,timeout); n+=1
    rec['hfk']=dict(rank=h['total_rank'],tau=h['tau'],g=h['seifert_genus'],M1=M1,cross=len(K.crossings))
    khr=rec.get('khr') or []
    res=rec.get('error','?')
    if khr and gtilde.valid(khr) and gtilde.jset(khr):
        k,j,pts=gtilde.jset(khr); a=gtilde.analyse(pts)
        qs=[q for q,d in pts]; top=len(set(d for q,d in pts if q==max(qs))); bot=len(set(d for q,d in pts if q==min(qs)))
        sq,other=squares_of(rec.get('bnchains',[])); wp,nq,found=quads(sq)
        nonunit=any(re.search(r'D\^\d',c) for c in rec.get('bnchains',[]))
        rec.update(k=k,j=j,dimN=len(pts),etop=a['etop'],ebot=a['ebot'],toplevels=top,botlevels=bot,nonunit=nonunit,wpairs=wp,quads=nq)
        res='dimN=%d rank=%d drop=%d | k=%d -4M1=%d | END %s NP %s | squares %d wpairs %d quads %d | nonunitD %s'%(len(pts),h['total_rank'],len(pts)-h['total_rank'],k,-4*M1,
            'ok' if a['etop']!=0 and a['ebot']!=0 else 'FAIL','ok' if top==1 and bot==1 else 'FAIL',len(sq),wp,nq,nonunit)
    out.write(json.dumps(rec,ensure_ascii=False)+'\n'); out.flush()
    print(w,'cross',len(K.crossings),'t=%s'%rec['time'],res,flush=True)
