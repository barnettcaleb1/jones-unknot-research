"""ENGINE lpgen: multi-box Farkas/LP generator over JET CLASSES.
Products  Y^N (B_1^{k_1} ... B_S^{k_S}) u_1 ... u_n  of non-rational boxes drawn from a finite set S of jet classes (multiplicity
vector k) and n rational non-integral boxes, closed horizontally (X^mu, every mu != 0) or vertically (every odd |a| >= 3).
End-jet data (rho_a, l2(a), rho_b, l2(b) at each end; sigma; delta) are ADDITIVE under the star product, so the weak-end casework
of engine C1 (v3b.cases / h3b.cases_pq, copied in c1copy/) is AFFINE in k (except the d=0 cases, which are quadratic in mB and are
sliced by the value m = mB).  The rational part is the n-fold sum of per-box vectors (rho_a, rho_q, l2(a), lambda_q), relaxed EXACTLY
to n * conv (flow polyhedron of the K=3 jet automaton: n unit paths from init, edge vectors (l1,l2) of D, terminal (rho_q,lambda_q)).
So for each case the set of (k, n) admitting no certificate is a POLYHEDRON; infeasibility <=> a Farkas certificate valid for ALL
multiplicity vectors at once.  LPs solved by HiGHS (floats); every certificate is rationalised and VERIFIED EXACTLY (Fractions)."""
import sys, itertools, collections, time, pickle
from fractions import Fraction as Fr
C1='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/c1copy'
sys.path.insert(0,C1); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import numpy as np
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
import v3b3, v3b, h3b

ST=v3b3.STATES; NS=len(ST); INIT=v3b3.INIT; EI=v3b3.EI; NE=len(EI)
FINS=[s for s in range(NS) if s!=INIT]
FIN={s:(v3b3.FIN[s][0],v3b3.FIN[s][1]) for s in FINS}

# ---------------- closure classes ----------------
def closure_classes():
    out=[]
    for end in ('top','bot'):
        for asg in (1,-1):
            typ='+' if (end=='top')==(asg>0) else '-'
            for a3 in (True,False):
                if typ=='+' and not a3: continue
                p,q=v3b.wdata(typ,a3)
                if typ=='-' and a3: nr=('eq',4)
                elif typ=='-': nr=('ge',6)
                else: nr=('ge',4)
                out.append(dict(kind='V',name='V %s a%s typ%s %s'%(end,'+' if asg>0 else '-',typ,'|a|=3' if a3 else '|a|>=5'),
                                end=end,p=p,q=q,sigstar=Fr(-1),d0n=nr,typ=typ,a3=a3,asg=asg))
    for mu in h3b.MUS:
        o,sgs,ds=h3b.WJ[mu]
        for end in ('top','bot'):
            p,q,_,_=o[end]
            out.append(dict(kind='H',name='H mu=%+d %s'%(mu,end),end=end,p=p,q=q,sigstar=Fr(sgs),d0n=('eq',-ds),mu=mu))
    return out
def tie_classes():
    """two-ended second-order tie possible iff mB = 0 and the delta-law admits n"""
    out=[dict(kind='V',name='V tie',sigstar=Fr(-1),n=('ge',4))]
    for mu in h3b.MUS:
        o,sgs,ds=h3b.WJ[mu]; out.append(dict(kind='H',name='H mu=%+d tie'%mu,sigstar=Fr(sgs),n=('eq',-ds),mu=mu))
    return out

