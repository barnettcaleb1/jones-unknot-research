from nt import *
from lp import ev
import itertools
from collections import Counter
def sder(f):  # f'(-1)/f(-1)
    v=ev(f,-1); d=sum(e*c*(-1)**((e-1)%2) for e,c in f.items())
    return v,d
seqs=normal_seqs(3,3)
C=Counter()
for s in seqs[:60]:
    u=box(s); a,b=chan(u)
    va,da=sder(a); vb,db=sder(b); v2=ev(u[1],-1)
    sa=da//va if da%va==0 else None
    print(s,'a(-1)',va,'b(-1)',vb,'v2(-1)',v2,'s(a)',sa,'norm bot a',bot(a)+sa,'norm top a',top(a)+sa)
