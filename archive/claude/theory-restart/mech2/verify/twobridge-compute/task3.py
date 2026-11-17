#!/usr/bin/env python3
"""TASK 3: run kht++ (quotient mode) on NEW two-letter half-diagram words and compare with the matrix formula.
usage: task3.py word1 word2 ...   (words in the letters X,Y,x,y; optional prefix 'r:' for the cap r1)
Each run: cwd = khtwork/, file examples/mine/<name>.kht, time limit via perl alarm, stdin closed.
J is read (i) directly from the b-generators of the BN~ chain file, (ii) from the Kh~ components by the rule."""
import json, os, subprocess, sys, time
from reflib import *
from chainparse import *
K = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.join(HERE, 'khtwork')
LET = {'Y': 'y0', 'y': 'x0', 'X': 'x1', 'x': 'y1'}
base = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
def saved_words():
    s = set()
    for d in [base + 'k138/examples/si/', base + 'tilt/examples/strong_inversions/2-bridge_knots/']:
        for f in os.listdir(d):
            if f.endswith('.kht'):
                s.add(open(d + f).read().split('\n')[1].strip())
    try:
        c = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/twobridge/work/cache.json'))
        lens = set(k.split('|')[0] for k in c)
    except Exception:
        lens = set()
    return s, lens
def run(spec, timeout=300):
    cap = 'l1'
    w = spec
    if ':' in spec:
        c, w = spec.split(':'); cap = c + '1'
    half = 's.' + cap + '.' + '.'.join(LET[L] for L in w) + '.u2'
    name = ('r_' if cap == 'r1' else 'l_') + ''.join({'X': 'X', 'Y': 'Y', 'x': 'a', 'y': 'b'}[L] for L in w)
    os.makedirs(os.path.join(W, 'examples', 'mine'), exist_ok=True)
    f = 'examples/mine/%s.kht' % name
    open(os.path.join(W, f), 'w').write('%% %s  (%s)\n%s\n,1\n' % (name, w, half))
    t0 = time.time()
    cmd = ['perl', '-e', 'alarm %d; exec @ARGV' % timeout, K, '-c2', '-q', '-s', f]
    r = subprocess.run(cmd, cwd=W, stdin=subprocess.DEVNULL, capture_output=True, text=True)
    dt = time.time() - t0
    d = os.path.join(W, 'examples', 'mine', name)
    rec = {'spec': spec, 'word': w, 'half': half, 'name': name, 'time': round(dt, 1), 'rc': r.returncode}
    pb = os.path.join(d, 'cxBNr-c2-qs'); pk = os.path.join(d, 'cxKhr-c2-qs')
    if not (os.path.exists(pb) and os.path.exists(pk)):
        rec['error'] = 'no output (rc %s): %s' % (r.returncode, (r.stdout + r.stderr)[-200:])
        return rec
    bn = parse_file(pb); kh = parse_file(pk)
    Jbn = J_from_BN(bn)
    rec['nb'] = sum(1 for c in bn for g in c['gens'] if g[0] == 'b')
    rec['bn_components'] = len(bn); rec['kh_components'] = [(c.get('type'), c.get('len'), c.get('slope')) for c in kh]
    jr = J_from_khr([{k: c[k] for k in ('type', 'len', 'slope', 'q', 'delta')} for c in kh])
    Jm = J_matrix(w)
    Jb = A_to_t(J_bracket(half_letters(half))[0])
    rec['J_BN'] = pstr(Jbn); rec['J_matrix'] = pstr(Jm)
    rec['BN==matrix'] = pnorm(Jbn) == pnorm(Jm)
    rec['BN==matrix after mirror only'] = (pnorm(Jbn) != pnorm(Jm)) and pnorm(Jbn) == pnorm(pflip(Jm))
    rec['rule==BN exactly'] = (jr is not None and jr[2] == Jbn)
    rec['bracket==matrix'] = pnorm(Jb) == pnorm(Jm)
    rec['norm'] = list(pnorm(Jm))
    return rec
if __name__ == '__main__':
    saved, lens = saved_words()
    out = open(os.path.join(HERE, 'task3_runs.jsonl'), 'a')
    for spec in sys.argv[1:]:
        cap = 'l1'; w = spec
        if ':' in spec: cap = spec.split(':')[0] + '1'; w = spec.split(':')[1]
        mid = '.'.join(LET[L] for L in w)
        new = all(('s.%s.%s.u2' % (c, mid)) not in saved and ('s.%s.%s.u2' % (c, mid)) not in lens for c in ('l1', 'r1'))
        rec = run(spec)
        rec['new'] = new
        out.write(json.dumps(rec, ensure_ascii=False) + '\n'); out.flush()
        print(json.dumps(rec, ensure_ascii=False), flush=True)
