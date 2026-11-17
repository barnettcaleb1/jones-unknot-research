"""exact search E-D6 (GAP-ELIG): INELIGIBLE depth-one classes (|lc b/lc a| != 1 at an end or span a < 1), excluded by every
certificate theorem (C1, lpgen, ARB).  The 120 most frequent ineligible n=2 signatures: B u (R(4)), B u u' (R(4)), B^2, B^2 u, B^3."""
import sys, pickle, collections, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact_arb, lib
if __name__=='__main__':
    A=pickle.load(open('gen1_R5_n2.pkl','rb'))
    R5=lib.rational(5); R4=lib.rational(4)
    inel=[k for k,v in A.items() if not v[1]]
    inel.sort(key=lambda k:-A[k][0])
    print('ineligible n=2 signatures',len(inel),'boxes',sum(A[k][0] for k in inel),'of',sum(v[0] for v in A.values()),flush=True)
    jobs=[]
    for k in inel[:120]:
        B=exact_arb.tree_of(A[k][2],R5)
        jobs.append(('1',[B]))
        for u in R4: jobs.append(('1u',[B,u[2]]))
        for u,v in itertools.combinations_with_replacement(R4,2): jobs.append(('1uu',[B,u[2],v[2]]))
        jobs.append(('2',[B,B]))
        for u in R4: jobs.append(('2u',[B,B,u[2]]))
        jobs.append(('3',[B,B,B]))
    print('jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_d6.pkl',procs=3)
