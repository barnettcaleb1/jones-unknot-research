"""exact search E-D4: the 80 most frequent UNSAFE depth-one classes with 3 or 4 rational children (certtest2): B u (R(4)),
B u u' (R(4)), B^2, B^2 u, and for sigma = -1 classes the V-tie configuration n = delta(B) + 4 (|a| = 3; 120 random multisets)."""
import sys, pickle, collections, itertools, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact_arb, lib
if __name__=='__main__':
    random.seed(17)
    C=pickle.load(open('certtest2.pkl','rb')); reps=C['reps']
    P3=pickle.load(open('gen1_R5_n3.pkl','rb')); P4=pickle.load(open('gen1_R4_n4.pkl','rb'))
    R5=lib.rational(5); R4=lib.rational(4)
    uns=[(l,k) for l,k,c in C['unsafe'] if l.split('_')[0] in ('n3','n4')]
    def cnt(l,k): return (P3 if l.startswith('n3') else P4)[k][0]
    uns.sort(key=lambda x:-cnt(*x)); uns=uns[:80]
    jobs=[]
    for l,k in uns:
        f,rep=reps[l]; Rp=R5 if 'R5' in f else R4
        B=exact_arb.tree_of(rep,Rp)
        for u in R4: jobs.append(('1u:'+l,[B,u[2]]))
        for u,v in itertools.combinations_with_replacement(R4,2): jobs.append(('1uu:'+l,[B,u[2],v[2]]))
        jobs.append(('2:'+l,[B,B]))
        for u in R4: jobs.append(('2u:'+l,[B,B,u[2]]))
        if k[2]==-1:
            n=int(k[3])+4
            if n>=1:
                for _ in range(120): jobs.append(('tie:'+l,[B]+[random.choice(R4)[2] for _ in range(n)]))
    print('unsafe n3/n4 classes',len(uns),'jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_d4.pkl',procs=3)
