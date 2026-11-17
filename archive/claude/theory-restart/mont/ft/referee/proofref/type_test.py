# Map random 3-site configurations to labelled types; compare exact eps*W3 and eps*Delta^3 v3 with the type tables.
import sys, random, json
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
from ss import *
from vk_test_lib import VK, v3
import flat_search as fs, words
W3=json.load(open('table_m3.json')); V3=json.load(open('v3sym_m3.json'))
def key_of(recs):
    pts=[]
    for i,r in enumerate(recs):
        if r['kind']=='off': pts+=[(r['a'],i),(r['b'],i)]
        else: pts.append((r['c'],i))
    pts.sort(); name={}; seq=[]
    for p,i in pts:
        if recs[i]['kind']=='on': seq.append('o')
        else:
            if i not in name: name[i]='c%d'%len(name)
            seq.append(name[i])
    inv={v:k for k,v in name.items()}
    labs=''.join(str(recs[inv['c%d'%j]]['tau']) for j in range(len(name)))
    return '%s | %s'%(' '.join(seq),labs)
seed=int(sys.argv[1]); N=int(sys.argv[2]); rnd=random.Random(seed)
okW=[0,0]; okV=[0,0]; hit=set(); done=0
while done<N:
    r=rnd.random()
    if r<0.3: w=myword(rnd,rnd.randint(14,26))
    elif r<0.7: w=fs.gen(rnd,rnd.randint(12,22))
    else:
        mm=rnd.choice([-2,-1,1,2]); rows=[rnd.choice([-5,-3,3,5]) for _ in range(rnd.randint(2,3))]
        w=words.mont(mm,rows,tw=rnd.choice('xy'),ax=rnd.choice('xy'),off=rnd.choice('xy'))
    if not w or not valid(w) or lp.J(w) is None: continue
    fl=crossing_tokens(w)
    if len(fl)<3: continue
    sites=rnd.sample(fl,3); Js=configs(w,sites)
    if Js is None: continue
    Vs={S:VK(flip(w,[s for s,b in zip(sites,S) if b])) for S in Js}
    if any(v is None for v in Vs.values()): continue
    done+=1
    exact=-quot_at_m1(alt_sum(Js),3)
    recs,L,ax=chord_data(w,sites); eps=1
    for i in range(3): eps*=n_site(L,ax,recs,i)//4
    k=key_of(recs); hit.add(k)
    okW[0 if eps*exact==W3[k][0] else 1]+=1
    d3v=sum((-1)**sum(S)*v3(V) for S,V in Vs.items())
    okV[0 if eps*d3v==V3[k] else 1]+=1
print('exact eps*W3 == table[type]:',okW,'  exact eps*Delta3 v3 == lift symbol[type]:',okV,'  distinct types hit:',len(hit),
      ' nonzero-W types hit:',sum(1 for k in hit if W3[k][0]!=0))
