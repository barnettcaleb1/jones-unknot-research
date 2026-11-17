# Compare J-moments M_2, M_3, M_4 with Vassiliev invariants of K itself (from V_K of the full symmetric diagram)
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, kauffman
from fractions import Fraction as F
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
def VK(word):
    kb=kauffman.bracket(word)
    if not kb: return None
    kb={e:c for e,c in kb.items() if c}
    es=sorted(kb); r=es[0]%4
    if any((e-r)%4 for e in es): return None
    V={-(e-r)//4:c for e,c in kb.items()}          # t = A^-4 up to a unit
    s=sum(V.values())
    if s not in (1,-1): return None
    V={e:c*s for e,c in V.items()}
    d=sum(e*c for e,c in V.items())               # V'(1); shift t^-d to make it 0
    return {e-d:c for e,c in V.items()}
def der(V,k,x=1):
    tot=0
    for e,c in V.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f*F(x)**(e-k)
    return tot
rnd=random.Random(int(sys.argv[1])); rows=[]
while len(rows)<int(sys.argv[2]):
    w=fs.gen(rnd,rnd.randint(6,16))
    if not w: continue
    Jn=lp.J(w)
    if Jn is None: continue
    V=VK(w)
    if V is None: continue
    a2K=F(-der(V,2),6)
    w3=der(V,3)+3*der(V,2)        # mirror-odd order-3 combination
    rows.append((w,M(Jn,2),M(Jn,3),M(Jn,4),a2K,w3))
bad2=sum(1 for r in rows if r[1]!=-24*r[4])
print('n',len(rows),' M2 == -24 a2(K) failures:',bad2)
ratios={}
for r in rows:
    key=('M3/w3', F(r[2],r[5]) if r[5] else ('w3=0',r[2]))
    ratios[key]=ratios.get(key,0)+1
for k,v in sorted(ratios.items(),key=lambda kv:-kv[1])[:12]: print(k,v)
import json; json.dump([[r[0],r[1],r[2],r[3],str(r[4]),str(r[5])] for r in rows],open('ident3_rows.json','w'))
