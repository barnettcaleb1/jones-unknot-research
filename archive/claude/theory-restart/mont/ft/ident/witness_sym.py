import sys, json, glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import fastsym, chord
from fractions import Fraction as F
found={}
for f in glob.glob('hunt_*.json'): found.update(json.load(open(f)))
out=[]; bad=0
for ty,(w,sites) in sorted(found.items()):
    if len(sites)!=3: 
        sym=fastsym.config_symbol(w,sites)
        print('m=%d %-12s M2=%s a2=%s'%(len(sites),ty,sym['M2'],sym['a2'])); continue
    sym=fastsym.config_symbol(w,sites)
    if sym is None: print('fail',ty); continue
    d8=F(sym['M3'])/36-12*F(sym['v3'])
    if (d8/40).denominator!=1: bad+=1
    out.append((ty,str(d8/40),str(sym['v3'])))
print('3-element witnesses',len(out),'with D-symbol not in 8Z:',bad)
print('nonzero D/8 on new types:',[(t,d) for t,d,v in out if d!='0'])
json.dump(out,open('witness_D.json','w'))
