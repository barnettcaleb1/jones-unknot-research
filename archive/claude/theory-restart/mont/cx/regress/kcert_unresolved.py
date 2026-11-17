"""kcert (V_K mod p, det, |Delta(2)|, |Delta(3)|) on every base knot with > 24 crossings (all types incl. R): any V_K != 1 or
Delta != 1 on a unit line would be a HIT candidate (J = 1 exactly on these lines)."""
import sys, pickle, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import kcert
from collections import Counter
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
big = pickle.load(open(OUT + 'big_bases.pkl', 'rb'))
words = sorted(set(w for D in big for w in big[D]))
st = Counter(); bad = []
for W in words:
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    s, why = kcert.certify(hw)
    st[s] += 1
    if s != 'V=1,Delta=1': bad.append((hw, s, why))
print(dict(st)); print(bad[:10])
json.dump({'stats': dict(st), 'bad': bad}, open(OUT + 'kcert_unresolved.json', 'w'))
