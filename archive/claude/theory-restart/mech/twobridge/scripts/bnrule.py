import sympy as sp
from collections import Counter
from parse import recs
from norm import strip
from rule import G_of, u, v
def polys(r):
    j=int(r['j']); k=r['k']
    w=strip(r['runs'])
    pos=all(n>0 for t,n in w)
    C=sp.Integer(0)
    for b in r['bn']:
        if not b['cyclic']: continue
        c=b['q']+4-24*j; d=int(b['delta'])-4*j
        if not pos:   # mirror: special pair at offsets q+4,q+6 -> mirrored pair; lower one after mirroring is -(q+6)
            c=-(b['q']+6-24*j); d=1-d
            kk=-k
        else: kk=k
        i=(c-(2*kk-2))//2; l=d-1
        C+=u**i*v**l
    return w,pos,C
if __name__=='__main__':
    seen=set()
    for r in recs():
        if r['dup'] or not r['runs']: continue
        w,pos,C=polys(r)
        if not w or not pos: continue
        key=tuple(n for _,n in w)
        if key in seen: continue
        seen.add(key)
        G,Gam=G_of(w)
        R=sp.expand(G-(1+u)*C)
        print(key,'| C =',sp.factor(C) if C!=0 else 0,'| arc part R =',sp.factor(R) if R!=0 else 0)
