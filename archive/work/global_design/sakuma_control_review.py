"""Read-only check of Claude's two saved figure-eight control projections.

This checks actual component isotopies; it does not run the generator, search
parameters, compute Jones polynomials, or certify any prospective candidate.
"""
from pathlib import Path
import hashlib
import json
import sys

WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORK / 'braid_classification' / 'packages'))
from spherogram import Link

SOURCE = Path('/private/tmp/claude-501/-Users-calebbarnett/'
              '7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak/out')


def check_projection(index, prefix='fig8_I1_2_1_rot1'):
    path = SOURCE / f'{prefix}_sakuma_proj{index}.json'
    raw = path.read_bytes()
    data = json.loads(raw)
    link = Link(data['pd']['pd'])
    assert len(link.link_components) == 2
    components = []
    for component in range(2):
        self_crossings = sum(c.strand_components[0] == component
                             and c.strand_components[1] == component
                             for c in link.crossings)
        if self_crossings == 0:
            components.append({'self_crossings': 0,
                               'certificate': 'simple planar projection'})
            continue
        knot = link.sublink(component)
        assert len(knot.link_components) == 1
        knot.simplify('basic')
        if knot.crossings:
            knot.simplify('global')
        assert not knot.crossings
        assert knot.unlinked_unknot_components == 1
        components.append({'self_crossings': self_crossings,
                           'certificate': 'Reidemeister/pickup simplification',
                           'remaining_crossings': 0,
                           'crossing_free_unknot_count': 1})
    return {'source': str(path), 'sha256': hashlib.sha256(raw).hexdigest(),
            'crossings': len(link.crossings), 'components': components,
            'jones_dictionary': data['jones_t_half_exponents']}


if __name__ == '__main__':
    records = [check_projection(i) for i in (0, 1)]
    assert records[0]['jones_dictionary'] == records[1]['jones_dictionary']
    print(json.dumps({'scope': 'saved control only; no candidate verdict',
                      'projections': records}, indent=2))
