"""(4b) step 2+3: exact bound LHS' - A|mB| <= b' on the order-2 F1' region with |mB| >= 31 (A = 6 > A* = 5.5), then order-3
equality slices 31 <= |mB| <= threshold.  (lpgen's f1b_large maximised LHS' + A|mB| (sign slip; harmless where bounded) with A = 4 < A*.)"""
import sys, math, time, pickle, collections
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import f1uni, f1b, lpg, classes, exact, runner
from fractions import Fraction as Fr
from multiprocessing import Pool
t0=time.time()
items=exact.load_items()
S=f1uni.subclasses(items,classes.top(300))+f1uni.subclasses(items,classes.d2pos())
f1b.SS=S
CL={cl['name']:cl for cl in lpg.closure_classes()}
A=Fr(6); allok=True; thr={}
for name,sgn in (('H mu=+2 top',-1),('H mu=-2 bot',-1)):
    cl=CL[name]; rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=1 e=-1']
    ex=[('ub',{j:-sgn*c.sig for j,c in enumerate(S) if c.sig},-31-sgn*cl['sigstar'])]
    L=lpg.build(S,cl,rows,0,kmin=1,extra=ex)
    r=f1b.row3(L,S,cl)
    obj={j:-float(v) for j,v in r.items()}
    for j,c in enumerate(S):
        if c.sig: obj[j]=obj.get(j,0)+float(sgn*A*c.sig)      # minimise -(r3.x - A sgn sigma.k)
    res=lpg.solve_primal(L,obj=obj)
    print(name,'LP status',res.status,flush=True)
    if res.status!=0: allok=False; continue
    opt=-res.fun                                  # max of r3.x - A sgn sigma.k
    bp_lin=Fr(math.floor(opt+1e-9)+1)             # certify  r3.x - A sgn sigma.k <= bp_lin - ... via infeasibility of >= bp_lin
    rr={j:-v for j,v in r.items()}
    for j,c in enumerate(S):
        if c.sig: rr[j]=rr.get(j,0)+sgn*A*c.sig
    L.add_ub(rr,-bp_lin)                           # -(r3.x - A sgn sigma.k) <= -bp_lin
    f=lpg.farkas(L); ok=isinstance(f,tuple)
    bprime=bp_lin+A*sgn*cl['sigstar']             # LHS' - A|mB| < b'
    p3=f1b.p3of(cl); c0=Fr(4,3)+p3-cl['q'][1]
    disc=A*A+2*(bprime+c0)
    mmax=float(A)+math.sqrt(float(disc)) if disc>=0 else float('-inf')
    thr[name]=(sgn,(int(math.floor(mmax)) if mmax>-1e300 else 30),p3)
    print('  max(LHS - 6|mB|) = %.3f + const; certified b_prime = %s (%s); c0 = %s; disc = %s => |mB| < %.2f'%(opt,bprime,'EXACT' if ok else f,c0,disc,mmax),flush=True)
    allok&=ok
print('bounds certified:',allok,thr,flush=True)
jobs=[]
for name,(sgn,mm,p3) in thr.items():
    for a in range(31,mm+1): jobs.append((CL[name],Fr(sgn*a),p3))
print('order-3 slices to run:',len(jobs),flush=True)
with Pool(3,initializer=f1b.init,initargs=(S,)) as P: res=P.map(f1b.one,jobs,chunksize=1)
c=collections.Counter(x[3] for x in res); print('slices',dict(c),flush=True)
for x in res:
    if x[3] not in ('closed','closed@2'): print('  OPEN',x[:4],str(x[4])[:300])
pickle.dump(dict(thr=thr,res=res),open('f1b_tail2.pkl','wb'))
print('time',round(time.time()-t0,1))
