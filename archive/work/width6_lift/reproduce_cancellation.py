"""Reproduce the 14-letter cap-slide cancellation and its actual topology.

Run from any directory with the workspace's existing Python packages.
The two-variable polynomial is computed independently of the saved JSON.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'width6'))
import lift_pairing as lp
import probe
import topology_classifier

BASE = [4, 3, 2, 1, 5, 4, 3, 2, 3, 4]
WORD = BASE + [2, 3, -1, -2]
C0 = 7

polynomial = lp.pairing(WORD, C0, C0)
factorized = lp.shift(lp.mul(
    lp.mul(lp.add(lp.ONE, lp.Q, -1), lp.add(lp.ONE, lp.T, -1)),
    lp.add(lp.ONE, lp.mul(lp.Q, lp.T))), 8)
assert polynomial == factorized and polynomial
assert len(polynomial) == 7
assert lp.pairing(BASE, C0, C0) == {}
assert lp.specialize(polynomial) == {}
assert probe.coefficient(WORD, C0, C0) == {}

topology = topology_classifier.classify(WORD, C0, C0)
assert topology['classification'] == 'split_certified'
assert topology['remaining_crossings'] == 0
closures = probe.closure_checks(WORD, C0, C0)
numerator = closures['numerator_closure']
denominator = closures['denominator_closure']
assert numerator['simplified_crossings'] == 0
assert numerator['simplified_components'] == 2
assert denominator['unknot_certified']

print(json.dumps({
    'word': WORD,
    'P': 'q^4(1-q)(1-t)(1+qt)',
    'P_nonzero': True,
    'Jones_coefficient_zero': True,
    'tangle_final_crossings': topology['remaining_crossings'],
    'numerator_final_components': numerator['simplified_components'],
    'denominator_actual_unknot': denominator['unknot_certified'],
}, indent=2))
