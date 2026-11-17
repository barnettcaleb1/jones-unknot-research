"""Bounded, actual face-band fusions of the EKT LLL(1) diagram.

No completeness claim. Every band lies in one diagram face and has at most
two half twists. Exact Goeritz determinant filters exact Jones evaluations.
"""
from pathlib import Path
import json,time,itertools,random
from collections import Counter
from lll_linking_form import lll,goeritz,det,regina
from spherogram import Link
from spherogram.links.bands.core import Band,add_one_band,normalize_crossing_labels

random.seed(3301)
HERE=Path(__file__).resolve().parent
def fusion_bands(L):
 normalize_crossing_labels(L)
 seen=set()
 for face in L.faces():
  for X,Z in itertools.combinations(face,2):
   Z=Z.opposite()
   if X.crossing.strand_components[X.strand_index]==Z.crossing.strand_components[Z.strand_index]:continue
   pair=[(x.crossing.label,x.strand_index)for x in (X,Z)]
   for twist in range(-2,3):
    b=Band(pair,[],twist);spec=b.compressed_spec()
    if spec in seen:continue
    seen.add(spec)
    M=add_one_band(L,b)
    assert len(M.link_components)==len(L.link_components)-1
    yield M,spec

def jones(L):
 return regina.Link.fromPD([[x+1 for x in r]for r in L.PD_code()]).jones()

def main():
 start=time.monotonic();counts=Counter();hits=[];samples=[]
 L=lll(1);original=L.PD_code()
 assert str(jones(L))=='x^2 + 2 + x^-2'
 # All first bands are enumerated, but second stages stop at the stated clock limit.
 first=list(fusion_bands(L));random.shuffle(first)
 counts['first_bands_available']=len(first)
 for M,spec1 in first:
  counts['first_bands_examined']+=1
  M.simplify('basic');normalize_crossing_labels(M)
  if len(M.link_components)!=2 or M.unlinked_unknot_components:
   counts['split_intermediates_skipped']+=1;continue
  mid=M.PD_code()
  for K,spec2 in fusion_bands(M):
   counts['two_band_knots']+=1
   K.simplify('basic')
   if not K.crossings:
    counts['diagrammatic_unknots']+=1;continue
   d=abs(int(det(goeritz(K))))
   if d!=1:continue
   counts['determinant_one']+=1
   V=jones(K)
   if len(samples)<4:samples.append({'first_band':spec1,'intermediate_pd':mid,'second_band':spec2,'pd':K.PD_code(),'jones':str(V)})
   if V.minExp()==V.maxExp()==0 and str(V[0])=='1':
    counts['jones_one']+=1
    before=K.PD_code();K.simplify('global')
    hits.append({'first_band':spec1,'intermediate_pd':mid,'second_band':spec2,'pd':before,'simplified_pd':K.PD_code(),'unlinked_unknot_components':K.unlinked_unknot_components})
   if time.monotonic()-start>120:break
  print(dict(counts),round(time.monotonic()-start,2),flush=True)
  if time.monotonic()-start>120:break
 out={'original_pd':original,'counts':dict(counts),'seconds':time.monotonic()-start,'hits':hits,'determinant_one_samples':samples,'limits':'Face bands only, at most two half twists per band; skip split intermediates; 120-second bound. Not exhaustive beyond stated enumeration.'}
 (HERE/'two_band_test.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in ['original_pd','hits','determinant_one_samples']}),flush=True)

if __name__=='__main__':main()
