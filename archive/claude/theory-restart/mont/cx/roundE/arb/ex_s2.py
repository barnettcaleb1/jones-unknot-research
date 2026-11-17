"""sanity E-S: random products of CERTIFIED depth-one classes (S** representatives: n2 certified, n3/n4 safe) with 0-2 rational
boxes (R(4)), exact Lemma-W closures.  ARB-2 predicts 0 units."""
import sys, pickle, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact_arb, lib
if __name__=='__main__':
    random.seed(99)
    F=pickle.load(open('ARB1_family.pkl','rb')); C=pickle.load(open('certtest2.pkl','rb'))
    R5=lib.rational(5); R4=lib.rational(4)
    trees=[exact_arb.tree_of(rep[1],R5) for l,k,rep in F['certified_new']]
    for l in C['safe']:
        f,rep=C['reps'][l]; trees.append(exact_arb.tree_of(rep,R5 if 'R5' in f else R4))
    jobs=[]
    for i in range(3000):
        k=random.choice([1,2,2,3]); n=random.choice([0,1,1,2]) if k>1 else random.choice([1,2])
        jobs.append(('s',[random.choice(trees) for _ in range(k)]+[random.choice(R4)[2] for _ in range(n)]))
    print('certified representatives',len(trees),'jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_s2.pkl',procs=2)
