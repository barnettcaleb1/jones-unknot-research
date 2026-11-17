"""exact search E-D2: integer roundings of LP-OPEN points (arblp_n2.pkl, 'd=0 r=0' excluded as vacuous): support classes with
multiplicities floor/ceil (total <= 8 non-rational boxes), representative boxes (gen1 reps; library boxes for top-300/D36
classes), rational part n in {round(n), round(n)+-1} >= 0 drawn from R(4) (all choices for n <= 1, 40 random for n = 2)."""
import sys, pickle, collections, itertools, random, math
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact_arb, lib, classes, exact
if __name__=='__main__':
    random.seed(5)
    A=pickle.load(open('arblp_n2.pkl','rb')); reps=A['reps']; keys=dict(zip(A['labels'],A['keys']))
    R5=lib.rational(5); R4=lib.rational(4)
    items=exact.load_items()
    def rep_tree(l):
        if l.startswith('g1'): return exact_arb.tree_of(reps[l][1],R5)
        xs=classes.SIGS[keys[l]]; return items[xs[0]][1]
    pts=[r for r in A['res'] if r[1]=='open' and not (r[0][0]=='case' and r[0][2]=='d=0 r=0') and not (r[0][0]=='big' and r[0][2]=='r0')]
    seen=set(); jobs=[]
    for r in pts:
        sup,n=r[2]
        ls=sorted(sup)
        opts=[sorted(set([max(0,math.floor(sup[l])),math.ceil(sup[l])])) for l in ls]
        for ks in itertools.product(*opts):
            if sum(ks)==0 or sum(ks)>8: continue
            conf=tuple((l,k) for l,k in zip(ls,ks) if k)
            for nn in sorted(set([max(0,round(n)-1),round(n),round(n)+1])):
                if (conf,nn) in seen: continue
                seen.add((conf,nn))
                base=[rep_tree(l) for l,k in conf for _ in range(k)]
                if len(base)+nn<2: continue
                if nn==0: jobs.append(('c%d'%len(jobs),base))
                elif nn==1:
                    for u in R4: jobs.append(('c%d'%len(jobs),base+[u[2]]))
                elif nn==2:
                    for _ in range(40):
                        u,v=random.choice(R4),random.choice(R4); jobs.append(('c%d'%len(jobs),base+[u[2],v[2]]))
    random.shuffle(jobs)
    jobs=jobs[:20000]
    print('LP-open points',len(pts),'configurations',len(seen),'jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_d2.pkl',procs=3)
