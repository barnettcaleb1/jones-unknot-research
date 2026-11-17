# Referee's own helpers: random half-word generator (independent of flat_search.gen), flips, Laurent division.
import sys, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, alex
def myword(rnd, L, pcap=0.18, pcup=0.18, paxis=0.25):
    """Random walk on the half-width w (number of half-strands right of the axis). Letters: x_i/y_i (i=0 on-axis, 1<=i<=w-1),
    l_i/r_i caps at half-strands (i-1,i), 1<=i<=w+1, u_i cups at (i-1,i), 1<=i<=w-1. Ends when w==1 after >= L letters."""
    w=1; toks=[]
    for step in range(10*L):
        if len(toks)>=L and w==1: break
        r=rnd.random()
        must_close = len(toks)>=L
        if (r<pcap and not must_close and w<5):
            i=rnd.randint(1,w+1); toks.append(rnd.choice('lr')+str(i)); w+=2
        elif (r<pcap+pcup or must_close) and w>=3:
            i=rnd.randint(1,w-1); toks.append('u'+str(i)); w-=2
        else:
            if w>=2 and rnd.random()>paxis: i=rnd.randint(1,w-1)
            else: i=0
            toks.append(rnd.choice('xy')+str(i))
    if w!=1: return None
    return 's.'+'.'.join(toks)
def valid(word):
    half=alex.parse(word); full=alex.symmetrize(half)
    return full is not None and alex.diagram(full) is not None
def flip(word, idxs):
    t=word.split('.')
    for i in idxs:
        a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
def crossing_tokens(word):
    t=word.split('.')
    return [i for i,a in enumerate(t) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
def padd(p,q,c=1):
    for e,v in q.items():
        nv=p.get(e,0)+c*v
        if nv: p[e]=nv
        elif e in p: del p[e]
def alt_sum(Js):
    """Js: dict S(tuple of 0/1) -> Laurent dict. Returns sum (-1)^|S| J_S."""
    out={}
    for S,J in Js.items(): padd(out,J,(-1)**sum(S))
    return out
def div1pt(p):
    """exact division of Laurent poly p by (1+t); returns quotient or None."""
    if not p: return {}
    p=dict(p); lo=min(p); hi=max(p); q={}
    for e in range(lo,hi):
        c=p.get(e,0)
        if c: q[e]=c; p[e]=0; p[e+1]=p.get(e+1,0)-c
    if any(p.get(e,0) for e in range(lo,hi+1)): return None
    return {e:c for e,c in q.items() if c}
def xorder(p, cap=40):
    """largest k with (1+t)^k | p (cap if p==0)."""
    k=0
    while k<cap:
        if not p: return cap
        q=div1pt(p)
        if q is None: return k
        p=q; k+=1
    return k
def quot_at_m1(p,m):
    """[p/(1+t)^m](t=-1), p divisible by (1+t)^m."""
    for _ in range(m):
        p=div1pt(p); assert p is not None
    return sum(c*(-1)**(e%2) for e,c in p.items())
def configs(word, sites):
    Js={}
    for S in itertools.product([0,1],repeat=len(sites)):
        J=lp.J(flip(word,[s for s,b in zip(sites,S) if b]))
        if J is None: return None
        Js[S]=J
    return Js
