"""Small fixed controls for the proposed plat-width reduction; no search."""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'braid_classification/packages'))
from spherogram.links.tangles import BraidTangle, ZeroTangle, IdentityBraid
import regina


def record(link):
    pd = link.PD_code()
    r = regina.Link.fromPD([[x + 1 for x in row] for row in pd])
    omitted = int(link.unlinked_unknot_components)
    if omitted:
        r.insertLink(regina.Link(omitted))
    assert r.countComponents() == len(link.link_components) + omitted
    result = {'PD': pd, 'components': r.countComponents(),
              'Jones': str(r.jones()), 'crossing_free_restored': omitted}
    r.simplify()
    result.update(simplified_crossings=r.size(),
                  simplified_components=r.countComponents())
    return result


results = {}
for n in (4, 6):
    tail = [] if n == 4 else [4]
    pair = {}
    for sign in (1, -1):
        word = [2, 2, sign, 2, 2, 2] + tail
        pair[str(sign)] = {'word': word, **record(
            BraidTangle(word, n).numerator_closure())}
    smoothing = (BraidTangle([2, 2], n)
                 * (ZeroTangle() | IdentityBraid(n - 2))
                 * BraidTangle([2, 2, 2] + tail, n)).numerator_closure()
    pair['horizontal_smoothing'] = record(smoothing)
    pair['smoothing_factors'] = [record(f) for f in smoothing.deconnect_sum()]
    assert pair['1']['Jones'] == '1'
    assert pair['1']['simplified_crossings'] == 0
    assert pair['1']['simplified_components'] == 1
    assert pair['-1']['Jones'] != '1'
    results[str(n)] = pair
assert results['4']['-1']['Jones'] == results['6']['-1']['Jones']
# The two-component smoothing has independently chosen component orientations;
# compare its diagrammatic factors, not an unadjusted oriented Jones value.
(HERE / 'check_results.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps({n: {key: {k: row[k] for k in
                          ('components', 'Jones', 'simplified_crossings')}
                     for key, row in pair.items() if key != 'smoothing_factors'}
                  for n, pair in results.items()}, indent=2))
