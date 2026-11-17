"""Certify all J = 1 words of the S2 enumeration: sister invariant (A_1 coloured 2) must be a unit if Theta is trivial."""
import sys, pickle, glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import relabel, sym, plat2
tot=0; bad=[]
for f in sorted(glob.glob(sys.argv[1])):
    res,units,n=pickle.load(open(f,'rb'))
    for w,triv in units:
        ev=sym.symmetric(plat2.top_events(w)); tot+=1
        if not relabel.sister_is_unit(ev): bad.append(w); print('NONTRIVIAL THETA WITH J=1 ?',w,flush=True)
print('J=1 words checked',tot,'sister non-unit',len(bad))
