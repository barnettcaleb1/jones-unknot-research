"""ORDER-3 cut for the mirror case F1' = 'd=1 e=-1' (offset +1, eps = -1; S1 leads):  f = s1 - u s2 = 1 + u + u^2 + 0u^3:
 X1 = 2, l2(s1) = X2 - 1, X2 = X1 + mB = 2 + mB pinned, and  l3(s1) - l2(s2) = mB^2/2 - 4/3  (EQUALITY; PROVED as in REPORT 5.2).
 LHS' = L3a - L_a - Lambda + sum_j k_j (l3a_j - l2b_j) = mB^2/2 - 4/3 - p3 + q2.  Uniform over all multisets, slices |mB| <= M."""
import sys, pickle, collections, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import f1uni, f1o3, lpg, classes, exact, runner, eng
from fractions import Fraction as Fr
from multiprocessing import Pool
def p3of(cl,mu5=False):
    if cl['kind']=='V': return Fr(0)
    mu=cl['mu'] if not mu5 else (5 if cl['mu']>0 else -5)
    return f1o3.lj(eng.W(mu)[0],cl['end'])[2]
def row3(L,S,cl):
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=f1o3.EL3[i]-l2
        if v: r[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        v=-lpg.FIN[s][1]
        if v: r[L.iG+jj]=v
    for j,b in enumerate(S):
        d3=b.d3[cl['end']]; v=d3[2]-d3[4]
        if v: r[j]=r.get(j,0)+v
    return r
SS=None
def init(s):
    global SS; SS=s
def one(job):
    cl,m,p3=job; S=SS
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=1 e=-1']
    L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m)
    if lpg.solve_primal(L).status!=0: return (cl['name'],m,p3,'closed@2',None)
    L.add_eq(row3(L,S,cl),m*m/2-Fr(4,3)-p3+cl['q'][1])
    d=runner.decide(L)
    if d[0]=='open': return (cl['name'],m,p3,'OPEN',{S[j].label:round(v,3) for j,v in enumerate(d[1][0]) if v>1e-9})
    return (cl['name'],m,p3,d[0],None)
if __name__=='__main__':
    t0=time.time(); M=int(sys.argv[1]); TOPK=int(sys.argv[2])
    items=exact.load_items()
    S=f1uni.subclasses(items,classes.top(TOPK))+f1uni.subclasses(items,classes.d2pos())
    jobs=[]
    for cl in lpg.closure_classes():
        p3s=[p3of(cl)]
        if cl['kind']=='H' and abs(cl['mu'])==4: p3s.append(p3of(cl,True))
        for p3 in sorted(set(p3s)):
            for m in range(-M,M+1): jobs.append((cl,Fr(m),p3))
    with Pool(4,initializer=init,initargs=(S,)) as P: res=P.map(one,jobs,chunksize=2)
    c=collections.Counter(r[3] for r in res); print("F1' (d=1 e=-1) uniform slices:",len(res),dict(c),'time',round(time.time()-t0,1),flush=True)
    for r in res:
        if r[3] not in ('closed','closed@2'): print('  ',r[:4],str(r[4])[:200])
    pickle.dump(res,open('f1b_%d_%d.pkl'%(M,TOPK),'wb'))
