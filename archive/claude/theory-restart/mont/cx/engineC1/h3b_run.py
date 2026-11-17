import sys, pickle, collections, time
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import h3b, ser, jets, vc
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
print('boxes',len(items),'excluded (lc ratio / scalar a)',dict(excl),'signatures',len(sigs),round(time.time()-t0,1),flush=True)
res={}
for n,(key,xs) in enumerate(sigs.items()):
    res[key]=h3b.prove({'top':key[0],'bot':key[1]},key[2],key[3],1)
    if n%1000==0: print(' ',n,round(time.time()-t0,1),flush=True)
allmu=collections.Counter(); permu=collections.Counter(); tot=collections.Counter(); opn=collections.Counter()
for key,xs in sigs.items():
    r=res[key]
    for x in xs:
        tag=items[x][0]; tot[tag]+=1
        if all(not v for v in r.values()): allmu[tag]+=1
        for mu,v in r.items():
            if not v: permu[(tag,mu)]+=1
            for o in v: opn[(mu,o.split(':')[-1])]+=1
print('H(B) proved for ALL mu:',{t:(allmu[t],tot[t]) for t in tot})
print('per mu class (proved/total):')
for mu in h3b.MUS: print('  mu',mu,{t:permu[(t,mu)] for t in tot})
print('open items (box-weighted):',opn.most_common(12))
pickle.dump(dict(res=res,sigs=dict(sigs)),open('h3b_res.pkl','wb'))
print('done',round(time.time()-t0,1))
