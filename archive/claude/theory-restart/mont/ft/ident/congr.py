# value checks: D = (M3/36 - 12 v3)/5 integral?  F4 = (M4 - loc4)/1440 integral?  on varied words
import sys, random, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, flat_search as fs, words
from fractions import Fraction as F
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
def check(w):
    J=lp.J(w)
    if J is None: return None
    inv=diag.K_invariants(w)
    if inv is None: return None
    a2,v3,a4,j4=inv['a2'],inv['v3'],inv['a4'],inv['j4']
    m3=F(M(J,3)); m4=F(M(J,4))
    D=(m3/36-12*v3)/5
    loc=-1440*a2*a2-1440*a4+864*j4-120*a2
    F4=(m4-loc)/1440
    return dict(w=w,a2=a2,v3=v3,a4=a4,j4=j4,M3=m3,M4=m4,D=D,F4=F4)
if __name__=='__main__':
  rnd=random.Random(int(sys.argv[1])); n=int(sys.argv[2]); out=[]; bad=[]
  while len(out)<n:
      w=fs.gen(rnd,rnd.randint(6,22))
      if not w: continue
      r=check(w)
      if r is None: continue
      out.append(r)
      if r['D'].denominator!=1 or r['F4'].denominator!=1: bad.append(r)
  print('checked',len(out),'non-integral D or F4:',len(bad))
  for b in bad[:5]: print(b)
  json.dump([{k:str(v) for k,v in r.items()} for r in out],open('congr_%s.json'%sys.argv[1],'w'))
