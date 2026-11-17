"""TWO d2pos boxes (class pairs closed at k_T = 0) + ANY multiset of top-300 boxes + any n >= 0."""
import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import d2fix, classes
from multiprocessing import Pool
if __name__=='__main__':
    t0=time.time()
    P=pickle.load(open('pairs_d2.pkl','rb')); lab50=P['labels']
    S=d2fix.S; lab=[c.label for c in S]; idx={l:i for i,l in enumerate(lab)}
    pairs=[(idx[lab50[c[0]]],idx[lab50[c[1]]]) for c,n,o in P['res'] if len(c)==2 and not o and lab50[c[1]].startswith('d2')]
    jobs=[{a:2} if a==b else {a:1,b:1} for a,b in pairs]
    print('closed d2xd2 class pairs to extend:',len(jobs),flush=True)
    with Pool(3) as Pl: res=Pl.map(d2fix.run,jobs,chunksize=8)
    clo=[f for f,o in res if not o]; op=[(f,o) for f,o in res if o]
    print('TWO d2pos boxes + ANY top-300 multiset + any n: closed for %d/%d closed-at-kT=0 pairs; open %d'%(len(clo),len(jobs),len(op)))
    for f,o in op[:20]: print('  OPEN',{lab[j]:v for j,v in f.items()},[(k[0],k[1],k[2],n,kt) for k,n,kt in o][:3])
    pickle.dump(dict(res=res,labels=lab),open('d2fix2.pkl','wb'))
    print('time',round(time.time()-t0,1))
