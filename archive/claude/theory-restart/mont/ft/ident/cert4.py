import sys, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import lp, modrank
from fractions import Fraction as F
exec(open('fit4.py').read().split('import modrank')[0].replace('import sympy as sp',''))  # reuse rows/feats definitions
def val2(r,f):
    out=F(1)
    for g in f.split('*'): out*=F(str(r[g]))
    return out
A=[[val2(r,f) for f in feats] for r in rows]; b=[val2(r,'F4') for r in rows]
c=modrank.certificate(A,b)
if c is None: print('F4 IS in the span (no certificate)')
else:
    y,val=c
    print('F4 certificate: %d words, y.F4 = %s'%(len(y),val))
    # verify exactly
    for j,f in enumerate(feats):
        s=sum(y[i]*A[i][j] for i in y); assert s==0,(f,s)
    print('verified: y annihilates all %d candidate columns'%len(feats))
    json.dump({'words':[rows[i]['w'] for i in y],'y':[str(y[i]) for i in y],'feats':feats},open('cert_F4.json','w'))
# D at value level against order<=3 odd candidates incl. products with N1
featsD=['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout','SLax','N1','N3','N1*N2','N1*N1*N1']+['N1*'+k+'.a2' for k in ['K','Kin','Kout','Uin','Uout']]
A=[[val2(r,f) for f in featsD] for r in rows]; b=[val2(r,'D') for r in rows]
c=modrank.certificate(A,b)
print('D value-level certificate:', None if c is None else (len(c[0]),c[1]))
