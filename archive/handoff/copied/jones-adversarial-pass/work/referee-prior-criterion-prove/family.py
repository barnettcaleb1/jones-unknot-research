import sys; d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
which=sys.argv[2]; pre=sys.argv[3]; per=sys.argv[4]; K=int(sys.argv[5])
sets={'A':{'c':[], 'x':[3], 'y':[4,3,2,3]}, 'B':{'c':[], 'x':[-3,2,-4], 'y':[5,-3,4,2,-3]}}
ctx=make_ctx(len(pre)+len(per)*K+4,sets[which])
def app(X,s):
    for ch in s: X=rmul_gen(ctx,X,ch.lower(),1 if ch.islower() else -1)
    return X
X=app(unit5(ctx),pre); print('prefix',pre,'D=',Dspan(X) if pre else 0)
prev=None
for k in range(1,K+1):
    X=app(X,per); L=len(pre)+k*len(per); Dv=Dspan(X)
    print('k=%d L=%d D=%d  8L+16=%d margin=%d  inc=%s'%(k,L,Dv,8*L+16,Dv-8*L-16, (Dv-prev) if prev is not None else '-')); prev=Dv
