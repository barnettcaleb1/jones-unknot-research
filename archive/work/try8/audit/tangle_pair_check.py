"""Independent check of the unframed two-probe example.

Run with PYTHONPATH=work/braid_classification/packages python3 this_file.py.
All equivalences below are certified by Reidemeister simplification to the
unknot or to an identical planar diagram, not merely by Jones equality.
"""
import json
from spherogram import Link
from spherogram.links.tangles import RationalTangle

X = RationalTangle(-1) + RationalTangle(1, 2) + RationalTangle(1, 3)
R = RationalTangle(1, 4)
target = sorted(Link(braid_closure=[-1] * 5).PD_code())
result = {}
for name, T in [('X', X), ('R', R)]:
    result[name] = []
    for probe in [0, 1]:
        L = (T + RationalTangle(probe)).numerator_closure()
        initial_crossings, initial_writhe = len(L.crossings), L.writhe()
        L.simplify('global')
        pd = sorted(L.PD_code())
        if probe == 0:
            assert not L.crossings and L.unlinked_unknot_components == 1
        else:
            assert pd == target
        result[name].append(dict(probe=probe,
            initial_crossings=initial_crossings,
            initial_writhe=initial_writhe, simplified_pd=pd,
            discarded_unknots=L.unlinked_unknot_components))
assert [x['initial_writhe'] for x in result['X']] == [0, -5]
assert [x['initial_writhe'] for x in result['R']] == [4, -5]
print(json.dumps(result, indent=2))
