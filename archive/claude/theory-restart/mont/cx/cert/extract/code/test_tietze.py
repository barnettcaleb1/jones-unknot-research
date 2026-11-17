import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import tietze, alex, rules
rnd = random.Random(3); ok = 0; n = 0
while n < 60:
    W = [rnd.choice(list(rules.CODE)) for _ in range(rnd.randint(3, 9))]
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    if alex.alex_eval(hw, -1) is None: continue
    n += 1
    a = [alex.alex_eval(hw, t) for t in (-1, 2, 3)]
    b = []
    for t in (-1, 2, 3):
        v = tietze.fox_alexander(hw, t)
        v = int(v) if v.denominator == 1 else v
        b.append(alex.strip(v, t) if isinstance(v, int) else v)
    ok += (a == b)
    if a != b: print('MISMATCH', hw, a, b)
print('Fox vs alex (det, |D(2)|, |D(3)|):', ok, '/', n)
