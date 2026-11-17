"""can a box with a top-300 (or d2pos) signature have span a <= 2?  span 1: a = c t^d (1 + x u): top (x, -x^2/2),
bottom (1/x, -1/(2x^2)).  span 2: a = c t^d (1 + x u + y u^2), y != 0: top (x, y - x^2/2), bottom (x/y, 1/y - x^2/(2y^2))."""
import pickle
from fractions import Fraction as Fr
CD=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/classdata.pkl','rb'))
hits=[]
for lab,r in CD.items():
    (ra,la,rb,lb),(ra2,la2,rb2,lb2),sig,dl=r['key']
    # span 1
    if ra!=0 and la==-ra*ra/2 and ra2==1/ra and la2==-1/(2*ra*ra): hits.append((lab,1))
    # span 2
    x=ra; y=la+ra*ra/2
    if y!=0 and ra2==x/y and la2==1/y-x*x/(2*y*y): hits.append((lab,2))
print('classes (top-300 + d2pos) whose a-jets admit span a <= 2:',hits if hits else 'NONE')
