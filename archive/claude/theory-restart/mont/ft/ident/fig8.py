# find half-words of the figure-eight knot, group by J (distinct inversions), report quotient constituents
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, kauffman, flat_search as fs
V41={-2:1,-1:-1,0:1,1:-1,2:1}
V31={1:1,3:1,4:-1}; V31m={-1:1,-3:1,-4:-1}
names={tuple(sorted(V41.items())):'4_1',tuple(sorted(V31.items())):'3_1',tuple(sorted(V31m.items())):'3_1*',((0,1),):'0_1',
       ((-7,-1),(-6,1),(-5,-1),(-4,1),(-2,1)):'5_1*?',((2,1),(4,1),(5,-1),(6,1),(7,-1)):'5_1?'}
def nm(V): return names.get(tuple(sorted(V.items())),str(sorted(V.items())))
rnd=random.Random(2); byJ={}
for it in range(30000):
    w=fs.gen(rnd,rnd.randint(4,10))
    if not w: continue
    J=lp.J(w)
    if J is None: continue
    V=diag.jones_from_bracket(kauffman.bracket(w))
    if V not in (V41,V31,V31m): continue
    key=(nm(V),tuple(sorted(J.items())))
    if key in byJ: continue
    inv=diag.all_invariants(w)
    byJ[key]=(w,nm(inv['Kin']['V']),nm(inv['Kout']['V']),nm(inv['Uin']['V']),nm(inv['Uout']['V']))
for (kn,J),(w,a,b,c,d) in sorted(byJ.items()):
    print('%-5s J=%s\n      word %s  K_in=%s K_out=%s U_in=%s U_out=%s'%(kn,dict(J),w,a,b,c,d))
