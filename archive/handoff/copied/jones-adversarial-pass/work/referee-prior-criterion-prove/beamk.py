"""Beam search: min over reduced words of D(rho(w)) - (8L+16) for k-curve systems (squared 3|3 twists)."""
import sys, time, random
d=sys.argv[1]; sys.path.insert(0,d)
from fastD import *
Lmax=int(sys.argv[2]); B=int(sys.argv[3]); which=sys.argv[4]
sets={'cxyu':{'c':[], 'x':[3], 'y':[4,3,2,3], 'u':[5,4,-2,3]},
      'cxyuv':{'c':[], 'x':[3], 'y':[4,3,2,3], 'u':[5,4,-2,3], 'v':[2,3,4,5,1]},
      'cxyz':{'c':[], 'x':[3], 'y':[4,3,2,3], 'z':[-2,4,3,-5]},
      'cxyzuv':{'c':[], 'x':[3], 'y':[4,3,2,3], 'z':[-2,4,3,-5], 'u':[5,4,-2,3], 'v':[2,3,4,5,1]}}
ctx=make_ctx(Lmax,sets[which])
letters=[(s,e) for s in ctx['names'] for e in (1,-1)]
random.seed(11); t0=time.time()
beam=[((),unit5(ctx))]; worst=None
for L in range(1,Lmax+1):
    cand=[]
    for w,X in beam:
        for (s,e) in letters:
            if w and w[-1]==(s,-e): continue
            Y=rmul_gen(ctx,X,s,e); cand.append((Dspan(Y),random.random(),w+((s,e),),Y))
    cand.sort(key=lambda t:(t[0],t[1])); beam=[(w,Y) for (_,_,w,Y) in cand[:B]]
    m=cand[0][0]; marg=m-(8*L+16); worst=marg if worst is None else min(worst,marg)
    if L<=8 or L%4==0:
        print('L=%d minD=%d 8L+16=%d margin=%d D/L=%.2f t=%.0fs w=%s'%(L,m,8*L+16,marg,m/L,time.time()-t0,''.join(s if e>0 else s.upper() for s,e in cand[0][2])),flush=True)
print(which,'worst margin',worst)
