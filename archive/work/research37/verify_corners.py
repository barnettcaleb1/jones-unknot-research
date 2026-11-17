from marked_hits import *
def clean(p):return {k:v for k,v in p.items()if v}
def add(p,q):
 r=dict(p)
 for k,v in q.items():r[k]=r.get(k,0)+v
 return clean(r)
def mul(p,q):
 r={}
 for i,a in p.items():
  for j,b in q.items():r[i+j]=r.get(i+j,0)+a*b
 return clean(r)
def poly(c):return {int(e):v for e,v in c.items()}
delta={1:-1,-1:-1};z={-4:1};one_minus_z={0:1,-4:-1}
j=json.loads((HERE/'marked_hits.json').read_text());out=[]
for r in j['hits']:
 if r['status']!='certified marked pair':continue
 corners=[]
 for site,(m,n)in enumerate([(1,0),(0,1)]):
  K=construct(r['sites'],[r['base_half_twists'][0]+2*m,r['base_half_twists'][1]+2*n]);c=rec(K)
  lhs=mul(delta,poly(c['coefficients']));rhs=add(mul(delta,z),mul(one_minus_z,poly(r['cuts'][site]['coefficients'])))
  assert lhs==rhs,(r['hit'],site,lhs,rhs)
  assert c['writhe']==r['anchor']['writhe']-2
  c.update(m=m,n=n);corners.append(c)
 out.append({'hit':r['hit'],'corners':corners,'recurrence_verified':True})
 print(r['hit'],'both corners verified',flush=True)
(HERE/'corner_verification.json').write_text(json.dumps(out,indent=2)+'\n')
