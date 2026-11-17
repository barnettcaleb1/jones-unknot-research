"""VALIDATION 2: single non-rational box (k = e_j), n >= 1 rational boxes: compare with C1's per-signature results gen2_res.pkl.
Every case C1 closed must be closed here (the LP finds a certificate whenever one exists in the same relaxation)."""
import sys, time, collections, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import classes, runner, lpg
from multiprocessing import Pool
def one(c):
    out=runner.run_all([c],1,fixk={0:1})
    return c.key,{k:v[0] for k,v in out.items()}
if __name__=='__main__':
    t0=time.time()
    K=int(sys.argv[1]) if len(sys.argv)>1 else 300
    S=classes.top(K); D=[c for c in classes.d2pos() if c.key not in set(x.key for x in S)]
    allS=S+D
    with Pool(9) as P: res=dict(P.map(one,allS,chunksize=4))
    G=classes.G
    cmp=collections.Counter(); worse=[]; better=collections.Counter()
    for c in allS:
        r=res[c.key]
        Vmine=all(v=='closed' for (cn,nm,m),v in r.items() if cn.startswith('V'))
        Vc1=G['resV'][c.key][0]
        Hmine={mu:all(v=='closed' for (cn,nm,m),v in r.items() if cn.startswith('H mu=%+d '%mu)) for mu in [1,-1,2,-2,3,-3,4,-4]}
        Hc1={mu:not G['resH'][c.key][mu] for mu in Hmine}
        if Vc1 and not Vmine: worse.append((c.label,'V'))
        if Vmine and not Vc1: better['V']+=c.w
        for mu in Hmine:
            if Hc1[mu] and not Hmine[mu]: worse.append((c.label,mu))
            if Hmine[mu] and not Hc1[mu]: better['H%+d'%mu]+=c.w
        cmp[('V',Vc1,Vmine)]+=c.w
        allH=all(Hmine.values()); allHc1=all(Hc1.values())
        cmp[('H',allHc1,allH)]+=c.w
        cmp[('BOTH',Vc1 and allHc1,Vmine and allH)]+=c.w
    unv=sum(1 for c in allS for v in res[c.key].values() if v not in ('closed','open'))
    print('classes',len(allS),'(top %d + %d d2pos-only), boxes'%(K,len(D)),sum(c.w for c in allS))
    print('C1-closed but lpgen-open (MUST be empty):',worse[:20],len(worse))
    print('(kind, C1 closed, lpgen closed) box-weighted:',sorted(cmp.items(),key=str))
    print('lpgen closes beyond C1 (box-weighted):',dict(better))
    print('unverified/err LPs:',unv)
    op=collections.Counter()
    for c in allS:
        for (cn,nm,m),v in res[c.key].items():
            if v!='closed': op[(cn.split(' ')[0]+(' '+cn.split(' ')[1] if cn.startswith('H') else ''),nm)]+=c.w
    print('open (box-weighted):',op.most_common(20))
    pickle.dump(res,open('val2_res_%d.pkl'%K,'wb'))
    print('time',round(time.time()-t0,1))
