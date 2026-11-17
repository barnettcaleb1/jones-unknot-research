"""merge census_fixed worker outputs: counts of unit-valued lines by direction and kind"""
import sys, pickle, glob, json
from collections import Counter, defaultdict
D1, D2 = int(sys.argv[1]), int(sys.argv[2])
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
files = sorted(glob.glob(OUT + 'census_%d_%d_w*.pkl' % (D1, D2)))
R = []; U = []; PL = []
for f in files:
    r, u, pl = pickle.load(open(f, 'rb')); R.append(r); U.extend(u); PL.extend(pl)
pairs = sum(r['pairs'] for r in R)
mh = Counter()
for r in R: mh.update(r['maskhist'])
ncand = sum(r['n_cand_offset'] for r in R)
nonunit = Counter()
for r in R: nonunit.update({tuple(k) if isinstance(k, list) else k: v for k, v in r['nonunit_offset'].items()})
sp = Counter(); slt = Counter()
for r in R: sp.update(r['single_pairs']); slt.update(r['single_lines_tested'])
byk = Counter((x[0], x[3]) for x in U)
dirs = sorted(set(d for _, d in byk) | set(sp), key=str)
print('D1,D2', D1, D2, 'workers', len(files), 'junctions (knots)', pairs, 'max worker loop time', max(r['time_loop'] for r in R))
print('|NZ| histogram', dict(sorted(mh.items())))
print('engineB-type (offset) candidates', ncand, ' unit', sum(v for (k, d), v in byk.items() if k == 'offset'), ' non-unit', sum(nonunit.values()))
print('single-group (junction,direction) pairs by direction', dict(sp))
print('UNIT LINES by direction:  offset-type | single-group-type | total')
tot = Counter()
for d in dirs:
    a = byk.get(('offset', d), 0); b = byk.get(('single', d), 0); tot['offset'] += a; tot['single'] += b
    print('   ', d, a, '|', b, '|', a + b)
print('   TOTAL', tot['offset'], '|', tot['single'], '|', tot['offset'] + tot['single'])
npl = len(PL); upl = sum(1 for x in PL if x[5])
print('|NZ| = 1 planes:', npl, ' unit-valued planes:', upl, ' (each = 16 x 49 unit lines)')
# distinct junctions carrying a single-group unit line, by direction
jd = defaultdict(set)
for x in U:
    if x[0] == 'single': jd[x[3]].add((x[1], x[2]))
print('junctions with a single-group unit line, by direction:', {d: len(s) for d, s in jd.items()})
# offsets of single-group unit lines
offs = Counter()
for x in U:
    if x[0] == 'single':
        d = x[3]; m0, n0 = x[4], x[5]
        offs[(d, d[1] * m0 - d[0] * n0)] += 1
print('single-group unit lines by (direction, transverse offset r = q m0 - p n0):', dict(sorted(offs.items(), key=str)))
json.dump({'pairs': pairs, 'maskhist': dict(mh), 'byk': {str(k): v for k, v in byk.items()}, 'single_pairs': {str(k): v for k, v in sp.items()},
           'planes': npl, 'unit_planes': upl, 'offsets': {str(k): v for k, v in offs.items()}},
          open(OUT + 'census_%d_%d_summary.json' % (D1, D2), 'w'), indent=1)
