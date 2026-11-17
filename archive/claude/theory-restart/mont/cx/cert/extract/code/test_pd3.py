import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import pd as PDm, rules, kauffman
rnd = random.Random(12); tested = 0; agree_mirror = 0; agree_direct = 0; chiral = 0
while tested < 300:
    W = [rnd.choice(list(rules.CODE)) for _ in range(rnd.randint(3, 8))]
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    q = PDm.PD.from_halfword(hw)
    if q is None or q.n() > 13 or q.n() < 3: continue
    a = PDm.unit_normal(PDm.bracket_statesum(q)); kb = kauffman.bracket(hw)
    m = PDm.unit_normal({-e: c for e, c in kb.items()}); d = PDm.unit_normal(kb)
    agree_mirror += (a == m); agree_direct += (a == d); chiral += (m != d); tested += 1
print('tested', tested, 'PD == mirror(kauffman)', agree_mirror, 'PD == kauffman', agree_direct, 'chiral brackets', chiral)
