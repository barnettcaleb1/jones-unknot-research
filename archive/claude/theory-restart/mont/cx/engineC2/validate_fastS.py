import sys, random, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import fastS, theta, sym, vc, lib
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
rnd=random.Random(3)
R7=lib.rational(6); G=lib.general()
ok=bad=0
def randtree(depth=0):
    r=rnd.random()
    if r<0.45 or depth>=2:
        return rnd.choice(R7)[2]
    if r<0.6: return rnd.choice(G)[2]
    if r<0.8: return ('p',[randtree(depth+1),randtree(depth+1)])
    m=rnd.choice([-2,-1,1,2])
    return ('n',m,[randtree(depth+1)])
n=0
while n<40:
    T=randtree()
    try: v=vc.vec(T)
    except AssertionError: continue
    if v is None: continue
    w=vc.word(T)
    m=rnd.choice([-4,-2,2,4])
    Jf=fastS.J_of(tab[m],v)
    Jd=theta.J_events(sym.symmetric(sym.Sneck_top(m,w)))
    n+=1
    if Jf==Jd: ok+=1
    else: bad+=1; print('BAD',m,w,Jf,Jd)
print('fastS vs direct evaluator:',ok,'ok',bad,'bad')
