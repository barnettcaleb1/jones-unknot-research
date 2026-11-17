"""compare lpgen's case_rows (lpg.py, imported read-only) with the independently derived rows: same affine solution set
(row-space equality of the augmented systems) at 40 random rational points (p1,p2,q1,q2,m)."""
import sys, pickle
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import lpg
VARS=['al','P','La','Lam','RA','LA','RB','LB','mB','None']
def rank(rows):
    M=[list(r) for r in rows]; rk=0; nc=len(M[0]) if M else 0
    for c in range(nc):
        piv=None
        for i in range(rk,len(M)):
            if M[i][c]!=0: piv=i; break
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
def theirs(row,msub=None):
    coef,a=row
    r=[Fr(0)]*10
    for i in range(4): r[i]+=coef[i]
    # minus aff: a = (c, ra, la, rb, lb, mB)
    r[4]-=a[1]; r[5]-=a[2]; r[6]-=a[3]; r[7]-=a[4]
    if msub is None: r[8]-=a[5]; r[9]-=a[0]
    else: r[9]-=a[0]+a[5]*msub
    return r
def mine(d,msub=None):
    r=[d[v] for v in VARS]
    if msub is not None:   # (already substituted in derivation for d=0 cases)
        pass
    return r
D=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/derived_numeric.pkl','rb'))
bad=[]; ok=0
for pt,rows in D:
    p=(pt['p1'],pt['p2']); q=(pt['q1'],pt['q2']); m=pt['m']
    T=dict(lpg.case_rows(p,q)); T0=dict(lpg.case_rows(p,q,m=m))
    for nm,lst in rows.items():
        if nm.startswith('d=0'):
            th=[theirs(r,msub=m) for r in T0[nm]]
        else:
            th=[theirs(r) for r in T[nm]]
        for variant in lst:
            mi=[[x[v] for v in VARS] for x in variant]
            r1,r2,r3=rank(mi),rank(th),rank(mi+th)
            if r1==r2==r3: ok+=1
            else: bad.append((nm,pt,r1,r2,r3))
print('case systems compared:',ok+len(bad),'identical solution sets:',ok,'DIFFERENT:',len(bad))
for b in bad[:10]: print('  ',b)
# names coverage
print('lpgen offset cases:',[nm for nm,_ in lpg.case_rows((0,0),(0,0))])
print('lpgen d=0 cases (m=1):',[nm for nm,_ in lpg.case_rows((0,0),(0,0),m=Fr(1))],' (m=0):',[nm for nm,_ in lpg.case_rows((0,0),(0,0),m=Fr(0))])
