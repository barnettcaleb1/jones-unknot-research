import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'.')
import alexall
from t45b import search
def torus_alex(p,q):
    # coefficients of (t^{pq}-1)(t-1)/((t^p-1)(t^q-1))
    N=(p-1)*(q-1)
    # semigroup method
    S=set()
    for a in range(0,N//p+2):
        for b in range(0,N//q+2):
            S.add(a*p+b*q)
    co=[0]*(N+1)
    for s in S:
        if s<=N: co[s]+=1
        if s+1<=N: co[s+1]-=1
    return co
def word3(gam,c='x',l='y'):   # 3-braid: w = s2 gam s2 rev(gam); fixed points on innermost strand
    tok={2:'1',1:'2'}
    return 's.l1.%s0.'%c+'.'.join(l+tok[g] for g in gam)+'.%s0.u1'%c
def word5(gam,c='x',l='y'):   # 5-braid: w = s2 s4 gam s4 s2 rev(gam)
    tok={4:'1',3:'2',2:'3',1:'4'}
    return 's.l1.%s0.l1.%s0.'%(c,c)+'.'.join(l+tok[g] for g in gam)+'.%s0.u1.%s0.u1'%(c,c)
if __name__=='__main__':
    for (name,p,q,gam,wf) in [('T(3,4)',3,4,(1,1,1),word3),('T(3,5)',3,5,(1,1,2,1),word3),('T(4,5)',4,5,(1,1,2,3,2,1),word5)]:
        tgt=torus_alex(p,q)
        for c in 'xy':
            for l in 'xy':
                w=wf(gam,c,l)
                try: co=alexall.alex_coeffs(w)
                except Exception as e: co='ERR '+repr(e)[:60]
                print(name,c,l,w,co==tgt, co if co!=tgt else '')
