"""ORDER-3 closure of F1 ('d=-1 e=-1') re-done with EXACT certificates for EVERY slice, verified by the own semantic
checker (semcheck.py) with own data (own automaton l3, own subclass l3 data, own closure q3/p2, own derived order-3 row).
S = all order-3 subclasses of the top-300 and the 60 d2pos classes (from own classdata.pkl), any multiplicities, n >= 0.
Parts: SLICES |mB| <= 30 (order-2 F1 slice LP; if feasible add the order-3 EQUALITY row); BOUND mB <= -31 (order 2);
LARGE mB >= 31 (LHS - 4 mB < b', then the quadratic).  Generation: lpgen's lpg.build/lpg.farkas + f1o3 l3 tables."""
import sys, pickle, time, collections, os, math
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import semcheck as SC, certcheck as CC
import lpg, f1o3
from multiprocessing import Pool
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
CD=CC.CD; W=CC.W
SUB=[]   # (label, order-2 key, (l3a_top, l3b_top, l3a_bot, l3b_bot))
for lab in ['top%d'%i for i in range(300)]+sorted([k for k in CD if k.startswith('d2_')],key=lambda s:int(s[3:])):
    for d3 in sorted(CD[lab]['sub']): SUB.append((lab,CD[lab]['key'],d3))
S=[lpg.Cls(k,1,l) for l,k,d3 in SUB]
NSUB=len(SUB)
def wd(cl):
    """own (p, q) log-jets to order 3 at the weak end for the closure class"""
    if cl['kind']=='V':
        a=(3 if cl['asg']>0 else -3) if (cl['typ']=='+' or cl['a3']) else (5 if cl['asg']>0 else -5)
        o=W['V'][a][0][cl['end']]
    else:
        mu=cl['mu']; o=W['H'][mu][0][cl['end']]
    return o[0],o[1]
def cdat(j,end):
    l,key,d3=SUB[j]; ra,la,rb,lb=key[0] if end=='top' else key[1]; sig=key[2]
    l3a,l3b=(d3[0],d3[1]) if end=='top' else (d3[2],d3[3])
    return ra,la,rb,lb,sig,l3a,l3b
def sem_case_rows(cl,rows,msub):
    """semantic rows from lpgen's case rows (checked to be implied by the own derivation) with OWN class data"""
    end=cl['end']; out=[]
    if rows:
        mine=CC.my_rows('d=-1 e=-1',cl['p'],cl['q'],None)
        th=[CC.their_vec(r,None) for r in rows]
        for variant in mine: assert CC.rank(variant+th)==CC.rank(variant), 'row not implied'
    for coef,a in rows:
        cls=[]
        for j in range(NSUB):
            ra,la,rb,lb,sig,l3a,l3b=cdat(j,end)
            cls.append(-(a[1]*ra+a[2]*la+a[3]*rb+a[4]*lb+a[5]*sig))
        out.append(dict(kind='eq',z=(coef[0],coef[1],coef[2],coef[3],0,0),cls=cls,n=0,b=a[0]-a[5]*cl['sigstar']))
    return out
def sem_order3(cl,m):
    """OWN order-3 equality: sum_boxes (l2a - l3a - l3q) - sum_j k_j (l3b_j - l2a_j) = 4/3 + q3 - p2 - m^2/2"""
    p,q=wd(cl); end=cl['end']
    cls=[]
    for j in range(NSUB):
        ra,la,rb,lb,sig,l3a,l3b=cdat(j,end); cls.append(-(l3b-la))
    return dict(kind='eq',z=(0,0,1,0,-1,-1),cls=cls,n=0,b=Fr(4,3)+q[2]-p[1]-m*m/2)
