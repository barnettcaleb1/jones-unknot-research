# R3: check raw closure identity alpha_m(B) = U_m * c(B) * e1^T X^{-m} v(B), U_m universal (from empty body), for all 50 general bodies
import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *
import flat_search as fs, alex
from kauffman import padd, pdelta
D=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))
def todict(l): return {e:c for e,c in l}
def tw(m): return ('y1.' if m>0 else 'x1.')*abs(m)
def raw_parts(word):
    half=alex.parse(word); y,x=fs.bracket_vector(half)
    u={}; padd(u,y); padd(u,pdelta(x)); u={e:c for e,c in u.items() if c}
    return y,x,u
# u monomials for several words
us=set()
for B,_ in D[:50]:
    for m in (-2,-1,0,1,2):
        y,x,u=raw_parts('s.r2.'+tw(m)+B+'.u1'); us.add(tuple(sorted(u.items())))
    for a in (-3,-1,1,3):
        y,x,u=raw_parts('s.l1.'+B+'.'+('x2.' if a>0 else 'y2.')*abs(a)+'u1'); us.add(tuple(sorted(u.items())))
print('distinct u monomials over horizontal+vertical closures:',us)
U={m:J_raw('s.r2.'+tw(m)+'u1') for m in (-3,-2,-1,1,2,3)}
U[0]=J_raw('s.r2.u1')
print('U_m (empty body):',{m:sorted(v.items()) for m,v in U.items()})
bad=0; tot=0
for i,(B,vv) in enumerate(D):
    v=[todict(vv[0]),todict(vv[1])]
    al={m:J_raw('s.r2.'+tw(m)+B+'.u1') for m in (-3,-2,-1,0,1,2,3)}
    cs=set()
    for m,am in al.items():
        pred=mul(U[m],close(-m,v))   # close(-m,v)= e1^T X^{-m} v
        # am = c * pred, c a signed monomial independent of m
        k=top(am)-top(pred); s=am[top(am)]//pred[top(pred)]
        ok = am==shift({e:s*c for e,c in pred.items()},k)
        cs.add((s,k) if ok else None); tot+=1
    if len(cs)!=1 or None in cs: bad+=1; print('MISMATCH body',i,B,cs)
print('bodies with m-independent c(B) for m=-3..3:',50-bad,'/ 50')
