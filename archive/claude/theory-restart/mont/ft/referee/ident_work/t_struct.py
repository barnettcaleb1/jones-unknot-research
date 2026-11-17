# Structured stress tests for integrality of D, F4, and additivity of D, F4 under body concatenation s.B1.B2
import sys, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, lp, flat_search as fs, words
from fractions import Fraction as Fr
rnd=random.Random(9801); t0=time.time()
def body(w): return w.split('.')[1:]
fams={'winding-runs':0,'wide':0,'necklace3-4':0}; bad=[]; cnt={k:0 for k in fams}
while time.time()-t0<150 and min(cnt.values())<120:
    f=rnd.choice(list(fams))
    if f=='winding-runs':
        # bodies with long runs of on-axis letters between generic pieces
        parts=['s']
        for _ in range(rnd.randint(1,3)):
            parts+=[rnd.choice(['x0','y0'])]*rnd.randint(2,6)
            b=R.gen2(rnd,rnd.randint(4,10),maxw=5,pw=0.15); parts+=body(b)
        w='.'.join(parts)
    elif f=='wide':
        w=R.gen2(rnd,rnd.randint(14,26),maxw=9,pw=0.25)
    else:
        m=rnd.randint(-3,3); parts=['s','r2']+[rnd.choice(['x1','y1'])]*abs(m)
        for _ in range(rnd.randint(3,4)):
            if rnd.random()<0.5: parts+=words.row(rnd.choice([-1,1])*rnd.choice([1,3,5]),ax=rnd.choice('xy'),off=rnd.choice('xy'))
            else: parts+=body(R.gen2(rnd,rnd.randint(4,9),maxw=3,pw=0.3))
        parts+=['u1']; w='.'.join(parts)
    v=R.all_vals(w)
    if v is None: continue
    cnt[f]+=1
    if v['D'].denominator!=1 or v['G4']%1440: bad.append((f,w,str(v['D']),str(v['G4']%1440)))
print('structured families checked:',cnt,'| failures:',len(bad),bad[:4],'| %.0fs'%(time.time()-t0))
# additivity under concatenation (equivariant connected sum along the axis; BRIEF Theorem N with mu = 0)
ok=0; tot=0; jm=0
while tot<60:
    a=R.gen2(rnd,rnd.randint(5,12),maxw=5,pw=0.3); b=R.gen2(rnd,rnd.randint(5,12),maxw=5,pw=0.3)
    va=R.all_vals(a,True); vb=R.all_vals(b,True)
    if va is None or vb is None: continue
    ab='.'.join(['s']+body(a)+body(b)); vab=R.all_vals(ab,True)
    if vab is None: continue
    tot+=1; jm+= vab['J']==lp.normalize(lp.mul(va['J'],vb['J']))
    ok+= (vab['D']==va['D']+vb['D'] and vab['F4']==va['F4']+vb['F4'])
print('concatenation s.B1.B2: J multiplicative %d/%d, D and F4 additive %d/%d'%(jm,tot,ok,tot))
