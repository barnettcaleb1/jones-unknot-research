"""Referee core: INDEPENDENT implementation (does not import notie/*). Laurent polys = {exp: int}.
Matrices from BRIEF: Y=[[1,0],[t^-3,t^-3]], X=[[1,1-t^4],[0,-t]], E=Y^-1 X."""
from fractions import Fraction
def cl(p): return {e:c for e,c in p.items() if c}
def ad(*ps):
    r={}
    for p in ps:
        for e,c in p.items(): r[e]=r.get(e,0)+c
    return cl(r)
def ng(p): return {e:-c for e,c in p.items()}
def ml(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return cl(r)
def mo(e,c=1): return {e:c}
def sh(p,k): return {e+k:c for e,c in p.items()}
def bar(p): return {-e:c for e,c in p.items()}
def tp(p): return max(p)
def bt(p): return min(p)
def sp(p): return max(p)-min(p)
ONE={0:1}
def mat(a,b,c,d): return [[a,b],[c,d]]
def mv(M,v): return [ad(ml(M[0][0],v[0]),ml(M[0][1],v[1])), ad(ml(M[1][0],v[0]),ml(M[1][1],v[1]))]
Y =mat(ONE,{},{-3:1},{-3:1})
Yi=mat(ONE,{},{0:-1},{3:1})
X =mat(ONE,{0:1,4:-1},{},{1:-1})
Xi=mat(ONE,{-1:1,3:-1},{},{-1:-1})
E =mat(ONE,{0:1,4:-1},{0:-1},{0:-1})
def Ypow(n,v):
    M=Y if n>=0 else Yi
    for _ in range(abs(n)): v=mv(M,v)
    return v
def Xpow(n,v):
    M=X if n>=0 else Xi
    for _ in range(abs(n)): v=mv(M,v)
    return v
def ubox(seq):
    """u(m_0,..,m_{k-1}) = E Y^{m_{k-1}} ... E Y^{m_0} e_1"""
    v=[ONE,{}]
    for m in seq:
        v=Ypow(m,v); v=mv(E,v)
    return v
S3={0:1,3:-1}   # 1 - t^3
def ach(v): return v[0]
def bch(v): return ad(v[0],ml(S3,v[1]))
def star(v,w): return [ml(v[0],w[0]), ad(ml(v[0],w[1]),ml(v[1],w[0]),ml(S3,ml(v[1],w[1])))]
def neck_matrix(mu,N,vs):
    p=vs[0]
    for v in vs[1:]: p=star(p,v)
    p=Ypow(N,p); p=Xpow(mu,p); return p[0]
def w1(mu): return ad({1:1}, ml({0:1,2:1}, {mu:(-1)**(mu%2)}))
def w3(mu): return ml({0:1,2:1}, ad(ONE,{mu:-((-1)**(mu%2))}))
PHI3={0:1,1:1,2:1}
def pdiv_exact(p,q):
    """exact division of Laurent polys (raises if not exact)"""
    p=dict(p); out={}
    dq=tp(q); cq=q[dq]
    while p:
        e=tp(p); c=p[e]
        if c%cq: raise ValueError('nonexact')
        k=c//cq; out[e-dq]=k
        for f,d in q.items():
            p[e-dq+f]=p.get(e-dq+f,0)-k*d
        p=cl(p)
        if p and tp(p)<bt(q)+ (e-dq) - 10**6: break
        if len(out)>100000: raise ValueError('runaway')
        if p and tp(p) < bt(q) - dq + bt(out) - 1 and False: pass
    return out
def neck_channels(mu,N,vs):
    """(w1 A + w3 t^{-3N} B)/Phi3 and the pieces"""
    A=ONE; B=ONE
    for v in vs: A=ml(A,ach(v)); B=ml(B,bch(v))
    Bp=sh(B,-3*N)
    G=ad(ml(w1(mu),A), ml(w3(mu),Bp))
    return G,A,Bp
def xs(p,n,end='top'):
    """normalised coefficients x_0=1,x_1..x_{n-1} at the top (or bottom) of a Laurent poly"""
    if end=='top':
        e=tp(p); c=p[e]; return [Fraction(p.get(e-i,0),c) for i in range(n)]
    e=bt(p); c=p[e]; return [Fraction(p.get(e+i,0),c) for i in range(n)]
def ser_ratio(p,q,n):
    """expansion at t=inf of p/q: (degree, [normalised coeffs...]) with leading coeff"""
    P={e:Fraction(c) for e,c in p.items()}
    dq=tp(q); cq=q[dq]; out=[]
    d0=tp(P)-dq
    for i in range(n):
        e=d0+dq-i
        c=P.get(e,Fraction(0))/cq
        out.append(c)
        if c:
            for f,d in q.items(): P[e-dq+f]=P.get(e-dq+f,0)-c*d
    return d0,out
# ---- fast exact multiplication via Kronecker substitution (big ints) ----
def fml(p,q):
    if not p or not q: return {}
    if len(p)<8 or len(q)<8: return ml(p,q)
    lp_,lq_=bt(p),bt(q)
    sp_=sum(abs(c) for c in p.values()); sq_=sum(abs(c) for c in q.values())
    B=((sp_*sq_).bit_length()+2+7)//8*8
    def enc(r,lo):
        n=0
        for e,c in r.items(): n+=c<<(B*(e-lo))
        return n
    prod=enc(p,lp_)*enc(q,lq_)
    L=(tp(p)-lp_)+(tp(q)-lq_)+1
    off=sum(1<<(B*i+B-1) for i in range(L)) if L<64 else int.from_bytes((b'\x00'*(B//8-1)+b'\x80')[::-1]*L,'little') if False else None
    if off is None:
        chunk=(1<<(B-1)).to_bytes(B//8,'little')
        off=int.from_bytes(chunk*L,'little')
    n=prod+off
    by=n.to_bytes(L*B//8+1,'little')
    out={}
    half=1<<(B-1); W=B//8
    base=lp_+lq_
    for i in range(L):
        d=int.from_bytes(by[i*W:(i+1)*W],'little')-half
        if d: out[base+i]=d
    return out
def fprod(ps):
    ps=list(ps)
    while len(ps)>1:
        nx=[]
        for i in range(0,len(ps)-1,2): nx.append(fml(ps[i],ps[i+1]))
        if len(ps)%2: nx.append(ps[-1])
        ps=nx
    return ps[0] if ps else ONE
