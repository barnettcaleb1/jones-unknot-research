from nt import *
from auto2 import run
from fractions import Fraction
import random
def bar(p): return {-e:c for e,c in p.items()}
rnd=random.Random(5); bad=0; cnt=0
seqs=normal_seqs(3,3)
for s in seqs:
    k=len(s); u=box(s); a,b=chan(u); um=box(mirror_seq(s)); am,bm=chan(um)
    if bar(a)!=shift(am,-4*k) or bar(b)!=shift(bm,-4*k-3): bad+=1
    cnt+=1
for trial in range(400):
    n=rnd.randint(2,4); ss=[rnd.choice(seqs) for _ in range(n)]
    mu=rnd.choice([m for m in range(-5,6) if m]); N=rnd.randint(-3,5)
    K=sum(len(s) for s in ss)
    J1=neck(mu,N,[box(s) for s in ss]); J2=neck(-mu,n-N,[box(mirror_seq(s)) for s in ss])
    if bar(J1)!=shift(J2,-4*K): bad+=1
    cnt+=1
# third-order law on alternating S boxes: x2(a) = -(k - [m0<=-2])/2
for s in normal_seqs(6,3):
    st,r=run(s)
    if st[0]=='S' and r==0:
        a=box(s)[0]; e=top(a)
        x2=Fraction(a.get(e-2,0),a[e]); pred=-Fraction(len(s)-(1 if s[0]<=-2 else 0),2)
        if x2!=pred: bad+=1; print('x2 bad',s,x2,pred)
        cnt+=1
print('checked',cnt,'bad',bad)
