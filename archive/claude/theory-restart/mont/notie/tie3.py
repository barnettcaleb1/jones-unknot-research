from nt import *
import itertools
def info(mu,N,ss):
    vs=[box(s) for s in ss]; Jv=neck(mu,N,vs); A=prod(vs)[0]
    return span(Jv), span(A), len(ss)
# zero-excess second-order ties: boxes (-2,) [S0] and (1,) [R1]
tests=[(1,4,[(-2,)]*7+[(1,)]*6),(2,4,[(-2,)]*6+[(1,)]*6),(3,4,[(-2,)]*6+[(1,)]*6),(-2,1,[(-2,)]*0+[(1,)]*2+[(-2,)]*1),
       (-3,1,[(1,)]+[(-2,)]),(-3,5,[(1,)]*7+[(-2,)]*7),(-1,1,[(-2,)]*1),(-1,5,[(1,)]*6+[(-2,)]*7),(-2,5,[(1,)]*7+[(-2,)]*6)]
for mu,N,ss in tests:
    rho=sum(1 for s in ss if s[-1]>0); d=2*rho-3*N
    sp,sA,n=info(mu,N,ss)
    print('mu',mu,'N',N,'n',n,'rho',rho,'d',d,'#S0',sum(1 for s in ss if s==(-2,)),'span',sp,'spanA',sA,'4n-3',4*n-3)
