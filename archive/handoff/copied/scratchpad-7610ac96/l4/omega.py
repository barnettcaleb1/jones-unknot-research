import json, cmath, sys
from fractions import Fraction
from collections import Counter
data=json.load(open(sys.argv[1]))
def P(d): return {int(Fraction(k)):v for k,v in d.items()}
data=[(w,P(J),P(V)) for w,J,V in data]
def ev(Pd,z): return sum(c*z**e for e,c in Pd.items())
w3=cmath.exp(2j*cmath.pi/3)
cnt=Counter(); ex=[]
for w,J,V in data:
    x=ev(J,w3); N=round(abs(x)**2,6)
    cnt[N]+=1
    if N<1.5: ex.append((w, round(x.real,4), round(x.imag,4), sorted(J.items())[:6], len(J)))
print('norm 1 count:',cnt[1.0],'of',len(data)); print('smallest norms',sorted(cnt.items())[:10])
for e in ex[:10]: print(e)
