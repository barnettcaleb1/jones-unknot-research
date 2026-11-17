"""Log-jets of slopes at both ends: L(q) = log(normalised series) = l1 u + l2 u^2 + l3 u^3 (u = 1/t at top, t at bottom)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import ser
from fractions import Fraction as Fr
def logs(s):
    # s = (s1,s2,s3,...) of 1 + s1 u + s2 u^2 + ...; return l1..lK of log
    K=len(s); S=[Fr(0)]+list(s)   # S[k]
    l=[Fr(0)]*(K+1)
    # derivative identity: k s_k = sum_{j=1..k} j l_j s_{k-j} (with s_0=1)
    for k in range(1,K+1):
        tot=k*S[k]
        for j in range(1,k): tot-=j*l[j]*S[k-j]
        l[k]=tot/k
    return tuple(l[1:])
def jet(v,K=3):
    tp=ser.slope(v,'top',K); bt=ser.slope(v,'bot',K)
    return dict(dt=tp[0],db=bt[0],lt=tp[1],lb=bt[1],Lt=logs(tp[2]),Lb=logs(bt[2]))
def tjet(w1,w,K=3):
    out=[]
    for end in ('top','bot'):
        T=ser.divD(ser.pdata(w1,end,K),ser.pdata(w,end,K)); out.append((T[0],-T[1],logs(T[2])))
    return dict(dt=out[0][0],db=out[1][0],lt=out[0][1],lb=out[1][1],Lt=out[0][2],Lb=out[1][2])
