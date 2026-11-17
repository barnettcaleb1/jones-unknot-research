"""sampled exact J search (vector calculus, all Lemma-W candidates H and V) of the complete F1' survivor families."""
import sys, random, time, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import f1p_search as FS
import lib
from multiprocessing import Pool
if __name__=='__main__':
    t0=time.time(); rng=random.Random(2026)
    CD=FS.CD; items=FS.items
    d497=CD['d2_497']['xs']; d460=CD['d2_460']['xs']; t197=CD['top197']['xs']
    R6=lib.rational(6); R7=lib.rational(7)
    jobs=[]
    for i in range(int(sys.argv[1])):
        xs=[rng.choice(d497) for _ in range(3)]; rr=[rng.randrange(len(R6)) for _ in range(2)]
        jobs.append((('A',tuple(xs),tuple(rr)),[items[x][2] for x in xs]+[R6[j][1] for j in rr]))
        xs=[rng.choice(d460) for _ in range(3)]; rr=[rng.randrange(len(R6)) for _ in range(2)]
        jobs.append((('B',tuple(xs),tuple(rr)),[items[x][2] for x in xs]+[R6[j][1] for j in rr]))
        for _ in range(2):
            xs=[rng.choice(t197)]+[rng.choice(d460) for _ in range(3)]; rr=[rng.randrange(len(R7))]
            jobs.append((('C',tuple(xs),tuple(rr)),[items[x][2] for x in xs]+[R7[j][1] for j in rr]))
    print('products',len(jobs),flush=True)
    tot=0; units=[]; gates=0; ms={}
    with Pool(3) as P:
        for o in P.imap_unordered(FS.check,jobs,chunksize=16):
            tot+=o['n']; gates+=o['gates']; fam=o['tag'][0]
            if o['units']: units.append((o['tag'],o['units'])); print('UNIT',o,flush=True)
            if o['minspan'] is not None and (fam not in ms or o['minspan']<ms[fam]): ms[fam]=o['minspan']
    print('F1-prime survivor families A/B/C: products %d candidates %d UNITS %d double-gate %d min span per family %s (%.0fs)'%(len(jobs),tot,len(units),gates,ms,time.time()-t0),flush=True)
