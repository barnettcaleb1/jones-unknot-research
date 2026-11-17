"""Certificate column test, general (candidates restricted to sigma in Z/2; sigma in Z/3, Z/4 classes left uncertified): S* = certified family from greedy_n2 (top-300 + D36 + n2-eligible minus D).
Candidates = D (n2 dangerous) + every ELIGIBLE signature of the extra gen1 pickles (n = 3, 4) not already in S*.
For every case-LP: exact Farkas (u,w) over S*; a candidate is compatible with that certificate iff its column c satisfies
c.(u,w) >= 0.  Candidates compatible with ALL certificates are SAFE: S* + (all safe) is still certified (same certificates).
The lattice of slices is taken from S* + ALL candidates (superset of attainable mB values)."""
import sys, pickle, time, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import arblp, d2two, lpg, run_arblp
from fractions import Fraction as Fr
from multiprocessing import Pool
G=None
def init(g):
    global G; G=g
def one(job):
    Sstar,Ccl=G
    L=arblp.build_job(Sstar,job)
    f=lpg.farkas(L)
    if not isinstance(f,tuple): return (job,'nocert',None)
    u,w,val=f
    L2=arblp.build_job(Sstar+Ccl,job)
    ns=len(Sstar); col=collections.defaultdict(Fr)
    for k,(r,b) in enumerate(L2.eq):
        if u[k]:
            for j,v in r.items():
                if j>=ns and j<ns+len(Ccl): col[j]+=u[k]*v
    for k,(r,b) in enumerate(L2.ub):
        if w[k]:
            for j,v in r.items():
                if j>=ns and j<ns+len(Ccl): col[j]+=w[k]*v
    viol=[j-ns for j,s in col.items() if s<0]
    return (job,'ok',viol)
if __name__=='__main__':
    t0=time.time()
    Gd=pickle.load(open('greedy_n2.pkl','rb')); D=set(Gd['D'])
    Sall,reps=run_arblp.load(['gen1_R5_n2.pkl'])
    Sstar=[c for c in Sall if c.label not in D]; Dcl=[c for c in Sall if c.label in D]
    keys=set(c.key for c in Sall)
    extra=[]
    for f in sys.argv[1:]:
        tot=pickle.load(open(f,'rb'))
        for k,(cnt,el,rep) in tot.items():
            if el and k not in keys and (k[2]*2).denominator==1:
                keys.add(k); c=lpg.Cls(k,cnt,'%s_%d'%(f.split('_')[2].split('.')[0],len(extra))); extra.append(c); reps[c.label]=(f,rep)
    Ccl=Dcl+extra
    jobs=arblp.jobs_for(Sstar+Ccl)
    print('S* %d classes, candidates %d (D %d + extra %d), jobs %d'%(len(Sstar),len(Ccl),len(Dcl),len(extra),len(jobs)),flush=True)
    res=[]
    with Pool(3,initializer=init,initargs=((Sstar,Ccl),)) as P:
        for r in P.imap_unordered(one,jobs,chunksize=4):
            res.append(r)
            if len(res)%200==0: print('progress',len(res),round(time.time()-t0,1),flush=True)
    nocert=[r[0] for r in res if r[1]!='ok']
    vc_=collections.Counter(i for r in res if r[1]=='ok' for i in r[2])
    safe=[i for i in range(len(Ccl)) if vc_[i]==0]
    print('jobs without certificate over S*:',len(nocert),nocert[:5])
    print('candidates violating >= 1 certificate: %d ; SAFE: %d (of D: %d, of extra: %d)'%(len(Ccl)-len(safe),len(safe),
          sum(1 for i in safe if i<len(Dcl)),sum(1 for i in safe if i>=len(Dcl))))
    pickle.dump(dict(safe=[Ccl[i].label for i in safe],unsafe=[(Ccl[i].label,Ccl[i].key,vc_[i]) for i in range(len(Ccl)) if vc_[i]],
                     reps=reps,nocert=nocert,n_extra=len(extra),n_D=len(Dcl),res=res,labels=[c.label for c in Ccl]),open('certtest2.pkl','wb'))
    print('time',round(time.time()-t0,1))