# ---------------- case rows (affine forms over (1, ra, la, rb, lb, mB)) ----------------
def aff(c=0,ra=0,la=0,rb=0,lb=0,mB=0): return tuple(Fr(x) for x in (c,ra,la,rb,lb,mB))
def ad(*xs): return tuple(sum(v) for v in zip(*xs))
def sc(s,x): return tuple(Fr(s)*v for v in x)
def case_rows(p,q,m=None,allow_r1=True):
    (p1,p2),(q1,q2)=p,q
    K1=aff(p1,ra=1); K2=aff(q1,rb=1); M1=aff(p2,la=1); M2=aff(q2,lb=1)
    P0=aff(p1-q1,ra=1,rb=-1,mB=1); one=aff(1); h=Fr(1,2)
    out=[]
    if m is None:
        out.append(('d>=3',[((1,0,0,0),ad(one,sc(-1,K1))),((0,0,1,0),ad(aff(h),sc(-1,M1)))]))
        for e in (1,-1):
            out.append(('d=2 e=%d'%e,[((1,0,0,0),ad(one,sc(-1,K1))),((0,0,1,0),ad(aff(h-e),sc(-1,M1)))]))
            X1=Fr(1-e)
            out.append(('d=1 e=%d'%e,[((1,0,0,0),ad(aff(X1),sc(-1,K1))),((e,e,1,0),ad(aff(1-X1*X1/2),sc(-1,M1),sc(-e,K2)))]))
            X2=Fr(1-e)
            out.append(('d=-1 e=%d'%e,[((1,1,0,0),ad(aff(X2),sc(-1,K2))),((e,0,1,1),ad(aff(1-X2*X2/2),sc(-1,M2),sc(-e,K1)))]))
            out.append(('d=-2 e=%d'%e,[((1,1,0,0),ad(one,sc(-1,K2))),((0,0,1,1),ad(aff(h-e),sc(-1,M2)))]))
        out.append(('d<=-3',[((1,1,0,0),ad(one,sc(-1,K2))),((0,0,1,1),ad(aff(h),sc(-1,M2)))]))
    else:
        m=Fr(m)
        out.append(('d=0 r=0',[((2,1,0,0),ad(aff(2),sc(-1,K1),sc(-1,K2))),((0,0,2,1),ad(aff(1-m*m/4),sc(-1,M1),sc(-1,M2)))]))
        if m!=0 and allow_r1:
            out.append(('d=0 r=1',[((m,0,0,1),ad(aff(m-m*m/2),M1,sc(-1,M2),sc(-m,K1)))]))
    return [(nm,[(tuple(Fr(c) for c in co),r) for co,r in rows]+[((Fr(0),Fr(1),Fr(0),Fr(0)),P0)]) for nm,rows in out]
def evalaff(a,ra,la,rb,lb,mB): return a[0]+a[1]*ra+a[2]*la+a[3]*rb+a[4]*lb+a[5]*mB

# ---------------- class data ----------------
class Cls:
    """a jet class: key = (top (ra,la,rb,lb), bot (...), sigma, delta)"""
    def __init__(s,key,w=1,label=''):
        s.key=key; s.top=key[0]; s.bot=key[1]; s.sig=Fr(key[2]); s.dl=Fr(key[3]); s.w=w; s.label=label
    def end(s,e): return s.top if e=='top' else s.bot

# ---------------- LP assembly ----------------
class LP:
    """primal: x = (k_1..k_S, n, f_1..f_E, g_s (s in FINS)) >= lower bounds; A_eq x = b_eq; A_ub x <= b_ub.  Exact Fractions kept."""
    def __init__(s,S):
        s.S=S; s.nk=len(S); s.iN=s.nk; s.iF=s.nk+1; s.iG=s.iF+NE; s.nv=s.iG+len(FINS)
        s.eq=[]; s.ub=[]; s.lb=[Fr(0)]*s.nv
    def row(s): return {}
    def add_eq(s,r,b): s.eq.append((r,Fr(b)))
    def add_ub(s,r,b): s.ub.append((r,Fr(b)))
    def zrow(s,coef4):
        """linear form coef4 . z(f,g) as a sparse row"""
        r={}
        ca,cq,cl,cL=coef4
        for i,(a,b,l1,l2) in enumerate(EI):
            v=ca*l1+cl*l2
            if v: r[s.iF+i]=r.get(s.iF+i,0)+v
        for j,st in enumerate(FINS):
            v=cq*FIN[st][0]+cL*FIN[st][1]
            if v: r[s.iG+j]=r.get(s.iG+j,0)+v
        return r
    def flow(s):
        for st in range(NS):
            r={}
            for i,(a,b,l1,l2) in enumerate(EI):
                if a==st: r[s.iF+i]=r.get(s.iF+i,0)-1
                if b==st: r[s.iF+i]=r.get(s.iF+i,0)+1
            if st==INIT: r[s.iN]=Fr(1)          # in - out + n = 0
            else: r[s.iG+FINS.index(st)]=Fr(-1)  # in - out - g = 0
            s.add_eq(r,0)
