"""exact version: jets fix the coefficient RATIOS of span-1/2 channels; |lc| conditions are scale-invariant and the
condition (1 - t^3) | (b - a) is checked for the minimal integral scaling and every relative shift (mod 3 suffices)."""
import pickle, math
from fractions import Fraction as Fr
CD=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','rb'))
def lcm(a,b): return a*b//math.gcd(a,b)
def poly_from_ratios(r):   # r = [1, x, y] ratios -> minimal integer coefficient list
    den=1
    for v in r: den=lcm(den,Fr(v).denominator)
    c=[int(Fr(v)*den) for v in r]; g=0
    for v in c: g=math.gcd(g,v)
    return [v//g for v in c]
out=[]
for lab,rec in CD.items():
    (ra,la,rb,lb),(ra2,la2,rb2,lb2),sig,dl=rec['key']
    cands=[]
    # a of span 1 or 2 consistent with BOTH ends
    if ra!=0 and la==-ra*ra/2 and ra2==1/ra and la2==-1/(2*ra*ra): cands.append([Fr(1),ra])
    y=la+ra*ra/2
    if y!=0 and ra2==ra/y and la2==1/y-ra*ra/(2*y*y): cands.append([Fr(1),ra,y])
    for ar in cands:
        sa=len(ar)-1; sb=sa+dl
        brs=[]
        if sb==0 and rb==lb==rb2==lb2==0: brs.append([Fr(1)])
        if sb==1 and rb!=0 and lb==-rb*rb/2 and rb2==1/rb and lb2==-1/(2*rb*rb): brs.append([Fr(1),rb])
        if sb==2:
            yb=lb+rb*rb/2
            if yb!=0 and rb2==rb/yb and lb2==1/yb-rb*rb/(2*yb*yb): brs.append([Fr(1),rb,yb])
        for br in brs:
            A=poly_from_ratios(ar); B0=poly_from_ratios(br)
            # |lc b / lc a| = 1 at top and bottom with b = s * B0 scaled: need |s B0[0]| = |A[0]| and |s B0[-1]| = |A[-1]|
            if Fr(abs(A[0]),abs(B0[0]))!=Fr(abs(A[-1]),abs(B0[-1])): continue
            s=Fr(abs(A[0]),abs(B0[0])); 
            for sg in (1,-1):
                Bc=[sg*s*v for v in B0]
                if any(Fr(v).denominator!=1 for v in Bc): 
                    # scale both by the denominator (divisibility is scale-invariant over Z by Gauss)
                    pass
                for sh in range(3):
                    Ad={sa-i:Fr(A[i]) for i in range(sa+1)}; Bd={sb-i+sh:Bc[i] for i in range(sb+1)}
                    D={e:Bd.get(e,0)-Ad.get(e,0) for e in set(Ad)|set(Bd)}
                    if all(sum(c for e,c in D.items() if e%3==r)==0 for r in range(3)):
                        cands_ok=(lab,A,Bc,sh); out.append(cands_ok)
print('classes admitting a REAL small-span (span a <= 2) channel pair with the full signature:',out if out else 'NONE')
