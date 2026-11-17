"""per-class ORDER-3 VERTICAL test (o3v.one) for unsafe classes from the given gen1k3u pickle; saves partial results every 200."""
import sys, pickle, collections, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import o3v
from multiprocessing import Pool
if __name__=='__main__':
    t0=time.time(); f=sys.argv[1]; K=pickle.load(open(f,'rb'))
    vj=[(k,d3) for k,subs in K.items() for d3 in subs]
    print('subclasses',len(vj),flush=True)
    res=[]
    with Pool(3) as P:
        for r in P.imap_unordered(o3v.one,vj,chunksize=4):
            res.append(r)
            if len(res)%500==0:
                print('progress',len(res),round(time.time()-t0,1),flush=True)
                pickle.dump(res,open('o3_uv_%s'%f.split('_')[-1],'wb'))
    pv=collections.defaultdict(list)
    for key,d3,o in res: pv[key].append(o)
    Vc=[k for k,os in pv.items() if all(not o for o in os)]
    H=pickle.load(open('o3_u_%s'%f.split('_')[-1],'rb')); Hc=set(H['Hc'])
    print('V3(B) closed:',len(Vc),'of',len(pv),'| H3 and V3 both:',len([k for k in Vc if k in Hc]),'time',round(time.time()-t0,1),flush=True)
    pickle.dump(dict(res=res,Vc=Vc),open('o3_uv_%s'%f.split('_')[-1],'wb'))
