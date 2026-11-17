import sys, pickle, glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import relabel, sym, plat2
f=sys.argv[1]; res,units,n=pickle.load(open(f,'rb')); bad=0
for w,triv in units:
    ev=sym.symmetric(plat2.top_events(w))
    if not relabel.sister_is_unit(ev): bad+=1; print('NONTRIVIAL THETA WITH J=1 ?',w,flush=True)
print(f,'J=1 words',len(units),'sister non-unit',bad)
