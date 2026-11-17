# R3 scope referee: check general bodies (general_boxes.json) against the note's hypotheses
import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
import flat_search as fs, alex
from kauffman import padd, pdelta
D=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
def todict(lst): return {e:c for e,c in lst}
def n0(B): return sum(1 for tok in B.split('.') if tok in ('x0','y0'))
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def ratio_unit(p,q):
    # is p = +-t^k q ?
    if not p or not q: return None
    k=top(p)-top(q); s=p[top(p)]//q[top(q)] if q[top(q)] else None
    if s not in (1,-1): return None
    return (s,k) if p==shift({e:s*c for e,c in q.items()},k) else None
def divexact(p,d):
    # exact division of Laurent poly p by d (dict), return None if not exact
    p=dict(p); q={}
    if not p: return {}
    dt=top(d); dc=d[dt]
    while p:
        pt=top(p); c=p[pt]
        if c%dc: return None
        e=pt-dt; q[e]=c//dc
        for f,g in d.items():
            p[e+f]=p.get(e+f,0)-q[e]*g
        p=clean(p)
        if p and top(p)<bot(d)+e and False: return None
        if p and len(q)>500: return None
        if p and top(p) < min(p)+0 and False: pass
        if p and top(p) < bot(d)+bot({e:1})-1000: return None
        if p and top(p) < dt + min(q) - 1 - 0 and top(p)-dt < min(q)-200: return None
    return clean(q)
ONE_MINUS_T4=P((1,0),(-1,4))
res=[]
for i,(B,vv) in enumerate(D):
    v=[todict(vv[0]),todict(vv[1])]
    a=a_of(v); b=b_of(v)
    # knot / body check: s.B is a knot (alex.diagram not None), single through arc
    half=alex.parse('s.'+B); full=alex.symmetrize(half); ok_knot = full is not None and alex.diagram(full) is not None
    # root sign
    s_a=ev(a,-1); s_b=ev(b,-1)
    eps=s_b//s_a if s_a in (1,-1) else None
    # scalar test
    sc=ratio_unit(b,a)
    # two raw closures recipe
    al0=J_raw('s.r2.'+B+'.u1'); alm1=J_raw('s.r2.'+tw(-1)+B+'.u1')
    num=sub(mul(mono(2),alm1),al0)
    v2=divexact(num,ONE_MINUS_T4)
    rv=None
    if v2 is not None:
        w=[al0,v2]
        # compare to stored v up to common unit
        k=top(a)-top(al0); s=a[top(a)]*al0[top(al0)]
        s=1 if s>0 else -1
        ws=[shift({e:s*c for e,c in w[0].items()},k), shift({e:s*c for e,c in w[1].items()},k)]
        rv = (ws[0]==v[0] and ws[1]==v[1])
    res.append((i,B,ok_knot,n0(B),eps,(-1)**n0(B),sc,rv))
    print(i,B,'knot',ok_knot,'n0',n0(B),'eps',eps,'(-1)^n0',(-1)**n0(B),'scalar',sc,'2raw==stored',rv)
print('ALL knots:',all(r[2] for r in res))
print('eps==(-1)^n0 all:',all(r[4]==r[5] for r in res))
print('2raw recipe agrees all:',all(r[7] for r in res))
print('scalar bodies:',[(r[0],r[1],r[6]) for r in res if r[6]])
