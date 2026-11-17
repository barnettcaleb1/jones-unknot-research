from escape import apply2,greedy
from classify import *
row=json.loads((ROOT/'certificate86.json').read_text());L=regina.Link.fromPD(row['pd']);ops=row['steps']
for st in ops:assert apply2(L,st['move'])
base=regina.Link(L);startops=list(ops)
for seed in range(30):
 L=regina.Link(base);ops=list(startops);rng=random.Random(seed)
 for k in range(5000):
  greedy(L,ops)
  if L.size()==0:break
  choices=[['r3',i,s] for i in range(L.size()) for s in (0,1) if L.hasR3(L.crossing(i),s)]
  if not choices:break
  op=rng.choice(choices);before=snap(L);assert apply(L,op);ops.append({'move':op,'before':before,'after':snap(L)})
 if L.size()==0:
  row['steps']=ops;(ROOT/'certificate86.json').write_text(json.dumps(row,indent=2));print('CERTIFIED86',len(ops),dict(collections.Counter(x['move'][0] for x in ops)));break
else:print('NOT FOUND',L.size())
