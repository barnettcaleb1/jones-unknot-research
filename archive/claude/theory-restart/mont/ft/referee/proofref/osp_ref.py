# Referee: independent osp(1|2) construction; Omega vs (P-K)/2; Koszul-signed Wilson-line weight system vs Brauer state sum.
import sys, itertools
import sympy as sp
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
import ss
from abstract_ref import shapes, realize
par=[0,1,1]                                    # v0 even, v1 v2 odd
B=sp.Matrix([[1,0,0],[0,0,1],[0,-1,0]])        # even supersymmetric form: symmetric on V0, symplectic on V1
def parity_of(X):
    ev=all(X[i,j]==0 for i in range(3) for j in range(3) if par[i]!=par[j])
    od=all(X[i,j]==0 for i in range(3) for j in range(3) if par[i]==par[j])
    return 0 if ev else (1 if od else None)
# osp condition: B(Xu,w) + (-1)^{|X||u|} B(u,Xw) = 0 for homogeneous basis vectors u,w
syms=sp.symbols('m0:9'); basis=[]
for p in (0,1):
    X=sp.Matrix(3,3,lambda i,j: syms[3*i+j] if (par[i]+par[j])%2==p else 0)
    eqs=[]
    for u in range(3):
        for w in range(3):
            eu=sp.zeros(3,1); eu[u]=1; ew=sp.zeros(3,1); ew[w]=1
            eqs.append(((X*eu).T*B*ew)[0] + (-1)**(p*par[u])*(eu.T*B*(X*ew))[0])
    sol=sp.linsolve(eqs,[s for s in syms if X.has(s)])
    (vec,)=sol
    free=sorted(set().union(*[sp.sympify(v).free_symbols for v in vec]),key=str)
    for f in free:
        Y=X.subs({s:v for s,v in zip([s for s in syms if X.has(s)],vec)}).subs({g:(1 if g==f else 0) for g in free})
        basis.append((Y,p))
print('dim osp(1|2) =',sum(1 for _,p in basis if p==0),'|',sum(1 for _,p in basis if p==1))
def str_(X): return sum(((-1)**par[i])*X[i,i] for i in range(3))
n=len(basis); G=sp.Matrix(n,n,lambda a,b: str_(basis[a][0]*basis[b][0])); Gi=G.inv()
dual=[(sum((Gi[c,b]*basis[c][0] for c in range(n)),sp.zeros(3,3)),basis[b][1]) for b in range(n)]
assert all(str_(basis[a][0]*dual[b][0])==(1 if a==b else 0) for a in range(n) for b in range(n))
# operators on V(x)V with Koszul signs: (X(x)Y)(e_u(x)e_w) = (-1)^{|Y||u|} X e_u (x) Y e_w
def kron_super(X,px,Y,py):
    M=sp.zeros(9,9)
    for u in range(3):
        for w in range(3):
            for u2 in range(3):
                for w2 in range(3):
                    M[3*u2+w2,3*u+w]+=((-1)**(py*par[u]))*X[u2,u]*Y[w2,w]
    return M
Om=sp.zeros(9,9)
for (X,p),(Y,q) in zip(basis,dual): Om+=((-1)**p)*kron_super(X,p,Y,q)   # invariant convention (odd sign -1)
P=sp.zeros(9,9)
for u in range(3):
    for w in range(3): P[3*w+u,3*u+w]=(-1)**(par[u]*par[w])
D=2*Om-P
print('rank(2 Omega - P) =',D.rank(),'  (2Omega-P)^2 == (2Omega-P):',sp.simplify(D*D-D)==sp.zeros(9,9),
      '  (so 2 Omega = P - K with K rank 1, K^2 = -K = sdim*K)')
g=sp.diag(1,-1,-1); print('str 1 =',str_(sp.eye(3)),' str g =',str_(g))
# Wilson-line word: <v0| prod_{positions} op |v0> with Koszul sign of reordering chord tensors into position order
def word_value(slots, deframe=False):
    pos={}
    for p,tk in enumerate(slots):
        if tk.startswith('c'): pos.setdefault(tk,[]).append(p)
    chords=sorted(pos); tot=0
    for idx in itertools.product(range(n),repeat=len(chords)):
        items=[]   # (position, matrix, parity, chord-order index)
        k=0
        for c,a in zip(chords,idx):
            p1,p2=pos[c]
            items.append((p1,basis[a][0],basis[a][1],k)); items.append((p2,dual[a][0],dual[a][1],k+1)); k+=2
        sign=1
        for c,a in zip(chords,idx): sign*=2*(-1)**basis[a][1]      # 2*Omega, Omega = sum (-1)^|a| x^a (x) x_a
        for i in range(len(items)):
            for j in range(len(items)):
                if items[i][3]<items[j][3] and items[i][0]>items[j][0]: sign*=(-1)**(items[i][2]*items[j][2])
        ops={it[0]:it[1] for it in items}
        M=sp.eye(3)
        for p,tk in enumerate(slots):
            if tk.startswith('c'): M=M*ops[p]
            elif tk=='g': M=M*g
            elif tk=='o': M=M*((g+3*sp.eye(3)) if not deframe else (3*(sp.eye(3)-g)))
        tot+=sign*M[0,0]
    return tot
def compare(m):
    ok=[0,0]; okJ=[0,0]; bad=[]
    for nc in range(m,-1,-1):
        for seq in shapes(nc,m-nc):
            for gpat in itertools.product([0,1],repeat=len(seq)-1):
                slots=realize(seq,gpat)
                L=len(slots); axis=set(p for p,tk in enumerate(slots) if tk in ('o','g')); recs=[]; pos={}
                for p,tk in enumerate(slots):
                    if tk.startswith('c'): pos.setdefault(tk,[]).append(p)
                for c in sorted(pos):
                    a,b=pos[c]; tau=sum(1 for p in axis if a<p<b)%2
                    recs.append(dict(kind='off',a=a,b=b,kap=1,pi=1,tau=tau))       # quotient sign +1
                for p,tk in enumerate(slots):
                    if tk=='o': recs.append(dict(kind='on',c=p,kap=-1))            # eps_j=+1
                Wh=ss.W_hat(L,axis,recs,list(range(len(recs))))
                wv=word_value(slots)
                good=(Wh==(-2)**nc*wv); ok[0 if good else 1]+=1
                if not good: bad.append((slots,Wh,wv))
                # deframed version: chord -> -2 eps^q (2 Omega + 2(-1)^tau) ; on-axis site -> eps_j * 6 P_odd = 3(1-g)
                WJ,_=ss.W_J(L,axis,recs)
                # expand chords (2Omega + 2(-1)^tau): sum over subsets of chords replaced by scalar 2(-1)^tau
                tot=0
                chords=sorted(pos)
                for T in itertools.product([0,1],repeat=len(chords)):
                    sl=list(slots); coef=1
                    for c,t,r in zip(chords,T,recs):
                        if t:
                            coef*=2*(-1)**r['tau']
                            sl=['g' if (x==c and False) else x for x in sl]
                    # remove replaced chords' endpoints (identity insertion)
                    rem=set(c for c,t in zip(chords,T) if t)
                    sl2=[x for x in sl if x not in rem]
                    tot+=coef*word_value(sl2,deframe=True)
                goodJ=(WJ==(-2)**nc*tot); okJ[0 if goodJ else 1]+=1
    print('order',m,' W(Jhat) == prod(-2)*<v0|WORD|v0>:',ok,'   W(J) == deframed word:',okJ, bad[:2])
for m in (1,2,3): compare(m)
if len(sys.argv)>1: compare(4)
