"""ENGINE C1: rigorous jet automaton for rational boxes at the top end (t = infinity), relative order K.
State r = v_2/v_1 of the TH-2BR vector; combined step for exponent m: r_pre = Y^m r, D = 1 + (1-t^4) r_pre, r' = -(1+r_pre)/D,
a -> a D.  Normal form u(m_0..m_{k-1}) = E Y^{m_{k-1}} ... E Y^{m_0} e_1 (m_0 not in {0,-1}, interior m_i != 0).
Series with ABSOLUTE PRECISION TRACKING: (c, P): c = {deg: Fraction} exact for all degrees >= P (P=None: exact polynomial).
A state key is (d, jet) with r = t^d (j_0 + j_1 u + ... + j_K u^K + O(u^{K+1})), or 'tiny' (r = O(t^{-4-K})), or 'init' (r = 0).
Soundness: every transition is computed from the key alone (precision-tracked) and we ASSERT the outputs are known to relative
order K; hence the key determines (D-jet, next key) for every exact r with that key.  Exponent clipping: m >= M stands for all
m >= M (verified: m = M, M+1, M+2 give identical outputs from every state), likewise m <= -M."""
from fractions import Fraction as Fr
import sys
INF=None
class S:
    __slots__=('c','P')
    def __init__(s,c,P): s.c={e:Fr(v) for e,v in c.items() if v and (P is None or e>=P)}; s.P=P
    def lead(s):
        return max(s.c) if s.c else None
def padd(x,y):
    P = x.P if y.P is None else (y.P if x.P is None else max(x.P,y.P))
    c=dict(x.c)
    for e,v in y.c.items(): c[e]=c.get(e,0)+v
    return S(c,P)
def pneg(x): return S({e:-v for e,v in x.c.items()},x.P)
def pshift(x,k): return S({e+k:v for e,v in x.c.items()}, None if x.P is None else x.P+k)
def pmul(x,y):
    dx=x.lead(); dy=y.lead()
    # precision: P = max(Px + dy, Py + dx); if a factor is 'zero to precision', product is zero to precision Px+top(y)
    if dx is None and dy is None:
        return S({}, x.P+y.P if (x.P is not None and y.P is not None) else (x.P if x.P is not None else y.P))
    cands=[]
    if x.P is not None: cands.append(x.P+(dy if dy is not None else y.P))
    if y.P is not None: cands.append(y.P+(dx if dx is not None else x.P))
    P=max(cands) if cands else None
    c={}
    for e,v in x.c.items():
        for f,w in y.c.items():
            if P is None or e+f>=P: c[e+f]=c.get(e+f,0)+v*w
    return S(c,P)
def pinv(x):
    d=x.lead(); assert d is not None, 'inverse of unknown/zero'
    lc=x.c[d]
    if x.P is None:
        # exact polynomial: invert as series to a generous precision
        P=d-60
    else: P=x.P
    rel=d-P          # relative precision of x
    # 1/x = lc^-1 t^-d (1+h)^-1, h = x/(lc t^d) - 1, relative precision rel
    h={e-d:v/lc for e,v in x.c.items() if e!=d and e-d>=-rel}
    inv={0:Fr(1)}
    for n in range(1,rel+1):
        s=0
        for k in range(1,n+1):
            s-=h.get(-k,0)*inv.get(-(n-k),0)
        if s: inv[-n]=s
    return S({e-d:v/lc for e,v in inv.items()}, -d-rel)
ONE=S({0:1},None)
def rel_prec(x):
    d=x.lead()
    if x.P is None: return 10**9
    if d is None: return None
    return d-x.P
def jet(x,K):
    d=x.lead(); assert d is not None
    assert x.P is None or d-x.P>=K, ('precision',d,x.P,K)
    lc=x.c[d]
    return d, tuple(x.c.get(d-i,Fr(0)) for i in range(K+1))
