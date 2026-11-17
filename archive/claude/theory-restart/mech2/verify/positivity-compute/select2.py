#!/usr/bin/env python3
"""Pick a stratified random sample of NEW one-sign three-strand words from the exhaustive lists (fixed seed)."""
import sys, os, json, random, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import khtorient, sidiag as S
SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/'
table = set()
for p in glob.glob(SI + '*.kht'):
    for line in open(p):
        line = line.strip()
        if line.startswith('s.'):
            table.add(line.replace('.r', '.l')); break
random.seed(int(sys.argv[1]))
files = sys.argv[3:]
per = int(sys.argv[2])
recs = []
for f in files:
    for l in open(f):
        recs.append(json.loads(l))
cats = collections.defaultdict(list)
for r in recs:
    if r['w'].replace('.r', '.l') in table:
        continue
    uses2 = ('x2' in r['w'] or 'y2' in r['w'])
    if r['gD'] == 0:
        cats[(r['c'], 'unknot')].append(r); continue
    sign = 'neg' if r['sign'] < 0 else 'pos'
    if r['ca'] == 0:
        cats[(r['c'], 'swap', sign)].append(r)
    else:
        cats[(r['c'], sign, 'adequate' if r['E'] == 1 else 'nonadequate', 'loops' if r['l'] > 0 else 'noloops', 'pos2' if uses2 else 'nopos2')].append(r)
out = []
seen_alex = collections.Counter()
for key in sorted(cats, key=str):
    lst = cats[key]
    random.shuffle(lst)
    n = per if key[1] != 'unknot' else 1
    # prefer Alexander polynomials not used yet
    lst.sort(key=lambda r: seen_alex[tuple(r['ap'])])
    for r in lst[:n]:
        fx = khtorient.fix_letters(r['w'])
        assert fx is not None and fx[1] == r['wr'], (r['w'], fx)
        seen_alex[tuple(r['ap'])] += 1
        out.append((fx[0], 'c%d|%s|g%d|E%d|l%d|ax%d' % (r['c'], '|'.join(str(k) for k in key[1:]), r['gD'], r['E'], r['l'], r['ca'])))
for w, tag in out:
    print(w + '\t' + tag)
