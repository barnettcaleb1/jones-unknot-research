"""Sanity: actual half-diagram words mont(m,rows) (knot-level J via lp.J) are non-units and match the necklace formula."""
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from lp import J, normalize, span, close, star, apply
from words import mont
def vrow(r):
    j=(abs(r)-1)//2
    return apply(('X'*j+'Y') if r>0 else ('x'*j+'y'))
t0=time.time(); ok=0; units=0; mism=0; skip=0
for rows in [[3,-3],[3,-5],[-3,5,-3],[5,-5],[3,3,-3],[-3,-3,-3],[7,-3],[3,-3,3,-3],[-5,3]]:
    for m in (-2,-1,1,2):
        w=mont(m,rows); Jw=J(w)
        if Jw is None: skip+=1; continue
        p=vrow(rows[0])
        for r in rows[1:]: p=star(p,vrow(r))
        F=normalize(close(-m,p))
        if F!=Jw: mism+=1
        if span(Jw)==0: units+=1
        ok+=1
print('pretzel words checked',ok,'formula mismatches',mism,'units',units,'skipped(non-knots)',skip,'time',round(time.time()-t0,1))
