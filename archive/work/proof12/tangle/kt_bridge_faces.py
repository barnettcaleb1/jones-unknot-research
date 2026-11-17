exec(open('work/proof12/tangle/kt_bridge_data.py').read().split("print('gauss'")[0])
from spherogram.links.links_base import CrossingStrand
op=L.overstrands();edge_to_pass={}
for i,path in enumerate(op):
 for x in path:
  # Inbound/outbound edges adjacent to an overcrossing lie in the same overpass.
  for j in [x.strand_index,(x.strand_index+2)%4]:
   cs=CrossingStrand(x.crossing,j)
   edge_to_pass[cs]=edge_to_pass[cs.opposite()]=i
for i,face in enumerate(L.faces()):
 seen={edge_to_pass[c] for c in face if c in edge_to_pass}
 if len(seen)==3:print('face',i,'length',len(face),'edges',[(c.crossing.label,c.strand_index,edge_to_pass.get(c)) for c in face])
