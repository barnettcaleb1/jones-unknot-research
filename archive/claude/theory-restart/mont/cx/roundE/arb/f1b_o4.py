"""ORDER-4 test of lpgen's two F1' survivors: B^3 u_1..u_n, B = box 50216 at H mu = +2 (weak TOP) and its mirror B = box 50139
at H mu = -2 (weak BOTTOM); offset +1, eps = -1, mB = -7.  The Phi_3 pattern f = s1 - u s2 = 1 + u + u^2 + 0u^3 + 0u^4 gives
  [u^1] X1 = 2;  [u^2] Y1 = X2 - 1;  [u^3] Z1 - Y2 = mB^2/2 - 4/3 (lpgen);  [u^4] s1_4 = s2_3   (NEW)
with X2 = X1 + mB (sigma-law, strong end r >= 2), s_k the normalised series coefficients, (X,Y,Z,W) = log-jet orders 1..4,
s1 = w1 * a_B^3 * prod a(u_i), s2 = w3 * b_B^3 * prod b(u_i).  Rational part EXACTLY via the K=4 jet automaton (refGen: PROVED for
all rational boxes; bottom data = top data of mirrors, same set): n unit flows from init (n >= 0 free), edge log-jets of D, terminal
log-jets of q.  Infeasibility is certified by an exact Farkas vector (lpg.farkas)."""
import sys, pickle
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import jauto, lpg, exact, eng, ser, jets
K=4
order,trans=jauto.build(K,verbose=True)
SI={k:i for i,k in enumerate(order)}; INIT=SI['init']
E={}
for (k,m),(Dj,nk) in trans.items():
    d,lc,s=jauto.norm_jet(Dj); l=jauto.logs(s)
    E[(SI[k],SI[nk],l)]=1
EI=list(E.keys())
FIN={}
for k in order:
    if k=='init': continue
    FIN[SI[k]]=jauto.qlog(k,K)[2]
print('K=4 automaton: states',len(order),'distinct edges',len(EI),flush=True)
items=exact.load_items()
class LPX:
    def __init__(s,nv): s.nv=nv; s.eq=[]; s.ub=[]; s.lb=[Fr(0)]*nv
    def add_eq(s,r,b): s.eq.append((r,Fr(b)))
    def add_ub(s,r,b): s.ub.append((r,Fr(b)))
def lj(f,end): return jets.logs(ser.pdata(f,end,K)[2])
def run(boxidx,mu,end,mB=Fr(-7),kB=3):
    v=items[boxidx][2]; la=lj(v[0],end); lb=lj(v[1],end)
    w1,w3=eng.W(mu); p=lj(w1,end); q=lj(w3,end)
    nE=len(EI); FS=sorted(FIN); iN=0; iF=1; iG=1+nE; nv=1+nE+len(FS)
    L=LPX(nv)
    for st in range(len(order)):            # flow conservation: in - out + [init] n - [final] g = 0
        r={}
        for i,(a,b,l) in enumerate(EI):
            if a==st: r[iF+i]=r.get(iF+i,0)-1
            if b==st: r[iF+i]=r.get(iF+i,0)+1
        if st==INIT: r[iN]=Fr(1)
        else: r[iG+FS.index(st)]=Fr(-1)
        L.add_eq(r,0)
    def RA(k): return {iF+i:l[k-1] for i,(a,b,l) in enumerate(EI) if l[k-1]}
    def RQ(k): return {iG+j:FIN[s][k-1] for j,s in enumerate(FS) if FIN[s][k-1]}
    def comb(*ps):
        out={}
        for c,r in ps:
            for i,x in r.items(): out[i]=out.get(i,0)+c*x
        return out
    X1c=p[0]+kB*la[0]; Y1c=p[1]+kB*la[1]; Z1c=p[2]+kB*la[2]; W1c=p[3]+kB*la[3]
    X2c=q[0]+kB*lb[0]; Y2c=q[1]+kB*lb[1]; Z2c=q[2]+kB*lb[2]
    X1=Fr(2); X2=X1+mB; Y1=X2-1
    L.add_eq(RA(1),X1-X1c)                                   # [u^1]
    L.add_eq(comb((1,RA(1)),(1,RQ(1))),X2-X2c)               # sigma-law: X2 = X1 + mB
    L.add_eq(RA(2),Y1-Y1c)                                   # [u^2]
    c3=mB*mB/2-Fr(4,3)                                       # [u^3]: Z1 - Y2 = c3
    L.add_eq(comb((1,RA(3)),(-1,RA(2)),(-1,RQ(2))),c3-Z1c+Y2c)
    # [u^4]: W1 + X1 Z1 + Y1^2/2 + X1^2 Y1/2 + X1^4/24 = Z2 + X2 Y2 + X2^3/6, with Z1 = Y2 + c3:
    #   W1 - Z2 + (X1 - X2) Y2 = X2^3/6 - X1 c3 - Y1^2/2 - X1^2 Y1/2 - X1^4/24
    rhs=X2**3/6-X1*c3-Y1*Y1/2-X1*X1*Y1/2-X1**4/24
    Y2form=comb((1,RA(2)),(1,RQ(2))); W1form=RA(4); Z2form=comb((1,RA(3)),(1,RQ(3)))
    row=comb((1,W1form),(-1,Z2form),(X1-X2,Y2form))
    L.add_eq(row,rhs-W1c+Z2c-(X1-X2)*Y2c)
    import numpy as np
    from scipy.optimize import linprog
    Aeq,beq=lpg._mat(L.eq,L.nv)
    res=linprog(np.zeros(L.nv),A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*L.nv,method='highs')
    # without the order-4 row (control: must be FEASIBLE, as in lpgen)
    L3=LPX(nv); L3.eq=L.eq[:-1]
    A3,b3=lpg._mat(L3.eq,L3.nv)
    res3=linprog(np.zeros(nv),A_eq=A3,b_eq=b3,bounds=[(0,None)]*nv,method='highs')
    out=dict(order3_feasible=(res3.status==0),n_at_order3=(res3.x[iN] if res3.status==0 else None),order4_status=res.status)
    if res.status==2:
        f=lpg.farkas(L); out['cert']=('EXACT' if isinstance(f,tuple) else f)
    elif res.status==0: out['point_n']=res.x[iN]
    return out
for bx,mu,end in ((50216,2,'top'),(50139,-2,'bot')):
    print('box',bx,'mu',mu,'weak',end,run(bx,mu,end),flush=True)
