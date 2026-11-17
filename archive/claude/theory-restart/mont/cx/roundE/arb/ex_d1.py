"""exact search E-D1: the 130 depth-one classes that occur in LP-open supports (arblp_n2): B^j u_1..u_n
(j=1: n=0,1,2 from R(4); j=2: n=0,1; j=3: n=0) and pairs B B' of the 30 most frequent with n = 0, 1 (R(4))."""
import sys, pickle, collections, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact_arb, lib
if __name__=='__main__':
    A=pickle.load(open('arblp_n2.pkl','rb')); reps=A['reps']
    sup=collections.Counter(l for r in A['res'] if r[1]=='open' for l in r[2][0] if l.startswith('g1'))
    R5=lib.rational(5); R4=lib.rational(4)
    T={l:exact_arb.tree_of(reps[l][1],R5) for l in sup}
    jobs=[]
    for l in sup:
        B=T[l]
        jobs.append(('1:'+l,[B]))
        for u in R4: jobs.append(('1u:'+l,[B,u[2]]))
        for u,v in itertools.combinations_with_replacement(R4,2): jobs.append(('1uu:'+l,[B,u[2],v[2]]))
        jobs.append(('2:'+l,[B,B]))
        for u in R4: jobs.append(('2u:'+l,[B,B,u[2]]))
        jobs.append(('3:'+l,[B,B,B]))
    top=[l for l,c in sup.most_common(30)]
    for a,b in itertools.combinations(top,2):
        jobs.append(('p:%s,%s'%(a,b),[T[a],T[b]]))
        for u in R4: jobs.append(('pu:%s,%s'%(a,b),[T[a],T[b],u[2]]))
    print('jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_d1.pkl',procs=3)
