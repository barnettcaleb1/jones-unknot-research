"""Independent, standard-library Kauffman state sums for the G2 audit.

PD rows are cyclic ports, beginning at an undercrossing. Each edge label
occurs twice. The chosen A-smoothing convention is immaterial to span.
There are only 128 states in each displayed seven-crossing closure.
"""
from collections import Counter
from itertools import product
from math import comb
import json

INITIAL = [(12,7,13,8), (6,13,7,10), (2,12,3,11),
           (10,2,11,1), (5,8,6,9), (9,4,0,5), (3,0,4,1)]
CLAIMED = [(12,7,13,8), (6,13,7,10), (2,12,3,11),
           (10,2,11,1), (8,6,9,5), (9,4,0,5), (3,0,4,1)]
DRAWN_FINAL = [(7,12,8,13), (11,6,12,7), (13,3,10,2),
               (1,11,2,10), (8,6,9,5), (9,4,0,5), (3,0,4,1)]

def bracket(pd):
    counts = Counter(label for crossing in pd for label in crossing)
    assert set(counts.values()) == {2}
    result = Counter()
    for state in product((0, 1), repeat=len(pd)):
        parent = {label: label for label in counts}
        def find(label):
            while parent[label] != label:
                parent[label] = parent[parent[label]]
                label = parent[label]
            return label
        def join(a, b):
            parent[find(a)] = find(b)
        for (a,b,c,d), choice in zip(pd, state):
            pairs = ((a,b),(c,d)) if choice == 0 else ((a,d),(b,c))
            for u,v in pairs:
                join(u,v)
        loops = len({find(label) for label in parent})
        power = loops - 1
        shift = len(pd) - 2*sum(state)
        for j in range(power+1):
            result[shift+2*power-4*j] += (-1)**power * comb(power,j)
    return dict(sorted((e,c) for e,c in result.items() if c))

if __name__ == '__main__':
    expected = {
        'initial': {-15:1, -11:-1, -7:2, -3:-1, 1:2, 5:-1},
        'claimed': {-5:1, -1:1},
        'drawn_final': {-9:1, -5:-1, -1:2, 3:-1, 7:2, 11:-1},
    }
    report = {}
    for name,pd in [('initial',INITIAL),('claimed',CLAIMED),
                    ('drawn_final',DRAWN_FINAL)]:
        value = bracket(pd)
        assert value == expected[name], (name, value)
        report[name] = {'PD': pd, 'bracket_A': value,
                        'span_A': max(value)-min(value),
                        'states_evaluated': 2**len(pd)}
    assert report['initial']['span_A'] != report['claimed']['span_A']
    assert expected['drawn_final'] == {e+6:c for e,c in expected['initial'].items()}
    print(json.dumps(report, indent=2))
