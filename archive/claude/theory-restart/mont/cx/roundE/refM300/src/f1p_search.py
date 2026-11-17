"""exact J search (vector calculus, every Lemma-W candidate, all mu and all odd a) of the order-3 F1' integer survivors:
patterns given as {subclass label/index: multiplicity} + n rational boxes from R(L).  Units -> HIT protocol."""
import sys, pickle, itertools, time, collections
EA='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
sys.path.insert(0,EA); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import vc, eng, lib, lp, spot_lib
import rlaurent as RL
from multiprocessing import Pool
items,pool=spot_lib.load()
CD=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','rb'))
def subclass_boxes(lab,d3):
    out=[]
    for x in CD[lab]['xs']:
        a,b=items[x][2]; t=[]
        for end in ('top','bot'):
            _,_,la=RL.logdata(a,end,3); _,_,lb=RL.logdata(b,end,3); t.append((la[2],lb[2]))
        if (t[0][0],t[0][1],t[1][0],t[1][1])==d3: out.append(x)
    return out
def z10(Jn):
    r=[0]*5
    for e,c in Jn.items():
        q,rem=divmod(e,5); r[rem]+=c*(-1)**(q%2)
    r[0]-=1; c4=r[4]; r=[r[0]-c4,r[1]+c4,r[2]-c4,r[3]+c4,0]
    return all(x==0 for x in r)
def check(job):
    tag,vecs=job
    p=vc.starall(vecs); out=dict(tag=tag,n=0,units=[],gates=0,minspan=None)
    cands=[('H',)+c for c in eng.hclosures(p) if c[0]!='all']+[('V',)+c for c in eng.vclosures(p)]
    for kind,x,N,J in cands:
        if J is None: continue
        out['n']+=1
        if len(J)==1: out['units'].append((kind,x,N)); continue
        Jn=vc.norm(J)
        if Jn is None: continue
        sp=max(Jn)-min(Jn)
        if out['minspan'] is None or sp<out['minspan']: out['minspan']=sp
        if lp.a2(Jn)==0 and z10(Jn): out['gates']+=1
    return out
if __name__=='__main__':
    t0=time.time()
    pats=eval(sys.argv[1]); L=int(sys.argv[2])
    R=lib.rational(L)
    jobs=[]
    for pat,n in pats:
        groups=[]
        for (lab,d3),mult in pat:
            bx=subclass_boxes(lab,d3); groups.append([list(c) for c in itertools.combinations_with_replacement(bx,mult)])
        for combo in itertools.product(*groups):
            xs=[x for g in combo for x in g]
            for rr in itertools.combinations_with_replacement(range(len(R)),n):
                jobs.append(((tuple(xs),rr),[items[x][2] for x in xs]+[R[i][1] for i in rr]))
    print('products',len(jobs),flush=True)
    tot=0; units=[]; gates=0; ms=None
    with Pool(3) as P:
        for o in P.imap_unordered(check,jobs,chunksize=8):
            tot+=o['n']; gates+=o['gates']
            if o['units']: units.append((o['tag'],o['units'])); print('UNIT',o,flush=True)
            if o['minspan'] is not None and (ms is None or o['minspan']<ms): ms=o['minspan']
    print('products %d candidates %d UNITS %d double-gate %d min span %s (%.0fs)'%(len(jobs),tot,len(units),gates,ms,time.time()-t0),flush=True)
