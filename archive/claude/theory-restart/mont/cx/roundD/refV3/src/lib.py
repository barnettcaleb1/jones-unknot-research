"""Box library for ENGINE A.  A box = (key, v, T, tag) with v = normalised channel vector canonical mod Y
(d_top(q) = top b - top a in {0,1,2}), T = vc tree (halfword via vc.hw / vc.word), tag = family label."""
import sys, itertools, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import vc
from vc import top, bot, shift
INV={'X':'x','x':'X','Y':'y','y':'Y'}
def canonY(v,T):
    a,b=v
    n=(top(b)-top(a))//3
    if n==0: return v,T
    v2=(a,shift(b,-3*n))
    T2=('p',[T,('w',('Y' if n>0 else 'y')*abs(n))])
    return v2,T2
def vkey(v): return (tuple(sorted(v[0].items())),tuple(sorted(v[1].items())))
def rational(Lmax):
    seen={}
    for L in range(1,Lmax+1):
        for w in itertools.product('XxYy',repeat=L):
            w=''.join(w)
            if w[0] in 'Yy': continue
            if any(INV[w[i]]==w[i+1] for i in range(L-1)): continue
            v=vc.rat(w)
            if len(v[0])==1: continue        # integral (unknot closure)
            v2,T=canonY(v,('w',w))
            k=vkey(v2)
            if k not in seen: seen[k]=(k,v2,T,'R')
    return list(seen.values())
NONRAT=[3,4,9,12,26,27,30,33,39,41,43,45,47,48]   # 6,35,44 have SCALAR states (local knot on the arc) and are excluded   # general_boxes.json indices NOT reducible to rational (ratred.py);
# the other 33 entries are rational vectors (18 distinct mod Y) or duplicates mod Y.
def general():
    out={}
    for i,(B,v) in enumerate(vc.gboxes()):
        if i not in NONRAT: continue
        v2,T=canonY(v,('g',i))
        k=vkey(v2)
        if k not in out: out[k]=(k,v2,T,'G')
    return list(out.values())
def node(m,N,kids):
    """box F_m(Y^N * prod kids) canonical mod Y; kids = list of boxes"""
    p=vc.starall([c[1] for c in kids])
    if N: p=vc.Ypow(N,p)
    if p[0]==p[1]: return None          # scalar product: F_m acts trivially
    v=vc.F(m,p)
    T=('n',m,[c[2] for c in kids]+([('w',('Y' if N>0 else 'y')*abs(N))] if N else []))
    v2,T2=canonY(v,T)
    return (vkey(v2),v2,T2,'N'+''.join(c[3] for c in kids))
