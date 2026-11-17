"""Spot check of the necklace formula (Theorem N, BRIEF) against the bracket state sum lp.J on NEW mixed-sign pretzel words."""
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp, words
from rcore import *
from t_pretzel import rowvec
def formula(m,rows):
    mu=-m
    A=fprod([ach(rowvec(r)) for r in rows]); B=fprod([bch(rowvec(r)) for r in rows])
    G=ad(ml(w1(mu),A),ml(w3(mu),B)); return lp.normalize(pdiv_exact(G,PHI3))
for m,rows in [(2,[3,-3]),(-2,[5,-3]),(1,[-3,-5]),(3,[3,-5]),(-1,[-3,3,-3]),(2,[-5,3]),(-3,[3,3]),(1,[3,-3,3])]:
    t0=time.time()
    w=lp.mont(m,rows) if hasattr(lp,'mont') else words.mont(m,rows)
    Jb=lp.J(w)
    Jf=formula(m,rows)
    print('m',m,'rows',rows,'bracket==formula:',Jb==Jf,'span',None if Jb is None else lp.span(Jb),'time',round(time.time()-t0,1),flush=True)
