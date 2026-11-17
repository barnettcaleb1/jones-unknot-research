"""Referee: pretzel T1 formula, clean-top formula, T2 class (top H >= -1, span >= 3n+1), probing beyond the builder's range."""
import random, sys, time, itertools
from rcore import *
from t_pretzel import Gclosed, topH, J_pretzel
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
t0=time.time()
# T1: rows -(2l+1), mu>=1
bad=0; cnt=0
for it in range(1500):
    n=rnd.randint(2,7); ls=[rnd.randint(1,15) for _ in range(n)]; mu=rnd.randint(1,12)
    if rnd.random()<0.4:  # force l_min = mu (degenerate)
        ls[0]=mu; ls[1:]=[max(x,mu+1) for x in ls[1:]] if rnd.random()<0.6 else ls[1:]
    rows=[-(2*l+1) for l in ls]
    th=topH(mu,rows)
    lm=min(ls); c=ls.count(lm); l2=sorted(ls)[1]
    if lm<mu: pred=mu+2-lm
    elif lm>mu or c>=2: pred=2
    else: pred=max(-1,mu+2-l2)
    cnt+=1
    if th!=pred: bad+=1; print('T1 formula FAIL',mu,ls,th,pred) if bad<10 else None
    J,_=J_pretzel(mu,rows)
    if sp(J)<3*n: print('T1 SPAN < 3n',mu,ls,sp(J))
print('T1 formula checked',cnt,'bad',bad)
# clean tops: mu>=1, p>=1 positive rows
bad=0; cnt=0
for it in range(1500):
    n=rnd.randint(2,7); mu=rnd.randint(1,12)
    rows=[rnd.choice([1,-1])*(2*rnd.randint(1,15)+1) for _ in range(n)]
    if all(r<0 for r in rows): rows[0]=-rows[0]
    pos=[(r-1)//2 for r in rows if r>0]
    pred=sum(pos)+mu+2+len(pos)
    cnt+=1
    if topH(mu,rows)!=pred: bad+=1; print('CLEAN TOP FAIL',mu,rows) if bad<10 else None
print('clean-top formula checked',cnt,'bad',bad)
# T2: one positive row j, negative rows l_i, mu=-m<=-2
cnt=0; minH=10**9; minexc=10**9; worst=None; fails=0; spanfail=0
for it in range(4000):
    m=rnd.randint(2,16); j=rnd.randint(1,16); q=rnd.randint(1,6)
    ls=[rnd.randint(1,18) for _ in range(q)]
    mode=rnd.random()
    if mode<0.25: j=m-1; ls=[max(l,j+1) for l in ls]                     # subcase (a)
    elif mode<0.6 and m>=3:                                                # subcase (b)
        j=rnd.randint(1,m-2); ls=[j]+[j+rnd.choice([2,2,3,4,5,1+rnd.randint(1,8)]) for _ in range(q-1)]
    rows=[2*j+1]+[-(2*l+1) for l in ls]; n=len(rows); mu=-m
    th=topH(mu,rows); J,_=J_pretzel(mu,rows)
    L=sum(ls); cnt+=1
    if sp(J)!=3*n+L+m-3+th: fails+=1; print('T2 span reduction FAIL',m,j,ls,sp(J),th)
    if th<minH: minH=th; worst=(m,j,ls,th,sp(J))
    minexc=min(minexc,sp(J)-3*n)
    if sp(J)<3*n+1: spanfail+=1; print('T2 span < 3n+1',m,j,ls,sp(J))
print('T2 checked',cnt,'reduction fails',fails,'min top H',minH,'at',worst,'min span-3n',minexc,'span<3n+1:',spanfail)
print('time',round(time.time()-t0,1))
