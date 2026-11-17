import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alexall, alex
target=[1,-1,0,0,1,0,-1,0,1,0,0,-1,1]
tok={1:'3',2:'2',3:'1'}
found=[]
def word(gam,ax,let='y'):
    return 's.l2.l1.%s0.'%ax[0]+'.'.join(let+tok[g] for g in gam)+'.%s0.u1.%s0.u1'%(ax[1],ax[2])
# quick filter using determinant |Delta(-1)| = 1 for T(4,5) and Delta(2)
import math
def quick(w):
    try:
        d=alex.alex_eval(w,-1)
    except Exception: return None
    return d
cnt=0
for ax in itertools.product('xy',repeat=3):
    for let in 'xy':
        for gam in itertools.product([1,2,3],repeat=6):
            w=word(gam,ax,let)
            d=quick(w)
            if d!=1: continue
            try: co=alexall.alex_coeffs(w)
            except Exception as e: continue
            if co==target:
                found.append((ax,let,gam,w)); 
                if len(found)<=12: print(ax,let,gam,w,flush=True)
print('found',len(found))
