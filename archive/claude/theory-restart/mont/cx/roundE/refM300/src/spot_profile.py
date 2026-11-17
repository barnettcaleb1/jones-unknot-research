import sys, time, collections, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import spot_lib, vc, lp
items,pool=spot_lib.load()
def depth(w):
    d=0; md=0
    for L in w.split('.'):
        if L.startswith('r') or L.startswith('l'): d+=1; md=max(md,d)
        elif L.startswith('u'): d-=1
    return md
prof=[]
for c in range(300):
    for x in pool[c]:
        w=vc.word(items[x][1]); prof.append((x,c,len(w.split('.')),depth(w)))
L=collections.Counter(p[3] for p in prof); print('nesting depth distribution of the 27,585 boxes:',sorted(L.items()))
ln=sorted(p[2] for p in prof); print('word length quantiles',ln[0],ln[len(ln)//4],ln[len(ln)//2],ln[3*len(ln)//4],ln[-1])
random.seed(2)
for dd in sorted(L):
    cand=[p for p in prof if p[3]==dd]
    for p in random.sample(cand,min(2,len(cand))):
        x=p[0]; w='s.'+vc.word(items[x][1])
        t=time.time(); J=lp.J(w); dt=time.time()-t
        print('depth',dd,'len',p[2],'lp.J single closure %.2fs'%dt,'agree with vc:',J==vc.Jtree(items[x][1]),flush=True)
        if dt>20: break
