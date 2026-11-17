from pretz import *
import itertools
bad=cnt=0
for m in range(2,8):
    j=m-1
    for q in (1,2,3):
        for ls in itertools.combinations_with_replacement(range(m,m+5),q):
            rows=[2*j+1]+[-(2*l+1) for l in ls]
            th=top(G(-m,rows))-2*len(rows)
            lmin=min(ls); pred=1 if lmin==m else (0 if lmin==m+1 else -1)
            cnt+=1
            if th!=pred: bad+=1; print('BAD',m,ls,th,pred)
# case (b) first order: l1=j unique < m-1: top H = 1 iff x1 != 0 (l1=m-2 or some l_i=l1+1)
for m in range(3,9):
    for l1 in range(1,m-1):
        for q in (0,1,2):
            for rest in itertools.combinations_with_replacement(range(l1+1,l1+5),q):
                ls=(l1,)+rest; rows=[2*l1+1]+[-(2*l+1) for l in ls]
                th=top(G(-m,rows))-2*len(rows)
                x1=-(1 if l1==m-2 else 0)-sum(1 for l in rest if l==l1+1)
                if x1!=0:
                    cnt+=1
                    if th!=1: bad+=1; print('BADb',m,ls,th)
print('checked',cnt,'bad',bad)
