"""Referee: (B) large twists |m| <= 8; (E) general (non-rational) nesting: a necklace used as a body inside another necklace.
Prediction from Thm 2.3 + Lemma 3.6: v(r2.(y1)^m.B1...Bk.u1) = X^-m (v(B1)*...*v(Bk))."""
import sys, time, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
t0=time.time()
bodies=gen_bodies_nontriv(9090, 10, Lmin=4, Lmax=9, kmax=4)
OneMinusT4=P((1,0),(-1,4))
r2u={m:J_raw(jn('s.r2',tw(m),'u1')) for m in (0,-1)}
def vec(N):
    a0=ratio_mono(J_raw(jn('s.r2',N,'u1')),r2u[0]); a1=ratio_mono(J_raw(jn('s.r2',tw(-1),N,'u1')),r2u[-1])
    v2=divexact(sub(a1,a0),OneMinusT4); return [a0,v2]
V={B:vec(B) for B in bodies}
stats={}
def rec(k,ok,info=None):
    stats.setdefault(k,[0,0]); stats[k][0 if ok else 1]+=1
    if not ok: print('FAIL',k,info)
# (B) large |m|
for B in bodies[:6]:
    for m in (-8,-7,-6,-5,5,6,7,8):
        rec('B: single box |m| in 5..8', J(jn('s.r2',tw(m),B,'u1'))==normalize(close(-m,V[B])), (B,m))
def Xpow(m,v):
    for _ in range(abs(m)): v=mvec(Xm if m>0 else Xi, v)
    return v
rnd=random.Random(5)
for trial in range(40):
    k=rnd.choice([1,2]); inner=rnd.sample(bodies,k); m_in=rnd.choice([-2,-1,1,2])
    NB=jn('r2',tw(m_in),*inner,'u1')          # nested necklace used as a body
    vin=V[inner[0]]
    for b in inner[1:]: vin=star(vin,V[b])
    vNB=Xpow(-m_in,vin)
    # (E1) the nested body's own recipe vector equals X^-m_in (prod) up to unit
    w=vec(NB)
    rec('E1: v(r2.(y1)^m.B..u1) = X^-m (v*..) up to unit', vec_unit_equal(w,vNB) is not None, (NB,))
    # (E2) inside an outer necklace with another body and outer twist
    other=rnd.choice(bodies); m_out=rnd.randint(-3,3)
    word=jn('s.r2',tw(m_out),NB,other,'u1')
    Jw=J(word)
    if Jw is None: rec('E2 knot?',False,word); continue
    rec('E2: outer necklace with nested body', Jw==normalize(close(-m_out,star(vNB,V[other]))), (word,))
    # (E3) doubly nested
    NB2=jn('r2',tw(rnd.choice([-1,1,2])),NB,rnd.choice(bodies),'u1')
for k,v in stats.items(): print('%-60s ok %d bad %d'%(k,v[0],v[1]))
print('time',round(time.time()-t0,1))
