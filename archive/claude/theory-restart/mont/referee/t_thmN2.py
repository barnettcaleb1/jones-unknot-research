import sys, time, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp, words
from rcore import *
from t_pretzel import rowvec
from t_thmN import formula
rnd=random.Random(99); t0=time.time(); ok=0; bad=0; units=0; none=0; cnt=0
while time.time()-t0<240 and cnt<300:
    n=rnd.randint(2,4); rows=[rnd.choice([1,-1])*rnd.choice([1,3,3,5,5,7,9]) for _ in range(n)]
    m=rnd.choice([x for x in range(-4,5) if x])
    w=words.mont(m,rows); Jb=lp.J(w)
    if Jb is None: none+=1; continue
    Jf=formula(m,rows); cnt+=1
    if Jb==Jf: ok+=1
    else: bad+=1; print('MISMATCH',m,rows)
    nonint=sum(1 for r in rows if abs(r)>=3)
    if len(Jb)==1:
        units+=1; print('UNIT J for',m,rows,'non-integral rows',nonint)
print('pretzel words',cnt,'formula ok',ok,'bad',bad,'unit J',units,'(None:',none,') time',round(time.time()-t0,1))
