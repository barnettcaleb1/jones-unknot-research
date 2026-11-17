import sys, json, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import fastsym, lp
def N(J,k): return sum(c*e**k for e,c in J.items())
def fn(w):
    J=lp.J(w)
    if J is None: return None
    return {'N1':N(J,1),'N2':N(J,2),'M2':sum(c*(-1)**(e%2)*e**2 for e,c in J.items())}
out=fastsym.sample(31,1,300,fn=fn)
by={}
for r in out: by.setdefault(r['type'],[]).append(r)
for ty,rr in sorted(by.items()):
    print(ty,len(rr),'N1 symbols:',sorted(set(r['sym']['N1'] for r in rr)))
out=fastsym.sample(32,2,300,fn=fn)
by={}
for r in out: by.setdefault(r['type'],[]).append(r)
print('level 2: N2 symbol consistency')
for ty,rr in sorted(by.items()):
    print(' ',ty,len(rr),'N2:',sorted(set(r['sym']['N2'] for r in rr)),'M2:',sorted(set(r['sym']['M2'] for r in rr)))
