import sys, time, random
sys.path.insert(0,'nest'); sys.path.insert(0,'.')
from nlib import *
import alex
from words import row
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 5)
def rowbox(r):
    j=(abs(r)-1)//2
    return ('box','.'.join(row(r)),apply(('X'*j+'Y') if r>0 else ('x'*j+'y')))
small_rat=[rowbox(r) for r in (-3,-1,1,3)]
small_gen=[('box',B,v) for B,v in load_boxes() if width(B)<=3 and len(B.split("."))<=9]
print('small general boxes',len(small_gen),[B for _,B,_ in small_gen])
def leaf(): return rnd.choice(small_rat) if rnd.random()<0.5 else rnd.choice(small_gen)
ok=bad=skip=0; t0=time.time()
for i in range(40):
    if time.time()-t0>420: break
    # depth 3 chain with side leaves: outer( inner( innermost(leaves), leaf ), leaf )
    T1=('neck',rnd.choice([-2,-1,1,2]),[leaf() for _ in range(rnd.choice([1,2]))])
    T2=('neck',rnd.choice([-2,-1,1,2]),[T1]+[leaf() for _ in range(rnd.choice([0,1]))]); 
    k2=T2[2][:]; rnd.shuffle(k2); T2=('neck',T2[1],k2)
    T3=('neck',rnd.choice([-2,-1,1,2]),[T2]+[leaf() for _ in range(rnd.choice([0,1]))])
    k3=T3[2][:]; rnd.shuffle(k3); T3=('neck',T3[1],k3)
    w='s.'+tree_word(T3)
    t1=time.time()
    Jw=J(w)
    if Jw is None: skip+=1; continue
    pred=normalize(tree_vec(T3)[0])
    good=(pred==Jw)
    ok+=good; bad+=(not good)
    print('  depth',tree_depth(T3),'width',width(w[2:]),'len',len(w.split('.')),'ok' if good else 'BAD','%.1fs'%(time.time()-t1),'span',span(Jw),flush=True)
    if not good: print('MISMATCH',w)
    if span(Jw)==0: print('UNIT',w,'det',alex.alex_eval(w,-1),'D(2)',alex.alex_eval(w,2),'D(3)',alex.alex_eval(w,3),flush=True)
print('DEPTH3 ok',ok,'bad',bad,'skip',skip,'time',round(time.time()-t0,1))
