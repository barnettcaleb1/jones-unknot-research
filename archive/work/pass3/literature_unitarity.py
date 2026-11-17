"""Exact continuous-arc unitarity check for the six published trace candidates.

Tests only characteristic-polynomial eigenvalues, not realization by braids.
Conventions: R_i(q)=q Burau_i(q^-2), writhe=5, determinant=-q^5.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from literature_trace_targets import add, mul, neg, shift


def refl(p):
    return {-k: v for k, v in p.items()}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def trim(p):
    while p and not p[-1]:
        p.pop()
    return p


def rem(p, q):
    p = p[:]
    while p and len(p) >= len(q):
        d = len(p)-len(q)
        c = p[-1]/q[-1]
        for i, b in enumerate(q):
            p[i+d] -= c*b
        trim(p)
    return p


def val(p, x):
    y = F(0)
    for c in reversed(p):
        y = y*x+c
    return y


def variations(vals):
    signs = [(1 if v > 0 else -1) for v in vals if v]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sturm(p):
    seq = [p, [i*p[i] for i in range(1,len(p))]]
    while seq[-1]:
        r = [-c for c in rem(seq[-2], seq[-1])]
        if not r:
            break
        # Multiplying a Sturm polynomial by a positive scalar is harmless.
        fac = abs(r[-1])
        seq.append([c/fac for c in r])
    va, vb = variations([val(p,0) for p in seq]), variations([val(p,2) for p in seq])
    return va, vb, len(seq)


data = json.loads(Path(__file__).with_name('literature_trace_targets.json').read_text())
answers = []
for item in data:
    t = {int(k):v for k,v in item['a31_target'].items()}
    nt = mul(t,refl(t))
    cube = mul(mul(t,t),t)
    disc = add(mul(nt,nt),scale(nt,18),scale(shift(cube,-5),4),
               scale(shift(refl(cube),5),4),{0:-27})
    assert disc == refl(disc)
    assert all(k%2==0 for k in disc)
    # q^(2j)+q^(-2j)=S_j(x), x=q^2+q^-2, S_j=x S_(j-1)-S_(j-2).
    s0,s1={0:2},{1:1}
    pol={0:disc.get(0,0)}
    for j in range(1,max(disc)//2+1):
        sj=s1 if j==1 else add(shift(s1,1),neg(s0))
        pol=add(pol,scale(sj,disc.get(2*j,0)))
        if j>1:
            s0,s1=s1,sj
    p=[F(pol.get(i,0)) for i in range(max(pol)+1)]
    va,vb,length=sturm(p)
    assert va==vb, (item['quotient_tuple'],va,vb)
    assert val(p,0)<0 and val(p,2)<0
    result={'quotient_tuple':item['quotient_tuple'],
            'discriminant_in_x_coefficients_ascending':[int(c) for c in p],
            'endpoint_values':[str(val(p,0)),str(val(p,2))],
            'sturm_variations_at_0_and_2':[va,vb],
            'sturm_sequence_length':length,
            'real_roots_in_0_2':va-vb,
            'conclusion':'Discriminant strictly negative throughout x in [0,2].'}
    answers.append(result)
    print(item['quotient_tuple'],'degree',len(p)-1,'V(0),V(2)',va,vb,'endpoints',val(p,0),val(p,2))
Path(__file__).with_suffix('.json').write_text(json.dumps(answers,indent=2)+'\n')
