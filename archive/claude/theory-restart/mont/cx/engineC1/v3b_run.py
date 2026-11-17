"""Apply the V3(B) theorem generator to boxes B (general bodies, library A non-rational boxes, d2pos boxes)."""
import sys, pickle, collections, time
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import v3b3 as v3b, ser, jets, lib
from fractions import Fraction as Fr
def bdata(v):
    out={}
    for end in ('top','bot'):
        da=ser.pdata(v[0],end,2); db=ser.pdata(v[1],end,2)
        la=jets.logs(da[2]); lb=jets.logs(db[2])
        out[end]=(la[0],la[1],lb[0],lb[1])
    tq=ser.slope(v,'top',1); bq=ser.slope(v,'bot',1)
    sig=tq[2][0]+bq[2][0]
    return out,sig
t0=time.time()
L=pickle.load(open('libA_jets.pkl','rb'))
items=[]
for (k,T,tag,tp,bt),v in zip(L['boxes'],L['vecs']):
    if tag=='R': continue
    items.append((tag,T,v))
d2=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl','rb'))
items+=[('d2pos',b[2],b[1]) for b in d2]
print('boxes',len(items),flush=True)
sigs=collections.defaultdict(list)
for x,(tag,T,v) in enumerate(items):
    bd,sg=bdata(v)
    key=(bd['top'],bd['bot'],sg)
    sigs[key].append(x)
print('distinct signatures',len(sigs),round(time.time()-t0,1),flush=True)
res={}; opencases=collections.Counter(); n=0
for key,xs in sigs.items():
    bd={'top':key[0],'bot':key[1]}; sg=key[2]
    ok,opn,_c=v3b.prove(bd,sg,1)
    res[key]=(ok,opn)
    for o in opn: opencases[(o[3] if isinstance(o,tuple) else o)]+=len(xs)
    n+=1
    if n%200==0: print(' ',n,round(time.time()-t0,1),flush=True)
cov=collections.Counter(); tot=collections.Counter()
for key,xs in sigs.items():
    for x in xs:
        tag=items[x][0]; tot[tag]+=1
        if res[key][0]: cov[tag]+=1
print('COVERED (V3(B) proved) by family:',{t:(cov[t],tot[t]) for t in tot})
print('open cases (weighted by boxes):',opencases.most_common(12))
pickle.dump(dict(res=res,sigs=dict(sigs),tags=[it[0] for it in items],trees=[it[1] for it in items]),open('v3b_res.pkl','wb'))
print('done',round(time.time()-t0,1))
