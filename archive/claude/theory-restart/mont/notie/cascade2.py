from nt import *
def sp(mu,N,ss): return span(neck(mu,N,[box(s) for s in ss]))
for m in (2,5):
    for jj in (3,6,10,14):
        u2=(-2,)+(-1,)*jj
        print(m,jj,'J(3;(-m,-1,-1),u2)=',sp(3,0,[(-m,-1,-1),u2]),' J(1;(-m),u2)=',sp(1,0,[(-m,),u2]),' J(2;(-m,-1),u2)=',sp(2,0,[(-m,-1),u2]),
              ' a-spans',span(box((-m,-1,-1))[0]),span(box(u2)[0]))
