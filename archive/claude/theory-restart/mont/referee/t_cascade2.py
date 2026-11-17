from rcore import *
def J_of(mu,N,seqs):
    bd=[(ach(u),bch(u)) for u in (ubox(s) for s in seqs)]
    A=fprod([a for a,b in bd]); B=fprod([b for a,b in bd])
    G=ad(ml(w1(mu),A),ml(w3(mu),sh(B,-3*N)))
    J=pdiv_exact(G,PHI3)
    return J,sum(sp(a) for a,b in bd),tp(G)-tp(A)
for m in (3,4,5,6,8,11,14,20):
    best=None
    for j in range(1,3*m+12):
        J,sA,T=J_of(3,0,[(-m,-1,-1),(-2,)+(-1,)*j])
        gap=sA-sp(J)
        if best is None or gap>best[0]: best=(gap,j,sp(J),sA,T)
    print('m',m,'max spanA-spanJ',best[0],'at j',best[1],'span J',best[2],'span A',best[3],'T',best[4])
