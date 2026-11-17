"""complete enumeration of the INTEGER configurations (k, n) of the 3 LP-open order-3 F1' slices: (1) participating
subclasses = those with max k_j > 0 over the slice polyhedron, with LP upper bounds; (2) every integer k pattern within
the bounds (sigma.k pinned by the slice) and every integer n in [0, nmax]: LP feasibility (infeasible -> exact certificate
verified by the own checker; feasible -> listed)."""
import sys, math, itertools, time
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import milp_f1p as M, f1redo as F, semcheck as SC
import lpg
NSUB=F.NSUB
CL={c['name']:c for c in lpg.closure_classes()}
for name,m in [('H mu=+2 top',Fr(-7)),('H mu=-2 bot',Fr(-7)),('H mu=-2 bot',Fr(-8))]:
    t0=time.time(); cl=CL[name]
    L,sem,semub=M.node(cl,m,[])
    # participating variables: maximise each k_j that can be positive (screen with one LP maximising sum k first)
    part={}
    r=lpg.solve_primal(L,obj={j:-1.0 for j in range(NSUB)})
    maxsum=-r.fun if r.status==0 else None
    # candidates: subclasses appearing in some vertex; test each j with an LP maximising k_j
    # iterative screening: maximise the sum of the not-yet-found k_j; every variable positive at the optimum joins
    found=set()
    while True:
        rest=[j for j in range(NSUB) if j not in found]
        rj=lpg.solve_primal(L,obj={j:-1.0 for j in rest})
        if rj.status==3: part[-1]=float('inf'); break
        if rj.status!=0 or -rj.fun<=1e-7: break
        new=[j for j in rest if rj.x[j]>1e-7]
        found|=set(new)
    for j in sorted(found):
        rj=lpg.solve_primal(L,obj={j:-1.0})
        part[j]=-rj.fun if rj.status==0 else float('inf')
    rn=lpg.solve_primal(L,obj={NSUB:-1.0}); nmax=(-rn.fun if rn.status==0 else float('inf'))
    print(name,'mB=%s'%m,'max sum k %.3f'%maxsum,'participating subclasses',{F.SUB[j][0]+'/'+str(j):round(v,3) for j,v in part.items()},'nmax %.3f'%nmax,flush=True)
    if any(v==float('inf') for v in part.values()) or nmax==float('inf'): print('   unbounded -> no enumeration'); continue
    J=sorted(part); bnd=[int(math.floor(part[j]+1e-9)) for j in J]; NM=int(math.floor(nmax+1e-9))
    feas=[]; inf=0; rej=0
    for ks in itertools.product(*[range(b+1) for b in bnd]):
        if sum(ks)==0: continue
        if sum(F.SUB[j][1][2]*k for j,k in zip(J,ks))!=m+cl['sigstar']: continue
        for n in range(NM+1):
            bounds=[(j,'le',k) for j,k in zip(J,ks)]+[(j,'ge',k) for j,k in zip(J,ks)]+[('n','le',n),('n','ge',n)]
            # all other subclasses fixed to 0
            Ln,semn,semubn=M.node(cl,m,bounds)
            for j in range(NSUB):
                if j not in part and False: Ln.add_ub({j:Fr(1)},Fr(0)); semubn.append(dict(kind='ub',z=(0,)*6,cls={j:1},n=0,b=Fr(0)))
            rr=lpg.solve_primal(Ln)
            if rr.status==0: feas.append(({F.SUB[j][0]+'/'+str(j):k for j,k in zip(J,ks) if k},n)); continue
            f=lpg.farkas(Ln)
            if not isinstance(f,tuple): rej+=1; continue
            u,w,val=f
            ok,info=SC.check(semn+semubn,list(u[19:])+list(w),NSUB,0)
            if ok: inf+=1
            else: rej+=1
    print('   integer configurations feasible in the relaxation:',feas,' certified-infeasible patterns:',inf,' uncertified:',rej,' (%.0fs)'%(time.time()-t0),flush=True)
