"""Referee P4b: Theorem V on the 24 FRESH boxes (r1_boxes.json) and new odd a; identity box vs J_3(T(2,a));
pretzels P(p,q,p) vertical at new (p,q); two inversions of P(p,q,p) (q even): J differ?"""
import json, sys, random
from rlib import *
from j3lib import J3, inv
Phi3 = P((1, 0), (1, 1), (1, 2)); Phi5 = P((1, 0), (1, 1), (1, 2), (1, 3), (1, 4))

def Vword(B, a):
    lt = 'x2' if a > 0 else 'y2'
    toks = ['s', 'l1'] + ([t for t in B.split('.') if t] if B else []) + [lt] * abs(a) + ['u1']
    return '.'.join(toks)

def thmV(A, Bc, a):
    s = (-1) ** (a % 2)
    F = add(mul(mono(1), A), mul(mono(a, s), add(mul(P((1, 0), (1, 2)), A), mul(mono(1), Bc))), mul(mono(3 * a - 1), mul(Phi5, Bc)))
    q = pdiv(F, Phi3)
    return None if q is None else normalize(q)

boxes = [(B, [dict(v[0]), dict(v[1])]) for B, v in json.load(open('r1_boxes.json'))]
boxes = [(B, [{int(e): c for e, c in v[0].items()}, {int(e): c for e, c in v[1].items()}]) for B, v in boxes]
ok = tot = 0; fails = []
rnd = random.Random(55)
for B, v in boxes:
    for a in rnd.sample([1, -1, 3, -3, 5, -5, 7, 9, -7, -9, 11], 4):
        w = Vword(B, a)
        Jw = J(w)
        if Jw is None:
            fails.append((B, a, 'not knot')); continue
        tot += 1
        pr = thmV(a_of(v), b_of(v), a)
        if pr == Jw:
            ok += 1
        else:
            fails.append((B, a))
print('Theorem V on fresh boxes: %d/%d' % (ok, tot), fails[:4])
# identity box: Theorem V with A = B = 1, J of word, and independent J_3(T(2,a))
for a in [3, 5, 7, 9, 11, -3, -5, -7]:
    w = Vword('', a)
    Jw = J(w); j3 = J3(w); pr = thmV(ONE, ONE, a)
    print('a=%3d  J(word)==ThmV(1,1): %s  J(word)==J3(T(2,a)) [indep 2-cable]: %s' % (a, Jw == pr, Jw == j3))
# pretzels P(p,q,p) vertical: VP(p,q) = s.l1.(x0)^q.(x2)^p.u1 ; A = 1, B = t^(3q)
ok = tot = 0; fails = []
for p in [11, -11, 13, 3, -3]:
    for q in [-9, -8, 8, 9, 10, -10, 1, -1]:
        body = '.'.join((['x0'] * q) if q > 0 else (['y0'] * (-q)))
        w = Vword(body, p)
        Jw = J(w)
        if Jw is None:
            continue
        tot += 1
        pr = thmV(ONE, mono(3 * q), p)
        if pr == Jw:
            ok += 1
        else:
            fails.append((p, q))
print('pretzel vertical (new p,q): %d/%d' % (ok, tot), fails[:5])
# two inversions of P(p,q,p), q even: horizontal = mont(-q/2,[p,p]) (necklace), vertical = VP(p,q)
from words import mont
same = diff = 0; a2ok = 0; cnt = 0; rows = []
for p in [3, 5, -3, -5, 7, 9]:
    for q in [2, -2, 4, -4, 6, -6, 8]:
        h = J(mont(-q // 2, [p, p]))
        body = '.'.join((['x0'] * q) if q > 0 else (['y0'] * (-q)))
        vv = J(Vword(body, p))
        if h is None or vv is None:
            continue
        cnt += 1
        eq = (vv == h or vv == {-e: c for e, c in h.items()})
        same += eq; diff += (not eq)
        a2ok += (a2(h) == a2(vv))
        if eq:
            rows.append((p, q))
print('P(p,q,p) q even: %d pairs, J equal (up to mirror) in %d: %s ; differ in %d ; a2 equal in %d' % (cnt, same, rows, diff, a2ok))
