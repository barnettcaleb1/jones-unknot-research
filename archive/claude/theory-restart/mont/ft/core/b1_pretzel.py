import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import clib, lp, words, alex
from fractions import Fraction as F
def hexp(V,kmax=4):
    """coefficients c_k of V(-e^h) = sum c_k h^k (exact): c_k = (1/k!) sum_e V_e (-1)^e e^k"""
    import math
    return [F(sum(c*(-1)**(e%2)*e**k for e,c in V.items()),math.factorial(k)) for k in range(kmax+1)]
w=words.mont(1,[3,7]); print('mont(1,[3,7]) =',w)
V=clib.VK(w); print('V(P(-2,3,7)) =',sorted(V.items()))
print('  Alexander:',alex.alex_poly(w), ' det', alex.alex_eval(w,-1))
print('  V(-1)=',lp.ev(V,-1),' c_k:',hexp(V))
VT={6:1,8:1,14:-1}
print('V(T(3,7)) =',sorted(VT.items()),' V(-1)=',lp.ev(VT,-1),' c_k:',hexp(VT))
Vm={-e:c for e,c in V.items()}
print('mirror P(-2,3,7): c_k:',hexp(Vm))
# J of the inversion
J=lp.J(w); print('J(P(-2,3,7)) =',sorted(J.items()),' a2 =',lp.a2(J))
