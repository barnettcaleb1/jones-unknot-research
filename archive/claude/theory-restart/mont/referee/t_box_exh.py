import itertools, time
from rcore import *
from t_box import auto, exact_state
from fractions import Fraction
t0=time.time(); n=0; bad=0
vals=[m for m in range(-3,4) if m]
for k in range(1,7):
    for s in itertools.product(vals,repeat=k):
        if s[0]==-1: continue
        u=ubox(s); a=ach(u); b=bch(u)
        st,rho,rq=auto(s); est=exact_state(u)
        xa=xs(a,2); xb=xs(b,2)
        if est!=st or xa[1]!=rho or xb[1]!=rho+rq or sp(a)<4: bad+=1; print('BAD',s)
        n+=1
print('exhaustive k<=6,|m|<=3:',n,'bad',bad,'time',round(time.time()-t0,1))
