"""AUDIT-1 test 1: can replay.check be made to accept a 'rep' (CERTIFIED_NONTRIVIAL) certificate on an UNKNOT?
Attack: give every Wirtinger generator the identity permutation (trivially satisfies every relator), add two EXTRA
image keys that are not generators, and name them as the 'noncommuting' pair.  replay._check verifies the images of
the generators and every relator, but never checks that the noncommuting pair consists of generators."""
import sys, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import replay

UNKNOTS = ['s.l1.x1.u2',                                   # 2-crossing diagram of the unknot
           's.l1.l1.x2.x1.x1.x1.y3.y3.x1.u2.u2']           # Codex regression family m = 1 (certified unknot)
for w in UNKNOTS:
    gens, rels = replay.wirtinger_presentation(w)
    ok_t = replay.check({'kind': 'jones24', 'halfword': w})
    d = 3
    ident = list(range(d))
    images = {str(g): ident for g in gens}
    images['999'] = [1, 0, 2]          # NOT a generator
    images['998'] = [0, 2, 1]          # NOT a generator
    forged = {'kind': 'rep', 'halfword': w, 'group': 'S3 (forged)', 'degree': d, 'images': images,
              'noncommuting': [999, 998]}
    res = replay.check(forged)
    print(w, '| genuine jones24 cert:', ok_t, '| forged rep cert ->', res)
    # same forged certificate written to disk and re-checked through the CLI path (json round-trip)
    p = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work/forged_rep_%d.json' % len(gens)
    json.dump(forged, open(p, 'w'))
    print('   json round trip:', replay.check(json.load(open(p))))
    # control: noncommuting pair among real generators (all identity) must be rejected
    ctrl = dict(forged); ctrl['noncommuting'] = [gens[0], gens[1]]
    print('   control (real generators, identity images):', replay.check(ctrl))
