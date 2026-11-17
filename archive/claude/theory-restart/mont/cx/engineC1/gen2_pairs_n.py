"""Depth-two step: TWO non-rational boxes B1, B2 (library A / d2pos signatures) plus ANY rational boxes.  The product B1*B2 is one
box whose end data are the SUMS of the signatures (log-jets, sigma, delta additive), so gen2 applies verbatim.  Top-K signatures."""
import sys, pickle, collections, time, itertools
sys.path.insert(0,'.')
import gen2
from fractions import Fraction as Fr
t0=time.time()
G=pickle.load(open('gen2_res.pkl','rb'))
sigs=G['sigs']
K=int(sys.argv[1]); NMIN=int(sys.argv[2]) if len(sys.argv)>2 else 1
top=sorted(sigs.items(),key=lambda kv:-len(kv[1]))[:K]
totw=sum(len(xs) for k,xs in sigs.items()); topw=sum(len(xs) for k,xs in top)
print('signatures',len(sigs),'top',K,'cover',topw,'of',totw,'boxes',flush=True)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
okw=0; allw=0; okV=0; okH=0; n=0; opn=collections.Counter()
for (k1,x1),(k2,x2) in itertools.combinations_with_replacement(top,2):
    w=len(x1)*len(x2) if k1!=k2 else len(x1)*(len(x1)+1)//2
    bd={'top':add(k1[0],k2[0]),'bot':add(k1[1],k2[1])}; sg=k1[2]+k2[2]; dl=k1[3]+k2[3]
    v=gen2.proveV(bd,sg,dl,NMIN); h=gen2.proveH(bd,sg,dl,NMIN)
    hv=all(not o for o in h.values())
    allw+=w; okV+=w*v[0]; okH+=w*hv; okw+=w*(v[0] and hv)
    for o in v[1]: opn[('V',o[3] if isinstance(o,tuple) else o)]+=w
    for mu,o in h.items():
        for x in o: opn[('H',mu,x.split(':')[-1])]+=w
    n+=1
    if n%500==0: print(' ',n,round(time.time()-t0,1),flush=True)
print('signature pairs',n,' box pairs (weighted)',allw)
print('PROVED vertical (all |a|>=3): %.4f   horizontal (all mu): %.4f   both: %.4f'%(okV/allw,okH/allw,okw/allw))
print('open (weighted):',opn.most_common(8))
print('done',round(time.time()-t0,1))
