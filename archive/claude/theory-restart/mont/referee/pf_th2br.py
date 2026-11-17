"""Referee: inputs. (I1) TH-2BR-A matrices vs lp: J(s.l1.W.u2) = norm(e1^T rho(W) e1), W random in y0,x0,x1,y1.
(I2) Cor 5.4 on new bodies: J(s.l1.B.W.u2) = norm(e1^T rho(W) v(B)) with v(B) from the raw r2-recipe."""
import sys, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
t0=time.time(); rnd=random.Random(99)
mp={'y0':'Y','x0':'y','x1':'X','y1':'x'}
stats={}
def rec(k,ok,info=None):
    stats.setdefault(k,[0,0]); stats[k][0 if ok else 1]+=1
    if not ok: print('FAIL',k,info)
for trial in range(150):
    W=[rnd.choice(list(mp)) for _ in range(rnd.randint(1,9))]
    Jw=J('s.l1.'+'.'.join(W)+'.u2')
    if Jw is None: continue
    p=apply(''.join(mp[l] for l in reversed(W)))
    rec('I1 TH-2BR matrices', Jw==normalize(p[0]), W)
bodies=gen_bodies_nontriv(555, 10, Lmin=4, Lmax=10, kmax=5)
OneMinusT4=P((1,0),(-1,4))
r2u={m:J_raw(jn('s.r2',tw(m),'u1')) for m in (0,-1)}
for B in bodies:
    a0=ratio_mono(J_raw(jn('s.r2',B,'u1')),r2u[0]); a1=ratio_mono(J_raw(jn('s.r2',tw(-1),B,'u1')),r2u[-1])
    v=[a0,divexact(sub(a1,a0),OneMinusT4)]
    for trial in range(6):
        W=[rnd.choice(list(mp)) for _ in range(rnd.randint(1,6))]
        Jw=J('s.l1.'+B+'.'+'.'.join(W)+'.u2')
        if Jw is None: continue
        p=apply(''.join(mp[l] for l in reversed(W)),v)
        rec('I2 Cor 5.4 two-bridge special region on new bodies', Jw==normalize(p[0]), (B,W))
for k,v in stats.items(): print('%-55s ok %d bad %d'%(k,v[0],v[1]))
print('time',round(time.time()-t0,1))
