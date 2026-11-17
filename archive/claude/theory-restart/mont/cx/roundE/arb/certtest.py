"""Given the certified family S* (greedy_<tag>.pkl: D = removed classes), recompute an exact Farkas certificate (u,w) for every
case-LP over S*, and test each removed class d: its column in the same LP (rows identical, extra column) satisfies the dual
constraint A^T(u,w) >= 0 iff adding ANY multiplicity of d keeps that certificate valid.  Classes passing ALL certificates are
SAFE (can all be added at once).  Output certtest_<tag>.pkl."""
import sys, pickle, time, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import arblp, d2two, lpg, run_arblp
from fractions import Fraction as Fr
from multiprocessing import Pool
G=None
def init(g):
    global G; G=g
def one(job):
    Sstar,Dcl=G
    L=arblp.build_job(Sstar,job)
    f=lpg.farkas(L)
    if not isinstance(f,tuple): return (job,'nocert',None)
    u,w,val=f
    L2=arblp.build_job(Sstar+Dcl,job)
    assert len(L2.eq)==len(L.eq) and len(L2.ub)==len(L.ub)
    ns=len(Sstar); viol=[]
    for i in range(len(Dcl)):
        j=ns+i; s=Fr(0)
        for k,(r,b) in enumerate(L2.eq):
            if u[k] and j in r: s+=u[k]*r[j]
        for k,(r,b) in enumerate(L2.ub):
            if w[k] and j in r: s+=w[k]*r[j]
        if s<0: viol.append(i)
    return (job,'ok',viol)
if __name__=='__main__':
    tag=sys.argv[1]; files=sys.argv[2:]; t0=time.time()
    Gd=pickle.load(open('greedy_%s.pkl'%tag,'rb')); D=set(Gd['D'])
    Sall,reps=run_arblp.load(files); NB=len(d2two.S)
    Sstar=[c for c in Sall if c.label not in D]; Dcl=[c for c in Sall if c.label in D]
    jobs=arblp.jobs_for(Sall)
    print('S* %d, D %d, jobs %d'%(len(Sstar),len(Dcl),len(jobs)),flush=True)
    with Pool(3,initializer=init,initargs=((Sstar,Dcl),)) as P: res=P.map(one,jobs,chunksize=4)
    nocert=[r[0] for r in res if r[1]!='ok']
    vc_=collections.Counter(i for r in res if r[1]=='ok' for i in r[2])
    safe=[Dcl[i].label for i in range(len(Dcl)) if vc_[i]==0]
    print('jobs without certificate over S*:',len(nocert),nocert[:5])
    print('removed classes violating >= 1 certificate: %d ; SAFE (pass all): %d'%(len(Dcl)-len(safe),len(safe)))
    pickle.dump(dict(safe=safe,viol={Dcl[i].label:c for i,c in vc_.items()},nocert=nocert),open('certtest_%s.pkl'%tag,'wb'))
    print('time',round(time.time()-t0,1))
