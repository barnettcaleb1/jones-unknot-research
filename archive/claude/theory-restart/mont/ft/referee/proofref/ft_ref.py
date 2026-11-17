# Referee FT test: Delta^m J divisible by (1+t)^m?  Own generator (myword), words.py Montesinos words, and fs.gen with new seeds.
import sys, random, itertools, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
from common import *
import flat_search as fs, words
seed=int(sys.argv[1]); N=int(sys.argv[2]); rnd=random.Random(seed)
stats={}; fails=[]; t0=time.time()
def test(word, m, mode, src):
    fl=crossing_tokens(word); toks=word.split('.')
    if mode=='on': fl=[i for i in fl if toks[i][1:]=='0']
    elif mode=='off': fl=[i for i in fl if toks[i][1:]!='0']
    if len(fl)<m: return
    sites=rnd.sample(fl,m)
    Js=configs(word,sites)
    if Js is None: return
    D=alt_sum(Js); k=xorder(D)
    key=(src,mode,m); st=stats.setdefault(key,[0,0,0])  # [ok, fail, order exactly m (symbol nonzero)]
    if k>=m: st[0]+=1
    else: st[1]+=1; fails.append((word,sites,k))
    if k==m: st[2]+=1
done=0
while done<N:
    r=rnd.random()
    if r<0.5:
        w=myword(rnd, rnd.randint(14,30)); src='my'
    elif r<0.8:
        w=fs.gen(rnd, rnd.randint(16,24)); src='fs'
    else:
        # Montesinos horizontal inversions P(2m, rows), rows odd
        mm=rnd.choice([-3,-2,-1,1,2,3]); rows=[rnd.choice([-5,-3,3,5]) for _ in range(rnd.randint(2,3))]
        try: w=words.mont(mm,rows,tw=rnd.choice('xy'),ax=rnd.choice('xy'),off=rnd.choice('xy'))
        except AssertionError: continue
        src='mont'
    if not w or not valid(w) or lp.J(w) is None: continue
    mode=rnd.choice(['mix','mix','off','on'])
    m=rnd.choice([2,3,4,5,6]) if src!='mont' else rnd.choice([2,3,4,5])
    test(w,m,mode,src); done+=1
for k in sorted(stats): print(k, 'ok/fail/order=m:', stats[k])
print('fails:',fails[:5]); print('time %.1fs'%(time.time()-t0))
