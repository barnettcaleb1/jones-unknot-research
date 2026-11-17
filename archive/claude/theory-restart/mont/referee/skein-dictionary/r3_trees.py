# R3: random trees over ALL 50 general bodies (incl. scalar 6,25,35,44 and rational-vector ones) + rational boxes;
# compare calculus (Theorems N/O/V with Norm) against lp.J of the explicit halfword.
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import vc, lp
rnd=random.Random(20261117)
SCAL=[6,25,35,44]
def leaf():
    r=rnd.random()
    if r<0.45: return ('g',rnd.choice(SCAL) if rnd.random()<0.4 else rnd.randrange(50))
    w=''.join(rnd.choice('XxYy') for _ in range(rnd.randint(1,3)))
    return ('w',w)
def tree(d):
    if d==0: return leaf()
    k=rnd.randint(1,2)
    kids=[tree(d-1) if rnd.random()<0.5 else leaf() for _ in range(k)]
    m=rnd.choice([-2,-1,1,2])
    return ('n',m,kids)
okH=okV=badH=badV=skip=0; scal_used=0
for it in range(70):
    T=('p',[tree(rnd.randint(0,2)) for _ in range(rnd.randint(1,2))])
    s=repr(T); scal_used+=any(("('g', %d)"%i) in s for i in SCAL)
    try: p=vc.vec(T)
    except AssertionError as e: print('THEOREM-O UNIT ASSERT FAILED',T,e); continue
    body=vc.word(T)
    if len(body)>140: skip+=1; continue
    mu=rnd.choice([-2,-1,1,2])
    Jw=lp.J('s.r2.'+vc.tw(-mu)+body+'.u1')
    Jc=vc.J_neck(mu,p)
    if Jw is None: skip+=1
    elif Jw==Jc: okH+=1
    else: badH+=1; print('H MISMATCH',T,mu)
    a=rnd.choice([-3,-1,1,3])
    Jw=lp.J(vc.vert_word(a,body)); Jc=vc.J_vert(a,p)
    if Jw is None: skip+=1
    elif Jw==Jc: okV+=1
    else: badV+=1; print('V MISMATCH',T,a)
print('horizontal ok',okH,'bad',badH,'| vertical ok',okV,'bad',badV,'| skipped',skip,'| trees using scalar bodies',scal_used)
