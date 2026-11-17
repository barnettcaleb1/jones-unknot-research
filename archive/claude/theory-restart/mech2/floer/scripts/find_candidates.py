#!/usr/bin/env python3
"""Random half-diagram words -> HFK^ (spherogram); keep knots that discriminate (|M1| != |tau|, or thick), small diagrams."""
import sys,random,json,signal,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from hfk_word import pd_of_word
import alex, alex_search
import spherogram
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)
seed,count,maxlen=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
rnd=random.Random(seed); seen=set(); out=[]; keys=set()
for it in range(count):
    L=rnd.randint(4,maxlen)
    w=alex_search.gen(rnd,L)
    if not w or w in seen: continue
    seen.add(w)
    try:
        pd=pd_of_word(w)
    except Exception: continue
    if pd is None or len(pd)<3: continue
    try:
        K=spherogram.Link(pd)
        if len(K.link_components)!=1: continue
        K.simplify('basic')
        n=len(K.crossings)
        if n<3 or n>16: continue
        signal.alarm(20); h=K.knot_floer_homology(); signal.alarm(0)
    except Exception as e:
        signal.alarm(0); continue
    ranks=h['ranks']
    M1=sum((-1)**(M%2)*M*rk for (A,M),rk in ranks.items())
    thin=len(set(A-M for (A,M) in ranks))==1
    key=tuple(sorted(ranks.items()))
    keym=tuple(sorted(((-A,M-2*A),r) for (A,M),r in ranks.items()))  # same knot type data
    if key in keys: continue
    keys.add(key)
    ncross=sum(1 for tok in w[2:].split('.') if tok[0] in 'xy')
    out.append(dict(word=w,half=ncross,cross=n,rank=h['total_rank'],tau=h['tau'],g=h['seifert_genus'],M1=M1,thin=thin,L=h['L_space_knot'],eps=h['epsilon']))
json.dump(out,open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts/candidates_%d.json'%seed,'w'))
print('distinct HFK types',len(out))
disc=[x for x in out if abs(x['M1'])!=abs(x['tau'])]
print('discriminating (|M1|!=|tau|):',len(disc))
for x in sorted(disc,key=lambda x:(x['half'],x['rank']))[:40]: print(x)
thick=[x for x in out if not x['thin'] and abs(x['M1'])==abs(x['tau'])]
print('thick, non-discriminating:',len(thick))
for x in sorted(thick,key=lambda x:(x['half'],x['rank']))[:15]: print(x)
