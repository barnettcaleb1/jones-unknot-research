"""One orbit-span certificate: cap-slide invariance kills generic fork module."""
from pathlib import Path
from fractions import Fraction as F
import json
import lkb_calibration as k
HERE=Path(__file__).resolve().parent
def invgen(g,q,t):
 I=k.eye(len(g))
 return k.scale(k.add(k.add(k.mm(g,g),k.scale(g,q+t*q*q-1)),k.scale(I,t*q**3-q-t*q*q)),1/(t*q**3))
def determinant(A):
 A=[r[:]for r in A];d=F(1)
 for j in range(len(A)):
  i=next(i for i in range(j,len(A))if A[i][j])
  if i!=j:A[i],A[j]=A[j],A[i];d=-d
  a=A[j][j];d*=a
  for i in range(j+1,len(A)):
   c=A[i][j]/a
   A[i]=[x-c*y for x,y in zip(A[i],A[j])]
 return d
def run():
 q=F(2);t=F(3);pairs,gs=k.fork(6,q,t);gi=[invgen(g,q,t)for g in gs]
 k.controls(gs)
 v=[F(0)]*15
 for pair,c in [((1,3),1),((1,4),-1),((2,3),-1),((2,4),1)]:v[pairs.index(pair)]=F(c)
 r=[2,1,-3,-2];rv=v[:]
 for a in reversed(r):rv=k.mv(gs[a-1]if a>0 else gi[-a-1],rv)
 d=[a-b for a,b in zip(rv,v)];rows=[d];paths=[[]];queue=[0]
 while queue and len(rows)<15:
  j=queue.pop(0)
  for i,g in enumerate(gs):
   u=k.mv(g,rows[j]);rank=len(k.rref(rows+[u])[1])
   if rank>len(rows):
    rows.append(u);paths.append([i+1]+paths[j]);queue.append(len(rows)-1)
    if len(rows)==15:break
 det=determinant(k.transpose(rows))if len(rows)==15 else None
 out={'q':str(q),'t':str(t),'cap_slide':r,'seed':'F13-F14-F23+F24',
      'defect':'(K(r1)-I)seed','rank':len(rows),'orbit_words':paths,
      'orbit_columns':k.encode(k.transpose(rows)),'determinant':str(det),
      'statement':'Any B6-equivariant linear quotient over Q(q,t) that identifies K(r1)seed with seed is the zero quotient.'if len(rows)==15 else'No full-span conclusion.'}
 (HERE/'cap_slide_span.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({a:b for a,b in out.items()if a not in ('orbit_columns','determinant')}))
 print('nonzero_determinant',bool(det))
if __name__=='__main__':run()
