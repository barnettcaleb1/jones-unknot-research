"""for the 6 classes whose a-jets admit span a <= 2: is there an actual channel pair (a, b) with the FULL signature,
span b = span a + delta, |lc b/lc a| = 1 at both ends, integer coefficients and b == a mod (1 - t^3)?"""
import pickle, itertools
from fractions import Fraction as Fr
CD=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','rb'))
def jets(coefs):   # coefs from top degree down: c0 t^s + c1 t^(s-1) + ... ; returns top (l1,l2), bottom (l1,l2)
    c0=Fr(coefs[0]); x=[Fr(c)/c0 for c in coefs[1:]]+[0,0]
    t=(x[0], x[1]-x[0]**2/2)
    r=list(reversed(coefs)); d0=Fr(r[0]); z=[Fr(c)/d0 for c in r[1:]]+[0,0]
    b=(z[0], z[1]-z[0]**2/2)
    return t,b
for lab in ['top119','top124','top125','top138','top150','top187']:
    (ra,la,rb,lb),(ra2,la2,rb2,lb2),sig,dl=CD[lab]['key']
    found=[]
    for sa in (1,2):
        sb=sa+dl
        if sb<0: continue
        rng=range(-6,7)
        for ca in itertools.product(rng,repeat=sa+1):
            if ca[0]==0 or ca[-1]==0: continue
            ta,ba=jets(list(ca))
            if ta!=(ra,la) or ba!=(ra2,la2): continue
            for cb in itertools.product(rng,repeat=sb+1):
                if cb[0]==0 or cb[-1]==0: continue
                tb,bb=jets(list(cb)) if sb>0 else (((Fr(0),Fr(0)),(Fr(0),Fr(0))))
                if tb!=(rb,lb) or bb!=(rb2,lb2): continue
                if abs(Fr(cb[0],ca[0]))!=1 or abs(Fr(cb[-1],ca[-1]))!=1: continue
                # b == a mod (1-t^3) up to a shift t^k of b relative to a: test all shifts in a window
                for sh in range(-12,13):
                    A={sa-i:ca[i] for i in range(sa+1)}; B={sb-i+sh:cb[i] for i in range(sb+1)}
                    D={e:B.get(e,0)-A.get(e,0) for e in set(A)|set(B)}
                    # divisibility by 1 - t^3: sum of coefficients in each residue class mod 3 vanish
                    if all(sum(c for e,c in D.items() if e%3==r)==0 for r in range(3)):
                        found.append((ca,cb,sh)); break
    print(lab,'key',CD[lab]['key'][2:],'small-span realisations (|coef|<=6):',found[:3] if found else 'NONE')
