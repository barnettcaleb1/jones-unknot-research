import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import fgroup, rules
from scalars import apply_vec, apply_covec, proportional, f0, PH
bad = 0
for nm, l, r in rules.LP:
    if fgroup.group_key([rules.NAME[x] for x in l]) != fgroup.group_key([rules.NAME[x] for x in r]): bad += 1; print('BAD', nm, l, r)
print('group rules', len(rules.LP), 'bad', bad)
for p, why in rules.TOPPAT:
    W = [rules.NAME[x] for x in p]; print('TOP', '.'.join(W), proportional(apply_vec(W, f0), f0), why)
for p, why in rules.BOTPAT:
    W = [rules.NAME[x] for x in p]; print('BOT', '.'.join(W), proportional(apply_covec(W, PH), PH), why)
