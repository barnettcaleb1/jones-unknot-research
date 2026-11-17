# Tiny exact check of normalisations for W(6,0) (= W(5,1) on B_5), Kauffman convention sigma_i -> A + A^-1 e_i.
# Laurent polynomials in A as dicts {exponent: int}.
def P(d): return {k:v for k,v in d.items() if v}
def add(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,0)+v
    return P(r)
def neg(p): return {k:-v for k,v in p.items()}
def mul(p,q):
    r={}
    for a,x in p.items():
        for b,y in q.items(): r[a+b]=r.get(a+b,0)+x*y
    return P(r)
def mon(e,c=1): return {e:c}
ZERO={}; ONE={0:1}
d=add(mon(2,-1),mon(-2,-1))          # delta = -A^2 - A^-2
def bar(p): return {-k:v for k,v in p.items()}
def deg(p): return (max(p),min(p)) if p else None
def show(p):
    return ' '.join(f"{v:+d}A^{k}" for k,v in sorted(p.items(),reverse=True))
N=5
# basis D1=(12)(34)(56) D2=(12)(36)(45) D3=(14)(23)(56) D4=(16)(23)(45) D5=(16)(25)(34)=rainbow
# images: e_i D_j = coef * D_target  (coef 'd' means delta)
tab={1:{1:('d',1),2:('d',2),3:(1,1),4:(1,2),5:(1,1)},
     2:{1:(1,3),2:(1,4),3:('d',3),4:('d',4),5:(1,4)},
     3:{1:('d',1),2:(1,1),3:(1,1),4:(1,5),5:('d',5)},
     4:{1:(1,2),2:('d',2),3:(1,4),4:('d',4),5:(1,4)},
     5:{1:('d',1),2:(1,1),3:('d',3),4:(1,3),5:(1,1)}}
def E(i):
    M=[[ZERO]*N for _ in range(N)]
    for j,(c,t) in tab[i].items():
        M[t-1][j-1]= d if c=='d' else ONE
    return M
def mm(X,Y):
    return [[ (lambda r,c: __import__('functools').reduce(add,[mul(X[r][k],Y[k][c]) for k in range(N)],ZERO))(r,c) for c in range(N)] for r in range(N)]
def mv(X,v): return [__import__('functools').reduce(add,[mul(X[r][k],v[k]) for k in range(N)],ZERO) for r in range(N)]
I=[[ONE if r==c else ZERO for c in range(N)] for r in range(N)]
def lin(a,X,b,Y): return [[add(mul(a,X[r][c]),mul(b,Y[r][c])) for c in range(N)] for r in range(N)]
S={i:lin(mon(1),I,mon(-1),E(i)) for i in range(1,6)}
Si={i:lin(mon(-1),I,mon(1),E(i)) for i in range(1,6)}
def word(w):
    M=I
    for g in w: M=mm(M, S[g] if g>0 else Si[-g])
    return M
def eq(X,Y): return all(P(add(X[r][c],neg(Y[r][c])))=={} for r in range(N) for c in range(N))
# Gram matrix: loops
d2=mul(d,d); d3=mul(d2,d)
L=[[3,2,2,1,2],[2,3,1,2,1],[2,1,3,2,1],[1,2,2,3,2],[2,1,1,2,3]]
pw={1:d,2:d2,3:d3}
G=[[pw[L[r][c]] for c in range(N)] for r in range(N)]
# checks
for i in range(1,5): assert eq(mm(S[i],mm(S[i+1],S[i])),mm(S[i+1],mm(S[i],S[i+1]))), i
for i in range(1,6):
    Et=[[E(i)[c][r] for c in range(N)] for r in range(N)]
    assert eq(mm(G,E(i)),mm(Et,G)), ('contravariance',i)
    assert eq(mm(S[i],Si[i]),I)
print("braid relations, inverses, Gram contravariance: OK")
vt=[neg(d),ONE,ONE,neg(d),add(d2,neg(ONE))]   # (delta^2-1) * v_c, v_c = p_3-coloured rainbow
for i in (1,2,4,5): assert all(x=={} for x in mv(E(i),vt)), i
print("e1,e2,e4,e5 kill v_c: OK")
T=word([1,2,1,2,1,2])
Tv=mv(T,vt); assert all(P(add(Tv[k],neg(mul(mon(6),vt[k]))))=={} for k in range(N))
for j in range(4):
    col=[T[r][j] for r in range(N)]
    assert all(P(add(col[r], neg(mon(-6) if r==j else ZERO)))=={} for r in range(N)), j
print("T_c=(s1 s2)^3 = A^-6 on span(D1..D4), A^6 on v_c: OK  => T_c = A^-6 (1 + (A^12-1) P_c)")
def H(x,y): # invariant Hermitian form  bar(x)^T G y
    Gy=mv(G,y); return __import__('functools').reduce(add,[mul(bar(x[k]),Gy[k]) for k in range(N)],ZERO)
hvv=H(vt,vt); D3=add(d3,neg(mul(mon(0,2),d)))
D2=add(d2,neg(ONE))
assert P(add(hvv,neg(mul(mul(D2,D2),D3))))=={}
print("H(v~,v~) = Delta_2^2 Delta_3, i.e. H(v_c,v_c) = Delta_3 =", show(D3))
# invariance check
g=word([3,-4,2,1,-5]); 
x=[mon(1),mon(-2),ONE,mon(3),mon(0,2)]; y=[ONE,mon(1),mon(5),ZERO,mon(-1)]
assert P(add(H(mv(g,x),mv(g,y)),neg(H(x,y))))=={}
print("H invariant under braid action: OK")
def report(name,w,extra=''):
    h=H(vt,mv(word(w),vt)); 
    top,bot=deg(h) if h else (None,None)
    print(f"{name:22s} H(v~,g v~): top {top}, bottom {bot}, span {None if h=={} else top-bot}, #terms {len(h)} {extra}")
    return h
h1=report("sigma3",[3],"i=2")
# r(c,sigma3 c) = H H-bar / H(v,v)^2 ; check equals 1/[3]^2 i.e. r*Delta_2^2 == 1
num=mul(h1,bar(h1)); den=mul(hvv,hvv)
assert P(add(mul(num,mul(D2,D2)),neg(den)))=={}
print("r(c, sigma3 c) = 1/[3]^2 exactly")
for k in range(2,7): report(f"sigma3^{k}",[3]*k, f"i={4*(k//2)}" if k%2==0 else "")
for k in range(1,6): report(f"(s3 s4^-1)^{k}",[3,-4]*k, "pA on disk{3,4,5}: i ~ 2.618^k")
