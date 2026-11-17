#!/usr/bin/env python3
"""Analyse one doubled tangle output folder: lattice picture, l-graded comparison with Kh~(K)^2, hull, extremes."""
import sys,os,collections,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import parse_file,bgens
from hullmod import hull
def khK(fn):
    gens=[]
    for l in open(fn).read().splitlines():
        m=re.match(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*)$',l)
        if not m: continue
        h,q=int(m.group(1)),int(m.group(2)); ch=m.group(4).strip()
        if ch=='⬮': gens.append((h,q))
        else:
            mm=re.match(r'^⬮——H(\^(\d+))?—>⬮$',ch); k=int(mm.group(2)) if mm.group(2) else 1
            gens.append((h,q)); gens.append((h+1,q+2*k))
    return gens
def run(dbl,knot):
    comps=parse_file(dbl)
    arc=[c for c in comps if not c['cyclic']][0]
    syms=[g[0] for g in arc['gens']]
    bs=bgens(arc)
    rho=bs[0] if syms[0]=='⬯' else bs[-1]
    def ab(h,q):
        h-=rho[0]; q-=rho[1]; b2=2*h-q; assert b2%2==0; b=b2//2; return (h-5*b,b)
    print('arc b-generators (a,b):',[ab(h,q) for h,q in bs])
    print('arc arrows between b-gens:',[(t,p) for (i,j,t,p) in arc['arrows'] if arc['gens'][i][0]=='⬮' and arc['gens'][j][0]=='⬮'])
    pts=[ab(h,q) for h,q in bs]
    sq=[]
    for c in comps:
        if not c['cyclic']: continue
        P=sorted(ab(h,q) for h,q in bgens(c)); sq.append(P); pts+=P
    print('compact components (b-gens):',sq)
    S=collections.Counter(pts)
    A=[a for a,b in S]; B=[b for a,b in S]
    print('dim N =',len(pts))
    for b in range(max(B),min(B)-1,-1):
        print('b=%3d  '%b+''.join((('%d'%S[(a,b)]) if S[(a,b)] else '.')+('*' if (a,b)==(0,0) else ' ') for a in range(min(A),max(A)+1)))
    print('       a from %d to %d'%(min(A),max(A)))
    kh=khK(knot)
    print('Kh~(K) (h,q):',kh,' rank',len(kh))
    lN=collections.Counter(-(a+3*b) for a,b in pts)   # l = h-q = -(a+3b) rel rho
    lK=collections.Counter((h1-q1)+(h2-q2) for h1,q1 in kh for h2,q2 in kh)
    # compare up to shift: Morse inequalities P_N - x^t P_K = (1+x) R, R>=0
    mN=min(lN); mK=min(lK)
    print('l-distribution of N   (shifted to start at 0):',[lN[mN+i] for i in range(max(lN)-mN+1)])
    print('l-distribution of Kh~^2 (shifted to start at 0):',[lK[mK+i] for i in range(max(lK)-mK+1)])
    H=hull(pts); print('hull vertices:',H)
    edges=set()
    import math
    for i in range(len(H)):
        p,q2=H[i],H[(i+1)%len(H)]; d=(q2[0]-p[0],q2[1]-p[1]); g=math.gcd(abs(d[0]),abs(d[1]))
        d=(d[0]//g,d[1]//g)
        if d[0]<0 or (d[0]==0 and d[1]<0): d=(-d[0],-d[1])
        edges.add(d)
    print('hull edge directions:',sorted(edges))
    qs=collections.Counter(2*a+8*b for a,b in pts)
    print('dim top q:',qs[max(qs)],' dim bottom q:',qs[min(qs)])
    f=lambda g:(min(g(a,b) for a,b in pts),max(g(a,b) for a,b in pts))
    print('ranges: b',f(lambda a,b:b),' a',f(lambda a,b:a),' a+b',f(lambda a,b:a+b),' a+2b',f(lambda a,b:a+2*b),' a+3b',f(lambda a,b:a+3*b))
    chi=collections.Counter()
    for a,b in pts: chi[a+4*b]+=(-1)**(a+b)
    print('chi (t-exponent:coeff):',{k:v for k,v in sorted(chi.items()) if v})
if __name__=='__main__': run(sys.argv[1],sys.argv[2])
