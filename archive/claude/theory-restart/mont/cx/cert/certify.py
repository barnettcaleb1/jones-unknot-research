#!/usr/bin/env python3
"""certify.py -- SOUND certifier for the covering knot K of a halfword s.P.W.S (cx lane, Claude, 17 Nov 2026).

API:   certify(halfword, **opts) -> (status, certificate)
CLI:   certify.py [--json] [--tietze-budget S] [--rep-budget S] HALFWORD [HALFWORD ...]

status in {'CERTIFIED_UNKNOT', 'CERTIFIED_NONTRIVIAL', 'UNRESOLVED', 'NOT_A_KNOT', 'COUNTEREXAMPLE'}:
  CERTIFIED_UNKNOT      a certificate accepted by the independent checker replay.py of one of the kinds
                        'tietze'  (pi_1 Wirtinger presentation -> <a | > by replayed Tietze moves; Dehn's lemma),
                        'jones24' (the Morse diagram of K has <= 24 crossings and V_K = 1; Tuzun-Sikora),
                        'unknot0' (crossing-free diagram);
  CERTIFIED_NONTRIVIAL  a 'rep' certificate: permutation images of ALL Wirtinger generators, every relator checked,
                        two images that do not commute (replay.py);
  COUNTEREXAMPLE        CERTIFIED_NONTRIVIAL and V_K = 1 (a nontrivial knot with trivial Jones polynomial): the HIT
                        file collab/HIT-<HHMM>.md is written immediately (BRIEF section 5);
  UNRESOLVED            nothing certified (retained; never to be called an unknot).
The certificate dict always carries 'halfword', 'crossings', 'V_K' (from the PD code), 'Delta', and the list
'certificates' of checker-accepted certificates (each re-checked by replay.check before it is returned).
V_K != 1 is recorded but is NOT used as a certificate of nontriviality (task standard: only explicit homomorphisms).
"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path: sys.path.insert(0, HERE)
import diagram, wirtinger, tietze, reps, replay

HIT_DIR = '/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/collab'


def _poly_str(p):
    if isinstance(p, dict): items = sorted(p.items())
    else: items = list(p)
    return ' '.join('%+d*t^%d' % (c, e) for e, c in items) or '0'


def write_hit(halfword, V, A, rep_cert, note=''):
    hhmm = time.strftime('%H%M')
    path = os.path.join(HIT_DIR, 'HIT-%s.md' % hhmm)
    k = 0
    while os.path.exists(path):
        k += 1; path = os.path.join(HIT_DIR, 'HIT-%s-%d.md' % (hhmm, k))
    with open(path, 'w') as f:
        f.write('# HIT (cert lane, certify.py): nontrivial knot K with V_K = 1\n')
        f.write('halfword: %s\nV_K: %s\nDelta_K: %s\nmethod: %s\n%s\n' % (halfword, _poly_str(V), _poly_str(A), rep_cert.get('group'), note))
        f.write('certificate (replay.py kind rep):\n```\n%s\n```\n' % json.dumps(rep_cert))
    return path


def certify(halfword, tietze_budget=None, rep_budget=30.0, seed=0, want_all=False, write_hits=True, blind=False):
    """Returns (status, certificate).  The Tietze route is attempted when V_K = 1 (default budget 30 s) and, with
    blind=True, also when V_K != 1 (default budget 3 s; used by the soundness suite (b)).  Representations are searched
    when no unknot certificate was found (default budget 30 s)."""
    t0 = time.time()
    info = {'halfword': halfword, 'certificates': [], 'notes': []}
    pd = diagram.pd_from_halfword(halfword)
    if pd is None:
        return 'NOT_A_KNOT', info
    info['crossings'] = pd.n
    if not diagram.check_pd(pd):
        info['notes'].append('PD self-check failed')
        return 'UNRESOLVED', info
    V = diagram.jones(pd)
    info['V_K'] = sorted(V.items()); info['Delta'] = None     # Delta is computed only when the rep search needs it
    v_trivial = (V == {0: 1})
    unknot_cert = None

    def accept(cert):
        ok, msg = replay.check(cert)
        if ok:
            cert['checker'] = msg; info['certificates'].append(cert)
        else:
            info['notes'].append('certificate REJECTED by checker: %s (%s)' % (cert.get('kind'), msg))
        return ok

    # route (c0): no crossings
    if pd.n == 0:
        if accept({'kind': 'unknot0', 'halfword': halfword}):
            info['secs'] = round(time.time() - t0, 3)
            return 'CERTIFIED_UNKNOT', info
    # route (b): Tietze on the Wirtinger presentation.  Attempted when V_K = 1 (the only case where it can succeed),
    # and ALWAYS when blind=True (soundness test suites: the simplifier must then fail on every nontrivial knot).
    gens, rels = wirtinger.wirtinger(pd)
    if v_trivial or blind:
        tb = tietze_budget if tietze_budget is not None else (30.0 if (v_trivial and not blind) else 3.0)
        ok, moves, fin, st = tietze.simplify(gens, rels, seed=seed, time_budget=tb)
        info['tietze'] = {'success': ok, 'attempts': st['attempts'],
                          'final_gens': len(fin[0]) if fin else None, 'final_rels': len(fin[1]) if fin else None,
                          'final_len': tietze.total_len(fin[1]) if fin else None}
        if ok:
            c = {'kind': 'tietze', 'halfword': halfword, 'moves': [list(m) for m in moves]}
            if accept(c): unknot_cert = c
    # route (a): <= 24 crossings and V_K = 1
    if (unknot_cert is None or want_all) and pd.n <= 24 and v_trivial:
        c = {'kind': 'jones24', 'halfword': halfword}
        if accept(c) and unknot_cert is None: unknot_cert = c
    if unknot_cert is not None:
        info['secs'] = round(time.time() - t0, 3)
        return 'CERTIFIED_UNKNOT', info
    # representations (needs Delta for the affine search)
    A = diagram.alexander(pd)
    info['Delta'] = list(A)
    r = reps.find_rep(gens, rels, A, time_budget=rep_budget)
    if r is not None:
        img, gname, note = r
        pair = reps.noncommuting_pair(img, gens)
        if pair is not None:
            c = {'kind': 'rep', 'halfword': halfword, 'group': gname, 'note': note,
                 'degree': len(next(iter(img.values()))), 'images': {str(k): list(v) for k, v in img.items()},
                 'noncommuting': list(pair)}
            if accept(c):
                info['secs'] = round(time.time() - t0, 3)
                if v_trivial and replay.VK_project(halfword) != {0: 1}:
                    info['notes'].append('PD bracket says V_K = 1 but the project bracket disagrees: BUG, no HIT written')
                    return 'UNRESOLVED', info
                if v_trivial:
                    info['notes'].append('NONTRIVIAL KNOT WITH V_K = 1 (V_K = 1 confirmed by the project bracket kauffman.py)')
                    if write_hits:
                        info['hit_file'] = write_hit(halfword, V, A, c, 'certify.py, %s' % note)
                    return 'COUNTEREXAMPLE', info
                return 'CERTIFIED_NONTRIVIAL', info
    info['secs'] = round(time.time() - t0, 3)
    if not v_trivial: info['notes'].append('V_K != 1 (K is not the unknot by the Jones polynomial; no rep found)')
    return 'UNRESOLVED', info


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description='certify the covering knot K of halfwords')
    ap.add_argument('words', nargs='+')
    ap.add_argument('--json', action='store_true', help='print full certificates as JSON')
    ap.add_argument('--tietze-budget', type=float, default=None)
    ap.add_argument('--rep-budget', type=float, default=30.0)
    ap.add_argument('--no-hit-file', action='store_true')
    a = ap.parse_args(argv)
    for w in a.words:
        st, cert = certify(w, tietze_budget=a.tietze_budget, rep_budget=a.rep_budget, write_hits=not a.no_hit_file)
        if a.json:
            print(json.dumps({'status': st, 'certificate': cert}))
        else:
            kinds = [c['kind'] + (':' + c['group'] if c['kind'] == 'rep' else '') for c in cert['certificates']]
            print('%s\t%s\tcrossings=%s\tV_K=1:%s\t%s\t%s s' % (st, w, cert.get('crossings'), cert.get('V_K') == [(0, 1)],
                                                         ','.join(kinds) or '-', cert.get('secs')))


if __name__ == '__main__':
    main(sys.argv[1:])
