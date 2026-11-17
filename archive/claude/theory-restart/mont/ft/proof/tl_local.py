# Exact check of the two local identities used in the proof of THEOREM FT, in the plain Temperley-Lieb algebra
# (Kauffman bracket conventions of tools/kauffman.py: crossing 'x' = A*vertical + A^-1*cupcap).
#  (L1) colour-2 crossing:  R - R^-1 = (A^4 - A^-4) (Id - E')   in (f2 x f2) TL_4 (f2 x f2)
#  (L2) full twist of colour 1 (strand 1) around colour 2 (strands 2,3):  F - F^-1 = (1+t)[ t^-1 F - t^-2 (1-t+t^2) Id ]
#       for the twist built from 'x' crossings (t = A^-4), and the mirror statement for 'y' crossings.
import sympy as sp, itertools
A=sp.symbols('A'); d=-A**2-A**-2
def compose(D1,D2,n):
    # D: tuple 'match' on points 0..2n-1: top i = i, bottom i = n+i. product D1*D2 = D1 on top of D2 (D1's bottom glued to D2's top)
    # build graph on: D1 points (label ('a',p)), D2 points ('b',p); glue a-bottom(n+i) with b-top(i)
    adj={}
    def link(u,v): adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    for p in range(2*n):
        q=D1[p]
        if p<q: link(('a',p),('a',q))
        q=D2[p]
        if p<q: link(('b',p),('b',q))
    for i in range(n): link(('a',n+i),('b',i))
    ext=[('a',i) for i in range(n)]+[('b',n+i) for i in range(n)]
    idx={e:k for k,e in enumerate(ext)}
    seen=set(); res=[None]*(2*n); loops=0
    for e in ext:
        if e in seen: continue
        prev=None; cur=e; seen.add(cur)
        while True:
            nb=[v for v in adj[cur] if v!=prev] if prev is not None else adj[cur]
            # each internal node has degree 2, external degree 1
            nxt=nb[0] if prev is not None else adj[cur][0]
            if prev is not None and len(adj[cur])==2:
                nxt=[v for v in adj[cur] if v!=prev][0]
            prev,cur=cur,nxt; seen.add(cur)
            if cur in idx: break
        res[idx[e]]=idx[cur]; res[idx[cur]]=idx[e]
    allnodes=set(adj)
    rest=allnodes-seen
    while rest:
        s=rest.pop(); loops+=1; stack=[s]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v in rest: rest.discard(v); stack.append(v)
    return tuple(res),loops
def mul(X,Y,n):
    out={}
    for D1,c1 in X.items():
        for D2,c2 in Y.items():
            D,l=compose(D1,D2,n)
            out[D]=sp.expand(out.get(D,0)+c1*c2*d**l)
    return {D:c for D,c in out.items() if sp.simplify(c)!=0}
def ident(n): return {tuple([n+i for i in range(n)]+[i for i in range(n)]):1}
def e(i,n):  # cup-cap on strands i,i+1 (0-based)
    m=list(range(n,2*n))+list(range(n))
    m[i],m[i+1]=i+1,i
    m[n+i],m[n+i+1]=n+i+1,n+i
    return {tuple(m):1}
def add(X,Y,a=1,b=1):
    out=dict()
    for D,c in X.items(): out[D]=out.get(D,0)+a*c
    for D,c in Y.items(): out[D]=out.get(D,0)+b*c
    return {D:sp.simplify(c) for D,c in out.items() if sp.simplify(c)!=0}
def cross(i,n,kind):  # 'x': A*vertical + A^-1*e ; 'y': A^-1*vertical + A*e
    a,b=(A,1/A) if kind=='x' else (1/A,A)
    return add(ident(n),e(i,n),a,b)
def prod(*Xs,n):
    r=ident(n)
    for X in Xs: r=mul(r,X,n)
    return r
def scal(X,s): return {D:sp.simplify(s*c) for D,c in X.items()}
def eq(X,Y): 
    Z=add(X,Y,1,-1); return all(sp.simplify(c)==0 for c in Z.values())
# f2 on strands (i,i+1) of n
def f2(i,n): return add(ident(n),e(i,n),1,-1/d)
n=4
P=mul(f2(0,4),f2(2,4),4)
C=prod(cross(1,4,'x'),cross(0,4,'x'),cross(2,4,'x'),cross(1,4,'x'),n=4)
Ci=prod(cross(1,4,'y'),cross(2,4,'y'),cross(0,4,'y'),cross(1,4,'y'),n=4)
print('C*Ci = Id ?', eq(mul(C,Ci,4),ident(4)))
R=prod(P,C,P,n=4); Ri=prod(P,Ci,P,n=4)
Ep=prod(P,e(1,4),e(0,4),e(2,4),e(1,4),P,n=4)
lhs=add(R,Ri,1,-1); rhs=scal(add(P,Ep,1,-1),A**4-A**-4)
print('(L1) R - R^-1 == (A^4-A^-4)(Id - E\') :', eq(lhs,rhs))
# integral expansion R = A^4 Id + (A^2+A^-2) E + A^-4 E'
E=prod(P,e(1,4),P,n=4)
print('     R == A^4 Id + (A^2+A^-2) E + A^-4 E\' :', eq(R, add(add(scal(P,A**4),scal(E,A**2+A**-2)),scal(Ep,A**-4))))
# (L2): strands 0 = axis (colour 1), 1,2 = band (colour 2). full twist = s0 s1 s1 s0 (kht++ quotient of y0/x0)
n=3; Q=f2(1,3); t=A**-4
for kind in 'xy':
    o='y' if kind=='x' else 'x'
    F=prod(Q,cross(0,3,kind),cross(1,3,kind),cross(1,3,kind),cross(0,3,kind),Q,n=3)
    Fi=prod(Q,cross(0,3,o),cross(1,3,o),cross(1,3,o),cross(0,3,o),Q,n=3)
    lhs=add(F,Fi,1,-1)
    if kind=='x': rhs=scal(add(scal(F,1/t),scal(Q,-(1-t+t**2)/t**2)),1+t)
    else:         rhs=scal(add(F,scal(Q,-(t**2-t+1)/t)),1+t)
    print('(L2) kind',kind,': F - F^-1 == (1+t)*[...] :', eq(lhs,rhs))
