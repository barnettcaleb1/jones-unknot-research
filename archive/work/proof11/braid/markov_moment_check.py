#!/usr/bin/env python3
"""Exact all-q first-trace versus second-moment countertests.
No claim of a nontrivial knot with Jones polynomial1.
"""
import sys,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'attack_search'))
from search import jones_a,knot

def power(i,m):return [i if m>=0 else -i]*abs(m)
def word(m):return power(2,2*m)+[1,2]+power(2,-2*m)+[-3]
def linking(word,n=4):
 labels=list(range(n));cross=[]
 for a in word:
  i=abs(a)-1;cross.append((labels[i],labels[i+1],1 if a>0 else -1))
  labels[i],labels[i+1]=labels[i+1],labels[i]
 parent=list(range(n))
 def root(i):
  while i!=parent[i]:i=parent[i]
  return i
 for i,j in enumerate(labels):parent[root(i)]=root(j)
 roots=[root(i) for i in range(n)]
 assert len(set(roots))==2
 mixed=sum(s for i,j,s in cross if roots[i]!=roots[j]);assert mixed%2==0
 return mixed//2

rows=[]
for m in range(-8,9):
 b=word(m);first=jones_a(b,4);second=jones_a(b*2,4)
 assert first=={0:1} and knot(b,4)
 assert sum(1 if a>0 else -1 for a in b)==1
 lk=linking(b*2);derivative=sum(e*c for e,c in second.items())
 assert lk==2*m and derivative==24*m
 rows.append({'m':m,'word':b,'Jones_A':first,'squared_closure_linking':lk,
              'squared_Jones_A':second,'derivative_at_A1':derivative})
standard=[1,2,-3]
morton=[-3,-3,2,-3,2,1,1,1,-2,1,-2]
assert jones_a(standard)==jones_a(morton)=={0:1}
assert jones_a(standard*2)!=jones_a(morton*2)
out={'convention':'sigma_i=A I+A^-1 e_i; delta=-A²-A^-2; V=(-A)^(-3w) bracket; t=A^-4',
     'family':rows,'Morton':{'word':morton,'Jones_A':jones_a(morton),
                           'square_Jones_A':jones_a(morton*2)},
     'standard_square_Jones_A':jones_a(standard*2)}
p=pathlib.Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 17 exact first-trace identities, component-linking counts, and second-moment derivative checks; Morton countertest.')
