import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/fukaya/scratch')
from typed import *

print("== V1: Cone_H(R_m) ~ q^-1 h^-1 s_{2m}(inf)  (source b of R at (0,0); special's source b at (-1,-1))")
for m in range(1, 7):
    R = row(m); C = cone_H(R); S = special(m).shift(-1, -1)
    ok, f = is_isomorphic(C, S)
    print(f"  m={m}: |Cone|={len(C)} |s|={len(S)} isomorphic={ok}")

print("== V1b: H.1 is null-homotopic on s_{2m}(inf):  Cone_H(S) ~ q^-1h^-1 S (+) q S")
for m in range(1, 5):
    S = special(m); C = cone_H(S)
    T = dsum('split', S.shift(-1, -1), S.shift(1, 0))
    ok, f = is_isomorphic(C, T)
    print(f"  m={m}: isomorphic={ok}")

print("== V2: hook splitting  Cone_H(R <-D- a(k))  ~  Cone_H(R) (+) Cone_H(a(k))  [tail b --D--> sink of R], k<=0")
def hookE(k, w, m=2, npow=1):
    """family E: rows R_1..R_w (hooks R_i.sink <-D- R_{i+1}.source), tail a(k) with tail.b --D^npow--> R_w.sink.
    Returns (TypeD, list of row source indices, tail b index). R_1.source at (0,0)."""
    idem = []; arrows = []
    rows = []
    L = 2 * m + 2
    for i in range(w):
        o = len(idem)
        R = row(m)
        idem += R.idem; arrows += [(x + o, y + o, a) for (x, y, a) in R.arrows]
        rows.append(o)
        if i > 0: arrows.append((o, o - 1, 'D'))        # R_{i+1}.source -> R_i.sink
    o = len(idem)
    A = arc(k)
    idem += A.idem; arrows += [(x + o, y + o, a) for (x, y, a) in A.arrows]
    if w > 0: arrows.append((o, o - 1, 'D' + (str(npow) if npow > 1 else '')))
    X = TypeD(f'E(k={k},w={w})', idem, arrows, base=0)
    return X, rows, o
def famV(k, w, m=2):
    """family V: tail a(k) receives: R_1.source --D--> tail.b ; R_{i+1}.source --D--> R_i.sink. tail.b at (0,0)."""
    A = arc(k)
    idem = list(A.idem); arrows = list(A.arrows)
    rows = []
    for i in range(w):
        o = len(idem)
        R = row(m)
        idem += R.idem; arrows += [(x + o, y + o, a) for (x, y, a) in R.arrows]
        rows.append(o)
        if i == 0: arrows.append((o, 0, 'D'))
        else: arrows.append((o, o - 1, 'D'))
    X = TypeD(f'V(k={k},w={w})', idem, arrows, base=0)
    return X, rows, 0

for k in (0, -4, -8):
    for w in (1, 2, 3):
        X, rows, tb = hookE(k, w)
        C = cone_H(X)
        parts = [cone_H(row(2).shift(X.q[r], X.h[r])) for r in rows] + [cone_H(arc(k).shift(X.q[tb], X.h[tb]))]
        T = dsum('split', *parts)
        ok, f = is_isomorphic(C, T)
        print(f"  E k={k} w={w}: gens {len(C)}; split iso = {ok}; row sources at", [(X.q[r], X.h[r]) for r in rows], 'tail b at', (X.q[tb], X.h[tb]))
print("== V2': families with bend at the tail: is Cone_H still split into rows + tail?")
for (fam, k) in (('E', 4), ('E', 8), ('V', -4), ('V', -8), ('V', 0), ('V', 4)):
    for w in (1, 2):
        X, rows, tb = (hookE(k, w) if fam == 'E' else famV(k, w))
        C = cone_H(X)
        parts = [cone_H(row(2).shift(X.q[r], X.h[r])) for r in rows] + [cone_H(arc(k).shift(X.q[tb], X.h[tb]))]
        T = dsum('split', *parts)
        ok, f = is_isomorphic(C, T)
        print(f"  {fam} k={k} w={w}: split iso = {ok}; row sources", [(X.q[r], X.h[r]) for r in rows], 'tail b', (X.q[tb], X.h[tb]))
print("== V2'': junction D^2 (as in 9_46 second inversion) still splits")
X, rows, tb = hookE(-4, 1, npow=2)
C = cone_H(X); T = dsum('split', cone_H(row(2).shift(X.q[rows[0]], X.h[rows[0]])), cone_H(arc(-4).shift(X.q[tb], X.h[tb])))
print('  ', is_isomorphic(C, T)[0], 'tail b at', (X.q[tb], X.h[tb]))
