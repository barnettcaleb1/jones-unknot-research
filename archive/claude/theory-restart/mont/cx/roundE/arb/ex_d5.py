"""exact search E-D5: ALIGNED POSITIVE POTENTIAL at high multiplicity (the LP-open points use 4-7 copies of a positive-potential
depth-one class, e.g. g1_575 x 5.6): all 28 positive-potential n=2 classes, B^j for j = 4..7 with n = 0, 1 (R(4)), and
B^j B'^j' for the 10 most frequent pairs with j + j' in {4, 5, 6}, n = 0."""
import sys, pickle, collections, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import exact_arb, lib
if __name__=='__main__':
    A=pickle.load(open('gen1_R5_n2.pkl','rb'))
    R5=lib.rational(5); R4=lib.rational(4)
    pos=[k for k,v in A.items() if v[1] and (k[0][0]>0 or k[1][0]>0 or k[0][2]>0 or k[1][2]>0)]
    pos.sort(key=lambda k:-A[k][0])
    T={k:exact_arb.tree_of(A[k][2],R5) for k in pos}
    jobs=[]
    for k in pos:
        for j in range(4,8):
            jobs.append(('B^%d'%j,[T[k]]*j))
            for u in R4: jobs.append(('B^%d u'%j,[T[k]]*j+[u[2]]))
    top=pos[:5]
    for a,b in itertools.combinations(top,2):
        for j in range(1,6):
            for jj in range(1,6):
                if 4<=j+jj<=6: jobs.append(('B^%d B\'^%d'%(j,jj),[T[a]]*j+[T[b]]*jj))
    print('positive-potential classes',len(pos),'jobs',len(jobs),flush=True)
    exact_arb.run(jobs,'ex_d5.pkl',procs=3)
