"""exact search of the LP-open frontier families J1-J4 (see REPORT section 4)."""
import sys, pickle, time, collections, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact, classes, lib
from multiprocessing import Pool
CAP=10
def main(fam):
    t0=time.time()
    items=exact.load_items()
    P=pickle.load(open('pairs_d2.pkl','rb')); lab=P['labels']
    S=classes.top(50)+classes.d2pos(); bylab={c.label:c for c in S}
    def boxes(label,cap=CAP): return classes.SIGS[bylab[label].key][:cap]
    R={L:lib.rational(L) for L in (4,5,6)}
    op1=sorted(set(lab[c[0]] for c,n,o in P['res'] if len(c)==1 and o))
    op2=[(lab[c[0]],lab[c[1]]) for c,n,o in P['res'] if len(c)==2 and o and lab[c[1]].startswith('d2')]
    op2t=[(lab[c[0]],lab[c[1]]) for c,n,o in P['res'] if len(c)==2 and o and not lab[c[1]].startswith('d2')]
    jobs=[]
    def rats(n,L):
        return [()] if n==0 else list(itertools.combinations_with_replacement(range(len(R[L])),n))
    if fam=='J1':     # d2 x d2 open class pairs, n = 0 (any), 1 (R6), 2 (R4)
        for a,b in op2:
            bp=[(x,y) for x in boxes(a) for y in boxes(b) if (a!=b or x<=y)]
            for x,y in bp:
                for n,L in ((0,4),(1,6),(2,4)):
                    for rr in rats(n,L):
                        jobs.append((('J1',a,b,x,y,L,rr),[items[x][2],items[y][2]]+[R[L][i][1] for i in rr]))
    if fam=='J2':     # open d2 singles x n = 1 (R6), 2 (R5), 3 (R4)
        for a in op1:
            for x in boxes(a):
                for n,L in ((1,6),(2,5),(3,4)):
                    for rr in rats(n,L):
                        jobs.append((('J2',a,x,L,rr),[items[x][2]]+[R[L][i][1] for i in rr]))
    if fam=='J3':     # open d2 x top-50 class pairs (3 boxes per top class), n = 0, 1 (R4)
        for a,b in op2t:
            for x in boxes(a,6):
                for y in boxes(b,3):
                    for n,L in ((0,4),(1,4)):
                        for rr in rats(n,L):
                            jobs.append((('J3',a,b,x,y,L,rr),[items[x][2],items[y][2]]+[R[L][i][1] for i in rr]))
    if fam in ('J4','J4a','J4b'):     # triples of d2 classes drawn from the open-pair classes (2 boxes per class), n = 0, 1 (R4)
        cls=sorted(set(x for p in op2 for x in p))
        nl={'J4':((0,4),(1,4)),'J4a':((0,4),),'J4b':((1,4),)}[fam]
        for tri in itertools.combinations_with_replacement(cls,3):
            for xs in itertools.product(*[boxes(c,2) for c in tri]):
                for n,L in nl:
                    for rr in rats(n,L):
                        jobs.append((('J4',)+tri+xs+(L,rr),[items[x][2] for x in xs]+[R[L][i][1] for i in rr]))
    print(fam,'jobs',len(jobs),flush=True)
    units=[]; gates=[]; ncand=0; minsp=collections.Counter(); best=[]; errs=0
    with Pool(6) as Pl:
        for i,o in enumerate(Pl.imap_unordered(exact.check,jobs,chunksize=64)):
            ncand+=o['n']
            if 'err' in o: errs+=1
            if o['units']: units.append((o['tag'],o['units'])); print('UNIT',o['tag'],o['units'],flush=True)
            for g in o['gates']: gates.append((o['tag'],g))
            if o['minspan']:
                minsp[o['minspan'][0]]+=1
                if o['minspan'][0]<=12: best.append((o['minspan'],o['tag']))
            if i%100000==0: print('  ',i,round(time.time()-t0,1),flush=True)
    print(fam,'products',len(jobs),'candidates',ncand,'UNITS',len(units),'errors',errs,'gate-passers (a2=0 & J(z10)=1)',len(gates),
          'min span hist',sorted(minsp.items())[:8],'time',round(time.time()-t0,1),flush=True)
    for g in sorted(gates,key=lambda x:x[1][3])[:10]: print('  GATE',g,flush=True)
    for b in sorted(best)[:10]: print('  SMALLSPAN',b,flush=True)
    pickle.dump(dict(units=units,gates=gates,best=best,minsp=minsp,ncand=ncand,nprod=len(jobs)),open('exact_%s.pkl'%fam,'wb'))
if __name__=='__main__':
    for fam in sys.argv[1:]: main(fam)
