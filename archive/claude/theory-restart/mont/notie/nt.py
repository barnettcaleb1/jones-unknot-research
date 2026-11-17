"""NO-TIE lane tools: rational boxes in normal form, channels, necklace J (exact, pure Python)."""
import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from lp import add, neg, sub, mul, mono, P, ONE, shift, top, bot, span, mmul, mvec, Xm, Xi, Ym, Yi, E1, star, a_of, b_of, close, normalize, clean
Em=[[ONE,P((1,0),(-1,4))],[mono(0,-1),mono(0,-1)]]   # E = Y^-1 X, E^2 = t^4
def Ypow(n,v):
    M=Ym if n>=0 else Yi
    for _ in range(abs(n)): v=mvec(M,v)
    return v
def Xpow(n,v):
    M=Xm if n>=0 else Xi
    for _ in range(abs(n)): v=mvec(M,v)
    return v
def box(seq,v=None):
    """u = E Y^{m_{k-1}} ... E Y^{m_0} e_1 ; seq=(m_0,...,m_{k-1}); rightmost acts first"""
    v=[ONE,{}] if v is None else v
    for m in seq:
        v=Ypow(m,v); v=mvec(Em,v)
    return v
def chan(v): return a_of(v), b_of(v)
def prod(vs):
    p=vs[0]
    for v in vs[1:]: p=star(p,v)
    return p
def neck(mu,N,vs):
    """unnormalised J = e_1^T X^mu Y^N (v_1*...*v_n)"""
    p=prod(vs); p=Ypow(N,p); p=Xpow(mu,p); return p[0]
def lead(p): e=max(p); return (e,p[e])
def tail(p): e=min(p); return (e,p[e])
def normal_seqs(K,M):
    """prefix-normalised sequences: m_0 not in {0,-1}, later m_i != 0, |m_i|<=M, length 1..K"""
    vals=[m for m in range(-M,M+1) if m!=0]
    out=[]
    for k in range(1,K+1):
        for s in itertools.product(vals,repeat=k):
            if s[0]==-1: continue
            out.append(s)
    return out
def mirror_seq(seq):
    """bar(u(seq)) = t^{-4k} D Y u(seq''), seq''=(-m0-1,-m1,...)"""
    return (-seq[0]-1,)+tuple(-m for m in seq[1:])
def ser_div(p,q,nterms):
    """expansion at t=infinity of p/q: list of (exp,coef) top nterms terms (exact rationals)"""
    from fractions import Fraction
    p={e:Fraction(c) for e,c in p.items()}
    dq,cq=lead(q)
    out=[]
    cur=dict(p)
    for _ in range(nterms):
        cur={e:c for e,c in cur.items() if c}
        if not cur: break
        e=max(cur); c=cur[e]/cq
        out.append((e-dq,c))
        for f,d in q.items():
            cur[e-dq+f]=cur.get(e-dq+f,0)-c*d
    return out
