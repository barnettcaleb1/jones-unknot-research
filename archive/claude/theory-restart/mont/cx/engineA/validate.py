"""Validate vc.py against lp.J on explicit halfwords (exact equality of normalised J)."""
import sys, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lp
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
def rword(L):
    w=''
    while len(w)<L:
        c=rnd.choice('XxYy')
        if w and {'X':'x','x':'X','Y':'y','y':'Y'}[c]==w[-1]: continue
        w+=c
    return w
def rtree(depth):
    if depth==0 or rnd.random()<0.3:
        r=rnd.random()
        if r<0.6: return ('w',rword(rnd.randint(1,4)))
        return ('g',rnd.randrange(50))
    n=rnd.choice([1,2,2,3])
    m=rnd.choice([-2,-1,1,2,3,-3])
    return ('n',m,[rtree(depth-1) for _ in range(n)])
ok=bad=skip=0; t0=time.time()
stats={'neck':[0,0],'vert':[0,0],'tree':[0,0]}
for trial in range(int(sys.argv[2]) if len(sys.argv)>2 else 60):
    T=rtree(rnd.choice([1,2,2,3]))
    w=vc.hw(T)
    if len(w.split('.'))>60: skip+=1; continue
    Jd=lp.J(w)
    if Jd is None: skip+=1; continue
    Jc=vc.Jtree(T)
    stats['tree'][0 if Jc==Jd else 1]+=1
    if Jc!=Jd: print('TREE MISMATCH',w,Jc,Jd)
    # vertical closure of the same body
    a=rnd.choice([-3,-1,1,3])
    vw=vc.vert_word(a,vc.word(T))
    if len(vw.split('.'))<=60:
        Jd=lp.J(vw)
        if Jd is not None:
            Jc=vc.J_vert(a,vc.vec(T))
            stats['vert'][0 if Jc==Jd else 1]+=1
            if Jc!=Jd: print('VERT MISMATCH',vw,Jc,Jd)
print(stats,'skipped',skip,'time',round(time.time()-t0,1))
