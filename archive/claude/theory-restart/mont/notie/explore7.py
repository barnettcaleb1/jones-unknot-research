from nt import *
import itertools
from collections import Counter, defaultdict
seqs=[s for s in normal_seqs(3,3)]
B={s:box(s) for s in seqs}
CH={s:chan(B[s]) for s in seqs}
S=[s for s in seqs if s[-1]<0]
def jidx(s):
    # S_j index
    st=None
    for i,m in enumerate(s):
        if i==0: st='R' if m>0 else 0
        else:
            if m>0: st='R'
            elif m<=-2: st=0
            else: st=0 if st=='R' else st+1
    return st
def T1(mu,N,ss):
    A=CH[ss[0]][0]
    for s in ss[1:]: A=mul(A,CH[s][0])
    Jv=neck(mu,N,[B[s] for s in ss])
    return top(Jv)+2-top(A), span(Jv), span(A)
# T1 main case: all S, N=0, mu>0, n=2
rows=[]
for ss in itertools.combinations_with_replacement(S,2):
    for mu in (1,2,3,4):
        T,sp,sA=T1(mu,0,ss)
        Ts=[T1(mu,0,(s,))[0] for s in ss]
        rows.append((mu,T,Ts,[jidx(s) for s in ss],ss,sp,sA))
C=Counter((r[0],r[1]) for r in rows)
print(sorted(C.items()))
# relation T vs single-box Ts
C2=Counter((r[0], r[1]-min(r[2])) for r in rows)
print('T - min single T:',sorted(C2.items()))
for r in rows:
    if r[1]<=-1 : print(r)
