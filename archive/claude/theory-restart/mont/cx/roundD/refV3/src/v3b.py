"""THEOREM-GENERATOR V3(B): vertical closures V_a(Y^N B u_1...u_n), n >= n_min rational non-integral boxes, any N, odd |a| >= 3.
Weak-end casework of Theorem V3 with B's channel jets as parameters; every case is reduced to linear equations in the sums
(alpha, P, L_a, Lambda) = sum over rational boxes of (rho_a, rho_q, l2(a), lambda_q) and closed by a FARKAS CERTIFICATE:
multipliers y with  sup_box g(box) <= 0  (g = y . per-box vector; sup computed EXACTLY by longest paths on the K=3 jet automaton)
and RHS > n_min * sup g.  Requires sigma(B) != sigma*_V = -1 (then the weak end exists and its slope mismatch is m_B = sigma(B)+1).
Mirror: the bottom data of rational boxes range over the same set as the top data (R2), so both weak ends use the same automaton."""
import sys, itertools
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import jauto
from fractions import Fraction as Fr
K=3
order,trans=jauto.build(K,verbose=False)
EDG=[]
for (k,m),(Dj,nk) in trans.items():
    d,lc,s=jauto.norm_jet(Dj); l=jauto.logs(s); EDG.append((k,nk,l[0],l[1]))
FIN={k:jauto.qlog(k,K)[2] for k in order if k!='init'}
_cache={}
def supg(ca,cq,cl,cL):
    """sup over all rational boxes of ca*rho_a + cq*rho_q + cl*l2(a) + cL*lambda_q (None if +infinity)"""
    key=(ca,cq,cl,cL)
    if key in _cache: return _cache[key]
    best={k:None for k in order}; best['init']=Fr(0)
    for it in range(len(order)+2):
        ch=False
        for (k,nk,l1,l2) in EDG:
            if best[k] is None: continue
            v=best[k]+ca*l1+cl*l2
            if best[nk] is None or v>best[nk]: best[nk]=v; ch=True
        if not ch: break
    else:
        _cache[key]=None; return None
    r=max(best[k]+cq*FIN[k][0]+cL*FIN[k][1] for k in order if k!='init' and best[k] is not None)
    _cache[key]=r; return r
Y=[Fr(x) for x in (0,1,-1,2,-2,3,-3,Fr(1,2),Fr(-1,2),10,-10,100,-100)]
def certify(eqs,P0,nmin):
    """eqs: list of (a,b,c,d,r): a*alpha + b*P + c*L_a + d*Lambda = r.  Also P = P0.  Return certificate or None."""
    E=list(eqs)+[(0,1,0,0,P0)]
    for ys in itertools.product(Y,repeat=len(E)):
        if all(y==0 for y in ys): continue
        ca=sum(y*e[0] for y,e in zip(ys,E)); cq=sum(y*e[1] for y,e in zip(ys,E))
        cl=sum(y*e[2] for y,e in zip(ys,E)); cL=sum(y*e[3] for y,e in zip(ys,E)); rhs=sum(y*e[4] for y,e in zip(ys,E))
        s=supg(ca,cq,cl,cL)
        if s is None: continue
        if s<=0 and rhs>nmin*s: return (ys,s,rhs)
    return None
def wdata(typ,a3):
    # (p1,p2),(q1,q2): log-jets of w_1 and wV at the weak end; typ '+' (top,a>=3 / bottom,a<=-3) or '-'
    if typ=='+': return (Fr(0),Fr(1)),(Fr(1),Fr(1,2))
    return (Fr(0),Fr(-1) if a3 else Fr(0)),(Fr(0),Fr(0))
def cases(Bd,mB,typ,a3):
    """Bd = (rho_a^B, lam_a^B, rho_b^B, lam_b^B) at the weak end.  Returns list of (name, eqs, P0)."""
    (p1,p2),(q1,q2)=wdata(typ,a3)
    ra,la,rb,lb=Bd
    K1=p1+ra; K2=q1+rb; M1=p2+la; M2=q2+lb
    P0=mB+(p1-q1)-rb+ra
    out=[]
    # X1 = K1 + alpha ; X2 = K2 + alpha + P ; l2(s1) = M1 + L_a ; l2(s2) = M2 + L_a + Lambda
    out.append(('d>=3',[(1,0,0,0,1-K1),(0,0,1,0,1-M1-Fr(1,2))],P0))
    for e in (1,-1):
        out.append(('d=2 e=%d'%e,[(1,0,0,0,1-K1),(0,0,1,0,1-M1-Fr(1,2)-e)],P0))
        X1=1-e
        # x2(s1) + e*X2 = 1 : M1 + L_a + X1^2/2 + e*(K2 + alpha + P) = 1
        out.append(("d=1 e=%d"%e,[(1,0,0,0,X1-K1),(e,e,1,0,1-M1-Fr(X1*X1,2)-e*K2)],P0))
        X2=1-e
        # x2(s2) + e*X1 = 1 : M2 + L_a + Lambda + X2^2/2 + e*(K1+alpha) = 1
        out.append(("d=-1 e=%d"%e,[(1,1,0,0,X2-K2),(e,0,1,1,1-M2-Fr(X2*X2,2)-e*K1)],P0))
        out.append(('d=-2 e=%d'%e,[(1,1,0,0,1-K2),(0,0,1,1,1-M2-Fr(1,2)-e)],P0))
    out.append(('d<=-3',[(1,1,0,0,1-K2),(0,0,1,1,1-M2-Fr(1,2))],P0))
    # delta = 0, eps = +1 (no cancellation): X1 + X2 = 2 ; x2(s1) + x2(s2) = 2
    kap=K1-K2-P0          # = X1 - X2 (constant)
    X1=(2+kap)/2; X2=(2-kap)/2
    out.append(('d=0 r=0',[(2,1,0,0,2-K1-K2),(0,0,2,1,2-M1-M2-X1*X1/2-X2*X2/2)],P0))
    # delta = 0, eps = -1, r = 1: kap != 0 ; M1 - M2 - Lambda + kap*(K1+alpha) - kap^2/2 = kap
    if kap!=0:
        out.append(('d=0 r=1',[(-kap,0,0,1,M1-M2+kap*K1-kap*kap/2-kap)],P0))
    return out
def prove(Bdata,sigB,nmin,verbose=False):
    """Bdata: {'top':(ra,la,rb,lb),'bot':(...)}.  Returns (ok, list of open cases)."""
    mB=sigB+1
    if mB==0: return False,['sigma(B) = sigma*']
    opn=[]
    for end in ('top','bot'):
        for asg in (1,-1):
            typ='+' if (end=='top')==(asg>0) else '-'
            for a3 in (True,False):
                if typ=='+' and not a3: continue
                for name,eqs,P0 in cases(Bdata[end],mB,typ,a3):
                    c=certify(eqs,P0,nmin)
                    if c is None: opn.append((end,asg,a3,name))
                    elif verbose: print(end,asg,a3,name,'cert',c)
    return (not opn),opn
if __name__=='__main__':
    # sanity: empty B (rational only), n_min = 2  ->  must reproduce Theorem V3
    Z=(Fr(0),Fr(0),Fr(0),Fr(0))
    ok,opn=prove({'top':Z,'bot':Z},Fr(0),2,verbose=True)
    print('rational-only (Theorem V3 re-derivation):',ok,opn)
