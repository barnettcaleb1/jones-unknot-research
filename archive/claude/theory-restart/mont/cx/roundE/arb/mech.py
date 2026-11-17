"""Mechanism check (exact): degree cancellation in a product turns an ADDITIVE log-jet into a LEADING coefficient.
P_k = Y^(2k/3) u^k (u an R_1-top rational box, deg_top q(u) = 2, lc -1, l1 = 1): deg_top q(P_k) = 0, lc = (-1)^k.
k even: q(P_k) = 1 + k u + ..., z = (q-1)/(q-e2) = k t^-1 + ...; the nested box F_{-1}(P_k) = X^{+1} P_k has top slope lc 1/(1+k)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, ser, jets
from fractions import Fraction as Fr
def topq(v,K=3):
    d=ser.slope(v,'top',K); return d[0],d[1],jets.logs(d[2])
def botq(v,K=3):
    d=ser.slope(v,'bot',K); return d[0],d[1],jets.logs(d[2])
# find an R_1-top rational box
for w in ['X','XY','XXY','XYY','YX','Xy','XXy','XyX','XYX']:
    v=vc.rat(w)
    try: print(w,'top q',topq(v),'bot q',botq(v),'deg a',max(v[0]),min(v[0]))
    except Exception as e: print(w,e)
print('--- family F_{-1}(Y^N u^k), u = XY, deg_top q(Y^N u^k) = -k - 3N')
u=vc.rat('XY')
for k in (3,6,9,12,18):
    N=-k//3
    P=vc.Ypow(N,vc.starall([u]*k))
    print('k=%d N=%d  top q(P) ='%(k,N),topq(P))
    for m in (-1,1,-2,2):
        B=vc.F(m,P)
        tq=topq(B); bq=botq(B)
        print('   F_%+d: top q (deg,lc,l1..3) ='%m,tq,' lc a top',vc.top(B[0]) and B[0][max(B[0])],' bot q',bq[:2])
