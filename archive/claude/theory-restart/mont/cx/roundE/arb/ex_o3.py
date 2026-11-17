"""exact search E-O3: the ORDER-3 SURVIVORS (single dangerous box B, k = 1): every (order-3 subclass, mu) with T3 possible / T2 open /
'd=0 r=1' open in o3h, and every subclass with an open vertical item in o3v.  Explicit box = the gen1k3 representative of the
subclass; n = the delta-law value (H: delta(B) - delta*(mu); V ties: delta + |a| + 1 for |a| = 3, 5, 7); rational parts: all
multisets from R(4) for n <= 3 (R(5) for n <= 2), 200 random for n >= 4."""
import sys, pickle, collections, itertools, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import exact_arb, lib, h3b
from fractions import Fraction as Fr
if __name__=='__main__':
    random.seed(31)
    K3=pickle.load(open('gen1k3_R5_n2.pkl','rb')); O=pickle.load(open('o3h.pkl','rb')); V=pickle.load(open('o3v.pkl','rb'))
    R5=lib.rational(5); R4=lib.rational(4)
    OK=('n<0','r1: closed@2','r1: order3 CLOSED','tie T3=False T2:closed')
    targets=set()
    for (key,d3,mu,end,mu3),v in O['res']:
        if v not in OK:
            o,sgs,ds=h3b.WJ[mu]; n=int(Fr(key[3])-ds)
            targets.add((key,d3,n))
    for key,d3,out in V['res']:
        if out:
            dl=int(Fr(key[3]))
            for a in (3,5,7): targets.add((key,d3,dl+a+1))
    def rational_parts(n):
        if n<=0: return [()]
        if n<=2: return list(itertools.combinations_with_replacement(R5,n))
        if n==3: return list(itertools.combinations_with_replacement(R4,3))
        return [tuple(random.choice(R4) for _ in range(n)) for _ in range(200)]
    jobs=[]
    for key,d3,n in sorted(targets,key=str):
        if n<1 or n>7: continue
        rep=K3[key][d3]; B=exact_arb.tree_of(rep,R5)
        for us in rational_parts(n): jobs.append(('o3 n=%d'%n,[B]+[u[2] for u in us]))
    print('order-3 survivor configurations',len(targets),'jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_o3.pkl',procs=3)
