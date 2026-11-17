"""EXACT search (Lemma W windows, every mu and odd a; lpgen exact.check imported read-only) of products built from
DANGEROUS (LP-uncertified) depth-one classes: B^j * u_1..u_n, pairs B*B'*u..., and integer roundings of LP-open points.
Logs units (HIT protocol!), double-gate passers (a_2 = 0 and J(zeta_10) = 1), min span J."""
import sys, pickle, time, itertools, random, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lib, exact
from multiprocessing import Pool
def tree_of(rep,R):
    idx,N,m=rep
    return ('n',m,[R[i][2] for i in idx]+([('w',('Y' if N>0 else 'y')*abs(N))] if N else []))
def work(job):
    tag,trees=job
    vecs=[vc.vec(T) for T in trees]
    out=exact.check((tag,vecs))
    out['trees']=trees
    return out
def run(jobs,outname,procs=3):
    t0=time.time(); tot=dict(products=0,cands=0,units=[],gates=[],minspan=None,err=0)
    with Pool(procs) as P:
        for o in P.imap_unordered(work,jobs,chunksize=2):
            tot['products']+=1; tot['cands']+=o['n']
            if 'err' in o: tot['err']+=1
            if o['units']: tot['units'].append((o['tag'],o['trees'],o['units'])); print('UNIT!!',o['tag'],o['trees'],o['units'],flush=True)
            if o['gates']: tot['gates'].append((o['tag'],o['trees'],o['gates']))
            if o['minspan'] and (tot['minspan'] is None or o['minspan'][0]<tot['minspan'][0]): tot['minspan']=(o['minspan'][0],o['tag'],o['trees'],o['minspan'][1:])
            if tot['products']%500==0: print('  progress',tot['products'],len(jobs),round(time.time()-t0,1),flush=True)
    pickle.dump(tot,open(outname,'wb'))
    print('%s: products %d, Lemma-W candidates %d, UNITS %d, double-gate passers %d, min span J %s, errors %d, time %.1f'%(
        outname,tot['products'],tot['cands'],len(tot['units']),len(tot['gates']),tot['minspan'][:2] if tot['minspan'] else None,tot['err'],time.time()-t0),flush=True)
    return tot
