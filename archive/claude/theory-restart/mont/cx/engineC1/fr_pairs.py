"""Pairs (frontier box) x (library A u R(8) u frontier): exact second/third-order two-ended tie census + exact closures at
order >= 3.  argv: tag"""
import sys, pickle, collections, time
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, front, lp
tag=sys.argv[1]
t0=time.time()
L=pickle.load(open('libA_jets.pkl','rb'))
F=pickle.load(open('fr_%s.pkl'%tag,'rb'))
nF=len(F['boxes'])
jets=F['jets']+[(b[3],b[4]) for b in L['boxes']]
vecs=F['vecs']+L['vecs']
names=[(b[1],b[2]) for b in F['boxes']]+[(b[1],b[2]) for b in L['boxes']]
H2=collections.Counter(); H3=collections.defaultdict(list)
for x,(tp,bt) in enumerate(jets):
    H2[front.key2(tp,bt)]+=1; H3[front.key3(tp,bt)].append(x)
print('frontier',nF,'library',len(L['boxes']),'hashed',round(time.time()-t0,1),flush=True)
T=front.targets()
c2=collections.Counter(); c3=collections.Counter(); deep=[]; units=[]
for i in range(nF):
    tp,bt=jets[i]
    for Tg in T:
        n2=H2.get(front.need(Tg,tp,bt,2),0)
        if not n2: continue
        c2[Tg[0][0]]+=n2
        for j in H3.get(front.need(Tg,tp,bt,3),()):
            if j<nF and j<i: continue
            tq,bq=jets[j]
            d3t=tp[2][2]+tq[2][2]-Tg[1][2][2]; d3b=bt[2][2]+bq[2][2]-Tg[2][2][2]
            J,rt,rb,N=front.exact_closure(Tg,vecs[i],vecs[j])
            c3[(Tg[0][0],min(rt,rb))]+=1
            rec=(min(rt,rb),rt,rb,vc.span(J) if J else None,Tg[0],N,i,j,str(d3t),str(d3b))
            deep.append(rec)
            if J and len(J)==1: units.append(rec); print('UNIT',rec,names[i],names[j],flush=True)
    if i%20000==0: print(' ',i,dict(c2),dict(c3),round(time.time()-t0,1),flush=True)
print('second-order two-ended ties by closure type:',dict(c2))
print('third-order+ two-ended ties: (type, min depth) ->',sorted(c3.items()))
deep.sort(key=lambda r:(-r[0],r[3] if r[3] is not None else 999))
for r in deep[:25]:
    print('  ',r,names[r[6]][1],names[r[7]][1])
pickle.dump(dict(c2=c2,c3=c3,deep=deep[:5000],units=units,names=[names[r[6]] for r in deep[:200]]+[names[r[7]] for r in deep[:200]]),open('fr_pairs_%s.pkl'%tag,'wb'))
print('UNITS',len(units),'done',round(time.time()-t0,1))
