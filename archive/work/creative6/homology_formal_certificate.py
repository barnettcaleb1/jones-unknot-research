"""Exact symbolic checks for abstract models, NEVER asserted knot realizations.

An affine expression in g is stored as (constant, coefficient of g).
All identities below hold for arbitrary integer g, not just a bounded sample.
"""
from collections import Counter, defaultdict
from pathlib import Path
import json

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(a,n): return (a[0]*n,a[1]*n)
def sub(a,b): return add(a,scale(b,-1))

# Entries (homological degree, quantum degree), both affine in g.
P = [((0,0),(0,-2)), ((-2,4),(0,0)), ((-1,4),(0,2)),
     ((-1,2),(0,-2)), ((0,2),(0,2))]
euler=defaultdict(int)
for h,q in P:
    assert h[1]%2==0
    euler[q] += (-1 if h[0]%2 else 1)
assert {q:n for q,n in euler.items() if n} == {(0,0):1}
delta=Counter(sub(q,scale(h,2)) for h,q in P)
assert delta == Counter({(0,-2):2,(2,-6):2,(4,-8):1})
# Bar endpoints are entries1->2 and3->4; differential raises h by1.
lengths=[]
for a,b in [(1,2),(3,4)]:
    assert sub(P[b][0],P[a][0])==(1,0)
    dq=sub(P[b][1],P[a][1]); assert all(x%2==0 for x in dq)
    lengths.append((dq[0]//2,dq[1]//2))
assert lengths==[(0,1),(0,2)]

# CFK-infinity model. Powers of U are coefficients times g.
names=['a','b','c','ap','bp']
M={'a':(0,0),'b':(1,-2),'c':(2,-4),'ap':(0,-2),'bp':(1,-4)}
A={'a':(0,1),'b':(0,1),'c':(0,0),'ap':(0,-1),'bp':(0,-1)}
d={'a':[], 'ap':[], 'b':[(1,0,'ap'),(1,1,'a')],
   'bp':[(1,1,'ap'),(1,2,'a')], 'c':[(1,0,'bp'),(-1,1,'b')]}
inv={'a':[(1,-1,'ap')], 'ap':[(1,1,'a')],
     'b':[(1,-1,'bp')], 'bp':[(1,1,'b')], 'c':[(-1,0,'c')]}
def apply(op,terms):
    out=defaultdict(int)
    for c,p,x in terms:
        for c2,p2,y in op[x]: out[(p+p2,y)]+=c*c2
    return {key:val for key,val in out.items() if val}
def terms(D): return [(c,p,x) for (p,x),c in D.items()]
for x in names:
    assert not apply(d,d[x])
    assert apply(inv,inv[x])=={(0,x):1}
    assert apply(d,inv[x])==apply(inv,d[x])
    for coeff,p,y in d[x]:
        assert sub(M[y],(0,2*p))==sub(M[x],(1,0))
        assert p>=0
        delta_A=sub(sub(A[y],(0,p)),A[x])
        assert delta_A[0]==0 and delta_A[1]<=0
# Hat differential retains only zero U powers: b->ap, c->bp; a survives.
hat={x:[(c,p,y) for c,p,y in d[x] if p==0] for x in names}
assert hat=={'a':[], 'b':[(1,0,'ap')], 'c':[(1,0,'bp')], 'ap':[], 'bp':[]}
hfk_delta=Counter(scale(sub(M[x],A[x]),2) for x in names)
assert hfk_delta==delta

report={
 'status':'ABSTRACT algebraic models only; no classical-knot realization claimed',
 'valid_parameter':'every integer g >= 2',
 'reduced_Kh_P':'q^(-2g)+t^(4g-2)+t^(4g-1)q^(2g)+t^(2g-1)q^(-2g)+t^(2g)q^(2g)',
 'Jones_Euler':'1', 'reduced_rank':5, 'unreduced_rank':10,
 'generalized_Lee_torsion_exponents':['g','2g'], 'free_Lee_s':'-2g',
 'half_delta_multiset':['-g','-g','1-3g','1-3g','2-4g'],
 'CFK_check':'d^2=0, grading, filtration, conjugation chain involution, hat rank1, same delta all verified symbolically',
 'CFK_tau':'g for the modeled HFK; Dowlin targets the mirror of the Kh knot',
 'tests':'exact affine arithmetic, valid for all g, no floating point or sample inference'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
