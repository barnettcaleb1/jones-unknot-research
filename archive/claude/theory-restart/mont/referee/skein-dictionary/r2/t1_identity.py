"""Direct bracket computation of F_a(I) for the vertical closure s.l1.(x2)^a.u1, a=-3..3.
F_a := A^(8a) <Theta_a> / Delta2, with <Theta_a> the colored theta evaluation (axis 1, arc 2, f2 on the
arc and, for even a, on the closed loop).  Compare with sum_c lambda_c^a Delta_c/Delta2 and with
flat_search's y (dictionary (2.1): <Theta> = Delta2 * y)."""
from r2lib import *
import sympy as sp
A=sp.symbols('A')
def S(p): return sum(c*A**e for e,c in p.items())
d=S(DELTA); D2=d**2-1; D4=d**4-3*d**2+1; t=A**4
lam=[sp.Integer(1),-t,t**3]; Dc=[sp.Integer(1),D2,D4]
# planar theta
v,k=theta_eval('s.')
print('planar theta: <Theta0> =', sp.factor(S(v)/d**k), ' Delta2 =', sp.expand(D2))
for a in range(-3,4):
    w='s.l1.'+('x2.' if a>0 else 'y2.')*abs(a)+'u1'
    if a==0: w='s.l1.u1'
    v1,k1=theta_eval(w)                 # f2 on arc only
    v2,k2=theta_eval(w,extra=[(1,4)])   # + f2 on the l1 band (loop for even a)
    th1=sp.cancel(S(v1)/d**k1); th2=sp.cancel(S(v2)/d**k2)
    F=sp.cancel(A**(8*a)*th2/D2)
    pred=sp.cancel(sum(lam[c]**a*Dc[c] for c in range(3))/D2)
    y,x=fs.bracket_vector(alex.parse(w)); yS=S(y); u=sp.expand(yS+d*S(x))
    print('a=%2d'%a, 'F_a =', sp.factor(F), '| pred sum lam^a Dc/D2 =', sp.factor(pred), '| equal:', sp.simplify(F-pred)==0,
          '| one-f2 vs two-f2 equal:', sp.simplify(th1-th2)==0,
          '| Delta2*y_flat == <Theta>(one f2):', sp.simplify(D2*yS-th1)==0, '| u_flat =', u)
