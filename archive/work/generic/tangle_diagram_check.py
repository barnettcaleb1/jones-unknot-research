#!/usr/bin/env python3
"""Replay the six-crossing numerator unknot; optionally regenerate its PD.
Requires Regina. With --regenerate, also requires Spherogram.
Run from an environment containing those packages, or set PYTHONPATH.
"""
from pathlib import Path
import argparse, json, sys

# Convenience for this workspace; ignored in an extracted evidence archive.
local = Path(__file__).resolve().parent.parent / 'braid_classification' / 'packages'
if local.exists(): sys.path.insert(0, str(local))
import regina

parser=argparse.ArgumentParser()
parser.add_argument('--regenerate',action='store_true')
args=parser.parse_args()
data=json.loads(Path(__file__).with_name('tangle_diagram_certificate.json').read_text())
pd=data['PD_zero_based']
if args.regenerate:
    from spherogram.links.tangles import RationalTangle
    t=RationalTangle(-1)+RationalTangle(1,2)+RationalTangle(1,3)
    rebuilt=[list(r) for r in t.numerator_closure().PD_code()]
    assert rebuilt==pd, (rebuilt,pd)
r=regina.Link.fromPD([[x+1 for x in row] for row in pd])
assert r.size()==6 and r.countComponents()==1
assert str(r.jones())=='1'
for move in data['moves']:
    typ,index,*extra=move
    assert getattr(r,typ)(r.crossing(index),*extra),move
assert r.size()==0 and r.countComponents()==1
print(f"Certified numerator unknot: {len(data['moves'])} checked Reidemeister moves, 6 -> 0 crossings.")
