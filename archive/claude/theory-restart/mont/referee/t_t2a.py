import itertools, time
from rcore import *
from t_pretzel import Gclosed
t0=time.time(); cnt=0; bad=0
for m in range(2,15):
    j=m-1
    vals=[m,m+1,m+2,m+3,m+5]
    for q in range(1,5):
        for ls in itertools.combinations_with_replacement(vals,q):
            rows=[2*j+1]+[-(2*l+1) for l in ls]; n=len(rows)
            th=tp(Gclosed(-m,rows))-2*n
            lm=min(ls); pred=1 if lm==m else (0 if lm==m+1 else -1)
            cnt+=1
            if th!=pred: bad+=1; print('T2(a) FAIL',m,ls,th,pred)
print('T2(a) exhaustive (m<=14, up to 4 negative rows from m..m+5):',cnt,'bad',bad,'time',round(time.time()-t0,1))
