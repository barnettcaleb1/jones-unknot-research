"""refM300: INDEPENDENT exact re-verification of lpgen's 955 THEOREM-M300 certificates (certs_M300.pkl).
Semantic check (no use of lpgen's automaton, class table or flow potentials):
  * case rows: lpgen's rows (multiplier basis) must each lie in the span of the OWN sympy-derived conditions at the exact
    closure data (p, q, m);
  * closure data p, q, sigma*, delta-law offsets: OWN computation from w1, w3, wV (wdata.pkl);
  * class data: OWN recomputation from the exact box vectors (classdata.pkl);
  * rational part: g0 = exact MIN over all non-integral rational boxes of G = sum_i u_i coef_i . z(box), computed on the
    OWN K=3 jet automaton (rauto.py; Bellman-Ford, None = unbounded);
  * Farkas inequality: Phi = sum_boxes G + sum_j col_j k_j + cn n + const <= 0 for every feasible configuration, while
    col_j >= 0, g0 + cn >= 0 and (g0 + cn) nmin + const > 0 force Phi > 0.  Contradiction => the case is impossible."""
import sys, pickle, time, collections
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rauto
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import lpg            # used ONLY for the definitions closure_classes/tie_classes/case_rows (the multiplier basis)
DP=pickle.load(open(HERE+'derived_poly.pkl','rb'))
VARS=['al','P','La','Lam','RA','LA','RB','LB','mB','None']
def peval(terms,pt):
    s=Fr(0)
    for mon,c in terms:
        t=c
        for x,e in zip(pt,mon): t*=x**e
        s+=t
    return s
def my_rows(nm,p,q,m):
    """own derived equations (list of 10-vectors) for case nm at closure data p=(p1,p2), q=(q1,q2), slice m"""
    pt=(Fr(p[0]),Fr(p[1]),Fr(q[0]),Fr(q[1]),Fr(m) if m is not None else Fr(0))
    out=[]
    for variant in DP[nm]:
        out.append([[peval(eq[v],pt) for v in VARS] for eq in variant])
    return out
def rank(rows):
    M=[list(r) for r in rows]; rk=0; nc=len(M[0]) if M else 0
    for c in range(nc):
        piv=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
def their_vec(row,msub):
    coef,a=row; r=[Fr(0)]*10
    for i in range(4): r[i]+=coef[i]
    r[4]-=a[1]; r[5]-=a[2]; r[6]-=a[3]; r[7]-=a[4]
    if msub is None: r[8]-=a[5]; r[9]-=a[0]
    else: r[9]-=a[0]+a[5]*msub
    return r
# ---- own data
W=pickle.load(open(HERE+'wdata.pkl','rb'))
CD=pickle.load(open(HERE+'classdata.pkl','rb'))
order3,trans3=rauto.build(3); E3=rauto.edges(order3,trans3)
FIN3={k:rauto.qdata(k,3) for k in order3 if k!='init'}
_gcache={}
def gmin(ca,cq,cl,cL):
    key=(ca,cq,cl,cL)
    if key not in _gcache:
        _gcache[key]=rauto.extremum(order3,E3,FIN3,lambda l:ca*l[0]+cl*l[1],lambda f:cq*f[2][0]+cL*f[2][1],'min')
    return _gcache[key]
def own_wdata_check(cl):
    """compare lpgen's closure-class p, q, sigstar, d0n with own computation"""
    if cl['kind']=='V':
        a_rep=(3 if cl['asg']>0 else -3) if cl.get('a3',True) else (5 if cl['asg']>0 else -5)
        if cl['typ']=='+' and cl['asg']>0 and cl['end']=='top': pass
        o,sg,ds=W['V'][a_rep]
        reps=[a for a in W['V'] if (a>0)==(cl['asg']>0) and ((abs(a)==3)==cl['a3'] if cl['typ']=='-' else True)]
        ok=all(tuple(W['V'][a][0][cl['end']][0][:2])==tuple(cl['p']) and tuple(W['V'][a][0][cl['end']][1][:2])==tuple(cl['q']) for a in reps)
        return ok and cl['sigstar']==-1
    mu=cl['mu']; reps=[x for x in W['H'] if (x==mu if abs(mu)<4 else (x>=4 if mu>0 else x<=-4))]
    ok=all(tuple(W['H'][x][0][cl['end']][0][:2])==tuple(cl['p']) and tuple(W['H'][x][0][cl['end']][1][:2])==tuple(cl['q']) and W['H'][x][1]==cl['sigstar'] and cl['d0n']==('eq',-W['H'][x][2]) for x in reps)
    return ok
