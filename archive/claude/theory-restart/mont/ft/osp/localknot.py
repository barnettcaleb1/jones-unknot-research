# Local knot in the quotient arc: (K,h) = (L # rL, swap). Schur => J(K,h) = J_3(L) (normalised). Check with lp.J on half-words,
# and compare moments with a_2(K), v_3(K) computed from V_K (ident3 conventions).
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/osp')
import lp, j3knots
from fractions import Fraction as F
import importlib.util
spec=importlib.util.spec_from_file_location('ident3','/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3.py')
src=open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3.py').read(); src=src[:src.index('rnd=random.Random')]
g={}; exec(src,g); VK=g['VK']; der=g['der']
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
def inv(P): return {-e:c for e,c in P.items()}
cases={'s.l1.x2.x2.x2.u1':(2,[1,1,1]), 's.l1.y2.y2.y2.u1':(2,[-1,-1,-1]), 's.l1.x2.x2.x2.x2.x2.u1':(2,[1,1,1,1,1])}
for w,(n,bw) in cases.items():
    Jw=lp.J(w); J3=j3knots.J3(n,bw)
    V=VK(w); a2K=F(-der(V,2),6); v3K=F(-(der(V,3)+3*der(V,2)),36)
    print(w,' J=',sorted(Jw.items()))
    print('   J_3(L)=',sorted(J3.items()),'  J==J_3?',Jw==J3,'  J==J_3(1/t)?',Jw==inv(J3))
    print('   a2(K)=',a2K,' v3(K)=',v3K,' M2=',M(Jw,2),' M3=',M(Jw,3),' M3/36=',F(M(Jw,3),36),' iota=(M3/36-7v3)/5=',(F(M(Jw,3),36)-7*v3K)/5)