def from_key(key,K):
    if key=='init': return S({},None)
    if key=='tiny': return S({},-3-K)
    d,j=key
    return S({d-i:v for i,v in enumerate(j)}, d-K)
def canon(r,K):
    d=r.lead()
    if r.P is None and d is None: return 'init'
    if d is None or d<=-4-K:
        # all known coefficients above -4-K vanish?  need P <= -3-K for soundness
        assert r.P is not None and r.P<=-3-K or r.P is None, ('tiny precision',r.P)
        if d is None or d<=-4-K:
            assert all(e<=-4-K for e in r.c), r.c
            return 'tiny'
    return jet(r,K)
def Ystep(r,m):
    if m>0:
        for _ in range(m): r=pshift(padd(ONE,r),-3)
    else:
        for _ in range(-m): r=padd(pneg(ONE),pshift(r,3))
    return r
ONEMT4=S({0:1,4:-1},None); ONEMT3=S({0:1,3:-1},None)
def step(key,m,K):
    r=from_key(key,K)
    rp=Ystep(r,m)
    D=padd(ONE,pmul(ONEMT4,rp))
    num=padd(ONE,rp)
    if num.lead() is None:
        if num.P is None: return None   # degenerate (exact zero): E Y^-1 e_1
        rn=S({},num.P-D.lead())          # zero to precision
    else:
        rn=pneg(pmul(num,pinv(D)))
    Dj=jet(D,K)
    return Dj, canon(rn,K)
def qjet(key,K):
    r=from_key(key,K)
    q=padd(ONE,pmul(ONEMT3,r))
    return jet(q,K)
def logs(s):
    Kp=len(s); Sx=[Fr(0)]+list(s); l=[Fr(0)]*(Kp+1)
    for k in range(1,Kp+1):
        tot=k*Sx[k]
        for j in range(1,k): tot-=j*l[j]*Sx[k-j]
        l[k]=tot/k
    return tuple(l[1:])
def norm_jet(j):
    d,c=j; return d, c[0], tuple(v/c[0] for v in c[1:])
def build(K,M=None,verbose=True):
    if M is None: M=K+3
    states={'init':0}; order=['init']; trans={}
    i=0
    while i<len(order):
        key=order[i]; i+=1
        ms=[m for m in list(range(1,M+1))+list(range(-M,0))]
        for m in ms:
            if key=='init' and m==-1: continue
            res=step(key,m,K)
            if res is None: continue
            Dj,nk=res
            if nk not in states:
                states[nk]=len(order); order.append(nk)
            trans[(key,m)]=(Dj,nk)
        # clipping check
        for m in (M,-M):
            if key=='init' and m==-1: continue
            r0=step(key,m,K)
            for mm in (m+ (1 if m>0 else -1), m+(2 if m>0 else -2)):
                r1=step(key,mm,K)
                assert norm_jet(r0[0])[1:]==norm_jet(r1[0])[1:] and r0[1]==r1[1], ('clip fail',key,m,mm)
        if len(order)>5000: raise RuntimeError('too many states')
    if verbose: print('K=%d M=%d: %d states, %d transitions'%(K,M,len(order),len(trans)))
    return order,trans
def run(seq,K,trans=None,M=None):
    """walk: returns (final key, log-jet of a (order K), list of steps)"""
    if M is None: M=K+3
    key='init'; la=[Fr(0)]*K
    for m in seq:
        mc=max(-M,min(M,m))
        if trans is not None: Dj,nk=trans[(key,mc)]
        else: Dj,nk=step(key,mc,K)
        d,lc,s=norm_jet(Dj)
        l=logs(s)
        la=[x+y for x,y in zip(la,l)]
        key=nk
    return key,tuple(la)
def qlog(key,K):
    if key=='init': return (0,1,tuple([Fr(0)]*K))
    if key=='tiny':
        return (0,1,tuple([Fr(0)]*K))
    d,lc,s=norm_jet(qjet(key,K)); return (d,lc,logs(s))
