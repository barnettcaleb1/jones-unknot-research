"""Exact finite checks of the skein identity used in an all-integer proof.
The proof itself uses the two eigenvalues and support spans, not interpolation.
"""
import json,sys
from pathlib import Path
from collections import defaultdict
HERE=Path(__file__).resolve().parent
from two_band_family import family,regina

def add(*ps):
 out=defaultdict(int)
 for p in ps:
  for e,c in p.items():out[e]+=c
 return {e:c for e,c in out.items()if c}
def scale(p,c):return {e:c*v for e,v in p.items()if c*v}
def shift(p,k):return {e+k:c for e,c in p.items()}
def mul(p,q):
 out=defaultdict(int)
 for e,c in p.items():
  for f,d in q.items():out[e+f]+=c*d
 return {e:c for e,c in out.items()if c}
def poly(r):return {int(e):c for e,c in r['Jones_x_coefficients'].items()}
def jones(L):
 p=regina.Link.fromPD([[x+1 for x in r]for r in L.PD_code()]).jones()
 return {e:int(str(p[e]))for e in range(p.minExp(),p.maxExp()+1)if p[e]!=0}
def at_i(p):
 # Exact Gaussian integers.
 out=[0,0]
 for e,c in p.items():
  k=e%4;out[k%2]+=c*(-1 if k>=2 else 1)
 return out

def main():
 source=json.loads((HERE/'two_band_family.json').read_text())
 delta={1:-1,-1:-1}
 cuts={tuple(r['active_bands']):poly(r)for r in source['cuts']}
 assert cuts[(False,False)]==mul(delta,delta)
 # S1 is the link after cutting band1, with band2 remaining.
 S1,S2=cuts[(False,True)],cuts[(True,False)]
 U,V=add(S1,scale(delta,-1)),add(S2,scale(delta,-1))
 assert at_i(S1)==at_i(S2)==[0,144]
 spans=[max(p)-min(p)for p in [U,V]]
 assert sorted(spans)==[22,24]
 checks=[]
 for m,n in [(0,0),(1,0),(0,1),(1,1),(1,-1),(-2,3),(2,-2),(-1,-1)]:
  L=family(m,n);P=jones(L)
  # z=x^-4. Divide neither side by delta in exact integer arithmetic.
  rhs=add(shift(U,-4*n),shift(V,-4*m),scale(shift(add(U,V),-4*(m+n)),-1))
  lhs=mul(delta,add(P,{0:-1}))
  assert lhs==rhs,(m,n,lhs,rhs)
  assert at_i(P)==[1-288*(m+n),0],(m,n,at_i(P))
  checks.append({'m':m,'n':n,'PD':L.PD_code(),'Jones_x':P,'V_at_minus_one':at_i(P),'writhe':L.writhe()})
 out={'S1':S1,'S2':S2,'S1_minus_delta_span':spans[0],'S2_minus_delta_span':spans[1],
      'both_S_at_x_i':[0,144],'determinant_evaluation_formula':'V_mn(t=-1)=1-288*(m+n)',
      'formula_verified_on':checks,'conclusion':'The eigenvalue formula and unequal support spans prove V_mn=1 iff m=n=0 for this fixed marked family.'}
 (HERE/'all_integer_formula_checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items()if k not in ['S1','S2','formula_verified_on']})

if __name__=='__main__':main()
