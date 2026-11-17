"""Two-channel formula for the branch-knot family L_n = [s0^f][s1^n][c]:  s^n = A^n (1 - e/delta) + (-A^-3)^n e/delta, so
<L_n> = A^n P + (-A^-3)^n Q,  P = <D_inf> - Q,  Q = <D_e>/delta,  D_inf = [s0^f][c] (unknot), D_e = [s0^f][e_12][c] (the T(0) link).
Brackets as in kauffman.py (<D>/delta).  Gives the extreme coefficients of V(L_n) for ALL n >= n0 (supports separate)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk, identK, examples
from kauffman import padd, pshift
name=sys.argv[1]
a,N,boxes=examples.EX[name]; hw=identK.halfword(a,N,boxes); f=bk.frame(hw)
Binf=bk.bracket_full(bk.full_closure(hw,bk.tw(0,f)+bk.C_INF))           # <D_inf>/delta
Be=bk.bracket_full(bk.full_closure(hw,bk.tw(0,f)+[('u',1),('r',1)]+bk.C_INF))   # <D_e>/delta  (e on positions 1,2 = cup then cap)
# with brackets normalised by delta:  <L_n>/delta = A^n (Binf - Be/delta) + (-A^-3)^n Be/delta
# delta*Be/delta^2 ... keep everything divided by delta: P' = Binf - Be/delta needs Be divisible by delta:
def divdelta(p):
    p=dict(p); r={}
    while p:
        e=max(p); v=p[e]
        r[e-2]=-v; padd(p,{e:-v,e-4:-v})
    return r
Q=divdelta(Be)
P={}; padd(P,Binf); padd(P,Q,-1)
print(name,'Binf (unknot) =',sorted(Binf.items()))
print('P: degrees [%d,%d] top %d bottom %d'%(min(P),max(P),P[max(P)],P[min(P)]))
print('Q: degrees [%d,%d] top %d bottom %d'%(min(Q),max(Q),Q[max(Q)],Q[min(Q)]))
# check against direct brackets
for n in (1,2,5):
    direct=bk.bracket_full(bk.full_Ln(hw,n,f))
    pred={}; padd(pred,pshift(P,n)); padd(pred,pshift(Q,-3*n,(-1)**n))
    print('n=%d two-channel formula == direct bracket:'%n, pred==direct)
# extreme terms of A^n P + (-A^-3)^n Q for n>=1: top A-degree from P (n+maxP) vs Q (-3n+maxQ); bottom from Q (-3n+minQ) vs P (n+minP)
n0=max(0,(max(Q)-max(P))//4+1,(min(Q)-min(P))//4+1)
print('for n >= %d: top coeff = %d (from P), bottom coeff = %d*(-1)^n (from Q); Jones extreme coefficients have |.| = %d and %d'%(n0,P[max(P)],Q[min(Q)],abs(P[max(P)]),abs(Q[min(Q)])))
