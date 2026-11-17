import sys, time, random
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
Lmax=int(sys.argv[2]); B=int(sys.argv[3]); which=sys.argv[4] if len(sys.argv)>4 else 'A'
conjsets={'A':{'c':[], 'x':[3], 'y':[4,3,2,3]},
          'B':{'c':[], 'x':[-3,2,-4], 'y':[5,-3,4,2,-3]}}
ctx=make_ctx(Lmax,conjsets[which])
letters=[(s,e) for s in ctx['names'] for e in (1,-1)]
random.seed(7)
t0=time.time()
beam=[((),unit5(ctx))]
worst_margin=None
for L in range(1,Lmax+1):
    cand=[]
    for w,X in beam:
        for (s,e) in letters:
            if w and w[-1]==(s,-e): continue
            Y=rmul_gen(ctx,X,s,e); cand.append((Dspan(Y),random.random(),w+((s,e),),Y))
    cand.sort(key=lambda t:(t[0],t[1]))
    # keep diversity: best B overall
    beam=[(w,Y) for (_,_,w,Y) in cand[:B]]
    m=cand[0][0]; marg=m-(8*L+16)
    worst_margin=marg if worst_margin is None else min(worst_margin,marg)
    if True:
        print('L=%d beam-minD=%d  8L+16=%d margin=%d  minD/L=%.2f t=%.0fs  w=%s'%(L,m,8*L+16,marg,m/L,time.time()-t0,''.join(s if e>0 else s.upper() for s,e in cand[0][2])),flush=True)
print('worst margin over beam',worst_margin)
