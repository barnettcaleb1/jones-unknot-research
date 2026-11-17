"""Fixed 9x9 osp(1|2) symbol comparison; no diagram search."""
from pathlib import Path
import contextlib, io, json, runpy
import sympy as S
with contextlib.redirect_stdout(io.StringIO()):
    ft=runpy.run_path(str(Path(__file__).with_name('ft_local.py')))
q=ft['q']; C=ft['C22']; P=ft['superflip']; I=S.eye(3)
Pi=S.diag(-1,1,-1)
co=ft['co'].subs(q,S.I)
ev=ft['ev'].subs(q,S.I)
K=co*ev
H=S.diag(1,0,-1)
Ep=S.zeros(3);Ep[0,2]=1
Em=S.zeros(3);Em[2,0]=1
Qp=S.zeros(3);Qp[0,1]=1;Qp[1,2]=-1
Qm=S.zeros(3);Qm[1,0]=1;Qm[2,1]=1
basis=[H,Ep,Em,Qp,Qm]; parity=[0,0,0,1,1]
G=S.Matrix(3,3,list(ev))
checks={}
def check(name,value):
    value=bool(value);checks[name]=value;assert value,name
    print(name+': PASS')
def super_tensor(A,B,pB): return S.kronecker_product(A*(Pi if pB else I),B)
def st(A): return S.trace(Pi*A)
def cop(X,p):return S.kronecker_product(X,I)+S.kronecker_product(Pi if p else I,X)
for idx,(X,p) in enumerate(zip(basis,parity)):
    check(f'generator {idx} preserves orthosymplectic form',X.T*G+(Pi if p else I)*G*X==S.zeros(3))
check('odd anticommutator is H',Qp*Qm+Qm*Qp==H)
check('positive odd square is -E',Qp*Qp==-Ep)
check('negative odd square is F',Qm*Qm==Em)
# Bilinear form B(X,Y)=str(XY)/2, with right-dual basis B(X_i,X^j)=delta_i^j.
dual=[-H,-2*Em,-2*Ep,-Qm,Qp]
check('displayed dual is dual for half supertrace',S.Matrix([[st(X*Y)/2 for Y in dual] for X in basis])==S.eye(5))
Omega=sum(((-1)**p*super_tensor(X,Y,p) for X,Y,p in zip(basis,dual,parity)),S.zeros(9))
check('Casimir equals superflip minus contraction',Omega==P-K)
check('contraction square is -contraction',K*K==-K)
check('superflip fixes contraction',P*K==K and K*P==K)
for idx,(X,p) in enumerate(zip(basis,parity)):
    check(f'Casimir invariant under generator {idx}',Omega*cop(X,p)==cop(X,p)*Omega)
check('raw crossing symbol is 2K-2I',C==2*K-2*S.eye(9))
check('transported chord symbol is -2Casimir',P*C==-2*Omega)
check('raw symbol Casimir plus allowed I,P corrections',C==-2*Omega+2*P-2*S.eye(9))
check('raw crossing symbol commutes with superflip',P*C==C*P)
result={'all_passed':all(checks.values()),'checks':checks,
 'conventions':{'basis':'w0 odd,w1 even,w2 odd','form':'B(X,Y)=str_V(XY)/2','chord':'superflip times crossing difference symbol'},
 'C22':str(C),'Omega':str(Omega),'contraction':str(K),
 'identity':'C22=2K-2I=-2Omega+2P-2I; P C22=-2Omega; Omega=P-K'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'ALL {len(checks)} CHECKS PASSED')
