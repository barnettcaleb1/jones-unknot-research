from pathlib import Path
import sys,json
WORK=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WORK/'braid_classification/packages'))
from spherogram import Link
import regina

def circles(pd,mask):
 p=list(range(2*len(pd)))
 def find(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for i,(a,b,c,d) in enumerate(pd):
  for x,y in ([(a,b),(c,d)] if not (mask>>i)&1 else [(b,c),(d,a)]):
   p[find(x)]=find(y)
 return len({find(i) for i in range(len(p))})

def lando(pd,baseline):
 s=circles(pd,baseline)
 verts=[i for i in range(len(pd)) if circles(pd,baseline^(1<<i))==s+1]
 adj=[0]*len(verts);edges=[]
 for ii,i in enumerate(verts):
  for jj in range(ii):
   j=verts[jj]
   if circles(pd,baseline^(1<<i)^(1<<j))!=s+2:
    adj[ii]|=1<<jj;adj[jj]|=1<<ii;edges.append([jj,ii])
 # I(G,-1), including the empty independent set.
 cache={0:1}
 def independence(mask):
  if mask not in cache:
   v=(mask&-mask).bit_length()-1;rest=mask^(1<<v)
   cache[mask]=independence(rest)-independence(rest&~adj[v])
  return cache[mask]
 seen=set();components=0
 for i in range(len(verts)):
  if i in seen:continue
  components+=1;todo=[i];seen.add(i)
  while todo:
   v=todo.pop()
   for j in range(len(verts)):
    if adj[v]>>j&1 and j not in seen:seen.add(j);todo.append(j)
 forest=len(edges)==len(verts)-components
 return {'vertices_crossings':verts,'edges':edges,'I_minus_one':independence((1<<len(verts))-1),'forest':forest,'state_circles':s}

def analyze(name,L):
 pd=L.PD_code();c=len(pd);a=lando(pd,0);b=lando(pd,(1<<c)-1)
 genus=(2+c-a['state_circles']-b['state_circles'])//2
 return {'name':name,'PD':pd,'crossings':c,'writhe':L.writhe(),'diagram_Turaev_genus':genus,'A':a,'B':b}

if __name__=='__main__':
 records=[]
 for n,count in [(3,1),(4,1),(5,2),(6,3),(7,7),(8,21),(9,49),(10,165)]:
  for i in range(1,count+1):
   name=f'{n}_{i}';d=analyze(name,Link(name));records.append(d)
 for name in ['11n34','11n42','11n95','11n118']:
  records.append(analyze(name,Link(name)))
 records.append(analyze('8_crossing_actual_unknot',Link(braid_closure=[1,2,1,-2,-1,-2,1,2])))
 # Report genuinely inadequate diagrams with forest extreme(s), and cancellation.
 interesting=[d for d in records if any(d[k]['vertices_crossings'] for k in ['A','B'])]
 Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
 print('checked',len(records),'diagrams')
 for d in interesting:
  if d['name'] in ['8_19','10_153','11n34','11n42','11n95','11n118','8_crossing_actual_unknot'] or all(d[k]['forest'] and d[k]['I_minus_one'] for k in ['A','B']):
   print(d['name'],'g',d['diagram_Turaev_genus'],[(k,len(d[k]['vertices_crossings']),d[k]['edges'],d[k]['I_minus_one'],d[k]['forest']) for k in ['A','B']])
