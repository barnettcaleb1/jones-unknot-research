# (a) deframed osp(1|2) insertions reproduce w(D) = W_m(J) (upstairs signs +1):
#     chord -> -2 eps^q (2 Omega) - 4 eps Id  (eps = +1, eps^q = (-1)^tau),  on-axis site -> (g+3) - 4g,  twist -> g.
# (b) infinitesimal braid relation [t12, t13 + t23] = 0 for t_ij = P_ij - K_ij in the Brauer algebra B_3(delta), delta symbolic.
import itertools, sympy as sp, sys
sys.argv=['x']
import osp12 as O, abstract as ab
def eval_deframed(D):
    pos={}
    for p,tk in enumerate(D):
        if tk[0]=='E': pos.setdefault(tk[1],[]).append(p)
    _,tau=ab.labels(D); chords=sorted(pos); tot=0
    for kinds in itertools.product(('Om','Id'),repeat=len(chords)):
        omc=[c for c,k in zip(chords,kinds) if k=='Om']
        coef=1
        for c,k in zip(chords,kinds): coef*=(-2*(-1)**tau[c]*2 if k=='Om' else -4)
        for alphas in itertools.product(range(len(O.bas)),repeat=len(omc)):
            elems=[]
            for c,a in zip(omc,alphas):
                p1,p2=pos[c]; elems.append((p1,O.dual[a][0]/O.lamv/2,O.dual[a][1])); elems.append((p2,O.bas[a][0],O.bas[a][1]))
            sgn=1
            for i in range(len(elems)):
                for j in range(i+1,len(elems)):
                    if elems[i][0]>elems[j][0] and elems[i][2]*elems[j][2]: sgn=-sgn
            op_at={e[0]:e[1] for e in elems}
            M=sp.eye(3)
            for p,tk in enumerate(D):
                if tk[0]=='E': X=op_at.get(p,sp.eye(3))
                elif tk[0]=='O': X=O.g+3*sp.eye(3)-4*O.g
                else: X=O.g
                M=M*X
            tot+=coef*sgn*M[0,0]
    return sp.nsimplify(tot)
res=[0,0]
for (no,nn) in [(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2)]:
    toks=[('E',i) for i in range(no) for _ in (0,1)]+[('O',j) for j in range(nn)]; seen=set()
    for perm in set(itertools.permutations(toks)):
        for parity in itertools.product([0,1],repeat=len(perm)-1):
            D=[perm[0]]
            for gb,tk in zip(parity,perm[1:]):
                if gb: D.append(('T',))
                D.append(tk)
            key=ab.shape(D)
            if key in seen: continue
            seen.add(key)
            res[0 if eval_deframed(D)==ab.w(D) else 1]+=1
print('(a) deframed osp(1|2) insertions == w(D): match, mismatch =',res)
# (b) Brauer algebra B_3(delta)
d=sp.symbols('delta')
def comp(D1,D2,n=3):
    # D: tuple matching on 2n points (top 0..n-1, bottom n..2n-1); D1*D2 = D1 on top of D2
    adj={}
    def link(u,v): adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    for p in range(2*n):
        if p<D1[p]: link(('a',p),('a',D1[p]))
        if p<D2[p]: link(('b',p),('b',D2[p]))
    for i in range(n): link(('a',n+i),('b',i))
    ext=[('a',i) for i in range(n)]+[('b',n+i) for i in range(n)]; idx={e:k for k,e in enumerate(ext)}
    res=[None]*(2*n); seen=set()
    for e in ext:
        if e in seen: continue
        prev=None; cur=e; seen.add(cur)
        while True:
            nb=[v for v in adj[cur] if v!=prev]
            if not nb: break
            prev,cur=cur,nb[0]; seen.add(cur)
            if cur in idx: break
        res[idx[e]]=idx[cur]; res[idx[cur]]=idx[e]
    rest=set(adj)-seen; loops=0
    while rest:
        st=[rest.pop()]; loops+=1
        while st:
            u=st.pop()
            for v in adj[u]:
                if v in rest: rest.discard(v); st.append(v)
    return tuple(res),loops
def mulB(X,Y):
    out={}
    for D1,c1 in X.items():
        for D2,c2 in Y.items():
            D,l=comp(D1,D2); out[D]=sp.expand(out.get(D,0)+c1*c2*d**l)
    return out
def addB(X,Y,s=1):
    out=dict(X)
    for D,c in Y.items(): out[D]=sp.expand(out.get(D,0)+s*c)
    return {D:c for D,c in out.items() if c!=0}
n=3
def perm(i,j):
    m=[None]*6
    for k in range(3):
        kk={i:j,j:i}.get(k,k); m[k]=3+kk; m[3+kk]=k
    return {tuple(m):1}
def cupcap(i,j):
    m=[None]*6; m[i]=j; m[j]=i; m[3+i]=3+j; m[3+j]=3+i
    k=({0,1,2}-{i,j}).pop(); m[k]=3+k; m[3+k]=k
    return {tuple(m):1}
t={}
for (i,j) in [(0,1),(0,2),(1,2)]: t[(i,j)]=addB(perm(i,j),cupcap(i,j),-1)
S=addB(t[(0,2)],t[(1,2)])
comm=addB(mulB(t[(0,1)],S),mulB(S,t[(0,1)]),-1)
print('(b) [t12, t13 + t23] in B_3(delta) == 0 :', all(sp.simplify(c)==0 for c in comm.values()))