def gen_o3row(L,cl,m):
    """generator-side order-3 row on lpgen's LP variables (their automaton edge l3 table f1o3.EL3/FL3)"""
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=l2-f1o3.EL3[i]
        if v: r[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        if f1o3.FL3[s]: r[L.iG+jj]=-f1o3.FL3[s]
    end=cl['end']
    for j in range(NSUB):
        ra,la,rb,lb,sig,l3a,l3b=cdat(j,end); v=-(l3b-la)
        if v: r[j]=v
    p,q=wd(cl)
    return r,Fr(4,3)+q[2]-p[1]-m*m/2
def slice_job(arg):
    cname,m=arg
    cl={c['name']:c for c in lpg.closure_classes()}[cname]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m)
    sem=sem_case_rows(cl,rows,None)+[dict(kind='eq',z=(0,)*6,cls=[SUB[j][1][2] for j in range(NSUB)],n=0,b=m+cl['sigstar'])]
    semub=[dict(kind='ub',z=(0,)*6,cls=[-1]*NSUB,n=0,b=-1)]
    r=lpg.solve_primal(L)
    if r.status!=0:
        f=lpg.farkas(L)
        if not isinstance(f,tuple): return (cname,m,'o2-nocert',r.status)
        u,w,val=f
        ok,info=SC.check(sem+semub,list(u[19:])+list(w),NSUB,0)
        return (cname,m,'o2-VERIFIED' if ok else 'o2-REJECTED',info if not ok else None)
    rr,c3=gen_o3row(L,cl,m); L.add_eq(rr,c3)
    r=lpg.solve_primal(L)
    if r.status==0:
        return (cname,m,'OPEN',{SUB[j][0]+'/'+str(j):round(v,3) for j,v in enumerate(r.x[:L.nk]) if v>1e-9})
    f=lpg.farkas(L)
    if not isinstance(f,tuple): return (cname,m,'o3-nocert',r.status)
    u,w,val=f
    sem3=sem+[sem_order3(cl,m)]
    ok,info=SC.check(sem3+semub,list(u[19:])+list(w),NSUB,0)
    return (cname,m,'o3-VERIFIED' if ok else 'o3-REJECTED',info if not ok else None)
def bound_job(arg):
    cname,sgn,B=arg
    cl={c['name']:c for c in lpg.closure_classes()}[cname]
    S2=[lpg.Cls(CD[l]['key'],1,l) for l in ['top%d'%i for i in range(300)]+sorted([k for k in CD if k.startswith('d2_')],key=lambda s:int(s[3:]))]
    keys=[c.key for c in S2]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    ex=[('ub',{j:-sgn*c.sig for j,c in enumerate(S2) if c.sig},-(B+1)-sgn*cl['sigstar'])]
    L=lpg.build(S2,cl,rows,0,kmin=1,extra=ex)
    r=lpg.solve_primal(L)
    if r.status==0: return (cname,sgn,'open')
    f=lpg.farkas(L)
    if not isinstance(f,tuple): return (cname,sgn,'nocert')
    u,w,val=f
    end=cl['end']; sem=[]
    for coef,a in rows:
        cls=[]
        for key in keys:
            ra,la,rb,lb=key[0] if end=='top' else key[1]; cls.append(-(a[1]*ra+a[2]*la+a[3]*rb+a[4]*lb+a[5]*key[2]))
        sem.append(dict(kind='eq',z=(coef[0],coef[1],coef[2],coef[3],0,0),cls=cls,n=0,b=a[0]-a[5]*cl['sigstar']))
    semub=[dict(kind='ub',z=(0,)*6,cls=[-1]*len(keys),n=0,b=-1),
           dict(kind='ub',z=(0,)*6,cls=[-sgn*k[2] for k in keys],n=0,b=-(B+1)-sgn*cl['sigstar'])]
    ok,info=SC.check(sem+semub,list(u[19:])+list(w),len(keys),0)
    return (cname,sgn,'VERIFIED' if ok else 'REJECTED')
