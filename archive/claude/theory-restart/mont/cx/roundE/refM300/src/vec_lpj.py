"""independent check of box vectors of listed top-300 boxes from the knot diagrams: v = (alpha_0, (t^2 alpha_-1 -
alpha_0)/(1-t^4)) (TH-2BR), alpha_m = lp.J_raw(s.r2.(y1)^m.B.u1) (BRIEF sec. 4); channels a = v1, b = v1 + (1-t^3) v2;
compare with the stored vector up to a unit and recompute the class signature with own code."""
import sys, pickle, random, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import spot_lib2, spot_lib, vc, lp
import rlaurent as RL
from fractions import Fraction as Fr
items,pool=spot_lib.load(); sh=spot_lib2.shallow(3)
CD=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','rb'))
rng=random.Random(99); cs=[c for c in range(300) if sh[c]]
N=int(sys.argv[1]); ok=0; bad=[]; t0=time.time()
chosen=rng.sample(cs,min(N,len(cs)))
for c in chosen:
    x=rng.choice(sh[c]); B=vc.word(items[x][1])
    a0=lp.J_raw('s.r2.'+B+'.u1'); am=lp.J_raw('s.r2.x1.'+B+'.u1')
    num=RL.psub(RL.pshift(am,2),a0); v2=RL.pdivexact(num,{0:1,4:-1})
    if v2 is None: bad.append((c,x,'not divisible')); continue
    a=a0; b=RL.padd(a0,RL.pmul({0:1,3:-1},v2))
    A,Bs=items[x][2]
    # unit: A = s t^k a
    k=max(A)-max(a); s=Fr(A[max(A)],a[max(a)])
    same=(abs(s)==1 and RL.pshift({e:c*s for e,c in a.items()},k)==dict(A) and RL.pshift({e:c*s for e,c in b.items()},k)==dict(Bs))
    # signature from the lp.J vector (own code)
    out={}
    for end in ('top','bot'):
        _,_,la=RL.logdata(a,end,2); _,_,lb=RL.logdata(b,end,2); out[end]=(la[0],la[1],lb[0],lb[1])
    sig=sum(out[e][2]-out[e][0] for e in out); dl=RL.pspan(b)-RL.pspan(a)
    key=(out['top'],out['bot'],sig,dl)
    if same and key==CD['top%d'%c]['key']: ok+=1
    else: bad.append((c,x,same,key==CD['top%d'%c]['key']))
print('boxes (one per class, %d classes): lp.J-derived vector == stored vector (unit) AND signature == class key: %d/%d  bad %s  (%.0fs)'%(len(chosen),ok,len(chosen),bad[:5],time.time()-t0))
