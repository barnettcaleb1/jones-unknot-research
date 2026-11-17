import sys, time
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
Lmax=int(sys.argv[2]); which=sys.argv[3]
sets={'A':{'c':[], 'x':[3], 'y':[4,3,2,3]}, 'B':{'c':[], 'x':[-3,2,-4], 'y':[5,-3,4,2,-3]}}
ctx=make_ctx(Lmax+2,sets[which]); letters=[(s,e) for s in ctx['names'] for e in (1,-1)]
best={}; t0=time.time(); n=0
stack=[((),unit5(ctx))]
while stack:
    w,X=stack.pop()
    if w:
        L=len(w); m=Dspan(X)-8*L-16; n+=1
        if L not in best or m<best[L][0]: best[L]=(m,w)
    if len(w)<Lmax:
        for (s,e) in letters:
            if w and w[-1]==(s,-e): continue
            stack.append((w+((s,e),),rmul_gen(ctx,X,s,e)))
f=lambda w:''.join(s if e>0 else s.upper() for s,e in w)
for L in sorted(best): print(which,'L=%d min(D-8L-16)=%d  %s'%(L,best[L][0],f(best[L][1])))
print('nodes',n,'t=%.0fs'%(time.time()-t0))
