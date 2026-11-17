# Untwisted Whitehead double L = Wh(3_1) (Alexander polynomial 1, so a_2 = 0 and all abelian knot invariants trivial).
# Computes V_L (check a_2 = 0) and J_3(L) via 2-cable sweeps; J of the local-knot inversion (L # rL, swap) equals J_3(L) (Schur).
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
from kauffman import padd, pshift, pdelta, cap, cup
import lp
from fractions import Fraction as F
def sweep(ops):
    state={():{0:1}}
    for c,i in ops:
        new={}
        for m,p in state.items():
            if c=='cap': padd(new.setdefault(cap(m,i),{}),p)
            elif c=='cup':
                m2,loop=cup(m,i); padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=cup(m,i); q=pdelta(p) if loop else p
                padd(new.setdefault(cap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    return state.get((),{})
def cable(ops):
    out=[]
    for c,i in ops:
        if c=='cap': out+=[('cap',2*i),('cap',2*i+1)]
        elif c=='cup': out+=[('cup',2*i+1),('cup',2*i)]
        else: out+=[(c,2*i+1),(c,2*i),(c,2*i+2),(c,2*i+1)]
    return out
def pdiv(p,q):
    if not p: return {}
    p=dict(p); out={}; qt=max(q); qb=min(q); qc=q[qt]
    while p:
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
def to_t(p):
    es=set(e%4 for e in p); assert len(es)==1, es
    r=min(p)%4
    return {-(e-r)//4:c for e,c in p.items()}
def normV(V):   # V(1)=1, V'(1)=0
    s=sum(V.values()); V={e:c*s for e,c in V.items()}; d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}
trefoil=[('cap',0),('cap',1),('x',2),('x',2),('x',2),('cup',1),('cup',0)]
def whitehead(base_braid_ops, twist, clasp='x'):
    # base: trefoil closure; double it; add 'twist' full twists (signed) on doubled braid strand (6,7); clasp; close.
    d=cable(base_braid_ops[:-2])               # caps + braid doubled
    tw=[('y' if twist<0 else 'x',6)]*(2*abs(twist))
    cl=[('cap',8),(clasp,7),(clasp,7),('cup',6)]
    return d+tw+cl+cable(base_braid_ops[-2:])
if __name__=="__main__":
  for twist in (-3,):
     W=whitehead(trefoil,twist)
     t0=time.time()
     b=sweep(W); V=normV(to_t(pdiv(b,{2:-1,-2:-1})))
     a2=F(-sum(c*e*(e-1) for e,c in V.items()),6)
     print('twist',twist,'V_L=',sorted(V.items()),' a2=',a2,' (%.1fs)'%(time.time()-t0))
     t0=time.time()
     b2=sweep(cable(W)); padd(b2,{0:-1})
     q=pdiv(b2,{4:1,0:1,-4:1})
     J3=lp.normalize(to_t(q))
     print('   J_3(L) normalised =',sorted(J3.items()),' (%.1fs)'%(time.time()-t0))
     ex=[sum(F(c*(-1)**(e%2)*e**k) for e,c in J3.items())/F(__import__('math').factorial(k)) for k in range(6)]
     print('   J_3(L)(-e^h) coefficients h^0..h^5:',[str(x) for x in ex])
     d2=sum(c*e*(e-1) for e,c in V.items()); d3=sum(c*e*(e-1)*(e-2) for e,c in V.items())
     print('   v3(L)=',F(-(d3+3*d2),36))
