"""Chase the depth-4 two-ended ties (body-43 frontier): nest one level deeper around the boxes that reach depth 4 (and their
jet-class mates and partners), then exact pair census against library A u g43-frontier u chase set."""
import sys, pickle, collections, time
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, lib, front
t0=time.time()
d=pickle.load(open('fr_pairs_g43.pkl','rb'))
F=pickle.load(open('fr_g43.pkl','rb')); L=pickle.load(open('libA_jets.pkl','rb'))
nF=len(F['boxes'])
deep4=[r for r in d['deep'] if r[0]>=4]
seedF=sorted(set(r[6] for r in deep4)); seedL=sorted(set(r[7]-nF for r in deep4 if r[7]>=nF))
# jet-class mates of the frontier seeds
k3s=set(front.key3(*F['jets'][i]) for i in seedF)
mates=[i for i in range(nF) if front.key3(*F['jets'][i]) in k3s]
print('seeds: frontier',len(seedF),'class mates',len(mates),'library partners',len(seedL),flush=True)
# rebuild box objects (key, vec, tree, tag)
def boxF(i): b=F['boxes'][i]; return (b[0],F['vecs'][i],b[1],b[2])
def boxL(j): b=L['boxes'][j]; return (b[0],L['vecs'][j],b[1],b[2])
seeds=[boxF(i) for i in mates[:400]]+[boxL(j) for j in seedL]
R4=lib.rational(4); U=[None]+R4
out=[]; seen=set()
for s in seeds:
    for u in U:
        for m in (1,-1,2,-2,3,-3):
            for N in range(-2,3):
                b=lib.node(m,N,[s] if u is None else [s,u])
                if b is None or b[0] in seen: continue
                seen.add(b[0]); out.append(b)
print('chase boxes',len(out),round(time.time()-t0,1),flush=True)
JJ=[front.jt(b[1]) for b in out]
pickle.dump(dict(boxes=[(b[0],b[2],b[3]) for b in out],vecs=[b[1] for b in out],jets=JJ),open('fr_chase.pkl','wb'))
print('saved',round(time.time()-t0,1))
