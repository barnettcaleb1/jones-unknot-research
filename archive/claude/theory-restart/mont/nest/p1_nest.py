import sys, time, random
sys.path.insert(0,'nest'); sys.path.insert(0,'.')
from nlib import *
import alex
from words import row
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 3)
gen_boxes=[(B,v) for B,v in load_boxes() if width(B)<=3]
def rowbox(r):
    j=(abs(r)-1)//2
    B='.'.join(row(r))
    v=apply(('X'*j+'Y') if r>0 else ('x'*j+'y'))
    return ('box',B,v)
rat=[rowbox(r) for r in (-5,-3,-1,1,3,5)]
gen=[('box',B,v) for B,v in gen_boxes]
print('pool: rational rows',len(rat),' general boxes (width<=3)',len(gen))
def rand_tree(depth, maxkids=3):
    if depth==0:
        return rnd.choice(rat) if rnd.random()<0.5 else rnd.choice(gen)
    k=rnd.choice([1,2,2,3][:maxkids+1])
    kids=[rand_tree(depth-1, maxkids=2)]+[rand_tree(rnd.choice([0,0,depth-1]),maxkids=2) for _ in range(k-1)]
    rnd.shuffle(kids)
    m=rnd.choice([-2,-1,1,2])
    return ('neck',m,kids)
def run(depth, count, tmax):
    ok=bad=skip=0; t0=time.time()
    for i in range(count):
        if time.time()-t0>tmax: break
        T=('neck',rnd.choice([-2,-1,1,2]),[rand_tree(depth-1)]+([rand_tree(rnd.choice([0,depth-1]))] if rnd.random()<0.6 else []))
        if tree_depth(T)!=depth: continue
        w='s.'+tree_word(T)
        if width(w[2:])>8: continue
        t1=time.time()
        Jw=J(w)
        if Jw is None: skip+=1; continue
        v=tree_vec(T)
        pred=normalize(v[0])
        if span(Jw)==0: print('UNIT',w,'alex',alex.alex_poly(w))
        if pred==Jw: ok+=1
        else: bad+=1; print('MISMATCH depth',depth,w)
        print('  depth',depth,'width',width(w[2:]),'len',len(w.split('.')),'ok' if pred==Jw else 'BAD','%.1fs'%(time.time()-t1),'span',span(Jw),flush=True)
    print('DEPTH',depth,'ok',ok,'bad',bad,'skip',skip,'time',round(time.time()-t0,1),flush=True)
run(2, 40, 240)
run(3, 20, 300)
