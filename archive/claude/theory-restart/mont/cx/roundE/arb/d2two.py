"""(4c) TWO boxes from the 36 D36 classes (depth-2 positive-potential classes closed singly, lpgen Theorem D36) + ANY multiset of
top-300 boxes + any n >= 0 rational boxes: ONE uniform LP per case with the D36 multiplicities as variables summing to EXACTLY 2
(the 24 open d2 classes excluded).  Cases closed in lpgen's uniform top-300+d2pos run (uni_t300d2_n0.pkl, slices |m| <= 8) are
closed a fortiori; here: (i) the cases open there, (ii) all d=0 slices beyond 8 up to the explicit bounds (H: from the delta-law,
V: |m| <= 14, beyond that the two-exceptional phi bound, section 4c of REPORT).  Copies lpgen code read-only (imports)."""
import sys, pickle, time, collections
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG)
import classes, runner, lpg
from fractions import Fraction as Fr
from multiprocessing import Pool
U=pickle.load(open(LPG+'/uni_t300d2_n0.pkl','rb'))
OPENKEYS=sorted(set(k for k,v,info in U['res'] if v=='open'),key=str)
OPEN24='457 459 460 497 536 565 895 902 1232 1238 1247 1494 2557 2780 3075 3076 3077 3933 4277 4643 5150 5152 5153 5154'.split()
T=classes.top(300); D36=[c for c in classes.d2pos() if c.label.split('_')[1] not in OPEN24]
S=T+D36; NT=len(T)
CL={cl['name']:cl for cl in lpg.closure_classes()}; TC={tc['name']:tc for tc in lpg.tie_classes()}
EXTRA=[('eq',{j:Fr(1) for j in range(NT,len(S))},Fr(2))]
def job_list():
    jobs=[]
    for (cn,nm,m) in OPENKEYS: jobs.append((cn,nm,m))
    # extra slices beyond the uniform run's window
    for cl in lpg.closure_classes():
        if cl['kind']=='V': ms=[x for x in range(-14,15) if abs(x)>8]
        else: ms=[x for x in range(-12,13) if abs(x)>8]
        for m in ms:
            for nm,rows in lpg.case_rows(cl['p'],cl['q'],m=Fr(m)):
                jobs.append((cl['name'],nm,Fr(m)))
    return jobs
def one(job):
    cn,nm,m=job
    if nm=='tie':
        tc=TC[cn]; L=lpg.build(S,dict(tc,end='top'),[],0,kmin=0,slice_m=0,nrule=tc['n'],extra=EXTRA)
    else:
        cl=CL[cn]
        if m is None: L=lpg.build(S,cl,dict(lpg.case_rows(cl['p'],cl['q']))[nm],0,kmin=0,extra=EXTRA)
        else:
            rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m)).get(nm)
            if rows is None: return (job,'n/a',None)
            L=lpg.build(S,cl,rows,0,kmin=0,slice_m=m,nrule=cl['d0n'],extra=EXTRA)
    d=runner.decide(L)
    if d[0]=='open':
        k,n=d[1]; return (job,'open',({S[j].label:v for j,v in enumerate(k) if v>1e-9},n))
    if d[0]=='closed':
        u,w,val=d[1]; return (job,'closed',str(val))
    return (job,d[0],None)
if __name__=='__main__':
    t0=time.time(); jobs=job_list()
    print('S: %d top + %d D36 classes; jobs %d (open-in-uniform %d)'%(NT,len(D36),len(jobs),len(OPENKEYS)),flush=True)
    res=[]
    with Pool(3) as P:
        for i,r in enumerate(P.imap_unordered(one,jobs,chunksize=2)):
            res.append(r)
            if r[1] not in ('closed','n/a'): print('  ',r[0],r[1],str(r[2])[:300],flush=True)
            if (i+1)%50==0:
                pickle.dump(res,open('d2two.pkl','wb')); print('progress',i+1,'/',len(jobs),round(time.time()-t0,1),flush=True)
    pickle.dump(res,open('d2two.pkl','wb'))
    c=collections.Counter(r[1] for r in res)
    print('DONE',len(res),'/',len(jobs),dict(c),'time',round(time.time()-t0,1))
