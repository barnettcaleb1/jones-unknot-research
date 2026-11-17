"""per-class ORDER-3 test (H via o3h.one + gen2.proveH; V via o3v.one) for the UNSAFE n=3/n=4 classes (gen1k3u_*.pkl)."""
import sys, pickle, collections, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import o3h, o3v, h3b, gen2
from multiprocessing import Pool
OK=('n<0','r1: closed@2','r1: order3 CLOSED','tie T3=False T2:closed')
def hjob(j): return (j,o3h.one(j)[1])
if __name__=='__main__':
    t0=time.time(); doV=('V' in sys.argv[1:]); files=[a for a in sys.argv[1:] if a.endswith('.pkl')]
    K={}
    for f in files:
        try: K.update(pickle.load(open(f,'rb')))
        except FileNotFoundError: print('missing',f)
    jobs=[]
    for key,subs in K.items():
        for d3 in subs:
            for mu in h3b.MUS:
                for mu3 in ([mu] if abs(mu)<4 else [mu,5 if mu>0 else -5]):
                    for end in ('top','bot'): jobs.append((key,d3,mu,end,mu3))
    print('unsafe n3/n4 classes with order-3 data',len(K),'H jobs',len(jobs),flush=True)
    with Pool(3) as P: res=P.map(hjob,jobs,chunksize=8)
    per=collections.defaultdict(lambda: collections.defaultdict(list))
    for (key,d3,mu,end,mu3),v in res: per[key][mu].append(v)
    Hc=[]
    for key,mus in per.items():
        r=gen2.proveH({'top':key[0],'bot':key[1]},key[2],key[3],1); ok=True
        for mu,opn in r.items():
            if not opn: continue
            names=[o.split(':')[-1] for o in opn]
            two=all(('d=0' in x) or ('tie' in x) for x in names)
            if not (two and all(v in OK for v in mus.get(mu,[]))): ok=False
        if ok: Hc.append(key)
    print('H3(B) closed:',len(Hc),'of',len(per),'time',round(time.time()-t0,1),flush=True)
    out=dict(Hc=Hc,n=len(per))
    if doV:
        vj=[(k,d3) for k,subs in K.items() for d3 in subs]
        with Pool(3) as P: vres=P.map(o3v.one,vj,chunksize=4)
        pv=collections.defaultdict(list)
        for key,d3,o in vres: pv[key].append(o)
        Vc=[k for k,os in pv.items() if all(not o for o in os)]
        both=[k for k in Vc if k in set(Hc)]
        print('V3(B) closed:',len(Vc),'of',len(pv),'| both:',len(both),'time',round(time.time()-t0,1),flush=True)
        out.update(Vc=Vc,both=both)
    pickle.dump(out,open('o3_u_%s.pkl'%('_'.join(f.split('_')[-1].split('.')[0] for f in files)),'wb'))
