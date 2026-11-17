"""ENGINE C1 frontier search: two-ended tie depth of necklace / vertical closures built on depth-3 (and body-43) boxes.
Jet calculus (engineA): a closure F = w1 A + w t^-3N B ties to order r at an end iff the product slope Q = t^-3N prod q_i agrees
with q* = -w1/w at that end in (deg, lc, l1..l_{r-1}).  Jets are additive (lc multiplicative), so second/third-order two-ended
ties of PAIRS are found by exact hashing (no sampling).  Every tie of order >= 3 at both ends is then evaluated exactly (Lemma W:
N fixed by degrees, mu/a fixed), and J is tested for units and gates."""
import sys, pickle, collections, time, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, jets
from fractions import Fraction as Fr
K=3
def jt(v):
    tp=ser.slope(v,'top',K); bt=ser.slope(v,'bot',K)
    return (tp[0],tp[1],jets.logs(tp[2])),(bt[0],bt[1],jets.logs(bt[2]))
def key2(tp,bt): return (tp[0]-bt[0], tp[0]%3, tp[1], tp[2][0], bt[1], bt[2][0])
def key3(tp,bt): return key2(tp,bt)+(tp[2][1],bt[2][1])
def targets():
    T=[]
    for mu in [m for m in range(-12,13) if m]:
        a1,a3=eng.W(mu)
        tt=ser.divD(ser.pdata(a1,'top',K),ser.pdata(a3,'top',K)); tb=ser.divD(ser.pdata(a1,'bot',K),ser.pdata(a3,'bot',K))
        T.append((('h',mu),(tt[0],-tt[1],jets.logs(tt[2])),(tb[0],-tb[1],jets.logs(tb[2]))))
    for a in [x for x in range(-13,14,2) if abs(x)>=3]:
        a1,aV=eng.WV(a)
        tt=ser.divD(ser.pdata(a1,'top',K),ser.pdata(aV,'top',K)); tb=ser.divD(ser.pdata(a1,'bot',K),ser.pdata(aV,'bot',K))
        T.append((('v',a),(tt[0],-tt[1],jets.logs(tt[2])),(tb[0],-tb[1],jets.logs(tb[2]))))
    return T
def need(T,tp,bt,order):
    (_,Tt,Tb)=T
    k=((Tt[0]-Tb[0])-(tp[0]-bt[0]), (Tt[0]-tp[0])%3, Fr(Tt[1])/tp[1], Tt[2][0]-tp[2][0], Fr(Tb[1])/bt[1], Tb[2][0]-bt[2][0])
    if order>=3: k=k+(Tt[2][1]-tp[2][1], Tb[2][1]-bt[2][1])
    return k
def exact_closure(T,v1,v2):
    """exact closure of the pair at target T; returns (J, rt, rb, N)"""
    p=vc.star(v1,v2); A,B=p
    kind,par=T[0]
    if kind=='h': a1,w=eng.W(par)
    else: a1,w=eng.WV(par)
    tq=ser.slope(p,'top',1)
    N=(tq[0]-T[1][0])//3
    S1=vc.mul(a1,A); S2=vc.mul(w,vc.shift(B,-3*N)); F=vc.add(S1,S2)
    rt=max(max(S1),max(S2))-max(F); rb=min(F)-min(min(S1),min(S2))
    J=vc.divexact(F,vc.PHI3)
    return J,rt,rb,N
