"""Is mB bounded on the ORDER-2 F1 region?  Add  mB >= B+1  (resp. <= -(B+1)) to the uniform F1 LP and ask for an exact Farkas
certificate: if both sides are infeasible, F1 is closed at order 2 for every multiset with |mB| > B."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import lpg, classes, runner
from fractions import Fraction as Fr
B=int(sys.argv[1]); which=sys.argv[2]
S=classes.top(50)+classes.d2pos() if which=='t50' else classes.top(300)+classes.d2pos()
bad=[]; ok=0
for cl in lpg.closure_classes():
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=-1 e=-1']
    for sgn in (1,-1):
        # sgn*(sigma.k - sigstar) >= B+1   <=>   -sgn*sigma.k <= -(B+1) - sgn*sigstar
        ex=[('ub',{j:-sgn*c.sig for j,c in enumerate(S) if c.sig},-(B+1)-sgn*cl['sigstar'])]
        L=lpg.build(S,cl,rows,0,kmin=1,extra=ex)
        d=runner.decide(L)
        if d[0]=='closed': ok+=1
        else: bad.append((cl['name'],sgn,d[0],d[1] if d[0]=='open' else None))
print(which,'B=%d: F1 order-2 LP with |mB| > B: closed %d/%d'%(B,ok,ok+len(bad)))
for b in bad: print('  OPEN',b[:3])
