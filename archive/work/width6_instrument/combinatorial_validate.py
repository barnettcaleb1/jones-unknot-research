"""Exact rational transport versus an independent Artin free-group oracle."""
from fractions import Fraction as F
from pathlib import Path
import json
import transport_pl as pl
import combinatorial_winding as cw

HERE = Path(__file__).resolve().parent


def inverse(w):
    return [-x for x in reversed(w)]


def artin(word, n=6):
    images = [[k+1] for k in range(n)]
    for g in word:
        k = abs(g)-1
        a, b = images[k:k+2]
        if g > 0:
            images[k], images[k+1] = cw.reduced(a+b+inverse(a)), a
        else:
            images[k], images[k+1] = b, cw.reduced(inverse(b)+a+b)
    return images


def meridian(j, radius=F(1, 4)):
    base = pl.point(0, -2)
    corner = pl.point(j-radius, -radius)
    stem = [base, pl.point(j-radius, -2), corner]
    loop = [corner, pl.point(j+radius, -radius),
            pl.point(j+radius, radius), pl.point(j-radius, radius), corner]
    return stem[:-1]+loop+list(reversed(stem[:-1]))


def geometric_images(word):
    curves = [pl.braid_curve(meridian(j), word) for j in range(1, 7)]
    lean = cw.choose_generic_lean(curves)
    return [cw.free_word(c, lean=lean) for c in curves], curves, lean


def run():
    assert [cw.free_word(meridian(j)) for j in range(1, 7)] == [[j] for j in range(1, 7)]
    controls = [[g] for g in range(1, 6)] + [[-g] for g in range(1, 6)]
    controls += [[1, 2], [2, 1], [1, 2, 1], [2, 1, 2], [2, -3, 1], [4, -5, -2, 1]]
    rows = []
    candidates = {'chronological': lambda w: list(reversed(w)),
                  'chronological_inverse_signs': lambda w: [-g for g in reversed(w)],
                  'as_written': lambda w: w,
                  'as_written_inverse_signs': lambda w: [-g for g in w]}
    possible = set(candidates)
    for w in controls:
        images, curves, lean = geometric_images(w)
        # Our upward-cut meridians use paths composed left-to-right.  The
        # conventional Artin oracle uses the opposite based-word convention.
        matches = [name for name, convert in candidates.items()
                   if [list(reversed(a)) for a in artin(convert(w))] == images]
        possible &= set(matches)
        rows.append({'geometric_word': w, 'free_group_images': images,
                     'curve_vertices': [len(c) for c in curves],
                     'cut_lean': str(lean), 'matching_conventions': matches})
        print(w, matches, [len(x) for x in images], flush=True)
    assert len(possible) == 1, possible
    data = {'status': 'EXACT_RATIONAL_TRANSPORT_ARTIN_CHECK',
            'output_free_word_conversion': 'Reverse each Artin image word',
            'common_convention': sorted(possible), 'controls': rows}
    (HERE / 'combinatorial_validate.json').write_text(json.dumps(data, indent=2)+'\n')
    # Exact monodromy sanity controls: one puncture winding and a half exchange.
    mobile = meridian(1)
    static = pl.point(8, -2)
    a, b = cw.configuration_monodromy([(p, static) for p in mobile])
    assert (a, b) == (1, 0), (a, b)
    pair = [(pl.point(-1, 0), pl.point(1, 0)),
            (pl.point(0, -1), pl.point(0, 1)),
            (pl.point(1, 0), pl.point(-1, 0))]
    a, b = cw.configuration_monodromy(pair, punctures=[])
    assert (a, b) == (0, 1), (a, b)
    print('exact monodromy controls passed')


if __name__ == '__main__':
    run()
