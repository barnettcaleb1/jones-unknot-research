import sys, time
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
Lmax=int(sys.argv[2])
ctx=make_ctx(Lmax,{'c':[], 'x':[3], 'y':[4,3,2,3]})
letters=[(s,e) for s in 'cxy' for e in (1,-1)]
t0=time.time()
layer=[((),unit5(ctx))]
for L in range(1,Lmax+1):
    new=[]; Ds=[]
    for w,X in layer:
        for (s,e) in letters:
            if w and w[-1]==(s,-e): continue
            Y=rmul_gen(ctx,X,s,e); new.append((w+((s,e),),Y)); Ds.append(Dspan(Y))
    layer=new
    m=min(Ds); worst=[layer[i][0] for i,dd in enumerate(Ds) if dd==m][:2]
    print('L=%d words=%d minD=%d (8L+16=%d) maxD=%d  t=%.1fs worst=%s'%(L,len(Ds),m,8*L+16,max(Ds),time.time()-t0,worst[0]),flush=True)
