from nt import *
from auto2 import run
from fractions import Fraction
from collections import Counter
import itertools
def alt_neg_end(s):
    return s[-1]<0 and all((s[i]>0)!=(s[i+1]>0) for i in range(len(s)-1))
C=Counter(); chk=0
for s in normal_seqs(5,4):
    st,rho=run(s)
    if st[0]=='S' and rho==0:
        chk+=1
        assert alt_neg_end(s), s
        a=box(s)[0]; e=top(a)
        x2=Fraction(a.get(e-2,0),a[e]); x1=Fraction(a.get(e-1,0),a[e])
        C[(x1,x2, 'k=1' if len(s)==1 else ('last=-1' if s[-1]==-1 else 'last<=-2'))]+=1
    elif alt_neg_end(s):
        print('alt but rho!=0?',s,st,rho)
print(chk, sorted(C.items(),key=str))
