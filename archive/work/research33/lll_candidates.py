"""Exact EKT §4.3 diagrams, left-associated dot products."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(ROOT/'work/ekt_model')]
from check_links import *
from ll1_scan import dot
from spherogram.links.tangles import IntegerTangle

def lll(n):
 t=IntegerTangle(2)
 for _ in range(n):
  t=dot(t,RationalTangle(1,2));t=dot(t,IntegerTangle(1))
 t=dot(dot(t,IntegerTangle(1)),IntegerTangle(2))
 return hopf(t,IntegerTangle(-3))
if __name__=='__main__':
 out=[]
 for n in range(4):
  link=lll(n);pd=link.PD_code();r=regina.Link.fromPD([[x+1 for x in row]for row in pd])
  row={'n':n,'pd':pd,'crossings':len(pd),'components':r.countComponents(),'jones':str(r.jones()),'H1':fox_factors(pd)}
  out.append(row)
  print({k:v for k,v in row.items()if k!='pd'},flush=True)
 (ROOT/'work/research33/lll_candidates.json').write_text(json.dumps(out,indent=2)+'\n')
