"""exact search E-D3: the V-TIE configurations of the dangerous sigma = -1 depth-one classes (sigma(B) = sigma*_V = -1, so a
single such box ties to order 2 at both ends of a vertical closure); the delta-law pins n = delta(B) + |a| + 1 rational boxes.
For the 40 most frequent such classes: |a| = 3 (and 5 when n <= 5): all multisets of n boxes from R(4) if n <= 3, else 150 random."""
import sys, pickle, collections, itertools, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact_arb, lib
from fractions import Fraction as Fr
if __name__=='__main__':
    random.seed(11)
    G=pickle.load(open('greedy_n2.pkl','rb')); D=G['D']
    A=pickle.load(open('gen1_R5_n2.pkl','rb'))
    R5=lib.rational(5); R4=lib.rational(4)
    cand=[(l,k,rep) for l,(k,rep) in D.items() if k[2]==-1]
    cand.sort(key=lambda x:-A[x[1]][0]); cand=cand[:40]
    jobs=[]
    for l,k,rep in cand:
        B=exact_arb.tree_of(rep[1],R5)
        for a in (3,5):
            n=int(k[3])+a+1
            if n<1 or n>5: continue
            if n<=3: ms=list(itertools.combinations_with_replacement(R4,n))
            else: ms=[tuple(random.choice(R4) for _ in range(n)) for _ in range(150)]
            for ms_ in ms: jobs.append(('tie a=%d %s'%(a,l),[B]+[u[2] for u in ms_]))
    print('sigma=-1 dangerous classes used',len(cand),'jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_d3.pkl',procs=2)
