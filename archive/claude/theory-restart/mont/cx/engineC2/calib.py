import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, theta, time
rnd=random.Random(5); n=0; ok={1:0,-1:0}; bad=0; T=0
while n<150:
    w=fs.gen(rnd,rnd.randint(4,14))
    if not w: continue
    J=lp.J(w)
    if J is None: continue
    n+=1
    t0=time.time()
    try:
        J1=theta.J_events(theta.from_halfword(w),1)
        Jm=theta.J_events(theta.from_halfword(w),-1)
    except AssertionError as e:
        print('ASSERT',w,e); bad+=1; continue
    T+=time.time()-t0
    if J1==J: ok[1]+=1
    if Jm==J: ok[-1]+=1
    if J1!=J and Jm!=J: bad+=1; print('MISMATCH',w,J,J1)
print('agree t=A^4:',ok[1],' t=A^-4:',ok[-1],' bad',bad,' n',n,' time/word %.4f'%(T/n/2))
