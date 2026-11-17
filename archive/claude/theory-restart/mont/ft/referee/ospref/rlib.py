"""Referee's own library (independent of kauffman.py / flat_search.py).
Laurent polys: dict exp->int.  Morse words: list of ops ('cap',i) ('cup',i) ('x',i) ('y',i) acting on strand positions i,i+1
(0-based).  Letter convention chosen to MATCH the project tools: x = A*vertical + A^-1*cupcap, y = A^-1*vertical + A*cupcap.
State = tuple of path labels (two open ends of one path share a label); canonical relabelling by first occurrence."""
from fractions import Fraction as F
import math
def P_add(*ps):
    r={}
    for p in ps:
        for e,c in p.items():
            r[e]=r.get(e,0)+c
    return {e:c for e,c in r.items() if c}
def P_scale(p,c): return {e:c*v for e,v in p.items() if c*v}
def P_shift(p,k): return {e+k:v for e,v in p.items()}
def P_mul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return {e:c for e,c in r.items() if c}
def P_sub(p,q): return P_add(p,P_scale(q,-1))
def P_divexact(p,q):
    """exact division in Z[x,1/x]; returns None if not exact"""
    p=dict(p); out={}
    if not p: return {}
    qt=max(q); qc=q[qt]; qb=min(q)
    guard=0
    while p:
        guard+=1
        if guard>100000: return None
        e=max(p)
        if e-qt < min(p)-qb: return None
        c=p[e]
        if c%qc: return None
        k=e-qt; out[k]=c//qc
        for f,d in q.items():
            v=p.get(f+k,0)-out[k]*d
            if v: p[f+k]=v
            else: p.pop(f+k,None)
    return out
DELTA={2:-1,-2:-1}
def canon(s):
    m={}; out=[]
    for a in s:
        if a not in m: m[a]=len(m)
        out.append(m[a])
    return tuple(out)
def st_cap(s,i):
    new=max(s)+1 if s else 0
    s=list(s); s[i:i]=[new,new]; return canon(s)
def st_cup(s,i):
    a,b=s[i],s[i+1]; s=list(s); loop=(a==b)
    if not loop: s=[a if v==b else v for v in s]
    del s[i:i+2]
    return canon(s),loop
def evaluate(ops, init=()):
    """returns dict: final state -> poly (loops weighted by delta)"""
    st={canon(init):{0:1}}
    for c,i in ops:
        new={}
        def put(k,p):
            if not p: return
            q=P_add(new.get(k,{}),p)
            if q: new[k]=q
            else: new.pop(k,None)
        for s,p in st.items():
            if c=='cap': put(st_cap(s,i),p)
            elif c=='cup':
                s2,loop=st_cup(s,i); put(s2,P_mul(p,DELTA) if loop else p)
            else:
                av,ac=(1,-1) if c=='x' else (-1,1)
                put(s,P_shift(p,av))
                s2,loop=st_cup(s,i); q=P_mul(p,DELTA) if loop else p
                put(st_cap(s2,i),P_shift(q,ac))
        st=new
    return st
def bracket_closed(ops):
    st=evaluate(ops)
    assert set(st)<= {()}, st.keys()
    return st.get((),{})
