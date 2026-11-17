# Claim 7: family P(2k,4k-1,4k+1) = words.mont(-k,[4k-1,4k+1]); everything computed directly from the half-word
# (lp.J of the half-word itself, V_K and Delta_K of its symmetric diagram), no necklace formula, no pretzel diagram.
import sys, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import refinv as R, words, lp
from fractions import Fraction as Fr
kmax=int(sys.argv[1]); alexmax=int(sys.argv[2])
for k in range(1,kmax+1):
    t0=time.time()
    w=words.mont(-k,[4*k-1,4*k+1])
    v=R.all_vals(w, with_alex=(k<=alexmax))
    v3f=Fr(-2*k*(7*k*k-1),3); Df=Fr(-2*k*(2*k*k+1),3); M3f=-2256*k**3+168*k
    s='k=%d a2=%s v3=%s (closed %s) j4=%s M3=%s (closed %s) D=%s (closed %s) M4=%s'%(k,v['a2'],v['v3'],v3f,v['j4'],v['M3'],M3f,v['D'],Df,v['M4'])
    if 'F4' in v: s+=' a4=%s F4=%s'%(v['a4'],v['F4'])
    s+=' | v3 mod5=%s j4 mod5=%s spanJ=%d  %.1fs'%(v['v3']%5, v['j4']%5 if v['j4'].denominator==1 else 'frac', max(v['J'])-min(v['J']), time.time()-t0)
    print(s, flush=True)
