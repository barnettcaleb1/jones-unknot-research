"""Pair census: query set = fr_<q>.pkl, partner pool = query u library A u fr_<extra>.pkl ...   argv: q extra..."""
import sys, pickle, collections, time
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, front, lp
q=sys.argv[1]; extras=sys.argv[2:]
t0=time.time()
Q=pickle.load(open('fr_%s.pkl'%q,'rb')); nQ=len(Q['boxes'])
jets=list(Q['jets']); vecs=list(Q['vecs']); names=[(b[1],b[2]) for b in Q['boxes']]
L=pickle.load(open('libA_jets.pkl','rb'))
jets+=[(b[3],b[4]) for b in L['boxes']]; vecs+=L['vecs']; names+=[(b[1],b[2]) for b in L['boxes']]
for e in extras:
    E=pickle.load(open('fr_%s.pkl'%e,'rb')); jets+=E['jets']; vecs+=E['vecs']; names+=[(b[1],b[2]) for b in E['boxes']]
H2=collections.Counter(); H3=collections.defaultdict(list)
for x,(tp,bt) in enumerate(jets):
    H2[front.key2(tp,bt)]+=1; H3[front.key3(tp,bt)].append(x)
print('query',nQ,'pool',len(jets),'hashed',round(time.time()-t0,1),flush=True)
T=front.targets(); c2=collections.Counter(); c3=collections.Counter(); deep=[]
PHI10={0:1,1:-1,2:1,3:-1,4:1}
for i in range(nQ):
    tp,bt=jets[i]
    for Tg in T:
        n2=H2.get(front.need(Tg,tp,bt,2),0)
        if not n2: continue
        c2[Tg[0][0]]+=n2
        for j in H3.get(front.need(Tg,tp,bt,3),()):
            if j<nQ and j<i: continue
            J,rt,rb,N=front.exact_closure(Tg,vecs[i],vecs[j])
            c3[(Tg[0][0],min(rt,rb))]+=1
            if min(rt,rb)>=4 or (J and len(J)<=8):
                Jn=vc.norm(J) if J else None
                g10=(vc.divexact(vc.sub(Jn,{0:1}),PHI10) is not None) if Jn else None
                deep.append((min(rt,rb),rt,rb,vc.span(J),Tg[0],N,i,j,lp.a2(Jn) if Jn else None,g10))
                if J and len(J)==1: print('UNIT',deep[-1],names[i],names[j],flush=True)
print('second-order ties:',dict(c2)); print('order>=3 ties (type,min depth):',sorted(c3.items()))
deep.sort(key=lambda r:(-r[0],r[3]))
for r in deep[:20]: print('  ',r,names[r[6]][1],names[r[7]][1])
pickle.dump(dict(c2=c2,c3=c3,deep=deep,names={k:names[k] for r in deep[:300] for k in (r[6],r[7])}),open('fr_pairs2_%s.pkl'%q,'wb'))
print('done',round(time.time()-t0,1))
