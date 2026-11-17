# Which cyclotomic points carry an exact relation between J_(K,h) and V_K?  (identification check, ~60 knots)
import sys, random, cmath, math
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs
import kauffman
def VK(word):
    kb=kauffman.bracket(word)
    if not kb: return None
    kb={e:c for e,c in kb.items() if c}
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}
    d=sum(e*c for e,c in V.items())
    return {e-d:c for e,c in V.items()}
def ev(p,x): return sum(c*x**e for e,c in p.items())
rnd=random.Random(5); data=[]
while len(data)<60:
    w=fs.gen(rnd,rnd.randint(6,18))
    if not w: continue
    Jn=lp.J(w)
    if Jn is None: continue
    V=VK(w)
    if V is None: continue
    data.append((Jn,V))
rels={'J=1':lambda J,V,z:ev(J,z)-1,
      'J=V(t)':lambda J,V,z:ev(J,z)-ev(V,z),
      'J=V(t^2)':lambda J,V,z:ev(J,z)-ev(V,z*z),
      'J=V(t^-2)':lambda J,V,z:ev(J,z)-ev(V,1/(z*z)),
      'J=V(t^2)^2':lambda J,V,z:ev(J,z)-ev(V,z*z)**2,
      'J=V(-t)':lambda J,V,z:ev(J,z)-ev(V,-z),
      'J=V(t^-1)':lambda J,V,z:ev(J,z)-ev(V,1/z),
      '|J|=|V(t^2)|':lambda J,V,z:abs(ev(J,z))-abs(ev(V,z*z))}
for m in range(1,37):
    ks=[k for k in range(1,m+1) if math.gcd(k,m)==1] if m>1 else [1]
    zs=[cmath.exp(2j*cmath.pi*k/m) for k in ks]
    hold=[name for name,f in rels.items() if all(abs(f(J,V,z))<1e-7 for J,V in data for z in zs)]
    if hold: print('m=%2d'%m, hold)
