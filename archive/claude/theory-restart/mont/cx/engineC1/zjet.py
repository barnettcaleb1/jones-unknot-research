"""z-coordinate (X-eigen coordinate) end jets: z = (q-1)/(q-e2) = -(1+t^2) beta/alpha, alpha=(ta+(1+t^2)b)/Phi3, beta=(a-b)/Phi3.
X^mu: z -> (-t)^mu z ; nested box F_m(p): z = (-t)^-m z(p).  Closure at mu: J = alpha (1 - (-t)^mu z)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, ser, jets
from vc import add, sub, mul, shift, divexact, PHI3, T2P1
def ab(v):
    A,B=v
    al=divexact(add(shift(A,1),mul(T2P1,B)),PHI3); be=divexact(sub(A,B),PHI3)
    return al,be
def zser(v,end,K=3):
    al,be=ab(v)
    num=mul(T2P1,be); num={e:-c for e,c in num.items()}
    if not num: return None
    D=ser.ratio(ser.pdata(num,end,K),ser.pdata(al,end,K))
    # order in u: top: ord = -deg ; bottom: ord = deg
    o=-D[0] if end=='top' else D[0]
    return (o,D[1],jets.logs(D[2]))
