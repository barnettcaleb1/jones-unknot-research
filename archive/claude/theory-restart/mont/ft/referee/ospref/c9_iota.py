import sys
from fractions import Fraction as F
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp
src=open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3.py').read(); src=src[:src.index('rnd=random.Random')]
g={}; exec(src,g); VK=g['VK']; der=g['der']
from rlib import *
from c9_local import longknot_letters, KN
from c11_wh import wh_double
def Mk(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
cases=dict((n,braid_ops(*KN[n])) for n in KN); cases['Wh(3_1)+']=wh_double('x'); cases['Wh(3_1)-']=wh_double('y')
for name,ops in cases.items():
    hw='s.'+'.'.join(longknot_letters(ops)); J=lp.J(hw); V=VK(hw)
    v3K=F(-(der(V,3)+3*der(V,2)),36); iota=(F(Mk(J,3),36)-7*v3K)/5
    print('%-10s v3(K)=%s  2*v3(L)=%s  M3=%d  iota=%s  iota==v3(K): %s'%(name,v3K,2*v3_of(jones(ops)),Mk(J,3),iota,iota==v3K))
# side remark: J_3 at t=+1
for name in ('3_1','4_1','5_2'):
    J=J3(braid_ops(*KN[name])); V=jones(braid_ops(*KN[name]))
    ex=[sum(F(c*e**k) for e,c in J.items())/__import__('math').factorial(k) for k in range(4)]
    print(name,'J_3(e^h) coeffs',[str(x) for x in ex],' -8a2 =',-8*a2_of(V),' -16v3 =',-16*v3_of(V))
