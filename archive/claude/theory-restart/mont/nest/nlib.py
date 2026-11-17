"""Helpers for lane NEST (pinned box vectors, units, nesting)."""
import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
D=P((1,-1),(-1,3))   # e1^T X^-1 = (1, D)
def divexact(p,d):
    p=dict(p); q={}
    if not p: return {}
    lo=bot(p)-bot(d); dt=top(d); dc=d[dt]
    while p:
        e=top(p); c=p[e]; k=e-dt
        if k<lo or c%dc: return None
        q[k]=c//dc
        p=sub(p,mul(mono(k,c//dc),d))
    return clean(q)
def tw(m,a='y',b='x'): return (a+'1.' if m>0 else b+'1.')*abs(m)
def body(m,boxes):
    """necklace body r2.(y1)^m.B1...Bn.u1 (no s.)"""
    return 'r2.'+tw(m)+'.'.join(boxes)+'.u1'
def vec(B, ms=(1,2,-1), extra=()):
    """pinned vector of body B: v1=J(s.B), v2 from twisted closure m=ms[0], checked on the others. returns list of candidates"""
    a=J('s.'+B)
    if a is None: return None
    Js={m:J('s.'+body(m,[B])) for m in tuple(ms)+tuple(extra)}
    if any(v is None for v in Js.values()): return None
    cands=[]
    m0=ms[0]
    # e1^T X^-m0 v = a + d_m0 v2
    d=close(-m0,[{},ONE])
    for k in range(-80,81):
        for s in (1,-1):
            q=divexact(sub(mul(mono(k,s),Js[m0]),a),d)
            if q is None: continue
            v=[a,q]
            if all(normalize(close(-m,v))==Js[m] for m in Js if m!=m0): cands.append(v)
    return cands
def unit_ratio(u,v):
    """return (s,k) with u = s t^k v, or None"""
    if not u[0] and not u[1] and not v[0] and not v[1]: return (1,0)
    for i in (0,1):
        if v[i]:
            if not u[i]: return None
            k=top(u[i])-top(v[i]); s=u[i][top(u[i])]//v[i][top(v[i])]
            if s not in (1,-1): return None
            break
    for i in (0,1):
        if shift({e:s*c for e,c in v[i].items()},k)!=u[i]: return None
    return (s,k)
def mpow(M,k):
    R=[[ONE,{}],[{},ONE]]
    for _ in range(k): R=mmul(R,M)
    return R
def Xpow(m):
    return mpow(Xm,m) if m>=0 else mpow(Xi,-m)
def ev1(v): return [ev(v[0],-1), ev(v[1],-1)]
def nax(B):
    return sum(1 for tok in B.split('.') if tok in ('x0','y0'))
def load_boxes():
    L=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
    return [(B,[dict((e,c) for e,c in v[0]),dict((e,c) for e,c in v[1])]) for B,v in L]
def fmt(p):
    if not p: return '0'
    return ' '.join(('%+d'%c)+('t^%d'%e if e else '') for e,c in sorted(p.items()))
def width(B):
    w=1; mx=1
    for tok in B.split('.'):
        if not tok: continue
        c=tok[0]
        if c in 'lr': w+=2
        elif c=='u': w-=2
        mx=max(mx,w)
    return mx
def eps(v): return ev(b_of(v),-1)
def F(m,p):
    """outer map: vector of necklace body r2.(y1)^m.<p>.u1 from product vector p"""
    e=eps(p)
    q=mvec(Xpow(-m),p)
    k=2*m*(1-e)
    return [shift(q[0],k),shift(q[1],k)]
def tree_word(T):
    if T[0]=='box': return T[1]
    return body(T[1],[tree_word(c) for c in T[2]])
def tree_vec(T):
    if T[0]=='box': return T[2]
    ps=[tree_vec(c) for c in T[2]]
    p=ps[0]
    for q in ps[1:]: p=star(p,q)
    return F(T[1],p)
def tree_depth(T):
    if T[0]=='box': return 0
    return 1+max(tree_depth(c) for c in T[2])
