import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import pd as PDm, rules
rnd = random.Random(7); tested = 0; bad = 0; r3s = 0
while tested < 150:
    n = rnd.randint(2, 7)
    W = [rnd.choice(list(rules.CODE)) for _ in range(n)]
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    q = PDm.PD.from_halfword(hw)
    if q is None or q.n() > 13 or q.n() == 0: continue
    b0 = PDm.unit_normal(PDm.bracket_statesum(q))
    # random R3 moves and R1/R2 removals, check the bracket after every move
    for step in range(6):
        tris = [f for f in q.triangles() if q.r3_data(f) is not None]
        if tris:
            q.apply_R3(rnd.choice(tris)); r3s += 1
            if PDm.unit_normal(PDm.bracket_statesum(q)) != b0: bad += 1; print('BAD after R3', hw); break
        c = q.find_R1()
        if c is not None:
            q.remove([c])
            if PDm.unit_normal(PDm.bracket_statesum(q)) != b0: bad += 1; print('BAD after R1', hw); break
        p = q.find_R2()
        if p is not None:
            q.remove(list(p))
            if PDm.unit_normal(PDm.bracket_statesum(q)) != b0: bad += 1; print('BAD after R2', hw); break
    tested += 1
print('tested', tested, 'R3 moves', r3s, 'bad', bad)
