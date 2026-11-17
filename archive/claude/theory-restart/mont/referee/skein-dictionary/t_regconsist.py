import sys, json, numpy as np, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from regmodel import *
from refskein import body_channels, to_t, tev, nax
from collections import Counter
bodies=[B for B,k in json.load(open('bodies.json')) if not k.startswith('necklace')]
def width(B):
    w=1;mx=1
    for tok in B.split('.'):
        c=tok[0]
        if c in 'lr': w+=2
        elif c=='u': w-=2
        mx=max(mx,w)
    return mx
sel=[B for B in bodies if width(B)<=5][:80]
qg=1.3*np.exp(0.4j); sg=np.sqrt(qg+1/qg)
cnt=Counter()
for B in sel:
    bc=body_channels(B); ra,at=to_t(bc['a']); rb,bt=to_t(bc['b'])
    rK=lambda t: complex(sum(c*t**e for e,c in bt.items())/sum(c*t**e for e,c in at.items()))
    for sx in (1,-1):
        a,b,res=channels(body_operator(B,qg,sg,sign_x=sx),qg,sg)
        r=b/a
        m2=abs(r-rK(qg**2))<1e-8*abs(r); mm2=abs(r-rK(qg**-2))<1e-8*abs(r)
        cnt[(sx,'t=q^2' if m2 and not mm2 else 't=q^-2' if mm2 and not m2 else 'both' if m2 else 'none')]+=1
print(cnt)
