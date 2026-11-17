"""make_full_words.py -- word lists of the COMPLETE sets S1, S2, S3a, S3b (not only the residues), from the extract lane's
regenerated data (cert/extract/data, read-only; regenerated from engineB's own scripts with counts identical to engineB):
  S1  : data/s1_rehits_d8_s11.json  (76,584 re-hits [depth, U1, U2]) -> s.l1.l1.freered(U1^-1 U2).u2.u2
  S2  : data/s2_survivors_7_7.json  (685,359 zeta_7 & zeta_10 survivors (V, U)) -> distinct s.l1.l1.V.U.u2.u2 (633,532 words;
        633,260 of them have J = 1 exactly per the extract lane; the others are zeta false positives, certified anyway)
  S3a : data/s3a_items.json (154,869 J = 1 window theta-curves) -> distinct s.l1.l1.W.u2.u2
  S3b : data/s3b_items.json (36,830 knots on unit lines) -> distinct s.l1.l1.W.u2.u2
Output: out/full/words_{S1,S2,S3a,S3b}.json = [[tag, halfword], ...] with tag = number of configurations behind the word."""
import json, os
from collections import Counter
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data'
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/out/full'
NAME = {1: 'x0', -1: 'y0', 2: 'x1', -2: 'y1', 3: 'x2', -3: 'y2', 4: 'x3', -4: 'y3'}
CODE = {v: k for k, v in NAME.items()}
def enc(s): return tuple(CODE[x] for x in s.split('.') if x)
def dec(w): return '.'.join(NAME[a] for a in w)
def inv(w): return tuple(-a for a in reversed(w))
def freered(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def hw(w): return 's.l1.l1.' + (dec(w) + '.' if w else '') + 'u2.u2'
def dump(name, cnt):
    items = [[c, w] for w, c in cnt.items()]
    json.dump(items, open(os.path.join(OUT, 'words_%s.json' % name), 'w'))
    print(name, 'configurations', sum(cnt.values()), 'distinct words', len(cnt))
d = json.load(open(os.path.join(D, 's1_rehits_d8_s11.json')))
c = Counter(hw(freered(inv(enc(u1)) + enc(u2))) for dep, u1, u2 in d['rehits']); dump('S1', c)
d = json.load(open(os.path.join(D, 's2_survivors_7_7.json')))
c = Counter(hw(enc(v) + enc(u)) for v, u in d['survivors']); dump('S2', c)
for name, f in (('S3a', 's3a_items.json'), ('S3b', 's3b_items.json')):
    d = json.load(open(os.path.join(D, f)))
    c = Counter(hw(enc(W)) for W, prov in d['items']); dump(name, c)
