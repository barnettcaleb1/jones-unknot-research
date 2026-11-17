# Honest osp(1|2) computation.  V = C^{1|2}: v0 even, v1, v2 odd; even supersymmetric form B (B(v0,v0)=1, B(v1,v2)=1=-B(v2,v1)).
# (1) find osp(1|2) (dim 3|2), the str-form, the Casimir Omega on V (x) V with Koszul signs; check Omega = lam (P + mu K).
# (2) single-strand weight system: <v0| ordered product along k |v0>, chord -> -2 Omega (two insertions, Koszul signs),
#     on-axis site -> (g + 3), non-site twist -> g = (-1)^F.  Compare with the Brauer state sum (abstract.W_hat, eps^q = +1).
import itertools
from fractions import Fraction as Fr
import sympy as sp
par=[0,1,1]
B=sp.Matrix([[1,0,0],[0,0,1],[0,-1,0]])
def unit(i,j):
    M=sp.zeros(3,3); M[i,j]=1; return M
# solve osp condition for even and odd parts separately
def osp_basis():
    basis=[]
    for p in (0,1):
        idx=[(i,j) for i in range(3) for j in range(3) if (par[i]+par[j])%2==p]
        cs=sp.symbols('c0:%d'%len(idx)); X=sum((c*unit(i,j) for c,(i,j) in zip(cs,idx)),sp.zeros(3,3))
        eqs=[]
        for u in range(3):
            for w in range(3):
                # B(Xu,w) + (-1)^{|X||u|} B(u,Xw) = 0 ;  B(a,b) = a^T B b for coordinate vectors
                eu=sp.zeros(3,1); eu[u]=1; ew=sp.zeros(3,1); ew[w]=1
                eqs.append(((X*eu).T*B*ew)[0]+(-1)**(p*par[u])*(eu.T*B*(X*ew))[0])
        sol=sp.linsolve(eqs,cs)
        (gen,)=sol
        free=sorted(set().union(*[sp.Matrix([g]).free_symbols for g in gen]),key=str)
        for f in free:
            sub={g:(1 if g==f else 0) for g in free}
            basis.append((X.subs(dict(zip(cs,[g.subs(sub) for g in gen]))),p))
    return basis
bas=osp_basis()
print('osp(1|2) dims (even|odd):',sum(1 for _,p in bas if p==0),'|',sum(1 for _,p in bas if p==1))
def strace(M): return sum((-1)**par[i]*M[i,i] for i in range(3))
G=sp.Matrix(len(bas),len(bas),lambda a,b: strace(bas[a][0]*bas[b][0]))
Gi=G.inv()
# dual basis: x^b = sum_a Gi[a,b] x_a  so that str(x_c x^b) = sum_a Gi[a,b] G[c,a] = delta_cb
dual=[(sum((Gi[a,b]*bas[a][0] for a in range(len(bas))),sp.zeros(3,3)),bas[b][1]) for b in range(len(bas))]
# operators on V (x) V: index (i,j) -> 3*i+j ; Koszul action (X (x) Y)(u (x) w) = (-1)^{|Y||u|} Xu (x) Yw
def tens(X,pX,Y,pY):
    M=sp.zeros(9,9)
    for u in range(3):
        for w in range(3):
            s=(-1)**(pY*par[u])
            for i in range(3):
                for j in range(3):
                    M[3*i+j,3*u+w]+=s*X[i,u]*Y[j,w]
    return M
Om=sum((tens(dual[a][0],dual[a][1],bas[a][0],bas[a][1]) for a in range(len(bas))),sp.zeros(9,9))   # Omega = sum x^a (x) x_a
P=sp.zeros(9,9)
for u in range(3):
    for w in range(3): P[3*w+u,3*u+w]=(-1)**(par[u]*par[w])
