#!/usr/bin/env python3
"""Four exact TL6 tests of overlapping five-strand Burau-kernel blocks.
No finite-field pass is accepted as a polynomial identity.
"""
import json, pathlib, sys, time
from functools import lru_cache
HERE=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'pass2'))
import braid_kernel as b
s=b.search
s.tables=lru_cache(None)(s.tables)
X=b.KERNEL
Y=[(1 if a>0 else -1)*(abs(a)+1) for a in X]
C=[1,2,3,4,5]
assert b.identity(b.burau(X,6)) and b.identity(b.burau(Y,6))
assert s.knot(C,6) and s.jones_a(C,6)=={0:1}
assert len(s.tables(6)[2])==132

def evaluate_A2(word):
    # Independent exact rational specialization of the diagram-vector walk.
    # Powers of 2 multiply away all A^-1 denominators at each crossing.
    ident,ts,loops=s.tables(6)
    v=[0]*len(loops);v[ident]=1
    # Choose A=2, delta=-17/4. Scale by 8 per crossing: 8g=16I+4e;
    # 8g^-1=4I+16e, which leaves denominators on e loops, cancelled here.
    for a in word:
        nv=[0]*len(v)
        ic,ec=(16,4) if a>0 else (4,16)
        for j,x in enumerate(v):
            nv[j]+=ic*x
            dst,lp=ts[abs(a)-1][j]
            assert lp in (0,1)
            nv[dst]+=ec*x if not lp else -(ec//4)*17*x
        v=nv
    # Normalize closure loop factors with fixed denominator 4^5.
    raw=sum(x*((-17)**(l-1))*(4**(6-l)) for x,l in zip(v,loops))
    writhe=sum(1 if x>0 else -1 for x in word)
    # Rational equality raw/(8^len*4^5)*(-8)^-w.
    return raw,8**len(word)*4**5*((-8)**writhe)

rows=[]
for e,f in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    block=b.comm(b.power(X,e),b.power(Y,f))
    word=b.reduce(block+C)
    assert b.identity(b.burau(block,6))
    assert b.permutation(block,6)==list(range(6))
    assert s.knot(word,6)
    start=time.monotonic()
    va=s.jones_a(word,6)
    assert all(d%4==0 for d in va)
    vt={-d//4:c for d,c in va.items()}
    # Exact rational Jones at A=2, via unrelated integer-scaled arithmetic.
    num,den=evaluate_A2(word)
    low=min(va)
    lhs=sum(c*2**(d-low) for d,c in va.items())
    if low>=0: assert num==den*lhs*2**low
    else: assert num*2**(-low)==den*lhs
    row=dict(e=e,f=f,word=word,length=len(word),writhe=sum(1 if a>0 else -1 for a in word),
             knot=True,burau_block_identity=True,jones_one=vt=={0:1},
             jones_t={str(k):v for k,v in sorted(vt.items())},
             min_t=min(vt),max_t=max(vt),terms=len(vt),
             lowest_coefficient=vt[min(vt)],highest_coefficient=vt[max(vt)],
             seconds=round(time.monotonic()-start,3))
    rows.append(row)
    print({k:v for k,v in row.items() if k not in ('word','jones_t')},flush=True)
(HERE/'braid_candidate.json').write_text(json.dumps(dict(
    convention='sigma_i=A*1+A^-1*e_i; delta=-A^2-A^-2; t=A^-4; V(U)=1',
    X=X,Y=Y,anchor=C,family='closure([X^e,Y^f] C), e,f in {+1,-1}',
    tests=rows),indent=2)+'\n')
