"""Extract Lee length-one bar sources from published KT rational Kh data.
Data: Sano2602.17435 Prop6.1. His delta=2h+q; our h is its negative.
Fusion1: Hom--Kang--Park2003.02832 p2. Length1: Sarkar1903.11095.
"""
from collections import defaultdict
from pathlib import Path
import json
strings={-2:[(-6,2,1),(-4,1,1),(-4,3,1),(-2,2,1),(0,1,2),(2,2,2),(4,1,1),(8,1,1)],0:[(-12,1,1),(-10,2,2),(-8,1,1),(-8,3,1),(-6,2,1),(-4,1,2),(-2,2,1),(0,1,2)]}
P=defaultdict(int)
for delta,terms in strings.items():
 for q,l,m in terms:
  for k in range(l):
   qq=q+4*k;h=(qq-delta)//2;P[h,qq]+=m
R=dict(P);R[0,0]-=1;R={k:v for k,v in R.items() if v};S={}
while R:
 h,q=min(R);v=R[h,q]
 assert v>0,(h,q,v)
 S[h,q]=v
 for key in ((h,q),(h+1,q+2)):
  R[key]=R.get(key,0)-v
  if not R[key]:del R[key]
rows={}
for(h,q),v in S.items():
 rows.setdefault(q,{'even':0,'odd':0})['even' if h%2==0 else 'odd']+=v
report={'source':'https://arxiv.org/pdf/2602.17435, Proposition6.1, pp76-77','homological_conversion':'our h=-Sano h; same quantum q','reduced_rank':sum(P.values()),'number_length1_bars':sum(S.values()),'bar_sources':[{'h':h,'q':q,'multiplicity':v} for(h,q),v in S.items()],'parity_by_source_q':rows,'mixed_source_q':[q for q,v in rows.items() if v['even'] and v['odd']],'extreme_source_q':[min(rows),max(rows)]}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
