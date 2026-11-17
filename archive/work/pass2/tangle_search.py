"""Exact bracket-guided search using a nonrational unknot-closure tangle.
No crossing-count completeness claim. Expressions are serialized for replay.
"""
from pathlib import Path
import sys,random,json,time
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'generic'))
from tangle_unit_check import *
T=pairmul(pairmul(power_b(-1),power_b(-2)[::-1]),power_b(-3)[::-1])
def mirror(p):return tuple({-e:c for e,c in q.items()} for q in p)
SEEDS=[T,T[::-1],mirror(T),mirror(T)[::-1]]
def val(ex):
    if ex[0]=='s':return SEEDS[ex[1]]
    if ex[0]=='b':return power_b(ex[1])
    if ex[0]=='r':return val(ex[1])[::-1]
    return pairmul(val(ex[1]),val(ex[2]))
def polyjson(p):return {str(e):c for e,c in sorted(p.items())}
rng=random.Random(20261101)
start=time.monotonic();hits=[];tot=0
N=int(sys.argv[1]) if len(sys.argv)>1 else 2000
for i in range(N):
    n=rng.choice([2,3,4,5,6]); ex=['s',rng.randrange(4)]; p=val(ex)
    for j in range(n-1):
        k=rng.randint(-4,4)
        if k:ex=['+',ex,['b',k]];p=pairmul(p,power_b(k))
        # Force alternating attachments; purely horizontal products would just
        # reproduce connected sums of known unknot closures.
        ex=['r',ex];p=p[::-1]
        leaf=['s',rng.randrange(4)]
        ex=['+',ex,leaf];p=pairmul(p,val(leaf))
    k=rng.randint(-4,4)
    if k:ex=['+',ex,['b',k]];p=pairmul(p,power_b(k))
    for closure in ('N','D'):
        c=add(mul(DELTA,p[0]),p[1]) if closure=='N' else add(p[0],mul(DELTA,p[1]))
        tot+=1
        if len(c)==1 and abs(next(iter(c.values())))==1:
            hits.append({'i':i,'seeds':n,'expression':ex,'closure':closure,'bracket':polyjson(c)})
    if (i+1)%200==0:print(i+1,'expressions',len(hits),'hits',round(time.monotonic()-start,1),'seconds',flush=True)
Path(__file__).with_name('tangle_search_hits.json').write_text(json.dumps({'seed':20261101,'expressions':N,'closures_checked':tot,'hits':hits},indent=2))
print('Finished',N,tot,'hits',len(hits),flush=True)
