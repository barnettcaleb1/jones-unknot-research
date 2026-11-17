"""INDEPENDENT re-check of THEOREM ARB-2 on random case-LPs: build the LP over the FULL certified family S** (S* + all safe
classes), take the exact Farkas vector y found over S* (lpg.farkas), and verify with independent code, in exact arithmetic, that
(i) A^T y >= 0 on EVERY column (x >= lb shifted), (ii) b'.y < 0 -- i.e. the LP over S** is infeasible with the same certificate."""
import sys, pickle, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import arblp, d2two, lpg, run_arblp
from fractions import Fraction as Fr
from multiprocessing import Pool
G=None
def init(g):
    global G; G=g
def check(job):
    Sstar,Sss=G
    L=arblp.build_job(Sstar,job); f=lpg.farkas(L)
    if not isinstance(f,tuple): return (job,'nocert')
    u,w,val=f
    L2=arblp.build_job(Sss,job)
    if len(L2.eq)!=len(L.eq) or len(L2.ub)!=len(L.ub): return (job,'rowmismatch')
    col=[Fr(0)]*L2.nv
    for k,(r,b) in enumerate(L2.eq):
        if u[k]:
            for j,v in r.items(): col[j]+=u[k]*v
    for k,(r,b) in enumerate(L2.ub):
        if w[k]<0: return (job,'w<0')
        if w[k]:
            for j,v in r.items(): col[j]+=w[k]*v
    if any(c<0 for c in col): return (job,'COLUMN VIOLATION %d'%sum(1 for c in col if c<0))
    lb=L2.lb
    bval=sum(u[k]*(b-sum(v*lb[j] for j,v in r.items())) for k,(r,b) in enumerate(L2.eq))+sum(w[k]*(b-sum(v*lb[j] for j,v in r.items())) for k,(r,b) in enumerate(L2.ub))
    return (job,'OK' if bval<0 else 'b.y >= 0')
if __name__=='__main__':
    random.seed(2026); t0=time.time()
    Gd=pickle.load(open('greedy_n2.pkl','rb')); D=set(Gd['D'])
    Sall,reps=run_arblp.load(['gen1_R5_n2.pkl'])
    Sstar=[c for c in Sall if c.label not in D]
    C=pickle.load(open('certtest2.pkl','rb')); safe=set(C['safe'])
    # rebuild candidate classes in the same way as certtest2
    keys=set(c.key for c in Sall); extra=[]
    for f in ('gen1_R5_n3.pkl','gen1_R4_n4.pkl'):
        tot=pickle.load(open(f,'rb'))
        for k,(cnt,el,rep) in tot.items():
            if el and k not in keys and (k[2]*2).denominator==1:
                keys.add(k); c=lpg.Cls(k,cnt,'%s_%d'%(f.split('_')[2].split('.')[0],len(extra))); extra.append(c)
    Dcl=[c for c in Sall if c.label in D]
    Sss=Sstar+[c for c in Dcl+extra if c.label in safe]
    jobs=arblp.jobs_for(Sstar+Dcl+extra)
    sample=random.sample(jobs,120)
    print('S* %d, S** %d, jobs %d, sample %d'%(len(Sstar),len(Sss),len(jobs),len(sample)),flush=True)
    with Pool(3,initializer=init,initargs=((Sstar,Sss),)) as P: res=P.map(check,sample,chunksize=2)
    import collections
    print(collections.Counter(r[1] for r in res),'time',round(time.time()-t0,1))
    pickle.dump(res,open('verify_arb2.pkl','wb'))
