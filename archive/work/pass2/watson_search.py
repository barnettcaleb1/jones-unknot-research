from watson_model import *
import random,json,time
from pathlib import Path
rng=random.Random(20261102);start=time.monotonic();rows=[];tested=0;anchors=0
for i in range(1000):
    alpha=[]
    for j in range(rng.choice([10,14,18,22,26])):
        choices=[x for x in (-2,-1,1,2) if not alpha or x!=-alpha[-1]]
        alpha.append(rng.choice(choices))
    base=watson(alpha,RationalTangle(0),RationalTangle(0));pd=base.PD_code()
    r=regina.Link.fromPD([[x+1 for x in row] for row in pd])
    if r.countComponents()!=1:continue
    r.simplify()
    if r.size()!=0:continue
    anchors+=1
    for n in (-5,-2,-1,1,2,5):
        l=watson(alpha,RationalTangle(n),RationalTangle(-n));pd=l.PD_code()
        r=regina.Link.fromPD([[x+1 for x in row] for row in pd]);cross=r.size()
        j=str(r.jones());assert j=='1', (alpha,n,j)
        r.simplify();tested+=1
        row={'alpha':alpha,'n':n,'crossings':cross,'Jones':j,'final_crossings':r.size(),'final_components':r.countComponents()}
        if r.size():row['PD_zero_based']=pd;print('UNRESOLVED',i,n,cross,r.size(),flush=True)
        rows.append(row)
    if i%100==0:print(i,'anchors',anchors,'tested',tested,'seconds',round(time.monotonic()-start,1),flush=True)
Path(__file__).with_name('watson_search.json').write_text(json.dumps({'seed':20261102,'samples':1000,'unknot_anchors':anchors,'rows':rows},indent=2))
print('Done',anchors,tested,'unresolved',sum(bool(x['final_crossings']) for x in rows),flush=True)
