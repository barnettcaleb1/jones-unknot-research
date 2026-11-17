"""splitlink_test.py -- after the F1/F2 fix, diagram.pd_from_halfword must return None EXACTLY when alex.diagram does
(knot test of the checker), on random words of the project grammar including mid-word caps/cups (split links occur).
usage: splitlink_test.py SEED COUNT OUT.json"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import diagram, replay, certify
import importlib.util
_spec = importlib.util.spec_from_file_location('diagram_old', '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/diagram.py')
diagram_old = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(diagram_old)     # UNFIXED builder version (read-only)
seed, count, outp = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
rng = random.Random(seed)
def rand_word():
    hw = 1; toks = []
    for _ in range(rng.randint(2, 14)):
        ops = ['x', 'y']
        if hw < 4: ops += ['l', 'r']
        if hw > 1: ops += ['u']
        c = rng.choice(ops)
        if c in 'xy': toks.append('%s%d' % (c, rng.randint(0, hw)))
        elif c in 'lr': toks.append('%s%d' % (c, rng.randint(1, hw))); hw += 2
        else: toks.append('u%d' % rng.randint(1, hw - 1)); hw -= 2
    while hw > 1: toks.append('u%d' % rng.randint(1, hw - 1)); hw -= 2
    return 's.' + '.'.join(toks)
stats = {'words': 0, 'both_knot': 0, 'both_none': 0, 'MISMATCH': 0, 'split_links_now_NOT_A_KNOT': 0}
mism = []
for _ in range(count):
    w = rand_word(); stats['words'] += 1
    a = replay.knot_crossings(w); p = diagram.pd_from_halfword(w)
    po = diagram_old.pd_from_halfword(w)
    if a is None and po is not None: stats['old_code_accepted_non_knot'] = stats.get('old_code_accepted_non_knot', 0) + 1
    if (a is None) != (p is None):
        stats['MISMATCH'] += 1; mism.append(w)
    elif a is None: stats['both_none'] += 1
    else: stats['both_knot'] += 1
for w in ['s.l1.y0.u1', 's.r1.x1.x0.x1.u1', 's.l1.x1.y0.u1', 's.l1.l1.x1.y0.u1.u1']:
    st, info = certify.certify(w, write_hits=False)
    stats['split_links_now_NOT_A_KNOT'] += (st == 'NOT_A_KNOT')
stats['mismatch_examples'] = mism[:10]
print(json.dumps(stats)); json.dump(stats, open(outp, 'w'), indent=1)
