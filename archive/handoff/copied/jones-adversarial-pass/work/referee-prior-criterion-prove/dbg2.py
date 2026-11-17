import sys; sys.path.insert(0,sys.argv[1])
from w60 import *
vc=[{2:1,-2:1},{0:1},{0:1},{2:1,-2:1},{4:1,0:1,-4:1}]
TC=[1,2]*3
kap=lmul(lmul({12:1},{6:1,-6:1}),{2:1,-2:1})
for j in range(DIM):
    e=[{} for _ in range(DIM)]; e[j]={0:1}
    lhs=rvec(TC*2,e)
    Ns={0:1} if j==4 else {}
    rhs=[lsh(ladd(e[i],lmul(lmul(kap,Ns),vc[i])),-12) for i in range(DIM)]
    print(j,[lstr(ladd(lhs[i],rhs[i],-1)) for i in range(DIM)])
