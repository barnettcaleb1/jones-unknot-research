"""AUDIT-1 test 8: the certifier's PD-based Wirtinger presentation (wirtinger.wirtinger(diagram.pd_from_halfword(w)))
vs the checker's (replay.wirtinger_presentation(w)) after the checker's normal form: literal equality (needed only for
the success rate: a mismatch makes the replay reject).  Also diagram.check_pd on every knot."""
import sys, random, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import audlib, replay, diagram, wirtinger
rnd = random.Random(23); n = 0; eq = 0; chk = 0; bad = []
seen = set()
while n < 1500:
    w = audlib.rand_halfword(rnd, rnd.randint(1, 16), maxhw=rnd.choice([3, 5, 7, 9]))
    if w in seen or not audlib.is_knot(w): continue
    seen.add(w); n += 1
    pd = diagram.pd_from_halfword(w)
    chk += diagram.check_pd(pd)
    a = replay.normal_form(*wirtinger.wirtinger(pd)); b = replay.normal_form(*replay.wirtinger_presentation(w))
    if a == b: eq += 1
    else: bad.append(w)
print(json.dumps({'knots': n, 'check_pd_ok': chk, 'literal_equal': eq, 'bad': bad[:5]}))
