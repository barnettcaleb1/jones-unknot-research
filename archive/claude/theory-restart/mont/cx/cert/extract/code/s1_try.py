import sys, json, time, random
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import rules, reduce as R
d = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s1_rehits_d8_s11.json'))
reh = d['rehits']
rnd = random.Random(1); sample = rnd.sample(reh, 3000)
t0 = time.time(); hist = Counter(); left = []
for dep, u1, u2 in sample:
    w = rules.inv(rules.enc(u1)) + rules.enc(u2)
    r, m = R.reduce_word(w, budget=3000)
    hist[(len(r) == 0, rules.crossings(r) <= 24)] += 1
    if r: left.append((u1, u2, rules.dec(r)))
print(hist, round(time.time() - t0, 1))
for x in left[:30]: print(x)
