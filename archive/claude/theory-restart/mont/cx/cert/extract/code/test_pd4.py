"""Larger R3 validation: random diagrams with 8-13 crossings, 15 random valid R3 moves each (no removals), bracket
(state sum) compared after EVERY move; plus PD bracket == mirror(kauffman.bracket) at the start."""
import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import pd as PDm, rules, kauffman
rnd = random.Random(99); diagrams = 0; moves = 0; bad = 0
while diagrams < 80:
    W = [rnd.choice(list(rules.CODE)) for _ in range(rnd.randint(5, 9))]
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    q = PDm.PD.from_halfword(hw)
    if q is None or not (8 <= q.n() <= 13): continue
    b0 = PDm.unit_normal(PDm.bracket_statesum(q))
    kb = kauffman.bracket(hw); assert b0 == PDm.unit_normal({-e: c for e, c in kb.items()})
    diagrams += 1
    for _ in range(15):
        tris = [f for f in q.triangles() if q.r3_data(f) is not None]
        if not tris: break
        q.apply_R3(rnd.choice(tris)); moves += 1
        if PDm.unit_normal(PDm.bracket_statesum(q)) != b0: bad += 1; print('BAD', hw); break
print('diagrams', diagrams, 'R3 moves', moves, 'bracket changes', bad)
