import sys, pickle, collections, time
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import gen2, h3b, ser, jets, vc
from fractions import Fraction as Fr
def bdata(v):
    out={}; lcok=True
    for end in ('top','bot'):
        da=ser.pdata(v[0],end,2); db=ser.pdata(v[1],end,2)
        la=jets.logs(da[2]); lb=jets.logs(db[2])
        out[end]=(la[0],la[1],lb[0],lb[1])
        if abs(Fr(db[1],da[1]))!=1: lcok=False
    tq=ser.slope(v,'top',1); bq=ser.slope(v,'bot',1)
    return out,tq[2][0]+bq[2][0],tq[0]-bq[0],lcok
t0=time.time()
L=pickle.load(open('libA_jets.pkl','rb'))
items=[(tag,T,v) for (k,T,tag,tp,bt),v in zip(L['boxes'],L['vecs']) if tag!='R']
d2=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl','rb'))
items+=[('d2pos',b[2],b[1]) for b in d2]
sigs=collections.defaultdict(list); excl=collections.Counter()
for x,(tag,T,v) in enumerate(items):
    bd,sg,dl,lcok=bdata(v)
    if not lcok or vc.span(v[0])<1: excl[tag]+=1; continue
    sigs[(bd['top'],bd['bot'],sg,dl)].append(x)
print('boxes',len(items),'excluded',dict(excl),'signatures',len(sigs),flush=True)
resV={}; resH={}
for n,(key,xs) in enumerate(sigs.items()):
    bd={'top':key[0],'bot':key[1]}
    resV[key]=gen2.proveV(bd,key[2],key[3],1)
    resH[key]=gen2.proveH(bd,key[2],key[3],1)
    if n%1000==0: print(' ',n,round(time.time()-t0,1),flush=True)
tot=collections.Counter(); cV=collections.Counter(); cHall=collections.Counter(); cboth=collections.Counter(); per=collections.Counter()
oV=collections.Counter(); oH=collections.Counter()
for key,xs in sigs.items():
    okV=resV[key][0]; rH=resH[key]; okH=all(not v for v in rH.values())
    for o in resV[key][1]: oV[o[3] if isinstance(o,tuple) else o]+=len(xs)
    for mu,v in rH.items():
        for o in v: oH[(mu,o.split(':')[-1])]+=len(xs)
    for x in xs:
        tag=items[x][0]; tot[tag]+=1
        cV[tag]+=okV; cHall[tag]+=okH; cboth[tag]+=(okV and okH)
        for mu,v in rH.items(): per[(tag,mu)]+= (not v)
print('V3(B) proved (all odd |a|>=3):',{t:(cV[t],tot[t]) for t in tot})
print('H(B) proved for ALL mu:',{t:(cHall[t],tot[t]) for t in tot})
print('BOTH (every vertical |a|>=3 and every horizontal mu):',{t:(cboth[t],tot[t]) for t in tot})
for mu in h3b.MUS: print('  H mu',mu,{t:per[(t,mu)] for t in tot})
print('open V:',oV.most_common(6)); print('open H:',oH.most_common(10))
pickle.dump(dict(resV=resV,resH=resH,sigs=dict(sigs),tags=[i[0] for i in items],trees=[i[1] for i in items]),open('gen2_res.pkl','wb'))
print('done',round(time.time()-t0,1))