def check_cert(S,cl,nm,rows,m,nrule,kmin,nmin,u,w,NS=19):
    """S: list of (key) class keys; returns (ok, info)"""
    info={}
    ncase=len(rows); ns=1 if m is not None else 0; neq=1 if (nrule is not None and nrule[0]=='eq') else 0
    nge=1 if (nrule is not None and nrule[0]=='ge') else 0; nk=1 if kmin else 0
    if len(u)!=NS+ncase+ns+neq or len(w)!=nk+nge: return False,{'err':'length','lu':len(u),'lw':len(w)}
    if any(x<0 for x in w): return False,{'err':'negative w'}
    uc=u[NS:NS+ncase]; us=u[NS+ncase] if ns else Fr(0); un=u[NS+ncase+ns] if neq else Fr(0)
    wk=w[0] if nk else Fr(0); wn=w[nk] if nge else Fr(0)
    off=Fr(nrule[1]) if nrule is not None else Fr(0)
    # (a) rows are consequences of the own derived conditions
    if ncase:
        msub=m if nm.startswith('d=0') else None
        mine=my_rows(nm,cl['p'],cl['q'],m)
        th=[their_vec(r,msub) for r in rows]
        for variant in mine:
            if not (rank(variant+th)==rank(variant)): return False,{'err':'row not implied by own derivation'}
    sigstar=cl['sigstar']
    # (b) G on rational boxes, exact min on own automaton
    ca=sum(ui*r[0][0] for ui,r in zip(uc,rows)); cq=sum(ui*r[0][1] for ui,r in zip(uc,rows))
    clq=sum(ui*r[0][2] for ui,r in zip(uc,rows)); cL=sum(ui*r[0][3] for ui,r in zip(uc,rows))
    g0=gmin(ca,cq,clq,cL) if ncase else Fr(0)
    if g0 is None: return False,{'err':'G unbounded below on rational boxes'}
    # (c) class columns with OWN class data at the weak end
    end=cl.get('end','top'); minc=None
    for key in S:
        top,bot,sig,dl=key; ra,la,rb,lb=(top if end=='top' else bot)
        v=sum(ui*(r[1][1]*ra+r[1][2]*la+r[1][3]*rb+r[1][4]*lb+r[1][5]*sig) for ui,r in zip(uc,rows))
        col=-v+us*sig-un*dl-wk+wn*dl
        minc=col if minc is None else min(minc,col)
    cn=un-wn
    const=-sum(ui*(r[1][0]-r[1][5]*sigstar) for ui,r in zip(uc,rows))-us*((m if m is not None else 0)+sigstar)-un*off+wk*kmin+wn*off
    info=dict(g0=g0,mincol=minc,cn=cn,const=const)
    ok=(minc>=0) and (g0+cn>=0) and ((g0+cn)*nmin+const>0)
    return ok,info
if __name__=='__main__':
    t0=time.time()
    C=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen/certs_M300.pkl','rb'))
    S=[CD['top%d'%i]['key'] for i in range(300)]
    # sanity: lpgen's class order == own order
    import classes
    assert [c.key for c in classes.top(300)]==S, 'class order differs'
    CL={cl['name']:cl for cl in lpg.closure_classes()}; TC={tc['name']:tc for tc in lpg.tie_classes()}
    wbad=[n for n,cl in CL.items() if not own_wdata_check(cl)]
    print('closure classes with closure data != own:',wbad)
    res=collections.Counter(); fails=[]; maxden=0; kinds=collections.Counter()
    for (cn_,nm,m),cert in C.items():
        u,w=cert['u'],cert['w']; maxden=max([maxden]+[x.denominator for x in list(u)+list(w)])
        if nm=='tie':
            tc=TC[cn_]; cl=dict(tc,end='top'); rows=[]; nrule=tc['n']; kinds['tie']+=1
        else:
            cl=CL[cn_]
            if m is None: rows=dict(lpg.case_rows(cl['p'],cl['q']))[nm]; nrule=None; kinds['offset']+=1
            else: rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m))[nm]; nrule=cl['d0n']; kinds['slice']+=1
        ok,info=check_cert(S,cl,nm,rows,m,nrule,2,0,u,w)
        res[ok]+=1
        if not ok: fails.append(((cn_,nm,m),info))
    print('certificates:',len(C),dict(kinds),' VALID (own data, own automaton, own rows):',res[True],' FAILED:',res[False],' max denominator',maxden,' time %.1fs'%(time.time()-t0))
    for f in fails[:20]: print('  FAIL',f)
    # completeness: the stored certificate set covers every job of the uniform run (24 x 11 offset, slices, ties)
    import run_uni, runner
    J=run_uni.jobs(classes.top(300),0,2,None,8)
    keys=set((cl['name'],nm,m) for cl,nm,rows,m,nr in J)
    print('jobs in the M300 run:',len(J),' certificates present for all jobs:',keys==set(C.keys()))
