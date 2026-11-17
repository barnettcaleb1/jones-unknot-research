"""Standard-library verification of the saved actual two-band counterexample.
The certificate is finite but proves nonvanishing for ALL integer twists.
"""
from pathlib import Path
import json,itertools
D=json.loads(Path(__file__).with_name('sign_counterexample.json').read_text())
Q=[{int(e):c for e,c in p.items()} for p in D['cut_Q']]
def add(*ps):
 d={}
 for p in ps:
  for e,c in p.items():d[e]=d.get(e,0)+c
 return {e:c for e,c in d.items() if c}
def neg(p):return {e:-c for e,c in p.items()}
A=add(Q[0],neg(Q[1]),neg(Q[2]),{0:1});B=add(Q[2],{0:-1});C=add(Q[1],{0:-1})
assert Q[3]=={0:1}
for key,p in zip(['A','B','C'],[A,B,C]):assert p=={int(e):c for e,c in D[key].items()}
leads=[(max(p),p[max(p)]) for p in [A,B,C]]
assert leads==[(5,-2),(5,1),(4,-1)]
assert len({c>0 for _,c in leads})==2
for residue in [0,1]:
 cs=[c for d,c in leads if d%2==residue]
 for n in range(1,len(cs)+1):
  for subset in itertools.combinations(cs,n):assert sum(subset)!=0
 print('residue',residue,'all nonempty leading coefficient subset sums nonzero:',cs)
# A simple lower-order obstruction also excludes this particular family.
for p in [A,B,C]:assert sum(p.values())==sum(e*c for e,c in p.items())==0
assert sum(c*e*e for p in [A,B,C] for e,c in p.items())==-60
print('PASS: mixed-sign ribbon template; all twists excluded by parity, and independently by V second derivative=-60.')
