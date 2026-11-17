"""Validate Hopf pattern homology formula along EKT omega orbits."""
from ll1_scan import *

def omega(t):return dot(dot(t+IntegerTangle(2),IntegerTangle(1)),IntegerTangle(2))
def omega_inverse(t):return dot(dot(t+IntegerTangle(-2),IntegerTangle(-1)),IntegerTangle(-2))
def pell(k):
    a,b=1,0
    for _ in range(abs(k)):a,b=3*a+8*b,a+3*b
    return a, b if k>=0 else -b

if __name__=='__main__':
    out=[]
    for m,n in [(0,-1),(0,0),(1,-1),(1,0),(2,1)]:
      for k in range(-3,4):
        t,u=ll1_tangle(m,n),IntegerTangle(-3)
        for _ in range(abs(k)):
          if k>0:t,u=omega(t),omega_inverse(u)
          else:t,u=omega_inverse(t),omega(u)
        l=hopf(t,u)
        pd=l.PD_code()
        H=fox_factors(pd)
        a,b=pell(k);A=4**m*(3*n+2)
        D=(a+2*b)**2-4*A*(3*a+8*b)*(a+3*b)
        wanted=(([abs(D)] if abs(D)>1 else []),1)
        assert H==wanted,(m,n,k,H,D)
        row={'m':m,'n':n,'k':k,'a':a,'b':b,'A':A,'D':D,'H1':H,'crossings':len(pd),'pd':pd}
        out.append(row)
        print({key:v for key,v in row.items()if key!='pd'},flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
