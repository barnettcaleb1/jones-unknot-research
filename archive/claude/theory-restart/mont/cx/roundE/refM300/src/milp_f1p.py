"""exact branch and bound for the LP-feasible order-3 F1' slices (integer k over the 3,735 subclasses, integer n)."""
import sys, time, math
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import f1redo as F, f1pre as P, semcheck as SC, certcheck as CC
import lpg, f1o3
NSUB=F.NSUB; S=F.S
def node(cl,m,bounds,mu5=False):
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=1 e=-1']
    ex=[]; semx=[]
    for var,sense,val in bounds:
        sg=1 if sense=='le' else -1; b=Fr(val) if sense=='le' else -Fr(val)
        if var=='n': ex.append(('ub',{NSUB:Fr(sg)},b)); semx.append(dict(kind='ub',z=(0,)*6,cls={},n=sg,b=b))
        else: ex.append(('ub',{var:Fr(sg)},b)); semx.append(dict(kind='ub',z=(0,)*6,cls={var:sg},n=0,b=b))
    L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m,extra=ex)
    end=cl['end']; sem=[]
    for coef,a in rows:
        cls=[]
        for j in range(NSUB):
            ra,la,rb,lb,sig,l3a,l3b=F.cdat(j,end); cls.append(-(a[1]*ra+a[2]*la+a[3]*rb+a[4]*lb+a[5]*sig))
        sem.append(dict(kind='eq',z=(coef[0],coef[1],coef[2],coef[3],0,0),cls=cls,n=0,b=a[0]-a[5]*cl['sigstar']))
    sem.append(dict(kind='eq',z=(0,)*6,cls=[F.SUB[j][1][2] for j in range(NSUB)],n=0,b=m+cl['sigstar']))
    p,q=P.wd3(cl,mu5)
    rr={}
    for i,(a,b,l1,l2) in enumerate(lpg.EI):
        v=f1o3.EL3[i]-l2
        if v: rr[L.iF+i]=v
    for jj,s in enumerate(lpg.FINS):
        v=-lpg.FIN[s][1]
        if v: rr[L.iG+jj]=v
    cls3=[]
    for j in range(NSUB):
        ra,la,rb,lb,sig,l3a,l3b=F.cdat(j,end); cls3.append(l3a-lb)
        if l3a-lb: rr[j]=rr.get(j,0)+(l3a-lb)
    c3=m*m/2-Fr(4,3)-p[2]+q[1]
    L.add_eq(rr,c3)
    sem.append(dict(kind='eq',z=(0,0,-1,-1,1,0),cls=cls3,n=0,b=c3))
    semub=[dict(kind='ub',z=(0,)*6,cls=[-1]*NSUB,n=0,b=-1)]+semx
    return L,sem,semub
def solve(cl,m,maxnodes=3000):
    t0=time.time(); stack=[[]]; nodes=0; leaves=0; found=[]
    while stack:
        bounds=stack.pop(); nodes+=1
        if nodes>maxnodes: return dict(status='node limit',nodes=nodes,leaves=leaves,found=found)
        L,sem,semub=node(cl,m,bounds)
        r=lpg.solve_primal(L)
        if r.status!=0:
            f=lpg.farkas(L)
            if not isinstance(f,tuple): return dict(status='no exact certificate at a leaf',bounds=bounds)
            u,w,val=f
            ok,info=SC.check(sem+semub,list(u[19:])+list(w),NSUB,0)
            if not ok: return dict(status='leaf certificate REJECTED',bounds=bounds,info=info)
            leaves+=1; continue
        x=r.x; frac=None; best=None
        for j in range(NSUB):
            fp=x[j]-math.floor(x[j])
            if 1e-7<fp<1-1e-7:
                sc=abs(fp-0.5)
                if best is None or sc<best: best=sc; frac=(j,x[j])
        if frac is None:
            fp=x[NSUB]-math.floor(x[NSUB])
            if 1e-7<fp<1-1e-7: frac=('n',x[NSUB])
        if frac is None:
            pt=({F.SUB[j][0]+'/'+str(j):int(round(x[j])) for j in range(NSUB) if x[j]>0.5},int(round(x[NSUB])))
            found.append(pt)
            # exclude this integer n and continue (enumerate all integer n in this k-pattern region)
            nn=int(round(x[NSUB]))
            stack.append(bounds+[('n','le',nn-1)]); stack.append(bounds+[('n','ge',nn+1)])
            continue
        var,v=frac
        stack.append(bounds+[(var,'le',math.floor(v))]); stack.append(bounds+[(var,'ge',math.floor(v)+1)])
    return dict(status='done',nodes=nodes,leaves=leaves,found=found,time=round(time.time()-t0,1))
if __name__=='__main__':
    CL={c['name']:c for c in lpg.closure_classes()}
    for name,m in [('H mu=+2 top',Fr(-7)),('H mu=-2 bot',Fr(-7)),('H mu=-2 bot',Fr(-8))]:
        print(name,'mB=%s'%m,solve(CL[name],m),flush=True)
