"""Referee (PROOF lane): word-level checks of the PROVED claims on an INDEPENDENT body generator (pf_common.random_body),
plus twist rows. Exact (lp.py)."""
import sys, time, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
t0=time.time()
SEED=int(sys.argv[1]) if len(sys.argv)>1 else 4242
NB=int(sys.argv[2]) if len(sys.argv)>2 else 24
bodies=gen_bodies_nontriv(SEED, NB, Lmin=5, Lmax=12, kmax=5, frac_trivial=0.15)
def row(j,ch='y'): return '.'.join(['r1']*j+[ch+'0']+[ch+str(2*i) for i in range(1,j+1)]+['u1']*j)
bodies += [row(1),row(2),row(1,'x')]
stats={}
def rec(k,ok,info=None):
    stats.setdefault(k,[0,0]); stats[k][0 if ok else 1]+=1
    if not ok: print('FAIL',k,info)
E1v=[ONE,{}]
def raw_r2(m,N): return J_raw(jn('s.r2',tw(m),N,'u1'))
def raw_l1(W,N): return J_raw(jn('s.l1',N,W,'u2'))
r2u={m:raw_r2(m,'') for m in range(-4,5)}
l1u={W:raw_l1(W,'') for W in ('','x1')}
print('raw units of empty body, r2-closures:',{m:r2u[m] for m in r2u}); print('raw units l1-closures:',l1u)
OneMinusT4=P((1,0),(-1,4))
def vec_r2(N):
    a0=ratio_mono(raw_r2(0,N),r2u[0]); a1=ratio_mono(raw_r2(-1,N),r2u[-1])
    if a0 is None or a1 is None: return None
    v2=divexact(sub(a1,a0),OneMinusT4)
    return None if v2 is None else [a0,v2]
def vec_l1(N):
    a0=ratio_mono(raw_l1('',N),l1u['']); a1=ratio_mono(raw_l1('x1',N),l1u['x1'])
    if a0 is None or a1 is None: return None
    v2=divexact(sub(a1,a0),OneMinusT4)
    return None if v2 is None else [a0,v2]
vecs={}
for B in bodies:
    v=vec_r2(B); w=vec_l1(B)
    rec('T3 r2-recipe vector integral (Prop 3.9/4.2)', v is not None, B)
    rec('T3b l1-recipe vector integral', w is not None, B)
    if v is None or w is None: continue
    rec('T3c r2-vector == l1-vector up to unit (Cor 3.4 at vector level)', vec_unit_equal(v,w) is not None, (B,v,w))
    rec('T3d v1 == J(s.B) up to unit (Prop 4.2)', unit_equal(v[0], J('s.'+B)) is not None, B)
    vecs[B]=v
# T1 Cor 3.4 and T4 Thm 4.1 single box and T5 Prop 3.9 exact factorisation
for B,v in vecs.items():
    for m in range(-4,5):
        a=J(jn('s.r2',tw(m),B,'u1')); b=J(jn('s.l1',B,tw(m),'u2'))
        rec('T1 Cor3.4 J(s.r2.(y1)^m.B.u1)=J(s.l1.B.(y1)^m.u2)', a==b, (B,m))
        rec('T4 Thm4.1 single box, m=-4..4', a==normalize(close(-m,v)), (B,m))
        raw=raw_r2(m,B); pred=mul(r2u[m],close(-m,v))
        rec('T5 Prop3.9 exact: alpha_m(B) = alpha_m(empty) * e1^T X^-m v_recipe(B)', raw==pred, (B,m))
# T2 commutativity and T4 necklaces
rnd=random.Random(SEED+1); keys=list(vecs)
for trial in range(60):
    k=rnd.choice([2,2,3]); bs=rnd.sample(keys,k); m=rnd.randint(-3,3)
    w1=jn('s.r2',tw(m),*bs,'u1'); w2=jn('s.r2',tw(m),*reversed(bs),'u1')
    a=J(w1); b=J(w2)
    rec('T2 order of boxes irrelevant', a==b, (bs,m))
    p=vecs[bs[0]]
    for B in bs[1:]: p=star(p,vecs[B])
    rec('T4 Thm4.1 necklaces of 2-3 boxes', a==normalize(close(-m,p)), (bs,m))
# T6 folding (y1 version and x1 version), T7 R-invariance, in TH-2BR contexts
Ws=['','y1','x1.x1','y0','y0.x1','x0.y1.y1']
for B in keys[:14]:
    for W in Ws:
        a=J(jn('s.l1',B,W,'u2')); b=J(jn('s.l1',Rrev(B),W,'u2'))
        rec('T7 Lemma1.2 R-invariance', a==b, (B,W))
        for m in (-3,-1,1,3):
            a=J(jn('s.l1.r2',tw(m,'x','y'),B,'u1',W,'u2')); b=J(jn('s.l1',B,tw(m,'x','y'),W,'u2'))
            rec('T6 Lemma3.6 folding [l1.r2.(x1)^m.B.u1]=[l1.B.(x1)^m]', a==b, (B,W,m))
# T8 multiplicativity and hairpin
for trial in range(30):
    B1,B2=rnd.sample(keys,2)
    a=J(jn('s',B1,B2)); b=mul(J('s.'+B1),J('s.'+B2))
    rec('T8 Cor5.2 J(s.B1.B2)=J(s.B1)J(s.B2)', a==normalize(b), (B1,B2))
for B in keys:
    rec('T8b s.r2.B.u1 ~ s.B (J)', J(jn('s.r2',B,'u1'))==J('s.'+B), B)
for k,v in stats.items(): print('%-90s ok %d  bad %d'%(k,v[0],v[1]))
print('bodies',len(bodies),'with vectors',len(vecs),'time',round(time.time()-t0,1))
