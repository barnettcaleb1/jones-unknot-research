"""UNIFORM runs: S = class set; every multiplicity vector k >= 0 with kmin <= sum k (<= kmax), every n >= nmin.
For each case LP: closed (exact Farkas certificate valid for ALL such k) or open; for open cases characterise the open region:
participating classes (k_j >= 1 feasible), unbounded classes (k_j >= 50 feasible), minimal integer combos (MILP)."""
import sys, time, collections, pickle, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import classes, runner, lpg
from fractions import Fraction as Fr
from multiprocessing import Pool
ARGS=None
def jobs(S,nmin,kmin,kmax,M):
    out=[]
    for cl in lpg.closure_classes():
        for nm,rows in lpg.case_rows(cl['p'],cl['q']):
            out.append((cl,nm,rows,None,None))
        for m in runner.slices(S,cl,None,M):
            for nm,rows in lpg.case_rows(cl['p'],cl['q'],m=m):
                out.append((cl,nm,rows,m,cl['d0n']))
    for tc in lpg.tie_classes():
        out.append((dict(tc,end='top'),'tie',[],0,tc['n']))
    return out
def extra_kmax(S,kmax):
    if kmax is None: return []
    return [('ub',{j:Fr(1) for j in range(len(S))},Fr(kmax))]
def init(a):
    global ARGS
    ARGS=a
def work(job):
    S,nmin,kmin,kmax=ARGS
    cl,nm,rows,m,nr=job
    ex=extra_kmax(S,kmax)
    L=lpg.build(S,cl,rows,nmin,kmin=kmin,slice_m=m,nrule=nr,extra=ex)
    d=runner.decide(L)
    key=(cl['name'],nm,m)
    if d[0]!='open': return key,d[0],None
    # characterise
    part=[]; unb=[]
    for j in range(len(S)):
        L2=lpg.build(S,cl,rows,nmin,kmin=kmin,slice_m=m,nrule=nr,extra=ex+[('ub',{j:Fr(-1)},Fr(-1))])
        r=lpg.solve_primal(L2)
        if r.status==0:
            part.append(j)
            if kmax is None:
                L3=lpg.build(S,cl,rows,nmin,kmin=kmin,slice_m=m,nrule=nr,extra=ex+[('ub',{j:Fr(-1)},Fr(-50))])
                if lpg.solve_primal(L3).status==0: unb.append(j)
    ri=lpg.solve_primal(L,integral=True)
    isol=None
    if ri.status==0 and ri.x is not None:
        isol=([int(round(x)) for x in ri.x[:L.nk]],int(round(ri.x[L.iN])))
    return key,'open',dict(real=d[1],part=part,unb=unb,isol=isol,milp=ri.status)
def main(tag,S,nmin,kmin,kmax=None,M=8):
    global ARGS
    t0=time.time()
    ARGS=(S,nmin,kmin,kmax)
    J=jobs(S,nmin,kmin,kmax,M)
    with Pool(9,initializer=init,initargs=(ARGS,)) as P: res=P.map(work,J,chunksize=2)
    cnt=collections.Counter(r[1] for r in res)
    print('[%s] |S|=%d nmin=%d kmin=%d kmax=%s: %d case-LPs, %s  (%.1fs)'%(tag,len(S),nmin,kmin,kmax,len(J),dict(cnt),time.time()-t0),flush=True)
    opn=[(k,info) for k,v,info in res if v=='open']
    for k,info in sorted(opn,key=str):
        print('  OPEN',k,'part=%s unb=%s isol=%s'%([S[j].label for j in info['part']][:12]+(['...%d'%len(info['part'])] if len(info['part'])>12 else []),
              [S[j].label for j in info['unb']][:8],
              (None if info['isol'] is None else ({S[j].label:v for j,v in enumerate(info['isol'][0]) if v},info['isol'][1]))),flush=True)
    bad=[(k,v) for k,v,info in res if v not in ('open','closed')]
    if bad: print('  NONSTANDARD',bad[:10])
    pickle.dump(dict(res=res,S=[(c.key,c.w,c.label) for c in S],nmin=nmin,kmin=kmin,kmax=kmax),open('uni_%s.pkl'%tag,'wb'))
    return res
if __name__=='__main__':
    which=sys.argv[1]
    if which=='t50':
        S=classes.top(50)+[c for c in classes.d2pos()]
        main('t50d2_n0',S,0,1)
    elif which=='t50only':
        main('t50_n0',classes.top(50),0,1)
    elif which=='t300only':
        main('t300_n0',classes.top(300),0,1)
    elif which=='t300':
        S=classes.top(300)+[c for c in classes.d2pos()]
        main('t300d2_n0',S,0,1)
if __name__=='__main__' and sys.argv[1]=='t300k2':
    main('t300_n0_k2',classes.top(300),0,2)
if __name__=='__main__' and sys.argv[1]=='t300n1':
    main('t300_n1_k1',classes.top(300),1,1)
if __name__=='__main__' and sys.argv[1]=='t50k2':
    main('t50_n0_k2',classes.top(50),0,2)
