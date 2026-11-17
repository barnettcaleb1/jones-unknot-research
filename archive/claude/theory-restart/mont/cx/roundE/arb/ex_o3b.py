"""exact search E-O3b: the n=3/4 unsafe classes NOT closed by H3(B) (o3_u_n3/n4): representative box (gen1k3u rep) + n rational
boxes for n = delta-law values of every mu-class (and 1, 2): all multisets of R(4) for n <= 2, 150 random for n >= 3."""
import sys, pickle, itertools, random
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import exact_arb, lib, h3b
if __name__=='__main__':
    random.seed(41); R5=lib.rational(5); R4=lib.rational(4)
    jobs=[]
    for tag,L in (('n3',5),('n4',4)):
        K=pickle.load(open('gen1k3u_R%d_%s.pkl'%(L,tag),'rb')); H=pickle.load(open('o3_u_%s.pkl'%tag,'rb')); Hc=set(H['Hc'])
        Rp=R5 if L==5 else R4
        for key,subs in K.items():
            if key in Hc: continue
            ns=set([1,2])
            for mu in h3b.MUS:
                o,sgs,ds=h3b.WJ[mu]; n=int(Fr(key[3])-ds)
                if 1<=n<=6: ns.add(n)
            for d3,rep in subs.items():
                B=exact_arb.tree_of(rep,Rp)
                for n in sorted(ns):
                    ms=list(itertools.combinations_with_replacement(R4,n)) if n<=2 else [tuple(random.choice(R4) for _ in range(n)) for _ in range(150)]
                    for us in ms: jobs.append(('%s n=%d'%(tag,n),[B]+[u[2] for u in us]))
    print('jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_o3b.pkl',procs=2)
