from watson_model import *
from pathlib import Path
import json,time
p=Path(__file__).with_name('watson_search.json');old=json.loads(p.read_text());alphas=[]
for row in old['rows']:
    if row['alpha'] not in alphas:alphas.append(row['alpha'])
Q=(RationalTangle(-1)+RationalTangle(1,2)+RationalTangle(1,3)).rotate(1)
inputs=[(Q,-Q),(Q,Q),(Q+RationalTangle(2),-Q+RationalTangle(-2)),(Q+Q,-Q)]
rows=[];start=time.monotonic()
for i,alpha in enumerate(alphas):
    for k,(t,u) in enumerate(inputs):
        l=watson(alpha,t,u);pd=l.PD_code();r=regina.Link.fromPD([[x+1 for x in row] for row in pd])
        j=str(r.jones());assert j=='1',(alpha,k,j)
        row={'alpha':alpha,'input_index':k,'crossings':len(pd),'Jones':j,'PD_zero_based':pd}
        l.simplify('global')
        row['final_crossings']=len(l.crossings);row['final_components']=len(l.link_components)+l.unlinked_unknot_components;rows.append(row)
        if l.crossings:print('UNRESOLVED',i,k,len(pd),len(l.crossings),flush=True)
    if i%10==0:print(i+1,'anchors',len(rows),'knots',round(time.monotonic()-start,1),'seconds',flush=True)
    Path(__file__).with_name('watson_q_search.json').write_text(json.dumps({'input_definitions':['Q, -Q','Q, Q','Q+2, -Q-2','Q+Q, -Q'],'rows':rows},indent=2))
print('Done',len(rows),'unresolved',sum(bool(r['final_crossings']) for r in rows))
