"""Three actual unknot samples on a coupled twist line do not suffice."""
from pathlib import Path
import sys,json
WORK=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WORK/'attack_search'))
from search import jones_a,knot

def inv(w):return [-s for s in w[::-1]]
def power(s,m):return [s if m>=0 else -s]*abs(m)
def comm(a,b):return a+b+inv(a)+inv(b)
def free_reduce(w):
 out=[]
 for s in w:
  if out and out[-1]==-s:out.pop()
  else:out.append(s)
 return out

def word(n):return comm(power(1,2*n),comm(power(2,2*(n-1)),power(1,2*(n-2))))+[1,2]
result=[]
for n in[0,1,2,3,4]:
 w=word(n);v=jones_a(w,3);assert knot(w,3)
 if n in[0,1,2]:assert free_reduce(w)==[1,2] and v=={0:1}
 else:assert v!={0:1}
 t={-e//4:c for e,c in v.items()};assert all(e%4==0 for e in v)
 result.append({'n':n,'braid_word':w,'freely_reduced_word':free_reduce(w),'Jones_t':t,'Jones_span':max(t)-min(t),'determinant':abs(sum(c*(1 if e%2==0 else-1)for e,c in t.items()))})
if '--diagrams' in sys.argv:
 sys.path.insert(0,str(WORK/'braid_classification/packages'))
 from spherogram import Link
 import regina
 for r in result:
  l=Link(braid_closure=r['braid_word']);pd=l.PD_code();reg=regina.Link.fromPD([[v+1 for v in c]for c in pd]);p=reg.jones()
  actual={e//2:int(str(p[e]))for e in range(p.minExp(),p.maxExp()+1)if int(str(p[e]))}
  assert actual==r['Jones_t'] or actual=={-e:c for e,c in r['Jones_t'].items()}
  r['PD']=pd;r['Regina_Jones']=str(p)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
for r in result:print(r['n'],'crossings',len(r['braid_word']),'span',r['Jones_span'],'det',r['determinant'])
