"""THEOREM D36* attempt: ANY multiset of boxes from top-300 u D36 classes (any number of D36 boxes, >= 1 box in all) x any n >= 0
rational boxes x any N: no flat closure.  All C1/lpgen case-LPs uniformly (kmin = 1), d=0 slices |m| <= 14 (H: the delta-law
bounds the box count by 3, so |mB| <= 14), and for vertical d=0 with mB >= 15 an exact LINEAR relaxation of the r=1 relation
  sum phi - c0 = (p2 - q2 - LAM)/mB,  mB >= 15   (two LPs by the sign of X = p2 - q2 - LAM)
and of the r=0 relations (sum phi = c0;  (La+Lb)_all + p2 + q2 = 1 - mB^2/4 <= 1 - 15 mB/4).
(mB <= -15 is impossible: every sigma >= 0 and sigma*_V = -1.)"""
import sys, pickle, time, collections
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import classes, runner, lpg, d2two
from fractions import Fraction as Fr
from multiprocessing import Pool
S=d2two.S; NT=d2two.NT
CL={cl['name']:cl for cl in lpg.closure_classes()}; TC={tc['name']:tc for tc in lpg.tie_classes()}
def jobs_all(M=14):
    jobs=[]
    for cl in lpg.closure_classes():
        for nm,rows in lpg.case_rows(cl['p'],cl['q']): jobs.append(('case',cl['name'],nm,None))
        for m in range(-M,M+1):
            for nm,rows in lpg.case_rows(cl['p'],cl['q'],m=Fr(m)): jobs.append(('case',cl['name'],nm,Fr(m)))
        if cl['kind']=='V':
            for kind in ('r1+','r1-','r0'): jobs.append(('big',cl['name'],kind,None))
    for tc in lpg.tie_classes(): jobs.append(('tie',tc['name'],'tie',0))
    return jobs
def addrow(L,kind,r,b):
    (L.add_eq if kind=='eq' else L.add_ub)(r,Fr(b))
def lin(L,coef4,kcoef):
    r=L.zrow(coef4)
    for j,v in kcoef.items():
        if v: r[j]=r.get(j,0)+v
    return r
def neg(r): return {i:-v for i,v in r.items()}
def comb(*pairs):
    out={}
    for s,r in pairs:
        for i,v in r.items(): out[i]=out.get(i,0)+s*v
    return out
def big(cl,kind):
    end=cl['end']; (p1,p2),(q1,q2)=cl['p'],cl['q']; c0=1-(p1+q1)/2; ss=cl['sigstar']
    L=lpg.build(S,cl,[],0,kmin=1,nrule=cl['d0n'])
    ra={j:c.end(end)[0] for j,c in enumerate(S)}; la={j:c.end(end)[1] for j,c in enumerate(S)}
    rb={j:c.end(end)[2] for j,c in enumerate(S)}; lb={j:c.end(end)[3] for j,c in enumerate(S)}
    sig={j:c.sig for j,c in enumerate(S)}
    RA=lin(L,(1,0,0,0),ra); RQ=lin(L,(0,1,0,0),{j:rb[j]-ra[j] for j in ra})
    LAM=lin(L,(0,0,0,1),{j:lb[j]-la[j] for j in ra}); LALB=lin(L,(0,0,2,1),{j:la[j]+lb[j] for j in ra})
    SPHI=comb((1,RA),(Fr(1,2),RQ))
    addrow(L,'eq',comb((1,RQ),(-1,sig)),p1-q1-ss)            # P0 row
    addrow(L,'ub',neg(sig),-(15+ss))                          # mB >= 15
    if kind=='r1+':
        addrow(L,'ub',LAM,p2-q2); addrow(L,'ub',neg(SPHI),-c0); addrow(L,'ub',comb((15,SPHI),(1,LAM)),p2-q2+15*c0)
    elif kind=='r1-':
        addrow(L,'ub',neg(LAM),-(p2-q2)); addrow(L,'ub',SPHI,c0); addrow(L,'ub',neg(comb((15,SPHI),(1,LAM))),-(p2-q2+15*c0))
    else:
        addrow(L,'eq',SPHI,c0); addrow(L,'ub',comb((1,LALB),(Fr(15,4),sig)),1-p2-q2+Fr(15,4)*ss)
    return L
def one(job):
    typ,cn,nm,m=job
    if typ=='tie':
        tc=TC[cn]; L=lpg.build(S,dict(tc,end='top'),[],0,kmin=1,slice_m=0,nrule=tc['n'])
    elif typ=='big': L=big(CL[cn],nm)
    else:
        cl=CL[cn]
        if m is None: L=lpg.build(S,cl,dict(lpg.case_rows(cl['p'],cl['q']))[nm],0,kmin=1)
        else:
            rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m)).get(nm)
            L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m,nrule=cl['d0n'])
    d=runner.decide(L)
    if d[0]=='open':
        k,n=d[1]; return (job,'open',({S[j].label:v for j,v in enumerate(k) if v>1e-9},n))
    return (job,d[0],str(d[1][2]) if d[0]=='closed' else None)
if __name__=='__main__':
    t0=time.time(); jobs=jobs_all()
    print('S = top-300 + %d D36 classes (any multiplicities); jobs %d'%(len(S)-NT,len(jobs)),flush=True)
    res=[]
    with Pool(3) as P:
        for r in P.imap_unordered(one,jobs,chunksize=4):
            res.append(r)
            if r[1]!='closed': print('  ',r[0],r[1],str(r[2])[:300],flush=True)
    pickle.dump(res,open('d36star.pkl','wb'))
    print('DONE',len(res),dict(collections.Counter(r[1] for r in res)),'time',round(time.time()-t0,1))
