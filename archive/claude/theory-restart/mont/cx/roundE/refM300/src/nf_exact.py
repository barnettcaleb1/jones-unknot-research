"""validate OWN automaton (K=3 and K=4) against EXACT Laurent computation on all normal forms u(m_0..m_{k-1}) with
sum|m_i| <= SMAX: top log-jets of a (order K), q (deg, lc, log-jet order K); bottom data of u == top data of the mirror
u'' = u(-m0-1, -m1, ..) (log-jets of a and q; deg q_bot = 3 - deg q_top(u''))."""
import sys, time, itertools, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rauto, rlaurent as RL
from fractions import Fraction as Fr
def exact_vec(ms):
    v1={0:1}; v2={}
    for m in ms:
        for _ in range(abs(m)):
            if m>0: v1,v2=v1,RL.pshift(RL.padd(v1,v2),-3)
            else: v1,v2=v1,RL.padd(RL.pneg(v1),RL.pshift(v2,3))
        v1,v2=RL.padd(v1,RL.pmul({0:1,4:-1},v2)),RL.pneg(RL.padd(v1,v2))
    a=v1; b=RL.padd(v1,RL.pmul({0:1,3:-1},v2))
    return a,b
def data(a,b,end,K):
    da,ca,xa=RL.enddata(a,end,K); db,cb,xb=RL.enddata(b,end,K)
    la=RL.logjet(xa); lb=RL.logjet(xb)
    return dict(la=la,lq=tuple(y-x for x,y in zip(la,lb)),dq=db-da,cq=Fr(cb,ca))
def forms(S):
    out=[]
    def rec(pre,rem):
        if pre: out.append(tuple(pre))
        for m in range(-rem,rem+1):
            if m==0: continue
            if not pre and m==-1: continue
            rec(pre+[m],rem-abs(m))
    rec([],S); return out
