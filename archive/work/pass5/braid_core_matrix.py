"""Exact two-through TL4 matrix for the Ren core, including its determinant."""
from pathlib import Path
from collections import defaultdict,deque
import json,itertools
ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'tangle_four_strand.json').read_text())
def add(*ps):
    r=defaultdict(int)
    for p in ps:
        for e,c in p.items():r[e]+=c
    return {e:c for e,c in r.items() if c}
def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def mul(a,b):
    r=defaultdict(int)
    for e,c in a.items():
        for f,d in b.items():r[e+f]+=c*d
    return {e:c for e,c in r.items() if c}
def mm(a,b):return [add(*(mul(a[3*i+k],b[3*k+j]) for k in range(3))) for i in range(3) for j in range(3)]
I=[{0:int(i==j)} if i==j else {} for i in range(3) for j in range(3)]
D={2:-1,-2:-1}
ES=[[D,{0:1},{},{},{},{},{},{},{}],
    [{},{},{},{0:1},D,{0:1},{},{},{}],
    [{},{},{},{},{},{},{},{0:1},D]]
base=data['identity_index'];trans=data['generator_transitions']
mats={base:I};todo=deque([base])
while todo:
    b=todo.popleft()
    for i in range(3):
        dest,lp=trans[i][b]
        if not lp and dest not in mats:mats[dest]=mm(mats[b],ES[i]);todo.append(dest)
assert len(mats)==14
M=[{} for _ in range(9)]
for b,p in enumerate(data['core_Laurent_coefficients']):
    p={int(e):c for e,c in p.items()}
    M=[add(a,mul(p,v)) for a,v in zip(M,mats[b])]
det={}
for perm in itertools.permutations(range(3)):
    sg=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    det=add(det,scale(mul(mul(M[perm[0]],M[3+perm[1]]),M[6+perm[2]]),sg))
assert det

def divide(a,b):
    out={};r=dict(a)
    while r and max(r)>=max(b):
        e=max(r)-max(b);c=r[max(r)]//b[max(b)]
        assert c*b[max(b)]==r[max(r)]
        out[e]=c;r=add(r,{f+e:-c*d for f,d in b.items()})
    return out,r
def factors(p):
    lo=min(p);p={e-lo:c for e,c in p.items()}
    assert all(e%4==0 for e in p)
    p={e//4:c for e,c in p.items()};fac={}
    for name,f in [('Phi1',{1:1,0:-1}),('Phi2',{1:1,0:1}),('Phi3',{2:1,1:1,0:1}),('Phi4',{2:1,0:1}),('Phi6',{2:1,1:-1,0:1})]:
        n=0
        while True:
            q,r=divide(p,f)
            if r:break
            n+=1;p=q
        if n:fac[name]=n
    return dict(A_monomial=lo,factors_in_A4=fac,remainder_in_A4=p)
def product(*ps):
    r={0:1}
    for p in ps:r=mul(r,p)
    return r
P1={4:1,0:-1};P2={4:1,0:1};P4={8:1,0:1};P6={8:1,4:-1,0:1}
lambda_plus=product({-18:1},P1,P1,P2,P4,P4,P6)
lambda_minus=product({-6:-1},P2,P6)
lambda_zero=product({-10:1},P1,P1,P2,P4)
assert lambda_zero==M[4]
def subtract_scalar(lam):return [add(p,scale(lam,-1) if i in (0,4,8) else {}) for i,p in enumerate(M)]
assert not any(mm(mm(subtract_scalar(lambda_plus),subtract_scalar(lambda_minus)),subtract_scalar(lambda_zero)))
assert product(lambda_plus,lambda_minus,lambda_zero)==det
# At a primitive 24th root A the specialization really is e_2, over Q(A),
# not merely the coincidental finite-field equality observed in the search.
def reduce24(p):
    r=defaultdict(int)
    for e,c in p.items():r[e%24]+=c
    return divide({e:c for e,c in r.items() if c},P6)[1]
assert all(not reduce24(add(p,scale(e,-1))) for p,e in zip(M,ES[1]))
out=dict(matrix=M,determinant=det,determinant_factorization=factors(det),
         middle_eigenvalue=M[4],middle_eigenvalue_factorization=factors(M[4]),
         eigenvalues=[lambda_zero,lambda_plus,lambda_minus],
         cubic_annihilating_identity_verified=True,
         specialization_at_primitive_24th_root_equals_e2=True)
(ROOT/'braid_core_matrix.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':print(json.dumps(out,indent=2))
