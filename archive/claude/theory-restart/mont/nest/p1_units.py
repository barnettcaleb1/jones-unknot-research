import sys, random, time
sys.path.insert(0,'nest')
from nlib import *
boxes=[(B,v) for B,v in load_boxes() if width(B)<=3]
rnd=random.Random(9); t0=time.time()
okp=badp=okn=badn=0
for i in range(10):
    (B1,v1),(B2,v2)=rnd.sample(boxes,2)
    c=vec(B1+'.'+B2)
    if not c or len(c)!=1: print('product not pinned',B1,B2); continue
    r=unit_ratio(c[0],star(v1,v2))
    if r==(1,0): okp+=1
    else: badp+=1; print('PRODUCT unit',r,'eps',eps(v1),eps(v2))
    m=rnd.choice([1,-1,2])
    cN=vec(body(m,[B1,B2]))
    if not cN or len(cN)!=1: print('body not pinned'); continue
    pred=F(m,star(v1,v2))
    if cN[0]==pred: okn+=1
    else: badn+=1; print('BODY mismatch m',m,'eps',eps(v1),eps(v2),'ratio',unit_ratio(cN[0],mvec(Xpow(-m),star(v1,v2))))
print('pinned product = v1*v2 exactly:',okp,'bad',badp,' | pinned 2-box body = F_m(v1*v2) exactly (eps(p) multiplicative unit):',okn,'bad',badn,' time',round(time.time()-t0,1))
