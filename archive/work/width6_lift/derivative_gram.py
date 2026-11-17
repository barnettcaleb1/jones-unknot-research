"""Exact polynomial comparison of the repaired Budney derivative with TL Gram."""
from pathlib import Path
import json
import generic_intertwiner as g
HERE=Path(__file__).resolve().parent
def derivative():
 out=[]
 for i,j in g.P:
  row=[]
  for k,l in g.P:
   if (i==k and j<l)or(i<k and j==l):p={2:2,0:-2}
   elif (k==i and l<j)or(k<i and j==l):p={}
   elif j==k:p={0:1,-2:-1}
   elif l==i:p={4:1,2:-1}
   elif i<k<j<l:p={2:1,0:-2,-2:1}
   elif k<i<l<j:p={4:1,2:-2,0:1}
   elif i==k and j==l:p={2:3,0:-1}
   else:p={}
   row.append(p)
  out.append(row)
 return out
def run():
 x=json.load(open(HERE/'generic_intertwiner.json'))
 B=[[{int(k):v for k,v in p.items()}for p in r]for r in x['embedding_15_by9']]
 barB=[[{-e:c for e,c in p.items()}for p in r]for r in B]
 H=g.mm(g.mm(list(map(list,zip(*B))),derivative()),barB)
 delta={1:-1,-1:-1};G=[]
 for row in g.tl.GRAM:
  rr=[]
  for loops in row:
   p={}if loops is None else{0:1}
   for _ in range(loops or 0):p=g.mul(p,delta)
   rr.append(p)
  G.append(rr)
 target=[[g.mul(p,{2:1,0:1})for p in r]for r in G]
 assert H==target
 out={'q':'s^2','t0':'-s^-2','epsilon':'1+q*t','sesquilinear_convention':'linear first: x^T G bar(y)',
      'formula':'B(s)^T (dGnorm/depsilon)|epsilon=0 B(s^-1) = (1+s^2) Gram_TL',
      'all81_entries_exact':True,'scalar':'1+q','scalar_is_Laurent_unit':False,
      'derivative_15_by15':derivative(),'pulled_back_9_by9':H,'TL_Gram':G}
 (HERE/'derivative_gram.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if not isinstance(v,list)}))
if __name__=='__main__':run()
