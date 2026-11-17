"""Raw-marking check of Section 7 (nested-cap slide): for N = r2.(y1)^m.B_1...B_n.u1 compute the raw
channel amplitudes (a_N,b_N) by the TL3 sandwich and compare with X^-m applied to the raw product
(channelwise product of raw (a_i,b_i)); report the common unit c with (a_N,b_N) = c * X^-m (a_p,b_p)."""
import sys, json, random
from r2lib import *
import sympy as sp
A=sp.symbols('A'); t=A**4
def S(p): return sum(c*A**e for e,c in p.items())
d=S(DELTA); Phi3=1+t+t**2
X_ab=sp.Matrix([[-t**3,(1+t)*(1+t**2)],[t*(1+t),1]])/Phi3
def ab(B):
    da,db=body_ab(B); return sp.Matrix([S(da)/d, S(db)/d])
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def unit_of(u,v):
    r0=sp.factor(sp.cancel(u[0]/v[0])); r1=sp.factor(sp.cancel(u[1]/v[1]))
    return r0, sp.simplify(r0-r1)==0
L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
bodies=[B for B,_ in L]
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
n=0; bad=0; units={}
for trial in range(int(sys.argv[2]) if len(sys.argv)>2 else 20):
    k=rnd.choice([1,1,2])
    Bs=[rnd.choice(bodies) for _ in range(k)]
    m=rnd.choice([-3,-2,-1,1,2,3])
    N='r2.'+tw(m)+'.'.join(Bs)+'.u1'
    p=sp.Matrix([1,1])
    for B in Bs:
        v=ab(B); p=sp.Matrix([sp.cancel(p[0]*v[0]), sp.cancel(p[1]*v[1])])
    pred=(X_ab**(-m))*p if m>0 else (X_ab**(-m))*p
    pred=sp.Matrix([sp.cancel(pred[0]), sp.cancel(pred[1])])
    vN=ab(N)
    c,ok=unit_of(vN,pred)
    eps=sp.cancel(p[1]).subs(A,sp.exp(sp.I*sp.pi/4))  # t=-1 at A=e^{i pi/4}
    n+=1
    if not ok: bad+=1; print('MISMATCH',N,c)
    units.setdefault((m,),set()).add(str(c))
    print(n, 'm=%d'%m, 'nbox=%d'%k, 'unit c =', c, ok)
print('checked',n,'bad',bad)
print(units)
