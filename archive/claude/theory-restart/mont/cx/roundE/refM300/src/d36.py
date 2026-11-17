"""THEOREM D36 re-done with EXACT certificates: for each of the 36 closed d2pos classes D: S = top-300 + [D] with k_D = 1
FIXED, top multiplicities free, n >= 0; every closure class x every case (10 offsets, d=0 slices sigma.k in [-15,15],
ties).  Certificates GENERATED with lpgen's LP builder/HiGHS (lpg.build / lpg.farkas, read-only import) and VERIFIED by
the own semantic checker (certcheck2).  Also the 24 'open' classes are run to confirm they are open (control)."""
import sys, pickle, time, collections
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import certcheck2 as C2, certcheck as CC
import lpg, runner
from multiprocessing import Pool
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
CD=CC.CD
TOPK=[CD['top%d'%i]['key'] for i in range(300)]
D2=sorted([(k,v['key']) for k,v in CD.items() if k.startswith('d2_')],key=lambda x:int(x[0][3:]))
OPEN24={'d2_457','d2_459','d2_460','d2_497','d2_536','d2_565','d2_895','d2_902','d2_1232','d2_1238','d2_1247','d2_1494','d2_2557','d2_2780','d2_3075','d2_3076','d2_3077','d2_3933','d2_4277','d2_4643','d2_5150','d2_5152','d2_5153','d2_5154'}
def jobs():
    out=[]
    for cl in lpg.closure_classes():
        for nm,rows in lpg.case_rows(cl['p'],cl['q']): out.append((cl,nm,rows,None,None))
        for x in range(-15,16):
            m=Fr(x)-cl['sigstar']
            for nm,rows in lpg.case_rows(cl['p'],cl['q'],m=m): out.append((cl,nm,rows,m,cl['d0n']))
    for tc in lpg.tie_classes(): out.append((dict(tc,end='top'),'tie',[],Fr(0),tc['n']))
    return out
def one(arg):
    lab,dkey=arg
    S=[lpg.Cls(k,1,'t') for k in TOPK]+[lpg.Cls(dkey,1,lab)]; jD=300
    keys=TOPK+[dkey]
    res=collections.Counter(); opn=[]; fails=[]
    for cl,nm,rows,m,nr in jobs():
        L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m,nrule=nr,extra=[('eq',{jD:Fr(1)},Fr(1))])
        r=lpg.solve_primal(L)
        if r.status==0:
            res['open']+=1; opn.append((cl['name'],nm,m)); continue
        f=lpg.farkas(L)
        if not isinstance(f,tuple): res['nocert']+=1; fails.append((cl['name'],nm,m,'nocert',r.status)); continue
        u,w,val=f
        ok,info=C2.check_cert_fix(keys,cl,nm,rows,m,nr,1,0,u,w,fix=[(jD,Fr(1))])
        if ok: res['VERIFIED']+=1
        else: res['REJECTED']+=1; fails.append((cl['name'],nm,m,info))
    return lab,dict(res),opn,fails
if __name__=='__main__':
    t0=time.time()
    with Pool(6) as P: out=P.map(one,D2,chunksize=1)
    clo=[]; op=[]
    for lab,res,opn,fails in out:
        tag='OPEN24' if lab in OPEN24 else 'D36'
        allv=(not opn) and (not fails)
        print('%-9s %-6s %s  open=%d fails=%d %s'%(lab,tag,res,len(opn),len(fails),'' if allv else str((opn+fails)[:3])),flush=True)
        (clo if allv else op).append(lab)
    print('ALL CASES EXACTLY CERTIFIED for %d classes; with open/failed cases: %d'%(len(clo),len(op)))
    print('certified set == lpgen D36 list:',set(clo)==set(l for l,k in D2 if l not in OPEN24),' certified & in OPEN24:',sorted(set(clo)&OPEN24))
    pickle.dump(out,open(HERE+'d36_res.pkl','wb'))
    print('time %.1f'%(time.time()-t0))