def build(S,cl,rows,nmin,kmin=1,slice_m=None,nrule=None,fixk=None,extra=None):
    """case LP.  rows: [(coef4, aff)] with E.z = aff(B-data(k)).  slice_m: add sigma.k - sigstar = m.  nrule: ('eq'/'ge', off): n vs delta.k + off.
    fixk: dict j->value (fix multiplicities).  kmin: sum k >= kmin (0 = none)."""
    L=LP(S); L.flow(); end=cl['end'] if 'end' in cl else 'top'
    for coef,a in rows:
        r=L.zrow(coef)
        for j,c in enumerate(S):
            ra,la,rb,lb=c.end(end)
            v=evalaff(a,ra,la,rb,lb,c.sig)-a[0]       # linear part (mB coefficient uses sigma_j)
            if v: r[j]=r.get(j,0)-v
        b=a[0]-a[5]*cl['sigstar']                      # constant part (mB = sigma.k - sigstar)
        L.add_eq(r,b)
    L.lb[L.iN]=Fr(nmin)
    if kmin and fixk is None and L.nk: L.add_ub({j:Fr(-1) for j in range(L.nk)},-kmin)
    if slice_m is not None:
        L.add_eq({j:c.sig for j,c in enumerate(S) if c.sig},Fr(slice_m)+cl['sigstar'])
    if nrule is not None:
        kind,off=nrule
        r={L.iN:Fr(1)}
        for j,c in enumerate(S):
            if c.dl: r[j]=-c.dl
        if kind=='eq': L.add_eq(r,off)
        else: L.add_ub({i:-v for i,v in r.items()},-Fr(off))
    if fixk is not None:
        for j in range(L.nk): L.add_eq({j:Fr(1)},Fr(fixk.get(j,0)))
    if extra:
        for kind,r,b in extra:
            (L.add_eq if kind=='eq' else L.add_ub)(r,b)
    return L
def _mat(rows,nv):
    import numpy as np
    A=np.zeros((len(rows),nv)); b=np.zeros(len(rows))
    for i,(r,bb) in enumerate(rows):
        for j,v in r.items(): A[i,j]=float(v)
        b[i]=float(bb)
    return A,b
def solve_primal(L,obj=None,integral=False):
    Aeq,beq=_mat(L.eq,L.nv); 
    lb=np.array([float(x) for x in L.lb])
    c=np.zeros(L.nv)
    if obj is None:
        c[:L.nk]=1.0
    else:
        for j,v in obj.items(): c[j]=v
    if L.ub: Aub,bub=_mat(L.ub,L.nv)
    if integral:
        cons=[LinearConstraint(Aeq,beq,beq)]
        if L.ub: cons.append(LinearConstraint(Aub,-np.inf,bub))
        integ=np.zeros(L.nv); integ[:L.nk+1]=1
        res=milp(c,constraints=cons,integrality=integ,bounds=Bounds(lb,np.inf),options=dict(time_limit=60))
        return res
    res=linprog(c,A_eq=Aeq,b_eq=beq,A_ub=Aub if L.ub else None,b_ub=bub if L.ub else None,
                bounds=list(zip(lb,[None]*L.nv)),method='highs')
    return res
def farkas(L):
    """dual LP: x' = x - lb >= 0;  find u (eq, |u|<=1), w (ub, 0<=w<=1) with A_eq^T u + A_ub^T w >= 0 and b'.u + c'.w < 0.
    Returns exact (u, w) verified, or None."""
    lbv=L.lb
    beq=[b-sum(v*lbv[j] for j,v in r.items()) for r,b in L.eq]
    bub=[b-sum(v*lbv[j] for j,v in r.items()) for r,b in L.ub]
    m1=len(L.eq); m2=len(L.ub); nv=L.nv
    # variables y = (u, w); constraints: -(A_eq^T u + A_ub^T w) <= 0
    A=np.zeros((nv,m1+m2))
    for i,(r,b) in enumerate(L.eq):
        for j,v in r.items(): A[j,i]+=float(v)
    for i,(r,b) in enumerate(L.ub):
        for j,v in r.items(): A[j,m1+i]+=float(v)
    c=np.array([float(x) for x in beq+bub])
    bounds=[(-1,1)]*m1+[(0,1)]*m2
    res=linprog(c,A_ub=-A,b_ub=np.zeros(nv),bounds=bounds,method='highs')
    if res.status!=0 or res.fun>-1e-9: return None
    for den in (1,2,6,12,60,840,10**4,10**6):
        y=[Fr(x).limit_denominator(den) for x in res.x]
        u=y[:m1]; w=y[m1:]
        if any(x<0 for x in w): continue
        ok=True
        for j in range(nv):
            s=Fr(0)
            # column j of A_eq^T u + A_ub^T w
            pass
        colsum=[Fr(0)]*nv
        for i,(r,b) in enumerate(L.eq):
            if u[i]:
                for j,v in r.items(): colsum[j]+=u[i]*v
        for i,(r,b) in enumerate(L.ub):
            if w[i]:
                for j,v in r.items(): colsum[j]+=w[i]*v
        if any(x<0 for x in colsum): continue
        val=sum(ui*bi for ui,bi in zip(u,beq))+sum(wi*bi for wi,bi in zip(w,bub))
        if val<0: return (u,w,val)
    return 'unverified'
