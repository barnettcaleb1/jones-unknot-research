# Numerical check of the v_3 symbol (upstairs Jones state sum) and of Delta^3 M_3^lp/36 = W_3/6 on random m = 3 configurations.
import sys, random, itertools
from fractions import Fraction as F
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/proof'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft')
import symbol as sy, abstract as ab, iota as io, lp, flat_search as fs, kauffman
def VK(word):
    kb=kauffman.bracket(word); kb={e:c for e,c in kb.items() if c}
    es=sorted(kb); r=es[0]%4
    V={-(e-r)//4:c for e,c in kb.items()}; s=sum(V.values()); V={e:c*s for e,c in V.items()}
    d=sum(e*c for e,c in V.items()); return {e-d:c for e,c in V.items()}
def der(V,k):
    tot=0
    for e,c in V.items():
        f=1
        for i in range(k): f*=(e-i)
        tot+=c*f
    return tot
def v3(word): V=VK(word); return F(-(der(V,3)+3*der(V,2)),36)
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
def abstract_of(word,sites):
    recs,L,axp=sy.chord_data(word,sites)
    tok={}
    for k,r in enumerate(recs):
        if r['kind']=='off': tok[r['a']]=('E',k); tok[r['b']]=('E',k)
        else: tok[r['c']]=('O',k)
    D=[]
    for p in range(L):
        if p in tok: D.append(tok[p])
        elif p in axp: D.append(('T',))
    eps=[sy.W_hat(L,[r],axp,[1])//4 for r in recs]
    return D,eps
rnd=random.Random(int(sys.argv[1])); res={'v3':[0,0],'M3':[0,0]}; done=0; nz=0
while done<int(sys.argv[2]):
    w=fs.gen(rnd,rnd.randint(8,15))
    if not w or lp.J(w) is None: continue
    toks=w.split('.'); fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
    if len(fl)<3: continue
    sites=rnd.sample(fl,3); D,eps=abstract_of(w,sites)
    num_v3=0; num_M3=0
    for S in itertools.product([0,1],repeat=3):
        ww=sy.flip(toks,[s for s,b in zip(sites,S) if b]); sg=(-1)**sum(S)
        num_v3+=sg*v3(ww); num_M3+=sg*M(lp.J(ww),3)
    pe=eps[0]*eps[1]*eps[2]
    pred_v3=pe*io.v3_symbol(D); pred_M3=pe*F(ab.w(D),6)*36
    done+=1; nz+=(num_v3!=0)
    res['v3'][0 if num_v3==pred_v3 else 1]+=1; res['M3'][0 if num_M3==pred_M3 else 1]+=1
print('m=3 samples',done,'(nonzero Delta^3 v3 in',nz,'):  v3 symbol (match, mismatch):',res['v3'],'   Delta^3 M3^lp = 6 W3:',res['M3'])