# invariant vector c in V(x)V (killed by X(x)1 + 1(x)X) and covector b (b o (X(x)1+1(x)X) = 0)
D=[tens(X,p,sp.eye(3),0)+tens(sp.eye(3),0,X,p) for X,p in bas]
cs=sp.symbols('z0:9'); cv=sp.Matrix(cs)
sol=sp.linsolve([e for Dm in D for e in (Dm*cv)],cs); (cg,)=sol; cvec=sp.Matrix(cg)
fs_=sorted(cvec.free_symbols,key=str); cvec=cvec.subs({fs_[0]:1})
sol=sp.linsolve([e for Dm in D for e in (cv.T*Dm)],cs); (bg,)=sol; bvec=sp.Matrix(bg)
fs_=sorted(bvec.free_symbols,key=str); bvec=bvec.subs({fs_[0]:1})
K=cvec*bvec.T
lamK=(K*K)[0,0]/K[0,0] if K[0,0]!=0 else None
K=K*(-1/( (bvec.T*cvec)[0] ))          # normalise so that K^2 = -K  (loop value sdim = -1)
print('K^2 == -K :', sp.simplify(K*K+K)==sp.zeros(9,9))
lam,mu=sp.symbols('lam mu')
eqs=list(Om-lam*(P+mu*K)); s=sp.solve(eqs,[lam,mu],dict=True)
print('Omega = lam (P + mu K) solved by:',s)
lamv=s[0][lam]
# (2) single strand weight system.  normalise chord operator Omt = Omega/lam  (= P - K)
g=sp.diag(1,-1,-1)
def evaluate(D):
    """D token list (abstract.py format). returns <v0| prod |v0> with chord -> -2*Omt, site -> (g+3), twist -> g."""
    pos={}
    for p,tk in enumerate(D):
        if tk[0]=='E': pos.setdefault(tk[1],[]).append(p)
    chords=sorted(pos)
    tot=0
    for alphas in itertools.product(range(len(bas)),repeat=len(chords)):
        # elements in canonical tensor order: for each chord (x_alpha at first endpoint, x^alpha at second)
        elems=[]   # (position, matrix, parity)
        for c,a in zip(chords,alphas):
            p1,p2=pos[c]
            elems.append((p1,dual[a][0]/lamv,dual[a][1])); elems.append((p2,bas[a][0],bas[a][1]))
        # Koszul sign of sorting by position
        sgn=1
        for i in range(len(elems)):
            for j in range(i+1,len(elems)):
                if elems[i][0]>elems[j][0] and elems[i][2]*elems[j][2]: sgn=-sgn
        op_at={e[0]:e[1] for e in elems}
        M=sp.eye(3)
        for p,tk in enumerate(D):          # U(g)-word read along k, first position LEFTMOST (Koszul-consistent with Omega = sum x^a (x) x_a)
            if tk[0]=='E': X=op_at[p]
            elif tk[0]=='O': X=g+3*sp.eye(3)
            else: X=g
            M=M*X
        tot+=sgn*M[0,0]
    return sp.nsimplify(tot*(-2)**len(chords))
if __name__=='__main__':
    import abstract as ab, random
    def qsign(D):
        _,tau=ab.labels(D); s=1
        for v in tau.values(): s*=(-1)**v
        return s
    res=[0,0]; ex=[]
    for (no,nn) in [(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2)]:
        toks=[('E',i) for i in range(no) for _ in (0,1)]+[('O',j) for j in range(nn)]
        seen=set()
        for perm in set(itertools.permutations(toks)):
            for parity in itertools.product([0,1],repeat=len(perm)-1):
                Dd=[perm[0]]
                for gbit,tk in zip(parity,perm[1:]):
                    if gbit: Dd.append(('T',))
                    Dd.append(tk)
                key=ab.shape(Dd)
                if key in seen: continue
                seen.add(key)
                offs=sorted(set(t[1] for t in Dd if t[0]=='E')); ons=sorted(set(t[1] for t in Dd if t[0]=='O'))
                brauer=qsign(Dd)*ab.W_hat(Dd,offs,ons)
                lie=evaluate(Dd)
                if brauer==lie: res[0]+=1
                else: res[1]+=1; ex.append((Dd,brauer,lie))
    print('osp(1|2) Lie superalgebra weight system == Brauer state sum (W(Jhat), eps^q=+1): match, mismatch =',res)
    for e in ex[:5]: print('  ',e)
