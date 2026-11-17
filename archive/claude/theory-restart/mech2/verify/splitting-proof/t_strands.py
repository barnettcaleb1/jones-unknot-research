# knot types (via dim Kh~ over F_2) of the two strands of the quotient tangle closed up alone, for the 138 table inversions,
# against dim N = 1 + 2m from the saved data.  Theorem A(i) predicts dim N >= product.
from t_common import *
import json, os, glob
SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'
rows = {}
for l in open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/k138.jsonl'):
    r = json.loads(l); rows[r['file']] = r
MAXC = int(sys.argv[1]) if len(sys.argv) > 1 else 14
out = []
for fn in sorted(glob.glob(SI + '/*.kht')):
    name = os.path.basename(fn)[:-4]
    word = open(fn).read().split('\n')[1].strip()
    assert word.startswith('s.')
    key = name.replace('-', '^')
    r = rows.get(key)
    dimN = None
    if r is not None:
        m = sum(1 for c in r['khr'] if c['type'] == 's')
        dimN = 1 + 2 * m
    try:
        D = closure13(quotient_word(word[2:]))
    except AssertionError as e:
        print(name, 'diagram error', e); continue
    if D.ncomp != 2 or D.comp[D.marks[0]] == D.comp[D.marks[1]]:
        print(name, 'closure not a 2-component link with one mark each:', D.ncomp); continue
    dims = []; ncs = []
    for c in range(2):
        S = SubDiagram(D, c); ncs.append(S.n)
        if S.n > MAXC: dims.append(None); continue
        H = homology_bigraded(Complex(S, deform=False))
        dims.append(sum(H.values()))
    prod = None if None in dims else dims[0] * dims[1]
    flag = ''
    if prod is not None and dimN is not None:
        flag = 'OK' if dimN >= prod and (dimN - prod) % 2 == 0 else 'VIOLATION'
        if dimN == prod: flag += ' (equality)'
    print('%-8s crossings %2d  strands: %s crossings, dim Kh~ = %s  product %s   dim N = %s   %s' % (name, D.n, ncs, dims, prod, dimN, flag), flush=True)
    out.append((name, D.n, ncs, dims, prod, dimN))
json.dump(out, open('strands_table.json', 'w'))
kn = [o for o in out if o[4] is not None and o[5] is not None]
print('computed', len(kn), 'of', len(out))
print('both strands unknotted:', sum(1 for o in kn if o[4] == 1), ';  product > 1:', sum(1 for o in kn if o[4] > 1), ';  equality dim N = product:', sum(1 for o in kn if o[4] == o[5]), ';  violations:', sum(1 for o in kn if o[5] < o[4]))
