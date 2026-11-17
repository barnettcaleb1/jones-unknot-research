import sys
sys.path.insert(0,'nest')
from nlib import *
import alex
def Vw(a,b):
    """vertical inversion word of P(a,b,a): s.l1.(axis)^|b|.(off)^|a|.u1 ; sign convention: b>0 -> x0, a>0 -> y2 (8_19 = (3,2))"""
    mid=['x0' if b>0 else 'y0']*abs(b)
    off=['y2' if a>0 else 'x2']*abs(a)
    return '.'.join(['s','l1']+mid+off+['u1'])
print('8_19 check: Vw(3,2) =',Vw(3,2))
J819=J(Vw(3,2)); print(' J =',fmt(J819))
from words import mont
print(' mont(1,[3,3]) J equal?', J(mont(1,[3,3]))==J819)
T0='s.r1.x2.y0.r2.y0.y1.y0.y1.x2.u3.u1'
JT0=J(T0)
print('J(T_0) =',fmt(JT0),' alex',alex.alex_poly(T0))
for a in (-5,-3,-1,1,3,5):
    for b in range(-4,5):
        w=Vw(a,b); Jw=J(w)
        if Jw is None: continue
        tag=''
        if Jw==JT0: tag='  <== equals J(T_0)'
        print('a=%2d b=%2d span %2d  alex %s%s'%(a,b,span(Jw),alex.alex_poly(w),tag))
