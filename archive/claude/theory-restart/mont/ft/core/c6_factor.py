# Factor f(t) := J(-t) - V_K(t^2) for sample words; find the common cyclotomic divisor.
import sys, random, collections
import clib, lp, sympy as sp
t=sp.symbols('t')
def topoly(P):
    lo=min(P); return sp.expand(sum(c*t**(e-lo) for e,c in P.items())), lo
rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
common=None; seen=set(); n=0; facs=collections.Counter()
ex=[]
cases=['s.l1.y0.x1.u2','s.l1.y0.y0.x1.u2','s.l1.y0.x1.y0.x1.u2','s.l1.x0.x0.x0.x1.x1.u2']
while n<N:
    if cases: w=cases.pop(0); J=lp.J(w)
    else:
        w,J=clib.randJ(rnd,6,14)
    if w in seen: continue
    seen.add(w); V=clib.VK(w)
    if V is None: continue
    Jm={e:c*(-1)**(e%2) for e,c in J.items()}
    V2={2*e:c for e,c in V.items()}
    f=lp.sub(Jm,V2)
    n+=1
    if not f: facs['f=0']+=1; continue
    pf,lo=topoly(f)
    fl=sp.factor_list(pf)
    cyc=[]
    for fac,mult in fl[1]:
        # identify cyclotomic factors
        for m in range(1,61):
            if sp.expand(fac-sp.cyclotomic_poly(m,t))==0 or sp.expand(fac+sp.cyclotomic_poly(m,t))==0:
                cyc.append((m,mult))
    cyc_d=dict(cyc)
    for m,mu in cyc: facs[(m,mu)]+=1
    common=cyc_d if common is None else {m:min(mu,cyc_d.get(m,0)) for m,mu in common.items() if cyc_d.get(m,0)>0}
    if len(ex)<4: ex.append((w,sorted(cyc_d.items()),fl[0]))
print('samples',n)
print('common cyclotomic divisor of J(-t) - V_K(t^2): {Phi_m: multiplicity}:',common)
print('content/examples:'); [print('  ',e) for e in ex]
print('frequency of (m,mult):',sorted(facs.items(),key=lambda kv:str(kv[0]))[:40])
