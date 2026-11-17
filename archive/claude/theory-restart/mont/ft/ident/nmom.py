# moments at t=+1: N_k = sum_e J_e e^k  (= k! [h^k] J(e^h)); test FT at t=+1 and relation to M_3
import sys, json, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, chord, flat_search as fs
from fractions import Fraction as F
def N(J,k): return sum(c*e**k for e,c in J.items())
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
rows=json.load(open('inv_rows2.json'))
print('N0,N1 values:',sorted(set((N(lp.J(r['w']),0),N(lp.J(r['w']),1)) for r in rows))[:10])
# FT test at t=+1: alternating sums of N_k over m flips
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
rnd=random.Random(7); res={}
done=0
while done<60:
    w=fs.gen(rnd,rnd.randint(8,14))
    if not w or lp.J(w) is None: continue
    toks=w.split('.'); fl=[i for i,a in enumerate(toks) if len(a)>=2 and a[0] in 'xy' and a[1:].isdigit()]
    m=rnd.choice([2,3,4])
    if len(fl)<m: continue
    sites=rnd.sample(fl,m); Js={}; ok=True
    for S in itertools.product([0,1],repeat=m):
        J=lp.J(flip(toks,[s for s,b in zip(sites,S) if b]))
        if J is None: ok=False; break
        Js[S]=J
    if not ok: continue
    done+=1
    for k in range(0,6):
        alt=sum((-1)**sum(S)*N(Js[S],k) for S in Js)
        res.setdefault((m,k),[0,0])[0 if alt==0 else 1]+=1
for key in sorted(res): print(key,res[key],'(zero expected if m>k)' if key[0]>key[1] else '')
