import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import pd as PDm, rules, kauffman
rnd = random.Random(11); tested = 0; bad = 0; r3s = 0; agree = 0
while tested < 120:
    n = rnd.randint(3, 7)
    W = [rnd.choice(list(rules.CODE)) for _ in range(n)]
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    q = PDm.PD.from_halfword(hw)
    if q is None or q.n() > 12 or q.n() < 3: continue
    b0 = PDm.unit_normal(PDm.bracket_statesum(q))
    kb = PDm.unit_normal(kauffman.bracket(hw))
    if b0 == kb: agree += 1
    else: print('PD vs kauffman disagree', hw)
    for step in range(10):
        tris = [f for f in q.triangles() if q.r3_data(f) is not None]
        if not tris: break
        q.apply_R3(rnd.choice(tris)); r3s += 1
        if PDm.unit_normal(PDm.bracket_statesum(q)) != b0: bad += 1; print('BAD after R3', hw); break
    tested += 1
print('tested', tested, 'PD bracket == kauffman.bracket', agree, 'R3 moves', r3s, 'bad', bad)
