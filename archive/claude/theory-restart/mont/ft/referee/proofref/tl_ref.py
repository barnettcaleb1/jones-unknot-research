# Referee's independent Temperley-Lieb check of (L1), (L2).  Diagrams on n strands: a perfect matching of
# 2n points: top points 0..n-1, bottom points n..2n-1. Product a*b = a on top of b (a's bottom glued to b's top).
import sympy as sp
A=sp.symbols('A'); d=-A**2-A**-2
def compose(a,b,n):
    # a: matching on top/bottom; glue a.bottom(i) = b.top(i). Return (matching, loops)
    # points: a-top i -> ('a',i), a-bot i -> ('a',n+i) ; b-top i -> ('b',i), b-bot -> ('b',n+i)
    adj={}
    def lk(u,v): adj.setdefault(u,[]).append(v); adj.setdefault(v,[]).append(u)
    for i in range(2*n):
        j=a[i]
        if i<j: lk(('a',i),('a',j))
        j=b[i]
        if i<j: lk(('b',i),('b',j))
    for i in range(n): lk(('a',n+i),('b',i))   # glue
    ext=[('a',i) for i in range(n)]+[('b',n+i) for i in range(n)]
    seen=set(); res=[None]*(2*n); loops=0
    def walk(s):
        prev=None; cur=s; path=[s]
        while True:
            nx=[v for v in adj[cur] if v!=prev]
            if not nx: return cur
            # each internal point has degree 2; external degree 1
            if len(adj[cur])==1 and cur!=s: return cur
            nxt=nx[0] if prev is not None or len(adj[cur])==1 else nx[0]
            prev,cur=cur,nxt; seen.add(cur)
            if cur in ext: return cur
    for k,u in enumerate(ext):
        if u in seen: continue
        seen.add(u); v=walk(u); res[k]=ext.index(v); res[ext.index(v)]=k
    # count loops: internal points not seen
    internal=[p for p in adj if p not in ext and p not in seen]
    rem=set(internal); 
    while rem:
        s=rem.pop(); loops+=1; prev=None; cur=s
        while True:
            nx=[v for v in adj[cur] if v!=prev]
            nxt=nx[0]; prev,cur=cur,nxt
            if cur==s: break
            rem.discard(cur)
    return tuple(res),loops
class TL:
    def __init__(s,n,terms=None): s.n=n; s.t=dict(terms or {})
    @staticmethod
    def one(n): return TL(n,{tuple([n+i for i in range(n)]+[i for i in range(n)]):sp.Integer(1)})
    @staticmethod
    def e(n,i):   # cup-cap on strands i,i+1 (0-indexed)
        m=[None]*(2*n)
        for k in range(n):
            if k not in (i,i+1): m[k]=n+k; m[n+k]=k
        m[i]=i+1; m[i+1]=i; m[n+i]=n+i+1; m[n+i+1]=n+i
        return TL(n,{tuple(m):sp.Integer(1)})
    def __add__(s,o): r=dict(s.t); [r.__setitem__(k,r.get(k,0)+v) for k,v in o.t.items()]; return TL(s.n,r)
    def __rmul__(s,c): return TL(s.n,{k:c*v for k,v in s.t.items()})
    def __sub__(s,o): return s+(-1)*o
    def __mul__(s,o):
        if not isinstance(o,TL): return TL(s.n,{k:o*v for k,v in s.t.items()})
        r={}
        for a,ca in s.t.items():
            for b,cb in o.t.items():
                m,l=compose(a,b,s.n); r[m]=r.get(m,0)+ca*cb*d**l
        return TL(s.n,r)
    def simp(s): return TL(s.n,{k:sp.simplify(v) for k,v in s.t.items() if sp.simplify(v)!=0})
    def iszero(s): return all(sp.simplify(v)==0 for v in s.t.values())
def sig(n,i,inv=False):  # 'x' crossing = A*1 + A^-1 e ; inverse = A^-1*1 + A e
    return (A**-1 if inv else A)*TL.one(n)+(A if inv else A**-1)*TL.e(n,i)
# (L1): n=4, f2 on (0,1) and (2,3)
n=4; I4=TL.one(n)
f2a=I4-(1/d)*TL.e(n,0); f2b=I4-(1/d)*TL.e(n,2); P=f2a*f2b
C=sig(n,1)*sig(n,0)*sig(n,2)*sig(n,1); Ci=sig(n,1,True)*sig(n,0,True)*sig(n,2,True)*sig(n,1,True)
print('C*Ci==1:', (C*Ci-I4).iszero())
R=P*C*P; Ri=P*Ci*P
Ep=P*TL.e(n,1)*TL.e(n,0)*TL.e(n,2)*TL.e(n,1)*P
lhs=R-Ri; rhs=(A**4-A**-4)*(P-Ep)
print('(L1) R-R^-1 == (A^4-A^-4)(Id-E\'):', (lhs-rhs).iszero())
# also check sign: is R the one with eigenvalue A^4 on f4? compute R*f4-type: R acting on P - (stuff); use trace test
# eigen-check via minimal polynomial: (R-A^-8)(R+A^-4)(R-A^4) == 0 on P-space
Z=(R-A**-8*P)*(R+A**-4*P)*(R-A**4*P)
print('(R-A^-8)(R+A^-4)(R-A^4)=0:', Z.iszero())
# (L2): n=3, f2 on strands (1,2); F = s0 s1 s1 s0 ('x')
n=3; I3=TL.one(n); f2=I3-(1/d)*TL.e(n,1)
F=f2*sig(n,0)*sig(n,1)*sig(n,1)*sig(n,0)*f2; Fi=f2*sig(n,0,True)*sig(n,1,True)*sig(n,1,True)*sig(n,0,True)*f2
t=A**-4
print('(L2) F-F^-1 == (1+t)[t^-1 F - t^-2(1-t+t^2) Id]:', ((F-Fi)-(1+t)*((1/t)*F-(t**-2*(1-t+t**2))*f2)).iszero())
print('(L2y) Fy-Fy^-1 == (1+t)[Fy - t^-1(t^2-t+1) Id]:', ((Fi-F)-(1+t)*(Fi-(t**-1*(t**2-t+1))*f2)).iszero())
print('F min poly (F-t^2)(F-t^-1)=0:', ((F-t**2*f2)*(F-t**-1*f2)).iszero())
