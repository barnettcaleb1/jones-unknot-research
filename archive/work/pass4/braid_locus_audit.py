"""Independent highest-degree-tie audit of the three-parameter Jones locus."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,itertools,time
ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'ren_jones_locus.json').read_text())
TERMS=[(tuple(map(F,row[:4])),row[4]) for row in data['affine_y_terms']]

def rref(equations):
    a=[list(row) for row in equations];piv=0
    for col in range(3):
        row=next((i for i in range(piv,len(a)) if a[i][col]),None)
        if row is None:continue
        a[piv],a[row]=a[row],a[piv]
        v=a[piv][col];a[piv]=[x/v for x in a[piv]]
        for i in range(len(a)):
            if i==piv:continue
            v=a[i][col];a[i]=[x-v*y for x,y in zip(a[i],a[piv])]
        piv+=1
    if any(not any(row[:3]) and row[3] for row in a):return None
    return tuple(tuple(row) for row in a[:piv])

def restrict(rows):
    sums=defaultdict(int)
    for b,c in TERMS:
        b=list(b)
        for row in rows:
            i=next(i for i in range(3) if row[i]);v=b[i]
            b=[x-v*y for x,y in zip(b,row)]
        sums[tuple(b)]+=c
    return {b:c for b,c in sums.items() if c}

seen=set();leaves=[]
def solve(rows=()):
    if rows in seen:return
    seen.add(rows);red=restrict(rows)
    if not red:leaves.append(rows);return
    if len(rows)==3:return
    # Group monomials by their remaining variable-exponent vector. Within a
    # group only its highest constant exponent can be the leading term.
    tops={}
    for b in red:
        if b[:3] not in tops or b[3]>tops[b[:3]][3]:tops[b[:3]]=b
    if len(tops)==1:return
    # At a zero at least two groups have equal highest exponents. Branch on
    # every pair; unlike the original solver this does not use coefficient signs.
    for b,d in itertools.combinations(tops.values(),2):
        eq=tuple(x-y for x,y in zip(b,d));nr=rref(rows+(eq,))
        if nr is not None:
            assert len(nr)==len(rows)+1
            solve(nr)

def add(*ps):
    r=defaultdict(int)
    for p in ps:
        for e,c in p.items():r[e]+=c
    return {e:c for e,c in r.items() if c}
def mul(p,q):return add(*({i+j:a*b for j,b in q.items()} for i,a in p.items()))
def shift(p,k,c=1):return {e+k:v*c for e,v in p.items()}
DELTA={2:-1,-2:-1};D2=mul(DELTA,DELTA);CHANNEL=add(D2,{0:-1})
def powers(p):
    f,g={0:1},{}
    for _ in range(abs(p)):
        s=1 if p>0 else -1
        f,g=shift(f,s),add(shift(g,s),shift(f,-s),shift(mul(g,DELTA),-s))
    return f,g
def audit_formula():
    raw=json.loads((ROOT/'tangle_ren_twists.json').read_text())['four_block_annular_brackets']
    blocks=[{int(z):{int(e):c for e,c in p.items()} for z,p in bl.items()} for bl in raw]
    tests=0
    for m,l,n in itertools.product(range(-2,3),repeat=3):
        p,q=1+2*m,1+2*l;f,g=powers(p);h,k=powers(q)
        weights=[mul(f,h),mul(g,h),mul(f,k),mul(g,k)]
        a,b=[add(*(mul(w,bl.get(z,{})) for w,bl in zip(weights,blocks))) for z in (2,0)]
        numerator=add(mul(add(shift(CHANNEL,8*n),{0:1}),a),b,shift(DELTA,3*(p+q),-1))
        scaled=shift(mul(D2,numerator),-p-q)
        predicted={}
        for affine,c in TERMS:
            exponent=4*(affine[0]*m+affine[1]*l+affine[2]*n+affine[3])+2
            assert exponent.denominator==1
            predicted=add(predicted,{int(exponent):c})
        assert predicted==scaled,(m,l,n)
        tests+=1
    return tests

if __name__=='__main__':
    started=time.monotonic();tests=audit_formula();solve()
    integer=[];positive_dim=[]
    for rows in leaves:
        if len(rows)<3:positive_dim.append(rows);continue
        point=tuple(-row[3] for row in rows)
        if all(x.denominator==1 for x in point):integer.append(tuple(map(int,point)))
    assert not positive_dim
    assert integer==[(-1,0,0)],integer
    result=dict(method='recursive highest-degree ties; independent RREF; no integrality pruning',
                visited=len(seen),rational_solution_loci=len(leaves),integer_solutions=integer,
                positive_dimensional_loci=0,coefficient_formula_checks=tests,
                seconds=time.monotonic()-started)
    (ROOT/'braid_locus_audit.json').write_text(json.dumps(result,indent=2));print(result)
