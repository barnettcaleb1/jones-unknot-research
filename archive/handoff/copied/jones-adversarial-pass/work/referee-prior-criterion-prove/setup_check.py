import sys; sys.path.insert(0,sys.argv[1])
from w60 import *
# basis listing
for i,m in enumerate(BASIS): print(i, [(a+1,m[a]+1) for a in range(NP) if a<m[a]])
TC=[1,2]*3
# find eigenvector of rho(TC) with eigenvalue A^6: solve via projector (T - A^-6) applied to basis vectors
M=rmat(TC)
cand=None
for j in range(DIM):
    e=[{} for _ in range(DIM)]; e[j]={0:1}
    Te=rvec(TC,e); w=[ladd(Te[i], lsh(e[i],-6), -1) for i in range(DIM)]
    if any(w): print('col',j,'(T-A^-6)e_j =',[lstr(x) for x in w])
