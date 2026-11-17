"""gate_check.py -- the residue runs start only if the soundness-relevant validations of the FIXED code passed:
forgeries (0 holes, controls accepted), suite (a) all CERTIFIED_UNKNOT, suite (b) all CERTIFIED_NONTRIVIAL with 0 Tietze
successes in blind mode, transplant test 0 accepted.  Exit code 0 iff all passed."""
import json, os, sys
V = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/out/validation'
ok = True; msgs = []
f = json.load(open(os.path.join(V, 'forgeries.json')))['summary']
ok &= (f['HOLES'] == 0 and f['controls_rejected'] == 0); msgs.append(('forgeries', f))
for s, n in (('suiteA1', 1300), ('suiteA2top', 700), ('suiteA2bot', 700), ('suiteA2codex', 21)):
    d = json.load(open(os.path.join(V, s + '.summary.json')))
    good = d['status'] == {'CERTIFIED_UNKNOT': n}; ok &= good; msgs.append((s, d['status'], good))
for s, n in (('suiteB_alextriv', 144), ('suiteB_random', 900), ('suiteB_mirrors', 900)):
    d = json.load(open(os.path.join(V, s + '.summary.json')))
    good = d['status'] == {'CERTIFIED_NONTRIVIAL': n} and d['tietze_success'] == 0; ok &= good; msgs.append((s, d['status'], d['tietze_success'], good))
t = json.load(open(os.path.join(V, 'transplant.json')))
ok &= (t['ACCEPTED'] == 0 and t['transplants_tried'] > 1000); msgs.append(('transplant', t['transplants_tried'], t['ACCEPTED']))
for m in msgs: print(m)
print('GATE', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
