"""Evaluate actual bodies in the regular model (ft_integral maps) at generic q and near the root; compare with TL3."""
import sys, json, numpy as np, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from regmodel import *
from refskein import body_channels, to_t, tev, nax
bodies=[B for B,k in json.load(open('bodies.json')) if not k.startswith('necklace')]
def width(B):
    w=1;mx=1
    for tok in B.split('.'):
        c=tok[0]
        if c in 'lr': w+=2
        elif c=='u': w-=2
        mx=max(mx,w)
    return mx
rnd=random.Random(3)
sel=[B for B in bodies if width(B)<=5]
rnd.shuffle(sel); sel=sel[:60]
qg=1.3*np.exp(0.4j); sg=np.sqrt(qg+1/qg)
res=[]; ok_gen={1:0,-1:0}; ok_root=0; ok_resid=0
for B in sel:
    bc=body_channels(B)
    ra,at=to_t(bc['a']); rb,bt=to_t(bc['b'])
    ratioK=lambda t: complex(sum(c*t**e for e,c in bt.items())/sum(c*t**e for e,c in at.items()))
    out={}
    for sx in (1,-1):
        beta=body_operator(B,qg,sg,sign_x=sx)
        a,b,resid=channels(beta,qg,sg)
        out[sx]=(b/a,resid)
    # compare b/a with Kauffman ratio at t=q^2 and t=q^-2
    for sx in (1,-1):
        r,resid=out[sx]
        if resid<1e-8 and (abs(r-ratioK(qg**2))<1e-8*abs(r) or abs(r-ratioK(qg**-2))<1e-8*abs(r)): ok_gen[sx]+=1
    # near root
    h=1e-10; q=1j*np.exp(h/2); s=np.sqrt(q+1/q)
    beta=body_operator(B,q,s,sign_x=1)
    a,b,resid=channels(beta,q,s)
    # direct check of the root operator shape: beta ~ a*Id x Pi_w1 + b*Id x Pi_odd
    Pw1=np.kron(np.eye(2),np.diag([0,1,0])); Pod=np.kron(np.eye(2),np.diag([1,0,1]))
    shape_err=np.linalg.norm(beta-a*Pw1-b*Pod)
    n0=nax(B)
    good= abs(abs(a)-1)<1e-3 and abs(b/a-(-1)**n0)<1e-3
    ok_root+=good; ok_resid+= shape_err<1e-3
    res.append((B,n0,complex(np.round(a,6)),complex(np.round(b,6)),shape_err))
print('generic b/a agrees with TL3 (either t=q^2 or q^-2): sign_x=+1:',ok_gen[1],' sign_x=-1:',ok_gen[-1],' of',len(sel))
print('root: |a|=1 and b/a=(-1)^n0:',ok_root,'/',len(sel),'  root operator = a Id x Pi_w1 + b Id x Pi_odd:',ok_resid)
from collections import Counter
print('root a values',Counter(r[2] for r in res))
for r in res[:6]: print(r)
