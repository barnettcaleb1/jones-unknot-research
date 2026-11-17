"""Exact affine-exponent branch solver for odd top twists and meridional twists.

Each cancellation branch imposes equality of a positive and negative monomial.
The parameter rank is three, so this exhaustive search terminates at depth <=3.
No bound on the integer twist parameters is imposed.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import json, math, time

ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'tangle_ren_twists.json').read_text())
blocks=[{int(z):{int(e):c for e,c in p.items()} for z,p in b.items()}
        for b in data['four_block_annular_brackets']]

def add(*ps):
    d=defaultdict(int)
    for p in ps:
        for e,c in p.items():d[e]+=c
    return {e:c for e,c in d.items() if c}
def scale(p,k):return {e:c*k for e,c in p.items() if c*k}
def mul(p,q):
    d=defaultdict(int)
    for e,c in p.items():
        for f,v in q.items():d[e+f]+=c*v
    return {e:c for e,c in d.items() if c}
delta={2:-1,-2:-1}
delta2=mul(delta,delta)
Delta2=add(delta2,{0:-1})

def Fs(z):
    a,b,c,d=[bl.get(z,{}) for bl in blocks]
    return [d,add(mul(delta,b),scale(d,-1)),
            add(mul(delta,c),scale(d,-1)),
            add(mul(delta2,a),scale(mul(delta,add(b,c)),-1),d)]

# Affine A exponent is (m,l,n,constant); p=1+2m, q=1+2l.
def expterms(fs):
    out=defaultdict(int)
    shifts=[(-8,-8,0,-8),(-8,0,0,-4),(0,-8,0,-4),(0,0,0,0)]
    signs=[1,-1,-1,1]
    for f,b,s in zip(fs,shifts,signs):
        for e,c in f.items():out[b[:3]+(b[3]+e,)]+=s*c
    return {b:c for b,c in out.items() if c}
fa,fb=expterms(Fs(2)),expterms(Fs(0))
terms=defaultdict(int)
for b,c in fa.items():
    terms[b]+=c
    for e,k in Delta2.items():terms[(b[0],b[1],b[2]+8,b[3]+e)]+=c*k
for b,c in fb.items():terms[b]+=c
for e,c in mul(delta2,delta).items():terms[(4,4,0,e+4)]-=c
# Divide common A^2 and switch to y=A^4.
poly={}
for b,c in terms.items():
    if c:
        assert all(x%4==0 for x in b[:3]) and (b[3]-2)%4==0
        poly[(b[0]//4,b[1]//4,b[2]//4,(b[3]-2)//4)]=c
assert poly

def extend(rows,eq):
    """Canonical rational RREF for equations b*x+constant=0."""
    v=list(map(Q,eq))
    for row in rows:
        p=next(i for i in range(3) if row[i])
        k=v[p]
        if k:v=[a-k*b for a,b in zip(v,row)]
    inds=[i for i in range(3) if v[i]]
    if not inds:return rows if not v[3] else None
    p=inds[0];k=v[p];v=tuple(a/k for a in v)
    nr=[]
    for row in rows:
        k=row[p]
        nr.append(tuple(a-k*b for a,b in zip(row,v)))
    nr.append(v)
    return tuple(sorted(nr,key=lambda row:next(i for i in range(3) if row[i])))

def reduced(rows):
    d=defaultdict(int)
    for b,c in poly.items():
        v=list(map(Q,b))
        for row in rows:
            p=next(i for i in range(3) if row[i])
            k=v[p]
            if k:v=[a-k*x for a,x in zip(v,row)]
        d[tuple(v)]+=c
    return {b:c for b,c in d.items() if c}

def int_possible(rows):
    # Necessary divisibility for every rational-RREF row; exact at full rank.
    for row in rows:
        den=math.lcm(*(x.denominator for x in row))
        ints=[int(x*den) for x in row]
        g=math.gcd(*ints[:3])
        if ints[3]%g:return False
    return True

seen=set();leaves=[];stats=defaultdict(int);t0=time.monotonic()
def solve(rows=()):
    if rows in seen:return
    seen.add(rows);stats[f'rank{len(rows)}']+=1
    if not int_possible(rows):stats['nonintegral']+=1;return
    red=reduced(rows)
    if not red:leaves.append(rows);return
    if len(rows)==3:return
    candidates=[]
    for b,c in red.items():
        opp=[d for d,k in red.items() if k*c<0 and d[:3]!=b[:3]]
        if not opp:return
        candidates.append((len(opp),b,opp))
    _,b,opp=min(candidates)
    for d in opp:
        eq=tuple(x-y for x,y in zip(b,d))
        nr=extend(rows,eq)
        if nr is not None:solve(nr)

if __name__=='__main__':
    print('affine monomials',len(poly),flush=True)
    solve()
    result={'parameterization':'p=1+2m,q=1+2l,meridional twist n',
            'equation':'(A^(8n)*Delta2+1)*Fa+Fb-delta^3*A^(2(p+q))=0',
            'affine_y_terms':[[*b,c]for b,c in sorted(poly.items())],
            'stats':dict(stats),'solution_loci_rref':[[[str(x)for x in row]for row in s]for s in leaves],
            'elapsed_seconds':time.monotonic()-t0}
    (ROOT/'ren_jones_locus.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items()if k!='affine_y_terms'},indent=2))
