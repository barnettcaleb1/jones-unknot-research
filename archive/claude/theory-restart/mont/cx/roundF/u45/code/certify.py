#!/usr/bin/env python3
"""certify.py -- SOUND certifier for the covering knot K of a halfword s.P.W.S (cx lane, Claude, 17 Nov 2026).

API:   certify(halfword, **opts) -> (status, certificate)
CLI:   certify.py [--json] [--tietze-budget S] [--rep-budget S] HALFWORD [HALFWORD ...]

[cert/run copy with the audit fixes; see run/REPORT.md section 1]
status in {'CERTIFIED_UNKNOT', 'CERTIFIED_NONTRIVIAL', 'UNRESOLVED', 'NOT_A_KNOT', 'INVALID_WORD', 'COUNTEREXAMPLE'}:
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
# guard: the FIXED copies in run/code must be the ones imported (never cert/*.py)
for _m in (diagram, wirtinger, tietze, reps, replay):
    assert os.path.dirname(os.path.abspath(_m.__file__)) == HERE, 'wrong module imported: %s' % _m.__file__

HIT_DIR = '/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/collab'
ALARM_DIR = os.path.join(os.path.dirname(HERE), 'out')
EXACT_ALEX_MAX = 80          # exact Alexander polynomial only up to this many crossings (cert/run fix F3)


def _poly_str(p):
    if p is None: return 'None'
    if isinstance(p, dict): items = sorted(p.items())
    else: items = list(p)
    return ' '.join('%+d*t^%d' % (c, e) for e, c in items) or '0'


def _vk_project(halfword):
    """the project bracket (tools/kauffman.py, ident3 normalisation) as implemented in the checker"""
    return replay.VK_project(halfword)


def third_bracket_V(halfword):
    """Third, independent bracket (audit-2's own Morse-sweep implementation, copied to run/code/a2lib_indep.py),
    used only to reconcile a disagreement between the PD bracket and the project bracket.  Returns V dict or None."""
    try:
        import a2lib_indep as A
        br = A.bracket_full(A.full_of(halfword))
        return A.VK_from_bracket(br)
    except Exception:
        return None


def write_hit(halfword, V_pd, V_proj, V_third, A, rep_cert, note=''):
    """HIT file (BRIEF section 5): word, J (exact, lp.J), V_K (all brackets), Delta_K, method, certificate."""
    try:
        sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
        import lp
        J = lp.J(halfword)
    except Exception as e:
        J = 'lp.J failed: %r' % (e,)
    hhmm = time.strftime('%H%M')
    path = os.path.join(HIT_DIR, 'HIT-%s.md' % hhmm)
    k = 0
    while os.path.exists(path):
        k += 1; path = os.path.join(HIT_DIR, 'HIT-%s-%d.md' % (hhmm, k))
    with open(path, 'w') as f:
        f.write('# HIT (cert/run lane, certify.py): CERTIFIED_NONTRIVIAL knot K with V_K = 1\n')
        f.write('halfword: %s\nJ (lp.J, normalised): %s\n' % (halfword, _poly_str(J) if isinstance(J, dict) else J))
        f.write('V_K (PD bracket, diagram.py): %s\nV_K (project bracket, kauffman.py + ident3 normalisation): %s\n' % (_poly_str(V_pd), _poly_str(V_proj)))
        f.write('V_K (third bracket, audit-2 a2lib): %s\nDelta_K: %s\nmethod: nonabelian rep to %s, checked on every Wirtinger relator by replay.py\n%s\n'
                % (_poly_str(V_third), _poly_str(A) if A is not None else 'not computed', rep_cert.get('group'), note))
        f.write('certificate (replay.py kind rep):\n```\n%s\n```\n' % json.dumps(rep_cert))
        f.write('A second independent check (other implementation, e.g. SnapPy) must follow (BRIEF section 5).\n')
    return path


def _alarm(halfword, what, data):
    try:
        os.makedirs(ALARM_DIR, exist_ok=True)
        with open(os.path.join(ALARM_DIR, 'ALARMS.jsonl'), 'a') as f:
            f.write(json.dumps({'time': time.strftime('%H:%M:%S'), 'halfword': halfword, 'what': what, 'data': data}) + '\n')
    except Exception:
        pass


def certify(halfword, tietze_budget=None, rep_budget=30.0, seed=0, want_all=False, write_hits=True, blind=False,
            n_seeds=5, groups=None):
    """Returns (status, certificate).
    status in CERTIFIED_UNKNOT / CERTIFIED_NONTRIVIAL / COUNTEREXAMPLE / UNRESOLVED / NOT_A_KNOT / INVALID_WORD.
    V_K is computed by BOTH brackets (PD bracket of diagram.py and the project bracket kauffman.py); V_K = 1 by EITHER one
    routes the knot to the unknot routes (Tietze with up to n_seeds seeds, then jones24) and makes a nontriviality
    certificate a COUNTEREXAMPLE candidate (cert/run fixes: audit-1 F3 'HIT detection through both brackets', audit-2 F5
    'several seeds').  blind=True: Tietze forced on every knot with one seed (soundness suite)."""
    t0 = time.time()
    info = {'halfword': halfword, 'certificates': [], 'notes': []}
    if not diagram.valid_halfword(halfword):
        return 'INVALID_WORD', info
    pd = diagram.pd_from_halfword(halfword)
    if pd is None:
        return 'NOT_A_KNOT', info
    info['crossings'] = pd.n
    if not diagram.check_pd(pd):
        info['notes'].append('PD self-check failed')
        return 'UNRESOLVED', info
    V = diagram.jones(pd)
    Vp = _vk_project(halfword)
    info['V_K'] = sorted(V.items()); info['V_K_project'] = sorted(Vp.items()) if Vp else None
    info['Delta'] = None     # Delta is computed only when the rep search needs it
    if Vp != V:
        info['notes'].append('BRACKET DISAGREEMENT: PD bracket %s vs project bracket %s' % (_poly_str(V), _poly_str(Vp)))
        _alarm(halfword, 'bracket disagreement', {'pd': sorted(V.items()), 'project': sorted(Vp.items()) if Vp else None})
    v_trivial = (V == {0: 1}) or (Vp == {0: 1})
    unknot_cert = None

    def accept(cert):
        ok, msg = replay.check(cert)
        if ok:
            cert['checker'] = msg; info['certificates'].append(cert)
        else:
            info['notes'].append('certificate REJECTED by checker: %s (%s)' % (cert.get('kind'), msg))
        return ok

    # route (c0): no crossings (accepted only through the checker)
    if pd.n == 0:
        if accept({'kind': 'unknot0', 'halfword': halfword}):
            info['secs'] = round(time.time() - t0, 3)
            return 'CERTIFIED_UNKNOT', info
    # route (b): Tietze on the Wirtinger presentation.  Attempted when V_K = 1 (the only case where it can succeed),
    # and ALWAYS when blind=True (soundness test suites: the simplifier must then fail on every nontrivial knot).
    gens, rels = wirtinger.wirtinger(pd)
    if v_trivial or blind:
        tb = tietze_budget if tietze_budget is not None else (30.0 if (v_trivial and not blind) else 3.0)
        seeds = [seed] if blind else [seed + k for k in range(max(1, n_seeds))]
        tz = []
        for sd in seeds:
            ok, moves, fin, st = tietze.simplify(gens, rels, seed=sd, time_budget=tb)
            tz.append({'seed': sd, 'success': ok, 'attempts': st['attempts'],
                       'final_gens': len(fin[0]) if fin else None, 'final_rels': len(fin[1]) if fin else None,
                       'final_len': tietze.total_len(fin[1]) if fin else None})
            if ok:
                c = {'kind': 'tietze', 'halfword': halfword, 'moves': [list(m) for m in moves], 'seed': sd}
                if accept(c):
                    unknot_cert = c; break
        info['tietze'] = dict(tz[-1], seeds_tried=len(tz), success=unknot_cert is not None)
    # route (a): <= 24 crossings and V_K = 1
    if (unknot_cert is None or want_all) and pd.n <= 24 and v_trivial:
        c = {'kind': 'jones24', 'halfword': halfword}
        if accept(c) and unknot_cert is None: unknot_cert = c
    if unknot_cert is not None:
        info['secs'] = round(time.time() - t0, 3)
        return 'CERTIFIED_UNKNOT', info
    # representations (exact Delta for the affine search up to EXACT_ALEX_MAX crossings; beyond that the affine search
    # runs on the reduced presentation mod p without Delta)
    if pd.n <= EXACT_ALEX_MAX:
        A = diagram.alexander(pd); info['Delta'] = list(A)
        r = reps.find_rep(gens, rels, A, time_budget=rep_budget, groups=groups)
    else:
        A = None
        r = reps.find_rep(gens, rels, None, time_budget=rep_budget, groups=groups, affine_reduced=True)
    if r is not None:
        img, gname, note = r
        pair = reps.noncommuting_pair(img, gens)
        if pair is not None:
            c = {'kind': 'rep', 'halfword': halfword, 'group': gname, 'note': note,
                 'degree': len(next(iter(img.values()))), 'images': {str(k): list(v) for k, v in img.items()},
                 'noncommuting': list(pair)}
            if accept(c):
                info['secs'] = round(time.time() - t0, 3)
                if v_trivial:
                    # COUNTEREXAMPLE candidate (V_K = 1 by at least one bracket).  Reconcile with a third bracket.
                    V3 = third_bracket_V(halfword)
                    info['V_K_third'] = sorted(V3.items()) if V3 else None
                    votes = sum(1 for x in (V, Vp, V3) if x == {0: 1})
                    if Vp == {0: 1} or votes >= 2:
                        info['notes'].append('NONTRIVIAL KNOT WITH V_K = 1 (brackets saying V_K = 1: %d of 3; project bracket: %s)'
                                             % (votes, Vp == {0: 1}))
                        _alarm(halfword, 'COUNTEREXAMPLE', {'votes': votes})
                        if write_hits:
                            info['hit_file'] = write_hit(halfword, V, Vp, V3, A, c, 'certify.py (cert/run), %s' % note)
                        return 'COUNTEREXAMPLE', info
                    info['notes'].append('PD bracket says V_K = 1 but the project bracket and the third bracket disagree: '
                                         'bracket BUG, knot certified nontrivial, not a HIT')
                    _alarm(halfword, 'pd bracket alone says V=1 on a certified nontrivial knot', {'votes': votes})
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
