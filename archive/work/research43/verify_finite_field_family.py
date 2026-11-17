#!/usr/bin/env python3
"""Standalone exact TL3 certificate for K_N=closure([s1^N,s2^N]s1s2).

Python standard library only. No precomputed knot polynomial or external
Temperley--Lieb engine is used. Laurent dictionaries use exponent:integer.
Conventions: delta=-A^2-A^-2; s_i=A I+A^-1 e_i; unknot bracket=1;
V=(-A^3)^(-w)*bracket and t=A^-4.

The finite-field theorem is an all-N algebraic argument recorded in the
JSON, not an inference from the two finite exact examples checked here.
"""
from collections import defaultdict
from pathlib import Path
import json


def clean(p):
    return {k:v for k,v in p.items() if v}


def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items():out[k]+=v
    return clean(out)


def shift(p,k,c=1):
    return {j+k:c*v for j,v in p.items() if c*v}


def mul(p,q):
    out=defaultdict(int)
    for i,a in p.items():
        for j,b in q.items():out[i+j]+=a*b
    return clean(out)


def loop(p):
    return add(shift(p,2,-1),shift(p,-2,-1))


def planar_matchings(xs):
    if not xs:
        yield ();return
    for j in range(1,len(xs),2):
        for left in planar_matchings(xs[1:j]):
            for right in planar_matchings(xs[j+1:]):
                yield ((xs[0],xs[j]),)+left+right


def partner(pairs,n=6):
    p=[None]*n
    for i,j in pairs:p[i]=j;p[j]=i
    return tuple(p)


def components(edges,n):
    p=list(range(n))
    def find(i):
        while p[i]!=i:
            p[i]=p[p[i]];i=p[i]
        return i
    for i,j in edges:p[find(i)]=find(j)
    return [find(i) for i in range(n)]


def compose(a,b):
    # Rows 0..2, 3..5, 6..8. Glue lower row of a to upper row of b.
    edges=[(i,a[i]) for i in range(6) if i<a[i]]
    edges += [(i+3,b[i]+3) for i in range(6) if i<b[i]]
    cc=components(edges,9)
    outer=[0,1,2,6,7,8]
    groups=defaultdict(list)
    for j,k in enumerate(outer):groups[cc[k]].append(j)
    assert all(len(g)==2 for g in groups.values())
    closed=len(set(cc))-len(groups)
    return partner(groups.values()),closed


BASIS=[partner(p) for p in planar_matchings((0,1,2,5,4,3))]
assert len(BASIS)==5
INDEX={b:i for i,b in enumerate(BASIS)}
IDENT=partner([(0,3),(1,4),(2,5)])
ES=[partner([(i,i+1),(i+3,i+4)]+[(j,j+3) for j in range(3) if j not in (i,i+1)])
    for i in range(2)]
TRANS=[[compose(b,e) for b in BASIS] for e in ES]


def jones_A(word):
    vec=[{} for _ in BASIS];vec[INDEX[IDENT]]={0:1}
    for letter in word:
        s=1 if letter>0 else -1
        out=[{} for _ in BASIS]
        for j,p in enumerate(vec):
            out[j]=add(out[j],shift(p,s))
            dest,loops=TRANS[abs(letter)-1][j]
            assert loops in (0,1)
            q=loop(p) if loops else p
            k=INDEX[dest]
            out[k]=add(out[k],shift(q,-s))
        vec=out
    raw={}
    for basis,p in zip(BASIS,vec):
        edges=[(i,basis[i]) for i in range(6) if i<basis[i]]
        cc=components(edges+[(0,3),(1,4),(2,5)],6)
        q=p
        for _ in range(len(set(cc))-1):q=loop(q)
        raw=add(raw,q)
    w=sum(1 if x>0 else -1 for x in word)
    return shift(raw,-3*w,(-1)**w)


def knot_permutation(word):
    p=list(range(3))
    for letter in word:
        i=abs(letter)-1;p[i],p[i+1]=p[i+1],p[i]
    unseen=set(range(3));cycles=[]
    while unseen:
        j=min(unseen);cycle=[]
        while j in unseen:
            unseen.remove(j);cycle.append(j);j=p[j]
        cycles.append(cycle)
    return cycles


def mm(a,b):
    return [[add(*(mul(a[i][k],b[k][j]) for k in range(2))) for j in range(2)] for i in range(2)]


def main():
    # Exact polynomial matrix identity in an indeterminate N, proving the
    # specialized commutator and anchor trace for every integer N.
    zero={};one={0:1};n={1:1};minus_n={1:-1}
    L=[[one,zero],[n,one]];Li=[[one,zero],[minus_n,one]]
    Ui=[[one,minus_n],[zero,one]];U=[[one,n],[zero,one]]
    M=mm(mm(mm(L,Ui),Li),U)
    expected=[[{0:1,2:1},{3:1}],[{3:1},{0:1,2:-1,4:1}]]
    assert M==expected
    R=[[one,{0:-1}],[one,zero]]
    MR=mm(M,R)
    assert add(MR[0][0],MR[1][1])=={0:1,2:1}

    # Explicit normalization controls on three-strand unknot closures.
    controls=[[1,2],[-1,-2],[1,-2]]
    for w in controls:assert jones_A(w)=={0:1}

    rows=[]
    for N in (2,4):
        word=[1]*N+[2]*N+[-1]*N+[-2]*N+[1,2]
        cycles=knot_permutation(word)
        assert len(cycles)==1
        writhe=sum(1 if s>0 else -1 for s in word)
        assert writhe==2
        VA=jones_A(word)
        assert all(e%4==0 for e in VA)
        V={-e//4:c for e,c in VA.items()}
        at_one=sum(V.values())
        at_minus_one=sum(c*(1 if e%2==0 else -1) for e,c in V.items())
        assert at_one==1
        assert sum(e*c for e,c in V.items())==0
        assert at_minus_one==1-N*N
        rows.append({'N':N,'word':word,'components':len(cycles),'writhe':writhe,
                     'V_t':dict(sorted(V.items())),'V_at_1':at_one,
                     'V_prime_at_1':0,'V_at_minus1':at_minus_one,
                     'determinant':abs(at_minus_one),'A_exponents_all_multiples_of_4':True})
    result={
      'conventions':'sigma_i=A I+A^-1 e_i; delta=-A^2-A^-2; V=(-A^3)^(-w)<closure>; t=A^-4',
      'all_N_symbolic_commutator_and_anchor_trace_verified':True,
      'unknot_normalization_controls':controls,
      'checks':rows,
      'finite_field_theorem':(
        'Given finitely many fields F_q of characteristics p, choose even N>=2 '
        'divisible by all p(q^4-1). For every t in each F_q^*, choose A in F_(q^4)^* '
        'with A^-4=t. The quadratic (g-A)(g+A^-3)=0 divides X^N-1 in that '
        'characteristic, so both generator Nth powers are identity. Thus beta_N '
        'is the full specialized TL identity, and V_KN(t)=1. Nevertheless '
        'V_KN(-1)=1-N^2 over Z, so K_N is a nontrivial knot.'),
      'scope':'Finite-field evaluation-function equality, not coefficientwise equality or complex-root equality.'}
    output=Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_N_matrix_identity':True,'checks':[
        {k:r[k] for k in ('N','components','writhe','V_at_1','V_at_minus1','determinant')}
        for r in rows],'output':str(output)}))


if __name__=='__main__':main()
