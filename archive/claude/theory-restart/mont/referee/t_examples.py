"""Referee: recompute the specific examples quoted in REPORT Sec 4, 6."""
from rcore import *
def J_of(mu,N,seqs):
    bd=[(ach(u),bch(u)) for u in (ubox(s) for s in seqs)]
    A=fprod([a for a,b in bd]); B=fprod([b for a,b in bd])
    P1_=ml(w1(mu),A); P3_=ml(w3(mu),sh(B,-3*N)); G=ad(P1_,P3_)
    J=pdiv_exact(G,PHI3)
    sA=sum(sp(a) for a,b in bd)
    T=tp(G)-tp(A)
    Tgen=max(tp(w1(mu)), tp(w3(mu))+tp(B)-tp(A)-3*N)
    return J,sA,T,Tgen,G,P1_,P3_
def show(J,k=4):
    e=tp(J); f=bt(J)
    return [J.get(e-i,0) for i in range(k)], [J.get(f+i,0) for i in range(k)]
# (1) n=13 counterexample to 4n-3
J,sA,T,Tg,*_=J_of(1,4,[(-2,)]*7+[(1,)]*6); print('n=13 mu=1 N=4: span',sp(J),'spanA',sA,'4n-3=',49, 'T',T,'Tgen',Tg)
J,sA,T,Tg,*_=J_of(-1,5,[(1,)]*6+[(-2,)]*7); print('n=13 mu=-1 N=5: span',sp(J),'spanA',sA, 'T',T,'Tgen',Tg)
J,sA,T,Tg,*_=J_of(-1,9,[(1,)]*7+[(-2,)]*6); print('mirror of first (mu=-1,N=9,u(1)^7 u(-2)^6): span',sp(J))
# (2) minimal family u(-2)^n mu=-1 N=1 ; and claimed mirror family u(1)^n, mu=-1, N=n ; true mirror u(1)^n, mu=1, N=n-1
for n in range(2,8):
    a=sp(J_of(-1,1,[(-2,)]*n)[0]); b=sp(J_of(-1,n,[(1,)]*n)[0]); c=sp(J_of(1,n-1,[(1,)]*n)[0])
    print('n',n,'u(-2)^n mu=-1 N=1 span',a,'| u(1)^n mu=-1 N=n span',b,'| u(1)^n mu=1 N=n-1 span',c,'| 3n',3*n,'4n-3',4*n-3)
# (3) P1 example
J,*_=J_of(-2,2,[(-2,)]*6); print('P1 example: top',show(J)[0],'bottom',show(J)[1],'span',sp(J))
# (4) cascade
for (m,j) in [(5,14),(5,3),(5,6),(5,10),(8,3),(8,6),(8,10),(8,14),(3,3),(3,6),(3,10),(3,14)]:
    J,sA,T,Tg,*_=J_of(3,0,[(-m,-1,-1),(-2,)+(-1,)*j])
    print('cascade m',m,'j',j,'span J',sp(J),'span A',sA,'T',T,'Tgen',Tg)
