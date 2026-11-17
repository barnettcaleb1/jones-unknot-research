# Compare referee state sum with exact symbols from lp.J; check n_i vs lp increments and vs upstairs signs.
import sys, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
from ss import *
import flat_search as fs, words
def lp_k(word):
    r=lp.J_raw(word); s=sum(c*(-1)**(e%2) for e,c in r.items()); d=sum(e*c*(-1)**((e-1)%2) for e,c in r.items())
    return d//s, s*(-1)**((d//s)%2)
def upstairs_signs(word):
    """alex-convention signs of the full-diagram crossings, grouped by half-token."""
    half=alex.parse(word); full=alex.symmetrize(half); cr=alex.diagram(full)
    grp={}; k=0
    for n,(c,s) in enumerate(half, start=1):
        if c in 'xy':
            cnt=1 if s==0 else 2
            for j in range(cnt):
                x=cr[k]; k+=1
                ov=(1,-1) if x['ty']=='x' else (-1,-1); un=(-1,-1) if x['ty']=='x' else (1,-1)
                if not x['od']: ov=(-ov[0],-ov[1])
                if not x['ud']: un=(-un[0],-un[1])
                grp.setdefault(n,[]).append(1 if ov[0]*un[1]-ov[1]*un[0]>0 else -1)
    assert k==len(cr)
    return grp
seed=int(sys.argv[1]); N=int(sys.argv[2]); rnd=random.Random(seed)
res={}; bad=[]; nchk=[0,0]; epschk=[0,0]; pairsame=[0,0]; t0=time.time(); done=0
while done<N:
    r=rnd.random()
    if r<0.5: w=myword(rnd,rnd.randint(12,26)); src='my'
    elif r<0.8: w=fs.gen(rnd,rnd.randint(12,22)); src='fs'
    else:
        mm=rnd.choice([-2,-1,1,2]); rows=[rnd.choice([-5,-3,3,5]) for _ in range(rnd.randint(2,3))]
        w=words.mont(mm,rows,tw=rnd.choice('xy'),ax=rnd.choice('xy'),off=rnd.choice('xy')); src='mont'
    if not w or not valid(w) or lp.J(w) is None: continue
    fl=crossing_tokens(w); m=rnd.choice([1,2,3,4])
    if len(fl)<m: continue
    sites=rnd.sample(fl,m)
    Js=configs(w,sites)
    if Js is None: continue
    done+=1
    exact=(-1)**m*quot_at_m1(alt_sum(Js),m)          # W^(t)_m
    recs,L,ax=chord_data(w,sites)
    mine,n=W_J(L,ax,recs)
    key=(src,m); st=res.setdefault(key,[0,0,0]); st[0 if mine==exact else 1]+=1
    if exact!=0: st[2]+=1
    if mine!=exact: bad.append((w,sites,mine,exact))
    # n_i vs lp normalisation increments, and vs upstairs signs
    k0,_=lp_k(w); ups=upstairs_signs(w)
    for i,sv in enumerate(sites):
        k1,_=lp_k(flip(w,[sv])); nchk[0 if k1-k0==n[i] else 1]+=1
        sg=ups[sv]; pairsame[0 if len(set(sg))==1 else 1]+=1
        epschk[0 if n[i]==-4*sg[0] else 1]+=1
for k in sorted(res): print(k,'agree/disagree/nonzero:',res[k])
print('n_i == lp increment:',nchk,'  n_i == -4*alexsign:',epschk,'  pair signs equal:',pairsame)
print('bad:',bad[:4]); print('time %.1f'%(time.time()-t0))
