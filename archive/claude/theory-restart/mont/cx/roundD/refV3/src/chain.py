"""refV3: test the V3 proof chain on actual closures.
(1) w-jets: l1,l2 of w_1(a), wV(a) at top and bottom vs the REPORT's top data and vs v3b.wdata (generator), odd 3 <= |a| <= 41;
    sigma*_V = -1 and delta*_V = -|a|-1.
(2) random closures V_a(Y^N u_1..u_n), u_i in R(8), n = 1..5, odd 3 <= |a| <= 15, N forced into a Lemma-W coincidence
    (N_top or N_bot) or random: measure (delta, eps, r) at both ends of F = w_1 A + wV t^-3N B; whenever an end has r >= 2,
    check the other end: mismatch s1(Q)-s1(q*) = +1 exactly, P = sum rho_q = s1(q*)+1, and the case equalities needed for the
    Phi_3 pattern fail; also check that no end pair has both r >= 2 (V2) and record max r."""
import sys, random, time, pickle
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
from fractions import Fraction as Fr
import vc, lib, v3b
from boxlemmas import jet, logs
def w1(a): return vc.add({1:1}, vc.mul(vc.tmono(a),vc.T2P1))
def wV(a): return vc.add(vc.shift(vc.tmono(a),1), vc.shift(vc.PHI5,3*a-1))
def lj(p,end):
    d,c,xs=jet(p,end,3); return d,c,logs(xs)
bad=[]
# (1)
for a in [x for x in range(-41,42,2) if abs(x)>=3]:
    for end in ('t','b'):
        d1,c1,L1=lj(w1(a),end); dV,cV,LV=lj(wV(a),end)
        typ='+' if (end=='t')==(a>0) else '-'
        (p1,p2),(q1,q2)=v3b.wdata(typ,abs(a)==3)
        if (L1[0],L1[1])!=(p1,p2) or (LV[0],LV[1])!=(q1,q2): bad.append(('wdata',a,end,L1[:2],LV[:2],(p1,p2),(q1,q2)))
    # sigma*, delta*: q* = -w_1/wV
    dt1,_,Lt1=lj(w1(a),'t'); dtV,_,LtV=lj(wV(a),'t'); db1,_,Lb1=lj(w1(a),'b'); dbV,_,LbV=lj(wV(a),'b')
    sig=(Lt1[0]-LtV[0])+(Lb1[0]-LbV[0])
    dlt=(vc.span(w1(a)))-(vc.span(wV(a)))
    if sig!=-1: bad.append(('sigma*',a,sig))
    if dlt!=-abs(a)-1: bad.append(('delta*',a,dlt))
    # REPORT top data: a>=3: w_1 = -t^(a+2)(1+0u+u^2..), wV = t^(3a+3)(1+u+u^2+u^3+u^4..); a<=-3: w_1 = t(1+0u-[|a|=3]u^2..), wV = -t^(a+1)(1+O(u^4))
    d,c,xs=jet(w1(a),'t',4); dv,cv,xv=jet(wV(a),'t',4)
    if a>=3:
        ok=(d,c,xs[:2])==(a+2,-1,(0,1)) and (dv,cv,xv[:4])==(3*a+3,1,(1,1,1,1))
    else:
        ok=(d,c,xs[:2])==(1,1,(0,-1 if a==-3 else 0)) and (dv,cv,xv[:3])==(a+1,-1,(0,0,0))
    if not ok: bad.append(('REPORT topdata',a,(d,c,xs),(dv,cv,xv)))
print('(1) w-jet / sigma* / delta* checks for odd 3<=|a|<=41: failures',bad[:5],len(bad),flush=True)
# (2)
R8=lib.rational(8)
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 3)
NS=int(sys.argv[2]) if len(sys.argv)>2 else 20000
def series_ratio_order(Q_num,Q_den,qs_num,qs_den,end):
    """r = order of Q/q* - 1 at the end (Q = Qn/Qd, q* = qn/qd as Laurent polys): compute X = Qn*qd - qn*Qd and Y = Qd*qn;
    if deg X (at end) == deg Y then r = 0 with ratio != 1 ... return (degree mismatch flag, r)"""
    X=vc.sub(vc.mul(Q_num,qs_den),vc.mul(qs_num,Q_den)); Yp=vc.mul(Q_den,qs_num)
    if end=='t':
        return (max(Yp)-max(X)) if X else 10**6
    return (min(X)-min(Yp)) if X else 10**6
stats=dict(n=0,strong=0,v2viol=0,mis_ok=0,mis_bad=0,P_bad=0,units=0,maxr=0)
t0=time.time()
for it in range(NS):
    n=rnd.randint(1,5)
    us=[rnd.choice(R8) for _ in range(n)]
    a=rnd.choice([x for x in range(-15,16,2) if abs(x)>=3])
    A=vc.ONE; B=vc.ONE
    for u in us: A=vc.mul(A,u[1][0]); B=vc.mul(B,u[1][1])
    W1=w1(a); WV=wV(a)
    nt=max(WV)+max(B)-max(W1)-max(A); nb=min(WV)+min(B)-min(W1)-min(A)
    mode=rnd.random()
    if mode<0.45 and nt%3==0: N=nt//3
    elif mode<0.9 and nb%3==0: N=nb//3
    else: N=rnd.randint(-15,15)
    BN=vc.shift(B,-3*N)
    # Q = BN/A, q* = -W1/WV ; Q/q* - 1 = -(BN*WV + A*W1)/(A*W1)
    F=vc.add(vc.mul(W1,A),vc.mul(WV,BN))
    S1=vc.mul(W1,A)
    rt=(max(S1)-max(F)) if F else 10**6
    rb=(min(F)-min(S1)) if F else 10**6
    # degree coincidence at each end
    ct=(max(vc.mul(WV,BN))==max(S1)); cb=(min(vc.mul(WV,BN))==min(S1))
    rt_eff=rt if ct else 0; rb_eff=rb if cb else 0
    stats['n']+=1
    if len(vc.divexact(F,vc.PHI3) or {0:1,1:1})==1: stats['units']+=1
    stats['maxr']=max(stats['maxr'],min(rt_eff,rb_eff))
    if rt_eff>=2 and rb_eff>=2: stats['v2viol']+=1; print('V2 VIOLATION',[u[2] for u in us],a,N,flush=True)
    for strong,weak in (('t','b'),('b','t')):
        rs=rt_eff if strong=='t' else rb_eff
        if rs<2: continue
        stats['strong']+=1
        # mismatch at weak end: s1(Q) - s1(q*)
        def s1(p,end): return jet(p,end,1)[2][0]
        s1Q=s1(BN,weak)-s1(A,weak)
        s1qs=s1(W1,weak)-s1(WV,weak)
        if s1Q-s1qs==1: stats['mis_ok']+=1
        else: stats['mis_bad']+=1; print('MISMATCH != +1',[u[2] for u in us],a,N,weak,s1Q-s1qs,flush=True)
        # P = sum rho_q at the weak end equals s1(q*)+1 (Y^N does not change jets)
        P=sum(jet(u[1][1],weak,1)[2][0]-jet(u[1][0],weak,1)[2][0] for u in us)
        if P!=s1qs+1: stats['P_bad']+=1
    if it%5000==0: print(it,stats,round(time.time()-t0,1),flush=True)
print('(2) FINAL',stats,round(time.time()-t0,1))
