"""Referee: depth-3 nesting check of v(r2.(y1)^m.B1...Bk.u1) = X^-m (v(B1)*...*v(Bk))."""
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
bodies=gen_bodies_nontriv(8642, 8, Lmin=3, Lmax=7, kmax=4)
OneMinusT4=P((1,0),(-1,4))
r2u={m:J_raw(jn('s.r2',tw(m),'u1')) for m in (0,-1)}
def vec(N):
    a0=ratio_mono(J_raw(jn('s.r2',N,'u1')),r2u[0]); a1=ratio_mono(J_raw(jn('s.r2',tw(-1),N,'u1')),r2u[-1])
    return [a0,divexact(sub(a1,a0),OneMinusT4)]
V={B:vec(B) for B in bodies}
def Xpow(m,v):
    for _ in range(abs(m)): v=mvec(Xm if m>0 else Xi, v)
    return v
rnd=random.Random(3); ok=bad=0
for trial in range(25):
    word=None; v=None
    B=rnd.choice(bodies); w=B; v=V[B]
    for depth in range(3):
        m=rnd.choice([-2,-1,1,2]); other=rnd.choice(bodies)
        w=jn('r2',tw(m),w,other,'u1'); v=Xpow(-m,star(v,V[other]))
    mo=rnd.randint(-2,2)
    Jw=J(jn('s.r2',tw(mo),w,'u1'))
    if Jw is None: print('not knot?'); continue
    if Jw==normalize(close(-mo,v)): ok+=1
    else: bad+=1; print('FAIL',w)
print('depth-3 nested necklaces: ok',ok,'bad',bad)