def large_job(arg):
    cname,A=arg
    cl={c['name']:c for c in lpg.closure_classes()}[cname]
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    L=lpg.build(S,cl,rows,0,kmin=1,extra=[('ub',{j:-c.sig for j,c in enumerate(S) if c.sig},-31-cl['sigstar'])])
    end=cl['end']
    # LHS row (generator side) and objective
    r={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=f1o3.EL3[i]-l2
        if v: r[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        if f1o3.FL3[s]: r[L.iG+jj]=f1o3.FL3[s]
    for j in range(NSUB):
        ra,la,rb,lb,sig,l3a,l3b=cdat(j,end); v=l3b-la
        if v: r[j]=r.get(j,0)+v
    obj={j:-float(v) for j,v in r.items()}
    for j,c in enumerate(S):
        if c.sig: obj[j]=obj.get(j,0)+float(A*c.sig)
    res=lpg.solve_primal(L,obj=obj)
    if res.status!=0: return (cname,'LP status %d'%res.status)
    opt=-res.fun+float(A*cl['sigstar']); bp=Fr(math.floor(opt)+1)
    r2={j:-v for j,v in r.items()}
    for j,c in enumerate(S):
        if c.sig: r2[j]=r2.get(j,0)+A*c.sig
    L.add_ub(r2,-bp+A*cl['sigstar'])
    f=lpg.farkas(L)
    if not isinstance(f,tuple): return (cname,'nocert',bp)
    u,w,val=f
    sem=sem_case_rows(cl,rows,None)
    cls_l=[]; 
    for j in range(NSUB):
        ra,la,rb,lb,sig,l3a,l3b=cdat(j,end); cls_l.append(-(l3b-la)+A*sig)
    semub=[dict(kind='ub',z=(0,)*6,cls=[-1]*NSUB,n=0,b=-1),
           dict(kind='ub',z=(0,)*6,cls=[-SUB[j][1][2] for j in range(NSUB)],n=0,b=-31-cl['sigstar']),
           dict(kind='ub',z=(0,0,1,0,-1,-1),cls=cls_l,n=0,b=-bp+A*cl['sigstar'])]
    ok,info=SC.check(sem+semub,list(u[19:])+list(w),NSUB,0)
    p,q=wd(cl); c0=Fr(4,3)+q[2]-p[1]
    disc=A*A+2*(bp+c0)      # mB^2/2 - A mB - (bp + c0) < 0 needs disc > 0 and mB < A + sqrt(disc)
    return (cname,'VERIFIED' if ok else 'REJECTED',bp,disc,'quadratic impossible' if disc<0 else ('mB < %.2f'%(float(A)+math.sqrt(float(disc)))))
if __name__=='__main__':
    t0=time.time(); which=sys.argv[1]
    names=[c['name'] for c in lpg.closure_classes()]
    print('subclasses',NSUB,flush=True)
    if which=='slices':
        M=int(sys.argv[2]); jobs=[(n,Fr(m)) for n in names for m in range(-M,M+1)]
        out=[]; cnt=collections.Counter()
        with Pool(5) as P:
            for res in P.imap_unordered(slice_job,jobs,chunksize=2):
                out.append(res); cnt[res[2]]+=1
                if res[2] not in ('o2-VERIFIED','o3-VERIFIED'): print('  ',res,flush=True)
                if len(out)%100==0: print(len(out),dict(cnt),'%.0fs'%(time.time()-t0),flush=True); pickle.dump(out,open(HERE+'f1redo_slices.pkl','wb'))
        pickle.dump(out,open(HERE+'f1redo_slices.pkl','wb'))
        print('SLICES |mB| <= %d: %d slice-LPs %s  (%.0fs)'%(M,len(out),dict(cnt),time.time()-t0),flush=True)
    elif which=='bound':
        jobs=[(n,s,30) for n in names for s in (1,-1)]
        with Pool(4) as P: out=P.map(bound_job,jobs)
        for o in out: print('  ',o)
        print('BOUND |mB| > 30 at order 2:',collections.Counter(o[2] for o in out if o[1]==-1),' (mB >= 31 side:',collections.Counter(o[2] for o in out if o[1]==1),')')
    elif which=='large':
        jobs=[(n,Fr(4)) for n in names]
        with Pool(4) as P: out=P.map(large_job,jobs)
        for o in out: print('  ',o)
