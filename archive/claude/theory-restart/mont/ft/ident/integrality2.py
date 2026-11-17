import sys, json, glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.argv=['x','0','0']
import integrality as I
found={}
for f in glob.glob('hunt_*.json'): found.update(json.load(open(f)))
bad=[]
for ty,(w,sites) in sorted(found.items()):
    A=I.alt(w,sites)
    if A is None: print('fail',ty); continue
    m=len(sites)
    if (m<=2 and A[0]%180!=0) or A[1]%1440!=0: bad.append((ty,A))
print('witnesses',len(found),'violations',bad)
