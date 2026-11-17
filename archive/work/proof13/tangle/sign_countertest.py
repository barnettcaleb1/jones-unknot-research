"""Small directed countertest: one familiar three-bridge knot and a stabilized two-bridge knot.
All tested template inputs recorded; stop at the first failure of leading-sign coherence.
"""
from pathlib import Path
import sys,json,itertools
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]/'proof12'/'tangle'))
import kt_double_cuts as geom
from spherogram import Link
from spherogram.links.links_base import CrossingStrand
import regina
ns={'__file__':__file__};exec((ROOT.parents[1]/'proof12/tangle/kt_leading_verify.py').read_text().split('rows=json.loads')[0],ns)
add,mul,divide,clean=ns['add'],ns['mul'],ns['divide'],ns['clean']
def jones(L):
 L=L.copy();L.simplify('global')
 R=regina.Link.fromPD([tuple(v+1 for v in r) for r in L.PD_code()]) if L.crossings else regina.Link(L.unlinked_unknot_components)
 if L.crossings:
  for _ in range(L.unlinked_unknot_components):R.insertLink(regina.Link(1))
 J=R.jones();return {e:int(str(J[e])) for e in range(J.minExp(),J.maxExp()+1) if int(str(J[e]))},L
trials=[]
for name in ['8_19','8_20','4_1','3_1','9_46']:
 geom.L=Link(name)
 for face_id,face in enumerate(geom.L.faces()):
  # Unique edges on a face, keeping its cyclic order.
  edges=[];seen=set()
  for cs in face:
   edge=frozenset([cs,cs.opposite()])
   if edge not in seen:seen.add(edge);edges.append((cs.crossing.label,cs.strand_index))
  if len(edges)<3:continue
  for triple in itertools.combinations(edges,3):
   geom.selected=list(triple)
   try:
    Lall=geom.build([0,1,2]);Lall.simplify('global')
   except ValueError:continue
   unlink=not Lall.crossings and Lall.unlinked_unknot_components==3
   trials.append({'knot':name,'face':face_id,'selected':triple,'all_cut_unlink':unlink})
   if not unlink:continue
   Q=[];data=[]
   for cut in [[],[1],[2],[1,2]]:
    L=geom.build([0]+cut);assert all(v==0 for row in L.linking_matrix() for v in row)
    P,S=jones(L);d={0:1}
    for _ in cut:d=mul(d,{1:-1,-1:-1})
    q=divide(P,d);assert all(e%2==0 and c.denominator==1 for e,c in q.items())
    Q.append({e//2:int(c) for e,c in q.items()})
    data.append({'cut':cut,'PD':L.PD_code(),'simplified_PD':S.PD_code(),'free_unlinks':S.unlinked_unknot_components,'Jones_x':P})
   A=add(Q[0],{e:-c for e,c in Q[1].items()},{e:-c for e,c in Q[2].items()},{0:1});B=add(Q[2],{0:-1});C=add(Q[1],{0:-1})
   leading=[None if not p else (max(p),p[max(p)]) for p in [A,B,C]]
   signs={1 if c>0 else -1 for z in leading if z for _,c in [z]}
   print(name,face_id,triple,leading,flush=True)
   if len(signs)>1:
    out={'base_knot':name,'base_PD':geom.L.PD_code(),'face_id':face_id,'selected_edges':triple,'cut_Q':Q,'A':A,'B':B,'C':C,'leading':leading,'cut_diagrams':data,'trials':trials}
    (ROOT/'sign_counterexample.json').write_text(json.dumps(out,indent=2));print('FOUND',flush=True);sys.exit()
(ROOT/'sign_trials.json').write_text(json.dumps(trials,indent=2))
