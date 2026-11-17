"""Fast Laurent polynomials in t as {exp:int} dicts; 2x2 matrices; J of half-diagram words."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import flat_search as fs, alex
def clean(p): return {e:c for e,c in p.items() if c}
def add(*ps):
    r={}
    for p in ps:
        for e,c in p.items(): r[e]=r.get(e,0)+c
    return clean(r)
def neg(p): return {e:-c for e,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return clean(r)
def mono(e,c=1): return {e:c}
def P(*terms):  # P((c,e),...) 
    return clean({e:c for c,e in terms})
ONE=mono(0)
def shift(p,k): return {e+k:c for e,c in p.items()}
def top(p): return max(p)
def bot(p): return min(p)
def span(p): return max(p)-min(p) if p else None
def ev(p,x): return sum(c*x**e for e,c in p.items())
def normalize(J):
    s=sum(c*(-1)**(e%2) for e,c in J.items())
    d=sum(e*c*(-1)**((e-1)%2) for e,c in J.items())
    if s not in (1,-1) or d%s: return None
    k=-(d//s) if False else None
    # want sgn*t^k*J: value sgn*(-1)^k*s=1, derivative sgn*[k(-1)^(k-1)s+(-1)^k d]=0 -> k s = d
    k=d//s
    sgn=s*(-1)**(k%2)
    out={e+k:sgn*c for e,c in J.items()}
    return out
def J_raw(word):
    half=alex.parse(word)
    full=alex.symmetrize(half)
    if full is None or alex.diagram(full) is None: return None
    y,x=fs.bracket_vector(half)
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x))
    u={e:c for e,c in u.items() if c}
    if len(u)!=1: return None
    (eu,cu),=u.items()
    out={}
    for e,c in y.items():
        if c:
            assert (e-eu)%4==0
            out[(e-eu)//4]=out.get((e-eu)//4,0)+c*cu
    return clean(out)
def J(word):
    r=J_raw(word)
    return None if r is None else normalize(r)
def a2(Jn):
    # -J''(-1)/24
    s=sum(c*e*(e-1)*(-1)**((e-2)%2) for e,c in Jn.items())
    return -s/24
# matrices: lists [[a,b],[c,d]] of polys
def mmul(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def mvec(A,v): return [add(mul(A[0][0],v[0]),mul(A[0][1],v[1])), add(mul(A[1][0],v[0]),mul(A[1][1],v[1]))]
Xm=[[ONE,P((1,0),(-1,4))],[{},mono(1,-1)]]
Xi=[[ONE,P((1,-1),(-1,3))],[{},mono(-1,-1)]]
Ym=[[ONE,{}],[mono(-3),mono(-3)]]
Yi=[[ONE,{}],[mono(0,-1),mono(3)]]
E1=[ONE,{}]
def apply(word,v=None):
    """word: string over X,x,Y,y (x = X^-1), applied right-to-left as written? we apply letters left to right to the vector: last letter acts first"""
    v=E1 if v is None else v
    for ch in reversed(word):
        M={'X':Xm,'x':Xi,'Y':Ym,'y':Yi}[ch]
        v=mvec(M,v)
    return v
def star(v,w):
    return [mul(v[0],w[0]), add(mul(v[0],w[1]),mul(v[1],w[0]),mul(P((1,0),(-1,3)),mul(v[1],w[1])))]
def a_of(v): return v[0]
def b_of(v): return add(v[0],mul(P((1,0),(-1,3)),v[1]))
def close(m,p):
    M=Xm if m>=0 else Xi
    for _ in range(abs(m)): p=mvec(M,p)
    return p[0]
