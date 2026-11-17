"""Independent algebra audit of the arbitrary B4 Ren-core obstruction.

Input raw A-variable TL4 core matrix independently computed by braid_core_matrix;
this script independently gauges it, derives both jets, and verifies representation
and lattice identities using integer Laurent arithmetic only.
"""
from pathlib import Path
from collections import defaultdict
import json,itertools
HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'braid_core_matrix.json').read_text())['matrix']
def add(*ps):
    d=defaultdict(int)
    for p in ps:
        for k,v in p.items():d[k]+=v
    return {k:v for k,v in d.items() if v}
def mul(p,q):
    d=defaultdict(int)
    for k,v in p.items():
        for l,w in q.items():d[k+l]+=v*w
    return {k:v for k,v in d.items() if v}
def smat(p,M):return [[mul(p,x) for x in row] for row in M]
def plus(M,N):return [[add(M[i][j],N[i][j]) for j in range(3)] for i in range(3)]
def mm(M,N):return [[add(*(mul(M[i][k],N[k][j]) for k in range(3))) for j in range(3)] for i in range(3)]
def det(M):
    out={}
    for p in itertools.permutations(range(3)):
        s=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        out=add(out,mul({0:s},mul(mul(M[0][p[0]],M[1][p[1]]),M[2][p[2]])))
    return out
I=[[{0:1} if i==j else {} for j in range(3)] for i in range(3)]
# Gauging by S=diag(1,A^2,A^4), then dividing by A^2.
M=[]
for i in range(3):
    row=[]
    for j in range(3):
        out={}
        for e,c in raw[3*i+j].items():
            aexponent=int(e)-2-2*i+2*j
            assert aexponent%4==0
            k=aexponent//4
            out=add(out,{-k:c*(-1 if k%2 else 1)})
        row.append(out)
    M.append(row)
M0=[[sum(p.values()) for p in row] for row in M]
M1=[[sum(k*v for k,v in p.items()) for p in row] for row in M]
assert M0==[[-15,0,15],[-25,0,25],[-15,0,15]]
assert M1==[[-33,0,0],[-40,-8,-15],[-15,0,-18]]
assert all(M0[i][j]%5==0 and M1[i][j]%5==2*(i==j) for i in range(3) for j in range(3))
E=[]
for i in range(3):
    a=[[{} for j in range(3)] for k in range(3)]
    a[i][i]={1:1,0:-1}
    if i:a[i][i-1]={1:-1}
    if i<2:a[i][i+1]={0:1}
    E.append(a)
R=[plus(I,e) for e in E]
for i,e in enumerate(E):
    assert mm(e,e)==smat({1:1,0:-1},e)
    assert mm(R[i],plus(I,smat({-1:-1},e)))==I
    assert det(R[i])=={1:1}
    for j in range(3):
        if abs(i-j)==1:
            assert mm(mm(e,E[j]),e)==smat({1:-1},e)
            assert mm(mm(R[i],R[j]),R[i])==mm(mm(R[j],R[i]),R[j])
        if abs(i-j)>1:assert mm(e,E[j])==mm(E[j],e)
u=[1,0,1];r=[1,0,-1];e2=[0,1,0]
R0=[[[sum(p.values()) for p in row] for row in a] for a in R]
for a in R0:assert [sum(a[i][j]*u[j] for j in range(3)) for i in range(3)]==u
basis=[[{0:v} if v else {} for v in row] for row in [[1,1,0],[0,0,1],[1,0,0]]]
assert det(basis)=={0:1}
assert M0==[[(-15*u[i]-25*e2[i])*r[j] for j in range(3)] for i in range(3)]
# Actual induced quotient generators in the basis e1,e2 modulo u.
Q=[]
for a in R0:
    q=[[a[0][0]-a[2][0],a[0][1]-a[2][1]],[a[1][0],a[1][1]]]
    assert q[0][0]*q[1][1]-q[0][1]*q[1][0]==1
    Q.append(q)
out={'M_at_1':M0,'M_derivative_at_1':M1,'normalized_generators_at_1':R0,'quotient_generators':Q,'basis_u_e1_e2_determinant':1,'representation_relations_verified':True,'raw_matrix_gauge_independently_verified':True,'obstruction':'If tr(MU)(1)=0, tr(U(1)) is 3 or -1; then derivative of tr(MU) at 1 is 1 or 3 modulo 5. Hence every such Laurent trace is nonzero and has vanishing order at most one at x=1.'}
(HERE/'homology_all_braids_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
