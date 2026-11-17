import sys; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from load import *
def cen(p):
    j=int(p['j']); S=Counter()
    for (c,d),m in p['S'].items(): S[(c-24*j, Fr(d)-4*j-Fr(1,2))]+=m
    return S
def profile(S):
    lv=sorted(set(d for c,d in S))
    return [(d,min(c for c,dd in S if dd==d),max(c for c,dd in S if dd==d)) for d in lv]
srcs={'k138':R+'lit/kht/out/k138/k138.jsonl','2br':R+'lit/kht/out/tilt/run_3_45.jsonl','dbl':R+'lit/kht/out/dbl/doubles.jsonl','c4':R+'lit/kht/out/comp/comp4.jsonl','c5':R+'lit/kht/out/comp/comp5.jsonl'}
allp=[]
for tag,pth in srcs.items():
    recs=load_jsonl(pth); n=0
    for r in recs:
        try: p=parse(r)
        except Exception as e: p=None
        if p is None or p['j'].denominator!=1: continue
        n+=1
        allp.append((tag,r.get('file') or r.get('knot'),p))
    print(tag,len(recs),n)
import pickle
pickle.dump(allp,open('/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts/allp.pkl','wb'))
for tag,name,p in allp[:40]:
    S=cen(p)
    print(tag,name,'k',p['k'],'j',p['j'],'n',sum(S.values()),' '.join('%s:[%d,%d]'%(d,a,b) for d,a,b in profile(S)))
