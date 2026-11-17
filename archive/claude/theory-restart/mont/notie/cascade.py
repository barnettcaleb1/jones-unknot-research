from nt import *
def info(mu,N,ss):
    vs=[box(s) for s in ss]; Jv=neck(mu,N,vs); A=prod(vs)[0]
    T=top(Jv)+2-top(A)
    return dict(span=span(Jv),spanA=span(A),T=T,diff=span(Jv)-span(A))
print(info(3,0,[(-5,-1,-1),(-2,)+(-1,)*10]))
for m in (2,3,5,8):
    for jj in (3,6,10,14):
        print(m,jj,info(3,0,[(-m,-1,-1),(-2,)+(-1,)*jj]))
