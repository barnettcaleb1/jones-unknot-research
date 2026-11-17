"""Check the T1-pretzel (all rows negative, mu>=1, k=0) top formula for H = G/Phi6^n and the span >= 3n consequence."""
from pretz import *
import itertools
PHI6n=lambda n: (lambda r: r)(None)
def topH(mu,rows):
    g=G(mu,rows); n=len(rows)
    return top(g)-2*n
def predT1(mu,ls):
    ls=sorted(ls); lmin=ls[0]; s=ls.count(lmin)
    if lmin<mu: return mu+2-lmin
    if lmin>mu or s>=2: return 2
    if len(ls)==1: return -1
    return max(-1,mu+2-ls[1])
bad=0; cnt=0; minsp={}
for n in (2,3,4):
    for ls in itertools.combinations_with_replacement(range(1,8),n):
        rows=[-(2*l+1) for l in ls]
        for mu in range(1,7):
            cnt+=1
            if topH(mu,rows)!=predT1(mu,list(ls)): bad+=1; print('BAD',mu,ls,topH(mu,rows),predT1(mu,list(ls)))
            sp=span(G(mu,rows))-2
            minsp[n]=min(minsp.get(n,99),sp)
print('T1 pretzel top formula: checked',cnt,'bad',bad,'min span by n',minsp)
