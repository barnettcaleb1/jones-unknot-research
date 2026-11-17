"""Budney Theorem 2 Gram form, with the displayed universal factor removed.
References: arXiv:math/0202246v3, p10. Uses Fraction at rational q,t.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
PAIRS=list(combinations(range(1,7),2))
def gram(q,t):
 q=F(q);t=F(t);out=[]
 for i,j in PAIRS:
  row=[]
  for k,l in PAIRS:
   if (i==k and j<l) or (i<k and j==l): x=-q*q*t*t*(q-1)
   elif (k==i and l<j) or (k<i and j==l): x=-(q-1)
   elif i<j and j==k and k<l: x=t*(q-1)
   elif k<l and l==i and i<j: x=q*q*t*(q-1)
   elif i<k<j<l: x=-t*(q-1)**2*(1+q*t)
   elif k<i<l<j: x=(q-1)**2*(1+q*t)
   elif k==i and j==l: x=(1-q*t)*(1+q*q*t)
   else: x=F(0)
   row.append(x)
  out.append(row)
 return out
def rref(a):
 a=[list(map(F,row))for row in a];m=len(a);n=len(a[0]);row=0;piv=[]
 for col in range(n):
  k=next((k for k in range(row,m)if a[k][col]),None)
  if k is None:continue
  a[row],a[k]=a[k],a[row];d=a[row][col];a[row]=[x/d for x in a[row]]
  for k in range(m):
   if k!=row and a[k][col]:
    d=a[k][col];a[k]=[x-d*y for x,y in zip(a[k],a[row])]
  piv.append(col);row+=1
  if row==m:break
 return a,piv
def main():
 rows=[]
 for q in [2,3,4]:
  g=gram(q,F(-1,q));r,piv=rref(g)
  # B has columns e_i+q e_j. The bar is q -> 1/q.
  b=[[F(int(k==i))+q*int(k==j)for i,j in PAIRS]for k in range(1,7)]
  bb=[[F(int(k==i))+F(1,q)*int(k==j)for i,j in PAIRS]for k in range(1,7)]
  target=[[-(q-1)*sum(bb[k][a]*b[k][c]for k in range(6))for c in range(15)]for a in range(15)]
  assert g==target
  rows.append({'q':q,'t':str(F(-1,q)),'rank_normalized_Gram':len(piv),'radical_dimension':15-len(piv),'factorization':'Gnorm=-(q-1)*B(q^-1)^T*B(q), Bcol(i,j)=e_i+q e_j'})
 Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
 print(json.dumps(rows,indent=2))
if __name__=='__main__':main()

def nullbasis(q):
 q=F(q)
 b=[[F(int(k==i))+q*int(k==j)for i,j in PAIRS]for k in range(1,7)]
 r,piv=rref(b);free=[j for j in range(15)if j not in piv]
 return [[F(int(j==f)) if j in free else -r[piv.index(j)][f] for j in range(15)]for f in free]
def derivative_test(q):
 q=F(q);a=gram(q,0);b=gram(q,-2/q)
 dg=[[(x-y)/2 for x,y in zip(r,s)]for r,s in zip(a,b)]
 vr=nullbasis(q);vl=nullbasis(1/q)
 h=[[sum(vl[i][a]*dg[a][b]*vr[j][b]for a in range(15)for b in range(15))for j in range(9)]for i in range(9)]
 return {'q':str(q),'derivative_rank':len(rref(h)[1]),'matrix':[[str(x)for x in row]for row in h]}
