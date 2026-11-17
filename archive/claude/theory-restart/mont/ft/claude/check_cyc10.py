# Check Astra's MOMENT-CYC10: J_(K,h)(t) == V_K(t^2) mod Phi_10(t) = t^4-t^3+t^2-t+1, on random half-words.
import sys, random, cmath
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, kauffman
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
roots=[cmath.exp(2j*cmath.pi*k/10) for k in (1,3,7,9)]
rnd=random.Random(int(sys.argv[1])); n=0; bad=0; badmir=0; ex=[]
while n<int(sys.argv[2]):
    w=fs.gen(rnd,rnd.randint(6,18))
    if not w: continue
    Jn=lp.J(w)
    if Jn is None: continue
    V=VK(w)
    if V is None: continue
    n+=1
    ok=all(abs(ev(Jn,z)-ev(V,z*z))<1e-8 for z in roots)
    okm=all(abs(ev(Jn,z)-ev(V,1/(z*z)))<1e-8 for z in roots)   # mirror convention t -> 1/t
    if not ok: bad+=1
    if not okm: badmir+=1
    if not ok and len(ex)<3: ex.append((w,Jn,V))
print('samples',n,'fail J==V(t^2) mod Phi10:',bad,'| fail with V(t^-2):',badmir)
for e in ex: print('example',e[0])
