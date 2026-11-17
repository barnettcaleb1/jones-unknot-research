"""Referee: exhaustive probe of the OPEN pretzel subcase T2(b) (row/antirow pair), incl. the third-order region x1=x2=0."""
import itertools, time, sys
from rcore import *
from t_pretzel import Gclosed
MMAX=int(sys.argv[1]) if len(sys.argv)>1 else 18
QMAX=int(sys.argv[2]) if len(sys.argv)>2 else 4
t0=time.time(); cnt=0; minH=10**9; worst=[]; hist={}
third=0; third_min=10**9
for m in range(3,MMAX+1):
    for l1 in range(1,m-1):           # j = l1 = l_min < m-1
        j=l1
        vals=[l1+d for d in range(1,8)]+[l1+12]
        for q in range(0,QMAX+1):
            for others in itertools.combinations_with_replacement(vals,q):
                ls=(l1,)+others
                rows=[2*j+1]+[-(2*l+1) for l in ls]; n=len(rows)
                th=tp(Gclosed(-m,rows))-2*n
                cnt+=1
                hist[th]=hist.get(th,0)+1
                x1=-(1 if l1==m-2 else 0)-sum(1 for l in others if l==l1+1)
                x2=-1+(1 if l1==m-3 else 0)+sum(1 for l in others if l==l1+2)
                if x1==0 and x2==0:
                    third+=1; third_min=min(third_min,th)
                if th<minH: minH=th; worst=[(m,j,ls,th)]
                elif th==minH and len(worst)<5: worst.append((m,j,ls,th))
                # predicted top H from x1,x2 when decisive
                if x1!=0 and th!=1: print('x1!=0 but top H',th,m,j,ls)
                if x1==0 and x2!=0 and th!=0: print('x1=0,x2!=0 but top H',th,m,j,ls)
print('T2(b) configurations',cnt,'top H histogram',dict(sorted(hist.items())),'min',minH,'examples',worst)
print('third-order region (x1=x2=0):',third,'min top H there',third_min,'time',round(time.time()-t0,1))
