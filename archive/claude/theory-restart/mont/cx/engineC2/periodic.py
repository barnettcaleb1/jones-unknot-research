"""Rate test for general (possibly pseudo-Anosov) operators: span J((W0)^n) for periodic S2 families."""
import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import plat2, lp, enum2
res=[]
seenW=set()
for L in range(2,5):
    for W0 in itertools.product('aAbBdD',repeat=L):
        W0=''.join(W0)
        if any(plat2.INVL[W0[i]]==W0[(i+1)%L] for i in range(L)): continue
        if W0 in seenW: continue
        rots={W0[i:]+W0[:i] for i in range(L)}; seenW|=rots
        sp=[]
        for n in range(1,9):
            w=W0*n
            if len(w)>16: break
            if not plat2.is_arc(w): sp.append(None); continue
            J=plat2.J(w); sp.append(lp.span(J))
        vals=[(i+1,s) for i,s in enumerate(sp) if s is not None]
        if len(vals)>=3:
            (n1,s1),(n2,s2)=vals[-2],vals[-1]
            rate=(s2-s1)/(n2-n1)
            res.append((rate,W0,vals))
res.sort()
print('families',len(res))
print('smallest growth rates:',[(r[0],r[1],r[2]) for r in res[:12]])
nz=[r for r in res if r[0]<=0 and any(s>0 for n,s in r[2])]
print('non-growing families with nonconstant/nonunit J:',[(r[1],r[2]) for r in nz][:10])
