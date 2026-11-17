"""transplant_test.py -- every Tietze certificate of an unknot from suite A1 (run/out/validation/suiteA1.jsonl) re-labelled with
the halfwords of up to 3 NONTRIVIAL knots of the same crossing number from suite (b) (run/out/validation/suiteB_*.jsonl):
the FIXED checker must reject all of them.  usage: transplant_test.py OUT.json"""
import sys, os, json, glob, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import replay
V = os.path.join(os.path.dirname(HERE), 'out', 'validation')
unk = []
for line in open(os.path.join(V, 'suiteA1.jsonl')):
    r = json.loads(line)
    for c in r['cert']['certificates']:
        if c['kind'] == 'tietze': unk.append((r['n'], c))
nontriv = {}
for f in glob.glob(os.path.join(V, 'suiteB_*.jsonl')):
    for line in open(f):
        r = json.loads(line)
        if r['status'] in ('CERTIFIED_NONTRIVIAL',): nontriv.setdefault(r['n'], []).append(r['w'])
rng = random.Random(3); tried = 0; accepted = []
for n, c in unk:
    for w in rng.sample(nontriv.get(n, []), min(3, len(nontriv.get(n, [])))):
        tried += 1
        ok, msg = replay.check(dict(c, halfword=w))
        if ok: accepted.append((w, c['halfword']))
summ = {'unknot_certs': len(unk), 'transplants_tried': tried, 'ACCEPTED': len(accepted), 'examples': accepted[:5]}
print(json.dumps(summ)); json.dump(summ, open(sys.argv[1], 'w'), indent=1)