# ---- orientation / writhe of a closed Morse diagram (one or more components) ----
def writhe(ops):
    """trace segments; returns (writhe, ncomponents). Sign rule fixed by the bracket: x with both strands same vertical
    direction is POSITIVE (checked: kink cap1,x0,cup1 gives -A^3)."""
    # build graph: each op creates/consumes segment ids
    nid=[0]
    def new():
        nid[0]+=1; return nid[0]
    pos=[]; adj={}   # segment id -> list of (neighbor segment, how)
    crosses=[]       # (letter, topL, topR, botL, botR)
    links=[]         # pairs of segment-ends joined (cap/cup) : (seg_a, end_a, seg_b, end_b) end in {'top','bot'}
    for c,i in ops:
        if c=='cap':
            a,b=new(),new(); pos[i:i]=[a,b]; links.append((a,'top',b,'top'))
        elif c=='cup':
            a,b=pos[i],pos[i+1]; links.append((a,'bot',b,'bot')); del pos[i:i+2]
        else:
            tl,tr=pos[i],pos[i+1]; bl,br=new(),new(); pos[i],pos[i+1]=bl,br
            crosses.append((c,tl,tr,bl,br))
    assert not pos
    # a segment runs from its top end to its bottom end (top = created point). Each segment's top is either a cap or a crossing
    # output; bottom is cup or crossing input. Crossing: tl continues to br, tr continues to bl (strands cross).
    nxt={}   # (seg,end) -> (seg,end) connected through a cap/cup or crossing
    for a,ea,b,eb in links: nxt[(a,ea)]=(b,eb); nxt[(b,eb)]=(a,ea)
    for c,tl,tr,bl,br in crosses:
        nxt[(tl,'bot')]=(br,'top'); nxt[(br,'top')]=(tl,'bot')
        nxt[(tr,'bot')]=(bl,'top'); nxt[(bl,'top')]=(tr,'bot')
    direction={}  # seg -> +1 if traversed top->bottom (down), -1 if up
    segs=set(); [segs.update([a,b]) for a,_,b,_ in links]; [segs.update([x[1],x[2],x[3],x[4]]) for x in crosses]
    ncomp=0
    for s0 in sorted(segs):
        if s0 in direction: continue
        ncomp+=1
        s,d=s0,1
        while s not in direction:
            direction[s]=d
            end='bot' if d==1 else 'top'
            s2,e2=nxt[(s,end)]
            d=1 if e2=='top' else -1
            s=s2
    w=0
    for c,tl,tr,bl,br in crosses:
        dl=direction[tl]   # strand entering from top-left (continues to br)
        dr=direction[tr]
        same=(dl==dr)
        sgn=1 if same else -1
        if c=='y': sgn=-sgn
        w+=sgn
    return w,ncomp
def cable2(ops):
    out=[]
    for c,i in ops:
        if c=='cap': out+=[('cap',2*i),('cap',2*i+1)]
        elif c=='cup': out+=[('cup',2*i+1),('cup',2*i)]
        else: out+=[(c,2*i+1),(c,2*i),(c,2*i+2),(c,2*i+1)]
    return out
def to_t_KL(p):
    """A-poly whose exponents are congruent mod 4 -> t-poly with t = A^-4 (after removing A^r)"""
    r=min(p)%4
    assert all((e-r)%4==0 for e in p), p
    return {-(e-r)//4:c for e,c in p.items()}, r
def jones(ops):
    """V_K(t), t = A^-4 (KL), from (-A^3)^-w <K>/delta"""
    b=bracket_closed(ops); w,nc=writhe(ops); assert nc==1
    q=P_divexact(b,DELTA)
    q=P_shift(q,-3*w)
    if w%2: q=P_scale(q,-1)
    assert all(e%4==0 for e in q), q
    return {-e//4:c for e,c in q.items()}
DELTA2={4:1,0:1,-4:1}
def J3(ops):
    """normalised colour-2 coloured Jones, KL t = A^-4: (A^8)^-w (<K^(2)> - 1)/Delta_2 ; <O> = delta"""
    w,nc=writhe(ops); assert nc==1
    b2=bracket_closed(cable2(ops)); b2=P_add(b2,{0:-1})
    q=P_divexact(b2,DELTA2); assert q is not None
    q=P_shift(q,-8*w)
    assert all(e%4==0 for e in q), q
    return {-e//4:c for e,c in q.items()}
def ev_h(P,order):
    """coefficients of P(-e^h) in h, k = 0..order (P in t)"""
    return [sum(F(c*(-1)**(e%2)*e**k) for e,c in P.items())/math.factorial(k) for k in range(order+1)]
def der1(P,k):
    tot=0
    for e,c in P.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f
    return tot
def a2_of(V): return F(-der1(V,2),6)
def v3_of(V): return F(-(der1(V,3)+3*der1(V,2)),36)
def braid_ops(n,word):
    """closure of an n-braid; word = list of signed generators 1..n-1; closure strands on the left"""
    ops=[('cap',0)]+[('cap',j) for j in range(1,n)]
    # after nested caps: positions 0..2n-1, closure strands 0..n-1 (reversed), braid strands n..2n-1
    for s in word:
        ops.append(('x' if s>0 else 'y', n+abs(s)-1))
    ops+=[('cup',j) for j in range(n-1,-1,-1)]
    return ops
