"""phi bound for the vertical d=0 cases with |mB| >= 15 and exactly two D36 boxes (REPORT 4c)."""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import d2two, lpg
from fractions import Fraction as Fr
T=d2two.T; D=d2two.D36
def phil(c,e):
    ra,la,rb,lb=c.end(e); return (ra+rb)/2, lb-la
for nm,S in (('top300',T),('D36',D)):
    ph=[phil(c,e) for c in S for e in ('top','bot')]
    print(nm,'max phi',max(p for p,l in ph),'max|lam|',max(abs(l) for p,l in ph))
pm=max(phil(c,e)[0] for c in D for e in ('top','bot')); lm=max(abs(phil(c,e)[1]) for c in D for e in ('top','bot'))
print('sigma D36',sorted(set(c.sig for c in D)),'sigma top',sorted(set(c.sig for c in T)))
ok=True
for cl in lpg.closure_classes():
    if cl['kind']!='V': continue
    (p1,p2),(q1,q2)=cl['p'],cl['q']; c0=1-(p1+q1)/2
    m=Fr(15)
    lhs=(m-9)*(Fr(1,2)-2/m)          # N_o (1/2 - 2/m) with N_o >= m - 9
    rhs1=2*pm-c0+(abs(p2-q2)+2*lm)/m
    r0=(2*pm-c0)                      # r=0 needs N_o <= 2(2pm - c0)
    print(cl['name'],'c0',c0,'p2-q2',p2-q2,'| r=1: need %s > %s : %s'%(lhs,rhs1,lhs>rhs1),'| r=0: need 6 > 2(2pm-c0)=%s : %s'%(2*r0,6>2*r0))
    ok&=(lhs>rhs1) and (6>2*r0)
print('phi bound closes all |mB| >= 15 (two D36 boxes):',ok)
