"""OWN recomputation of the order-2 (and order-3) jet signatures of every listed box of the top-300 classes and of the
60 d2pos classes, from the stored exact channel vectors (a, b), with own end-series code; comparison with C1's keys;
per-class order-3 subclasses; spans; additivity check on random products (product end data == sum of factor data)."""
import sys, pickle, time, random, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rlaurent as RL
from fractions import Fraction as Fr
t0=time.time()
G=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1/gen2_res.pkl','rb'))
SIGS=G['sigs']; TAGS=G['tags']
ORDER=sorted(SIGS.items(),key=lambda kv:(-len(kv[1]),str(kv[0])))
L=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1/libA_jets.pkl','rb'))
items=[(tag,T,v) for (k,T,tag,tp,bt),v in zip(L['boxes'],L['vecs']) if tag!='R']
d2=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl','rb'))
items+=[('d2pos',b[2],b[1]) for b in d2]
assert len(items)==len(TAGS) and all(items[i][0]==TAGS[i] for i in range(len(TAGS)))
print('items',len(items),'loaded %.1fs'%(time.time()-t0),flush=True)
def boxdata(v,K=3):
    a,b=v; out={}; ok=True
    for end in ('top','bot'):
        da,ca,la=RL.logdata(a,end,K); db,cb,lb=RL.logdata(b,end,K)
        out[end]=(la,lb)
        if abs(Fr(cb,ca))!=1: ok=False
    sig=sum(out[e][1][0]-out[e][0][0] for e in out)
    dl=RL.pspan(b)-RL.pspan(a)
    return out,sig,dl,ok,RL.pspan(a),RL.pspan(b)
TOP=ORDER[:300]
D2=[(i,k,x) for i,(k,x) in enumerate(ORDER) if any(TAGS[j]=='d2pos' for j in x)]
res={}
bad=[]; nb=0
for label,(key,xs) in [('top%d'%i,kv) for i,kv in enumerate(TOP)]+[('d2_%d'%i,(k,x)) for i,k,x in D2]:
    sub=collections.Counter(); minspan=None; spans=[]
    for x in xs:
        out,sig,dl,ok,sa,sb=boxdata(items[x][2]); nb+=1
        mykey=(tuple(out['top'][0][:2])+tuple(out['top'][1][:2]),tuple(out['bot'][0][:2])+tuple(out['bot'][1][:2]),sig,dl)
        # key layout (ra,la,rb,lb) per end
        mykey=((out['top'][0][0],out['top'][0][1],out['top'][1][0],out['top'][1][1]),(out['bot'][0][0],out['bot'][0][1],out['bot'][1][0],out['bot'][1][1]),sig,dl)
        if mykey!=key or not ok or sa<1: bad.append((label,x,mykey,key,ok,sa))
        sub[(out['top'][0][2],out['top'][1][2],out['bot'][0][2],out['bot'][1][2])]+=1
        spans.append(sa)
    res[label]=dict(key=key,n=len(xs),sub=dict(sub),minspan_a=min(spans),xs=list(xs))
print('boxes checked',nb,'key mismatches / ineligible:',len(bad),'  %.1fs'%(time.time()-t0),flush=True)
for b in bad[:5]: print('  BAD',b)
tops=[res['top%d'%i] for i in range(300)]
print('top-300: boxes',sum(r['n'] for r in tops),' min span a over all listed boxes',min(r['minspan_a'] for r in tops),
      ' order-3 subclasses',sum(len(r['sub']) for r in tops))
d2s=[r for l,r in res.items() if l.startswith('d2_')]
print('d2pos: classes',len(d2s),'boxes',sum(r['n'] for r in d2s),' min span a',min(r['minspan_a'] for r in d2s),' order-3 subclasses',sum(len(r['sub']) for r in d2s))
pickle.dump(res,open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','wb'))
# additivity: random products of 2-5 listed top-300 boxes; product end data computed DIRECTLY vs sum of factor data
random.seed(11); pool=[x for r in tops for x in r['xs']]
badadd=0; NT=300
for it in range(NT):
    k=random.randint(2,5); xs=[random.choice(pool) for _ in range(k)]
    a={0:1}; b={0:1}; S=None
    for x in xs:
        v=items[x][2]; a=RL.pmul(a,v[0]); b=RL.pmul(b,v[1])
    out,sig,dl,ok,sa,sb=boxdata((a,b))
    parts=[boxdata(items[x][2]) for x in xs]
    for end in ('top','bot'):
        for ch in (0,1):
            s=tuple(sum(p[0][end][ch][i] for p in parts) for i in range(3))
            if s!=out[end][ch]: badadd+=1
    if sig!=sum(p[1] for p in parts) or dl!=sum(p[2] for p in parts) or sa!=sum(p[4] for p in parts): badadd+=1
    if not ok: badadd+=1
print('additivity: %d random products of 2-5 listed boxes: log-jets (order 3, both ends, both channels), sigma, delta, span a additive; failures %d'%(NT,badadd))
print('time %.1f'%(time.time()-t0))
