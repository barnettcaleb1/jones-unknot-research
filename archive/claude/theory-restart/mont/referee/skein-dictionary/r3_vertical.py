# R3: Theorem V raw check. F_a(A0,B0) = [t A0 + (-t)^a((1+t^2)A0 + t B0) + t^(3a-1) Phi5 B0]/Phi3
import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
D=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
def todict(l): return {e:c for e,c in l}
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def vw(B,a): return 's.l1.'+(B+'.' if B else '')+('x2.' if a>0 else 'y2.')*abs(a)+'u1'
PHI3=P((1,0),(1,1),(1,2)); PHI5=P((1,0),(1,1),(1,2),(1,3),(1,4))
def divexact(p,d):
    p=dict(p); q={}
    dt=top(d); dc=d[dt]
    for _ in range(2000):
        if not p: return clean(q)
        pt=top(p); c=p[pt]
        if c%dc: return None
        e=pt-dt; q[e]=c//dc
        for f,g in d.items(): p[e+f]=p.get(e+f,0)-q[e]*g
        p=clean(p)
        if p and top(p)<bot(d)+min(q)-5: return None
    return None
def Fa(A0,B0,a):
    sgn=1 if a%2==0 else -1
    num=add(mul(mono(1),A0), mul(mono(a,sgn), add(mul(P((1,0),(1,2)),A0), mul(mono(1),B0))), mul(mul(mono(3*a-1),PHI5),B0))
    return divexact(num,PHI3)
W={a:J_raw(vw('',a)) for a in (-5,-3,-1,1,3,5)}
FI={a:Fa(ONE,ONE,a) for a in W}
print('raw identity-body vertical values:',{a:sorted(W[a].items()) for a in W})
print('F_a(I) from (8.4):',{a:sorted(FI[a].items()) for a in FI})
Wn={a:None for a in W}
for a in W:
    k=top(W[a])-top(FI[a]); s=W[a][top(W[a])]//FI[a][top(FI[a])]
    Wn[a]=(s,k) if W[a]==shift({e:s*c for e,c in FI[a].items()},k) else None
print('raw/F_a(I) units W_a:',Wn)
bad=0; same=0
for i,(B,vv) in enumerate(D):
    v=[todict(vv[0]),todict(vv[1])]
    A0=a_of(v); B0=b_of(v)
    # horizontal c(B)
    al0=J_raw('s.r2.'+B+'.u1')
    kh=top(al0)-top(A0); sh=al0[top(al0)]//A0[top(A0)]
    cs=set()
    for a in W:
        r=J_raw(vw(B,a)); f=Fa(A0,B0,a)
        if f is None: cs.add('nondiv'); continue
        s0,k0=Wn[a]; pred=shift({e:s0*c for e,c in f.items()},k0)
        k=top(r)-top(pred); s=r[top(r)]//pred[top(pred)]
        cs.add((s,k) if r==shift({e:s*c for e,c in pred.items()},k) else None)
    if len(cs)!=1 or None in cs or 'nondiv' in cs: bad+=1; print('MISMATCH',i,B,cs)
    elif list(cs)[0]==(sh,kh): same+=1
print('vertical raw identity with a-independent c\'(B):',50-bad,'/50; c\'(B)==horizontal c(B):',same,'/50')
