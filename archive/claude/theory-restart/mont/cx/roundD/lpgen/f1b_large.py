"""F1' ('d=1 e=-1') beyond the slices: (a) order-2 region with mB <= -31 / mB >= 31 (exact Farkas); (b) if open, bound
LHS' - A*|mB| on the order-2 region (exact) against LHS' = mB^2/2 - 4/3 - p3 + q2."""
import sys, math, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import f1uni, f1b, lpg, classes, exact, runner
from fractions import Fraction as Fr
items=exact.load_items()
S=f1uni.subclasses(items,classes.top(300))+f1uni.subclasses(items,classes.d2pos())
A=Fr(4); t0=time.time(); allok=True
for cl in lpg.closure_classes():
    rows=dict(lpg.case_rows(cl['p'],cl['q']))['d=1 e=-1']
    p3s=[f1b.p3of(cl)]+([f1b.p3of(cl,True)] if cl['kind']=='H' and abs(cl['mu'])==4 else [])
    for sgn in (1,-1):
        ex=[('ub',{j:-sgn*c.sig for j,c in enumerate(S) if c.sig},-31-sgn*cl['sigstar'])]
        L=lpg.build(S,cl,rows,0,kmin=1,extra=ex)
        if lpg.solve_primal(L).status!=0:
            f=lpg.farkas(L); print('%-24s sgn=%+d order-2 empty: %s'%(cl['name'],sgn,'EXACT' if isinstance(f,tuple) else f),flush=True)
            allok&=isinstance(f,tuple); continue
        r=f1b.row3(L,S,cl)
        obj={j:-float(v) for j,v in r.items()}
        for j,c in enumerate(S):
            if c.sig: obj[j]=obj.get(j,0)-float(sgn*A*c.sig)
        res=lpg.solve_primal(L,obj=obj)
        if res.status!=0: print(cl['name'],sgn,'LP status',res.status); allok=False; continue
        opt=-res.fun-float(sgn*A*cl['sigstar'])     # max of LHS' + sgn*A*(...)?  we bound LHS' - A*|mB| with |mB| = sgn*mB
        bp=Fr(math.floor(opt)+1)
        r2={j:-v for j,v in r.items()}
        for j,c in enumerate(S):
            if c.sig: r2[j]=r2.get(j,0)-sgn*A*c.sig
        L.add_ub(r2,-bp-sgn*A*cl['sigstar'])
        f=lpg.farkas(L); ok=isinstance(f,tuple)
        for p3 in p3s:
            c0=Fr(4,3)+p3-cl['q'][1]
            disc=A*A+2*(bp+c0)
            mmax=float(A)+math.sqrt(float(disc)) if disc>=0 else float('-inf')
            print('%-24s sgn=%+d p3=%s max(LHS - 4|mB|)=%.3f cert %s => |mB| < %.2f'%(cl['name'],sgn,p3,opt,'EXACT' if ok else f,mmax),flush=True)
            allok&=ok and mmax<=31
print('ALL CLOSED for |mB| >= 31:',allok,'time',round(time.time()-t0,1))
