"""UNIFORM order-3 test of F1 over multiplicity vectors: S = order-3 subclasses of top-50 and of the 60 d2pos classes; mB-slices
|m| <= M.  'closed' = one exact certificate for every multiset on that slice."""
import sys, pickle, collections, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import f1o3, lpg, classes, exact, runner, eng
from fractions import Fraction as Fr
from multiprocessing import Pool
def subclasses(items,S):
    sub={}
    for c in S:
        for x in classes.SIGS[c.key]:
            d3=f1o3.boxdata3(items[x][2])
            k=(c.key,d3['top'][2],d3['top'][5],d3['bot'][2],d3['bot'][5])
            if k not in sub:
                b=lpg.Cls(c.key,0,c.label+'/%d'%len(sub)); b.d3=d3; b.x=x; sub[k]=b
            sub[k].w+=1
    return list(sub.values())
SS=None
def init(s):
    global SS; SS=s
def one(job):
    cl,m,q3=job
    S=SS
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m)
    if lpg.solve_primal(L).status!=0: return (cl['name'],m,q3,'closed@2',None)
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=l2-f1o3.EL3[i]
        if v: r[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        if f1o3.FL3[s]: r[L.iG+jj]=-f1o3.FL3[s]
    for j,b in enumerate(S):
        d3=b.d3[cl['end']]; v=-(d3[5]-d3[1])
        if v: r[j]=v
    L.add_eq(r,Fr(4,3)+q3-cl['p'][1]-m*m/2)
    d=runner.decide(L)
    if d[0]=='open':
        return (cl['name'],m,q3,'OPEN',{S[j].label:round(v,3) for j,v in enumerate(d[1][0]) if v>1e-9})
    return (cl['name'],m,q3,d[0],None)
if __name__=='__main__':
    t0=time.time(); M=int(sys.argv[1]) if len(sys.argv)>1 else 8
    items=exact.load_items()
    TOPK=int(sys.argv[2]) if len(sys.argv)>2 else 50
    S=subclasses(items,classes.top(TOPK))+subclasses(items,classes.d2pos())
    print('subclasses',len(S),flush=True)
    jobs=[]
    for cl in lpg.closure_classes():
        q3s=[f1o3.wq3(cl)[0]]
        if cl['kind']=='H' and abs(cl['mu'])==4: q3s.append(f1o3.lj(eng.W(5 if cl['mu']>0 else -5)[1],cl['end'])[2])
        for q3 in sorted(set(q3s)):
            for m in range(-M,M+1): jobs.append((cl,Fr(m),q3))
    with Pool(4,initializer=init,initargs=(S,)) as P: res=P.map(one,jobs,chunksize=2)
    c=collections.Counter(r[3] for r in res); print('F1 uniform slices:',len(res),dict(c),'time',round(time.time()-t0,1))
    for r in res:
        if r[3] not in ('closed','closed@2'): print('  ',r[:4],str(r[4])[:200])
    pickle.dump(res,open('f1uni_%d_%d.pkl'%(M,TOPK),'wb'))
