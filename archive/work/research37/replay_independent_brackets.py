"""Replay the independent full bracket check of all 48 cut diagrams."""
from pathlib import Path
import json, runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
bracket=runpy.run_path(str(ROOT/'work/cancellation19/independent_pd_bracket.py'))['evaluate']
data=json.loads((HERE/'marked_hits.json').read_text())
count=0
for record in data['hits']:
    if record['status']!='certified marked pair':
        continue
    for cut in record['cuts']:
        b,_=bracket(cut['PD'])
        w=cut['writhe']
        assert all((e-3*w)%2==0 for e in b)
        v={-(e-3*w)//2:a*(-1 if w%2 else 1) for e,a in b.items()}
        expected={int(e):a for e,a in cut['coefficients'].items()}
        assert v==expected, (record['hit'],cut['active'])
        count+=1
assert count==48
print('PASS: all 48 complete cut polynomials match the independent bracket state sum.')
