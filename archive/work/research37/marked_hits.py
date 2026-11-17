from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'braid_classification/packages'))
sys.path.insert(0,str(HERE.parent/'research34'))
from two_band_family import insert_face_band_unrebuilt
from spherogram import Link,Crossing
from spherogram.links.bands.core import Band,normalize_crossing_labels
from spherogram.links.links_base import CrossingStrand
import regina
DATA=json.loads((HERE.parent/'research33/two_band_test.json').read_text()); BASE=DATA['original_pd']
oldrotate=Crossing.rotate
def rotate(self,s):
 self._port_rot=(getattr(self,'_port_rot',0)+s)%4
 return oldrotate(self,s)
Crossing.rotate=rotate

def base():
 L=Link(BASE);normalize_crossing_labels(L)
 for i,c in enumerate(L.crossings):c._orig=i;c._port_rot=0
 return L

def construct(sites,twists,active=(True,True),ori=None):
 L=base()
 for site,t,on in zip(sites,twists,active):
  if on:insert_face_band_unrebuilt(L,site,t)
 if ori is None:L._rebuild()
 else:
  for c in L.crossings:c._clear()
  L._build(start_orientations=[(L.crossings[c],p)for c,p in ori])
 assert L.is_planar()
 return L

def orientation(L):
 return [(c._orig,(b+c._port_rot)%4)for c in L.crossings if hasattr(c,'_orig')for a,b in c.directions]

def rec(L):
 pd=L.PD_code();R=regina.Link.fromPD([[i+1 for i in c]for c in pd]);assert R.writhe()==L.writhe()
 V=R.jones();cs={e:int(str(V[e]))for e in range(V.minExp(),V.maxExp()+1)if V[e]!=0}
 return {'PD':pd,'writhe':L.writhe(),'components':len(L.link_components),'Jones':str(V),'coefficients':cs}

def moments(coeff):
 p={int(e):int(c)for e,c in coeff.items()};p[1]=p.get(1,0)+1;p[-1]=p.get(-1,0)+1
 for n in range(25):
  m=sum(c*e**n for e,c in p.items())
  if m:return {'vanishing_order_at_1':n,'leading_Euler_moment':m,'deviation_coefficients':p}
 return {'vanishing_order_at_1':None,'leading_Euler_moment':0,'deviation_coefficients':p}

def process(i,h):
 b1,b2=Band(h['first_band']),Band(h['second_band']);assert len(b1.cs_along_top)==len(b2.cs_along_top)==2
 M=base();insert_face_band_unrebuilt(M,b1.cs_along_top,b1.num_twist);M._rebuild();M.simplify('basic');normalize_crossing_labels(M)
 if [list(c)for c in M.PD_code()]!=h['intermediate_pd']:return {'hit':i,'status':'intermediate mismatch'}
 site2=[]
 for j,p in b2.cs_along_top:
  c=M.crossings[j]
  if not hasattr(c,'_orig'):return {'hit':i,'status':'second band touches newly added crossing'}
  site2.append((c._orig,(p+c._port_rot)%4))
 sites=[b1.cs_along_top,site2];twists=[b1.num_twist,b2.num_twist]
 L=base();face_info=[];edge_sets=[]
 for site in sites:
  (i0,p0),(i1,p1)=site;X=CrossingStrand(L.crossings[i0],p0);Z=CrossingStrand(L.crossings[i1],p1)
  fs=[(fi,F.index(X),F.index(Z.opposite()),len(F))for fi,F in enumerate(L.faces())if X in F and Z.opposite()in F]
  if len(fs)!=1:return {'hit':i,'status':'pulled-back band not in one original face','sites':sites,'twists':twists}
  face_info.append(fs[0]);edge_sets.append({X.strand_label(),Z.strand_label()})
 if not edge_sets[0].isdisjoint(edge_sets[1]):return {'hit':i,'status':'shared original attaching edge','sites':sites,'twists':twists}
 if face_info[0][0]==face_info[1][0]:
  _,a,b,N=face_info[0];_,c,d,_=face_info[1]
  if ((c-a)%N<(b-a)%N)!=((d-a)%N<(b-a)%N):return {'hit':i,'status':'alternating original face chords','sites':sites,'twists':twists}
 K=construct(sites,twists);ori=orientation(K);anchor=rec(K)
 if anchor['Jones']!='1':return {'hit':i,'status':'pulled-back anchor not Jones one','sites':sites,'twists':twists,'anchor':anchor}
 K.simplify('global');assert len(K.crossings)==0 and K.unlinked_unknot_components==1
 cuts=[]
 for active in [(False,True),(True,False),(False,False)]:
  r=rec(construct(sites,twists,active,ori));r['active']=active
  if sum(active)==1:r.update(moments(r['coefficients']))
  cuts.append(r)
 out={'hit':i,'status':'certified marked pair','sites':sites,'base_half_twists':twists,'original_face_data':face_info,'attaching_edges':[sorted(x)for x in edge_sets],'induced_orientation_outgoing_ports':ori,'anchor':anchor,'cuts':cuts}
 return out
if __name__=='__main__':
 out=[]
 for i,h in enumerate(DATA['hits']):
  try:r=process(i,h)
  except Exception as e:r={'hit':i,'status':'error','error':repr(e)}
  out.append(r);print(i,r['status'],[(c.get('vanishing_order_at_1'),c.get('leading_Euler_moment'))for c in r.get('cuts',[])],flush=True)
  (HERE/'marked_hits.json').write_text(json.dumps({'original_PD':BASE,'hits':out},indent=2)+'\n')
