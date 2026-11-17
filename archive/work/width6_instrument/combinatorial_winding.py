"""Exact cut crossings, free words and configuration monodromy for rational PL paths.

No angles, rounding, sampled chord images or aggregate polynomial coefficients
are used.  The input path must itself be an actual collision-free PL path.
"""
from fractions import Fraction as F


def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def sign(x):
    return int(x > 0)-int(x < 0)


def reduced(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def cut_events(curve, punctures=range(1, 7), lean=F(1, 101)):
    """Crossings of disjoint upward cuts (j+lean*y,y), y>=0.

    The meridian generator x_j is counterclockwise: right-to-left crossing
    of its upward cut has sign +1.  Records are UNREDUCED geometric events.
    All vertices must avoid the positive cuts; choose_generic_lean can ensure
    this.  A puncture endpoint at y=0 does not itself create an event.
    """
    out = []
    prefix = 0
    for i, (a, b) in enumerate(zip(curve, curve[1:])):
        events = []
        for j in punctures:
            x = a[0]-lean*a[1]-j
            y = b[0]-lean*b[1]-j
            assert not (x == 0 and a[1] > 0), ('nongeneric vertex', i, j)
            assert not (y == 0 and b[1] > 0), ('nongeneric vertex', i+1, j)
            if x*y >= 0:
                continue
            t = x/(x-y)
            height = a[1]+t*(b[1]-a[1])
            if height <= 0:
                continue
            letter = j if x > 0 else -j
            events.append((t, letter, (a[0]+t*(b[0]-a[0]), height)))
        for t, letter, p in sorted(events):
            out.append({'segment': i, 'parameter': t, 'position': p,
                        'letter': letter, 'prefix_q_before': prefix,
                        'prefix_q_after': prefix+sign(letter)})
            prefix += sign(letter)
    return out


def choose_generic_lean(curves, punctures=range(1, 7)):
    for denominator in range(101, 10000, 2):
        lean = F(1, denominator)
        if all(not (p[1] > 0 and p[0]-lean*p[1] in punctures)
               for curve in curves for p in curve):
            return lean
    raise RuntimeError('No generic cut slope found in bounded list')


def free_word(curve, punctures=range(1, 7), lean=None):
    if lean is None:
        lean = choose_generic_lean([curve], punctures)
    return reduced([r['letter'] for r in cut_events(curve, punctures, lean)])


def ray_segment_count(a, b, center, lean=F(1, 101)):
    """Integer crossing of the positive ray from center in direction(lean,1).

    Counterclockwise winding has positive sign. Endpoint convention is
    half-open; the reference endpoint of the complete loop must avoid the cut.
    """
    u, v = sub(a, center), sub(b, center)
    f, g = u[0]-lean*u[1], v[0]-lean*v[1]
    if not ((f <= 0 < g) or (g <= 0 < f)):
        return 0
    t = f/(f-g)
    height = u[1]+t*(v[1]-u[1])
    if height == 0:
        raise ValueError('Path hits puncture/center')
    return (1 if f > g else -1) if height > 0 else 0


def line_segment_count(a, b, center=(F(0), F(0)), lean=F(1, 101)):
    """Signed crossing of full line x-lean*y=0, for half-exchange winding.

    A closed path of relative vectors gives twice its ordinary winding; a
    path ending at its negative gives an odd integer. The initial relative
    vector must avoid this line.  Each crossing sign is angular orientation.
    """
    u, v = sub(a, center), sub(b, center)
    if u == (0, 0) or v == (0, 0):
        raise ValueError('Configuration collision at vertex')
    d = cross(u, v)
    if d == 0 and u[0]*v[0]+u[1]*v[1] < 0:
        raise ValueError('Configuration collision inside segment')
    f, g = u[0]-lean*u[1], v[0]-lean*v[1]
    if (f <= 0 < g) or (g <= 0 < f):
        return sign(d)
    return 0


def configuration_monodromy(path, punctures=range(1, 7), lean=F(1, 101)):
    """Exact (a,b) for an unordered closed configuration path.

    path is a sequence of ordered pairs of rational points, continuously
    labeled along each segment. The final ordered pair may be swapped.
    Every simultaneous segment must be collision-free. The typical intended
    paths move just one point at a time, as in Bigelow's intersection rule.
    """
    assert path and sorted(path[0]) == sorted(path[-1])
    initial = sub(*path[0])
    assert initial[0]-lean*initial[1] != 0, 'Reference relative vector on cut'
    a = b = 0
    centers = [(F(j), F(0)) for j in punctures]
    for previous, current in zip(path, path[1:]):
        for k in (0, 1):
            for center in centers:
                a += ray_segment_count(previous[k], current[k], center, lean)
        b += line_segment_count(sub(*previous), sub(*current), lean=lean)
    assert b % 2 == int(path[0] != path[-1])
    return a, b


def encode_events(events):
    return [{**r, 'parameter': str(r['parameter']),
             'position': [str(x) for x in r['position']]} for r in events]
