"""Integrator NOTE 03:02 check: vertical closures V_a(Y^N (F_k(p) * F_k(p)~)) with mirror-paired nested bodies.
F_k(p) has slopes (1 at top, eps at bottom) for k>0; its mirror has (eps, 1): the pair has slope -> eps at BOTH ends."""
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lib, lp
def mir(v): return ({-e:c for e,c in v[0].items()},{-e:c for e,c in v[1].items()})
R5=lib.rational(5)
t0=time.time(); n=0; units=[]; best=None
for key,p,T,tag in R5:
    for k in range(1,7):
        for sgn in (1,-1):
            try: f=vc.F(sgn*k,p)
            except AssertionError: continue
            v=vc.star(f,mir(f))
            if v[0]==v[1]: continue
            for a in [-9,-7,-5,-3,3,5,7,9]:
                for N in range(-25,26):
                    J=vc.J_vert(a,vc.Ypow(N,v)); n+=1
                    if J is None: continue
                    if len(J)==1: units.append((T,sgn*k,a,N))
                    s=lp.span(J)
                    if best is None or s<best[0]: best=(s,T,sgn*k,a,N,lp.a2(J))
print('vertical closures of mirror-paired nested bodies:',n,'evaluations; units',len(units),units[:5],'; min span J',best,' time %.0f'%(time.time()-t0))
