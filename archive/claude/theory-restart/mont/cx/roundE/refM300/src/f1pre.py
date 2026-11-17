"""F1' ('d=1 e=-1', mirror of F1) re-done with exact certificates for every slice |mB| <= 30, own semantic check.
Order-3 EQUALITY (sympy): l3(s1) - l2(s2) = mB^2/2 - 4/3, i.e. sum_boxes (l3a - l2a - lambda_q) + sum_j k_j (l3a_j - l2b_j)
= mB^2/2 - 4/3 - p3 + q2 (p3 = l3(w1), q2 = l2(w2) at the weak end; |mu| = 4 and |mu| >= 5 differ in p3: both run)."""
import sys, pickle, time, collections
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import f1redo as F, semcheck as SC, certcheck as CC
import lpg, f1o3
from multiprocessing import Pool
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
NSUB=F.NSUB; S=F.S; W=CC.W
def wd3(cl,mu5=False):
    if cl['kind']=='V': return F.wd(cl)
    mu=cl['mu'] if not mu5 else (5 if cl['mu']>0 else -5)
    o=W['H'][mu][0][cl['end']]; return o[0],o[1]
def job(arg):
    cname,m,mu5=arg
    cl={c['name']:c for c in lpg.closure_classes()}[cname]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=1 e=-1']
    # own derivation check of the rows
    mine=CC.my_rows('d=1 e=-1',cl['p'],cl['q'],None); th=[CC.their_vec(r,None) for r in rows]
    for v in mine: assert CC.rank(v+th)==CC.rank(v)
    L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m)
    end=cl['end']; sem=[]
    for coef,a in rows:
        cls=[]
        for j in range(NSUB):
            ra,la,rb,lb,sig,l3a,l3b=F.cdat(j,end); cls.append(-(a[1]*ra+a[2]*la+a[3]*rb+a[4]*lb+a[5]*sig))
        sem.append(dict(kind='eq',z=(coef[0],coef[1],coef[2],coef[3],0,0),cls=cls,n=0,b=a[0]-a[5]*cl['sigstar']))
    sem.append(dict(kind='eq',z=(0,)*6,cls=[F.SUB[j][1][2] for j in range(NSUB)],n=0,b=m+cl['sigstar']))
    semub=[dict(kind='ub',z=(0,)*6,cls=[-1]*NSUB,n=0,b=-1)]
    r=lpg.solve_primal(L)
    if r.status!=0:
        f=lpg.farkas(L)
        if not isinstance(f,tuple): return (cname,m,mu5,'o2-nocert')
        u,w,val=f; ok,info=SC.check(sem+semub,list(u[19:])+list(w),NSUB,0)
        return (cname,m,mu5,'o2-VERIFIED' if ok else 'o2-REJECTED')
    p,q=wd3(cl,mu5)
    rr={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=f1o3.EL3[i]-l2
        if v: rr[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        v=-lpg.FIN[s][1]
        if v: rr[L.iG+jj]=v
    cls3=[]
    for j in range(NSUB):
        ra,la,rb,lb,sig,l3a,l3b=F.cdat(j,end); cls3.append(l3a-lb)
        if l3a-lb: rr[j]=rr.get(j,0)+(l3a-lb)
    c3=m*m/2-Fr(4,3)-p[2]+q[1]
    L.add_eq(rr,c3)
    r=lpg.solve_primal(L)
    if r.status==0: return (cname,m,mu5,'OPEN',{F.SUB[j][0]:round(v,3) for j,v in enumerate(r.x[:L.nk]) if v>1e-9},round(r.x[L.iN],3))
    f=lpg.farkas(L)
    if not isinstance(f,tuple): return (cname,m,mu5,'o3-nocert')
    u,w,val=f
    sem3=sem+[dict(kind='eq',z=(0,0,-1,-1,1,0),cls=cls3,n=0,b=c3)]
    ok,info=SC.check(sem3+semub,list(u[19:])+list(w),NSUB,0)
    return (cname,m,mu5,'o3-VERIFIED' if ok else 'o3-REJECTED')
if __name__=='__main__':
    t0=time.time(); M=30
    jobs=[]
    for cl in lpg.closure_classes():
        for m in range(-M,M+1):
            jobs.append((cl['name'],Fr(m),False))
            if cl['kind']=='H' and abs(cl['mu'])==4: jobs.append((cl['name'],Fr(m),True))
    out=[]; cnt=collections.Counter()
    with Pool(4) as P:
        for res in P.imap_unordered(job,jobs,chunksize=2):
            out.append(res); cnt[res[3]]+=1
            if res[3] not in ('o2-VERIFIED','o3-VERIFIED'): print('  ',res,flush=True)
    pickle.dump(out,open(HERE+'f1pre.pkl','wb'))
    print("F1' slices |mB| <= 30: %d slice-LPs %s (%.0fs)"%(len(out),dict(cnt),time.time()-t0),flush=True)
