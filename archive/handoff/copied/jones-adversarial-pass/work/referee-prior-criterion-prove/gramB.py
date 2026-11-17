import sys; d=sys.argv[1]; sys.path.insert(0,d)
from fastD import make_ctx
from w60 import lstr, lmul
ctx=make_ctx(4,{'c':[], 'x':[-3,2,-4], 'y':[5,-3,4,2,-3]})
for a in 'cxy': print(a,[lstr(ctx['N'][(a,b)]) for b in 'cxy'])
cyc=lmul(lmul(ctx['N'][('c','x')],ctx['N'][('x','y')]),ctx['N'][('y','c')]); print('cyclic',lstr(cyc))
