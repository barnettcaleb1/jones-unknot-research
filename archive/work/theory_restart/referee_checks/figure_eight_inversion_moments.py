"""Fixed two-inversion calibration; no search or scan.

Input halfwords are the two 4_1 entries in the archived KWZ table:
theory-restart/lit/kwz-inversions/data.json, khtpp.input.
Run with the existing theory-restart/tools/venv/bin/python -B.
"""
import json
from pathlib import Path
import sys

sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import lp

PAIRS = [
    ('4_1^1', 's.l1.y0.y0.x1.u2'),
    ('4_1^2', 's.l1.x0.x0.y1.u2'),
]

rows = []
for name, word in PAIRS:
    polynomial = lp.J(word)
    moments = [sum(c * (-1)**(e % 2) * e**k
                   for e, c in polynomial.items()) for k in range(5)]
    rows.append(dict(name=name, word=word,
                     J=dict(sorted(polynomial.items())), moments=moments))
assert rows[0]['moments'] == [1, 0, 24, -180, 1200]
assert rows[1]['moments'] == [1, 0, 24, 180, 1200]
assert rows[1]['J'] == {-e:c for e,c in rows[0]['J'].items()}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(rows, indent=2) + '\n')
print(json.dumps(rows, indent=2))
