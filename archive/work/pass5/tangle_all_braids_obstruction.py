"""Exact certificate: no B4 braid can erase Ren core's annular z^2 channel.

The argument is an integral first-jet obstruction modulo five, not a search.
"""
from pathlib import Path
from collections import deque
import json
import tangle_core_stdlib as t
add,mul,shift=t.six.add,t.six.mul,t.six.shift

def zero():return [[{} for _ in range(3)] for _ in range(3)]
def identity():return [[{0:1} if i==j else {} for j in range(3)] for i in range(3)]
def madd(a,b):return [[add(a[i][j],b[i][j]) for j in range(3)] for i in range(3)]
def mmul(a,b):
    out=zero()
    for i in range(3):
        for j in range(3):
            for k in range(3):out[i][j]=add(out[i][j],mul(a[i][k],b[k][j]))
    return out
def mscale(a,p):return [[mul(v,p) for v in row] for row in a]
def trace(a):return add(add(a[0][0],a[1][1]),a[2][2])

paths={t.IDENT:[]};queue=deque([t.IDENT])
while queue:
    j=queue.popleft()
    for i,transitions in enumerate(t.TRANSITIONS,1):
        k,loops=transitions[j]
        if not loops and k not in paths:
            paths[k]=paths[j]+[i];queue.append(k)
assert len(paths)==14

# E'_i=A^-2 e_i. E'_i^2=(x-1)E'_i and E'_i E'_(i+/-1) E'_i=-x E'_i.
E=[]
for i in range(3):
    e=zero();e[i][i]={1:1,0:-1}
    if i:e[i][i-1]={1:-1}
    if i<2:e[i][i+1]={0:1}
    E.append(e)

M=zero()
basis_trace_checks=[]
for j,p in enumerate(t.CORE):
    basis_matrix=identity()
    for i in paths[j]:basis_matrix=mmul(basis_matrix,E[i-1])
    # Undo the rescaling e_i=A^2 E'_i. On each nonidentity basis diagram,
    # the 3D matrix trace equals exactly its annular z^2 coefficient.
    trace_A={}
    for k,c in trace(basis_matrix).items():
        trace_A=add(trace_A,{2*len(paths[j])-4*k:c*(-1 if k%2 else 1)})
    if j==t.IDENT:trace_A=add(trace_A,{0:-3})
    c,e=t.TYPES[j]
    annular_A={0:1} if e==2 else {}
    for _ in range(c):annular_A=mul(annular_A,t.six.DELTA)
    assert trace_A==annular_A,j
    basis_trace_checks.append(j)
    coefficient={}
    for e,c in p.items():
        k=(e+2*len(paths[j])-2)//4
        assert e+2*len(paths[j])-2==4*k
        coefficient=add(coefficient,{-k:c*(-1 if k%2 else 1)})
    M=madd(M,mscale(basis_matrix,coefficient))

M0=[[sum(p.values()) for p in row] for row in M]
M1=[[sum(e*c for e,c in p.items()) for p in row] for row in M]
assert M0==[[-15,0,15],[-25,0,25],[-15,0,15]]
assert M1==[[-33,0,0],[-40,-8,-15],[-15,0,-18]]
assert all(M0[i][j]%5==0 and M1[i][j]%5==2*int(i==j) for i in range(3) for j in range(3))

def braid_matrix(word):
    result=identity()
    for i in word:
        # (I+E')^-1=I-x^-1 E'.
        R=madd(identity(),E[i-1]) if i>0 else madd(identity(),mscale(E[-i-1],{-1:-1}))
        result=mmul(result,R)
    return result

checks=[]
for word in [[],[1,3],[-1,3],[2],[1,2,3],[1,-2,3,2],[3,2,-1,-2,3],[-2,-1,3,-2,1]]:
    exponent=sum(1 if i>0 else -1 for i in word)
    expected={}
    for e,c in t.annular(word)[2].items():
        k=(e-exponent-2)//4
        assert e-exponent-2==4*k
        expected=add(expected,{-k:c*(-1 if k%2 else 1)})
    assert trace(mmul(M,braid_matrix(word)))==expected,word
    checks.append(word)

result={'statement':'For every four-strand braid B, annular closure of Ren core T times B has nonzero z^2 coefficient, hence degree exactly two.',
        'variables':'x=-A^-4; T=A^2 M(x) in the three-dimensional two-through-strand TL4 representation',
        'gauge':'Start with e_i row i diagonal delta and adjacent entries 1. For S=diag(1,A^2,A^4), Eprime_i=A^-2 S^-1 e_i S, and M=A^-2 S^-1 rho(T) S.',
        'M_Laurent_matrix':M,'M_at_1':M0,'M_derivative_at_1':M1,
        'normalized_braid_generators':'I+Eprime_i, where row i of Eprime_i has diagonal x-1, predecessor -x, successor 1',
        'trace_identity_checks':checks,
        'all_14_TL4_basis_trace_checks':basis_trace_checks,
        'proof':[
            'Every normalized braid matrix U(x) lies in GL3(Z[x,x^-1]); U(1) fixes primitive u=(1,0,1) and has determinant 1.',
            'Write r=(1,0,-1), e2=(0,1,0). M(1)=(-15u-25e2)r. Therefore tr(M(1)U(1))=-25 r U(1)e2.',
            'If the channel vanished identically then r U(1)e2=0. On the integral quotient Z3/<u>, using classes of e1,e2, the induced determinant-one matrix therefore has upper-right entry zero.',
            'Its diagonal entries are both +1 or both -1. Since u is fixed, tr U(1) is respectively 3 or -1.',
            'But tr(MU) derivative at 1 is tr(Mprime U+M Uprime), congruent modulo 5 to 2 tr U(1), which is 1 or 3 modulo 5, never zero.',
            'This contradicts identically zero tr(MU). The core has zero four-through coefficient, so its annular z2 coefficient is precisely this matrix trace times the nonzero scalar A^(2+braid exponent sum).'
        ]}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='M_Laurent_matrix'},indent=2))
