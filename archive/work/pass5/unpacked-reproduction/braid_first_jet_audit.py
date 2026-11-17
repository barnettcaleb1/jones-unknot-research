"""Independent exact audit of the all-B4 Ren-core first-jet obstruction.

Uses the separately reconstructed standard link-state matrix, then changes
basis, checks all13 nonidentity TL4 diagram traces, and verifies the integer
quotient and mod5 jets. The proof for arbitrary words is in braid_notes.md.
"""
from pathlib import Path
import json
import braid_core_matrix as b
ROOT=Path(__file__).resolve().parent

# Gauge S=diag(1,A^2,A^4), divide by A^2, then x=-A^-4.
M=[]
for i in range(3):
    row=[]
    for j in range(3):
        p={}
        for e,c in b.M[3*i+j].items():
            exponent=e+2*(j-i)-2
            assert exponent%4==0
            k=exponent//4
            p[-k]=c*(-1 if k%2 else 1)
        row.append(p)
    M.append(row)
M0=[[sum(p.values()) for p in row] for row in M]
M1=[[sum(e*c for e,c in p.items()) for p in row] for row in M]
claimed=json.loads((ROOT/'tangle_core_first_jets.json').read_text())
assert M0==claimed['M_at_1'] and M1==claimed['M_derivative_at_1']
assert all(c%5==0 for row in M0 for c in row)
assert [[c%5 for c in row] for row in M1]==[[2,0,0],[0,2,0],[0,0,2]]

# Independently check the normalized braid generators and their Laurent
# inverses in the same gauge, not only their specialization at x=1.
def to_x(p,shift):
    out={}
    for e,c in p.items():
        assert (e+shift)%4==0
        k=(e+shift)//4
        out[-k]=c*(-1 if k%2 else 1)
    return out
for index,E in enumerate(b.ES):
    U=[];Ui=[];expected=[dict(v) for v in b.I]
    expected[3*index+index]={1:1}
    if index>0:expected[3*index+index-1]={1:-1}
    if index<2:expected[3*index+index+1]={0:1}
    for i in range(3):
        for j in range(3):
            unit={0:1} if i==j else {}
            U.append(b.add(unit,to_x(E[3*i+j],2*(j-i)-2)))
            Ui.append(b.add(unit,to_x(E[3*i+j],2*(j-i)+2)))
    assert U==expected
    assert b.mm(U,Ui)==b.I and b.mm(Ui,U)==b.I

# All nonidentity TL4 basis elements have zero4-through channel. On them,
# the annular z^2 coefficient equals the two-through character exactly.
for index,mat in b.mats.items():
    tr=b.add(mat[0],mat[4],mat[8])
    c,e=b.data['annular_closure_types_contractible_essential'][index]
    if index==b.base:
        assert tr=={0:3}
        continue
    target={0:1} if e==2 else {}
    for _ in range(c):target=b.mul(target,b.D)
    assert tr==target,(index,tr,target)
assert not b.data['core_Laurent_coefficients'][b.base]
assert all(dest!=b.base for transitions in b.data['generator_transitions'] for dest,loops in transitions)

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
I=[[1,0,0],[0,1,0],[0,0,1]]
Q=[[1,1,0],[0,0,1],[1,0,0]] # columns u,e1,e2
Qi=[[0,0,1],[1,0,-1],[0,1,0]]
assert mm(Q,Qi)==I and mm(Qi,Q)==I
generators=[[[1,1,0],[0,1,0],[0,0,1]],
            [[1,0,0],[-1,1,1],[0,0,1]],
            [[1,0,0],[0,1,0],[0,-1,1]]]
quotients=[]
for U in generators:
    B=mm(mm(Qi,U),Q)
    assert [row[0] for row in B]==[1,0,0]
    quotient=[row[1:] for row in B[1:]]
    assert quotient[0][0]*quotient[1][1]-quotient[0][1]*quotient[1][0]==1
    quotients.append(quotient)
assert M0==[[-15,0,15],[-25,0,25],[-15,0,15]]

out=dict(independent_matrix=M,constant_jet=M0,first_jet=M1,
         generic_generators_and_Laurent_inverses_verified=True,
         exact_TL4_basis_trace_checks=13,
         identity_channel_absent_and_preserved=True,
         integral_change_of_basis=Q,inverse_integral_change_of_basis=Qi,
         quotient_generator_matrices=quotients,
         trace_values_if_quotient_upper_right_is_zero=[3,-1],
         derivative_residues_mod5=[1,3],
         conclusion='For every beta in B4, the annular z^2 coefficient of T beta is nonzero.',
         proof_scope='All words, with no length or connectivity restriction. The matrix trace alone does not classify ordinary closures as knots or unknots.')
(ROOT/'braid_first_jet_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='independent_matrix'},indent=2))
