"""Referee: are the 'exact' (regular-isotopy) claims exact at the RAW bracket level?
 (R1) Lemma 3.6: J_raw(s.l1.r2.(x1)^m.B.u1.W.u2) == J_raw(s.l1.B.(x1)^m.W.u2)
 (R2) Prop 3.7 recursion: J_raw(s.l1.ROW_{j+1}.W.u2) == J_raw(s.l1.r2.x1.ROW_j.u1.W.u2)
 (R3) Lemma 1.2: J_raw(s.l1.R(B).W.u2) == J_raw(s.l1.B.W.u2)
 (R4) Cor 3.4: J_raw(s.r2.(y1)^m.N.u1) / J_raw(s.l1.N.(y1)^m.u2) is a monomial independent of N
 (R5) Cor 5.2(a): J_raw(s.r2.N.u1) == J_raw(s.N)"""
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
t0=time.time()
bodies=gen_bodies_nontriv(31337, 12, Lmin=4, Lmax=10, kmax=5, frac_trivial=0.2)
def row(j,ch='y'): return '.'.join(['r1']*j+[ch+'0']+[ch+str(2*i) for i in range(1,j+1)]+['u1']*j)
stats={}
def rec(k,ok,info=None):
    stats.setdefault(k,[0,0]); stats[k][0 if ok else 1]+=1
    if not ok and stats[k][1]<=3: print('FAIL',k,info)
Ws=['','y1','x1.x1','y0.x1']
for B in bodies:
    for W in Ws:
        for m in (-2,-1,1,2):
            a=J_raw(jn('s.l1.r2',tw(m,'x','y'),B,'u1',W,'u2')); b=J_raw(jn('s.l1',B,tw(m,'x','y'),W,'u2'))
            rec('R1 folding exact (raw)', a==b, (B,W,m,a,b))
        a=J_raw(jn('s.l1',Rrev(B),W,'u2')); b=J_raw(jn('s.l1',B,W,'u2'))
        rec('R3 R-invariance exact (raw)', a==b, (B,W))
    rec('R5 hairpin exact (raw)', J_raw(jn('s.r2',B,'u1'))==J_raw('s.'+B), B)
for j in range(0,3):
    for W in Ws:
        for ch,och in (('y','x'),('x','y')):
            a=J_raw(jn('s.l1',row(j+1,ch),W,'u2')); b=J_raw(jn('s.l1.r2',och+'1',row(j,ch),'u1',W,'u2'))
            rec('R2 row recursion exact (raw)', a==b, (j,W,ch))
ratios={}
for B in bodies:
    for m in range(-3,4):
        a=J_raw(jn('s.r2',tw(m),B,'u1')); b=J_raw(jn('s.l1',B,tw(m),'u2'))
        q=None
        if len(b)>=1:
            # a/b monomial?
            k=bot(a)-bot(b); s=a[bot(a)]//b[bot(b)] if b[bot(b)] and a[bot(a)]%b[bot(b)]==0 else None
            if s in (1,-1) and {e+k:s*c for e,c in b.items()}==a: q=(s,k)
        rec('R4a raw ratio is a monomial', q is not None, (B,m))
        ratios.setdefault(m,set()).add(q)
for m in sorted(ratios): rec('R4b raw ratio independent of N (m=%d)'%m, len(ratios[m])==1, ratios[m])
print({m:ratios[m] for m in sorted(ratios)})
for k,v in stats.items(): print('%-45s ok %d bad %d'%(k,v[0],v[1]))
print('time',round(time.time()-t0,1))
