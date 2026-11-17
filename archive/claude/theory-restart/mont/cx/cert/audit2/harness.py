"""harness.py -- AUDIT-2: run the certifier on test knots and verify every returned certificate independently.

Halfword route: certify.certify(hw, write_hits=False, ...) (the public API).
PD / Morse route: the certifier's own pipeline pieces (diagram.PD, wirtinger.wirtinger, tietze.simplify, reps.find_rep,
replay.replay_moves) applied to a PD code we build ourselves (the public API only takes halfwords).
Independent verification (a2lib): my Wirtinger presentation, my Tietze replay, my relator check, my bracket.
"""
import sys, time, json, random, traceback
A2 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2'
CERT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert'
for p in (A2, CERT, '/Users/calebbarnett/jones-lanes/theory-restart/tools'):
    if p not in sys.path: sys.path.insert(0, p)
import a2lib


def _cert_mods():
    import certify, diagram, wirtinger, tietze, reps, replay
    return certify, diagram, wirtinger, tietze, reps, replay


def verify_certs_hw(hw, info, myV1=None):
    """Independent verification of every certificate the certifier returned for halfword hw."""
    out = []
    full = a2lib.full_of(hw)
    D = a2lib.morse_diagram(full)
    for c in info.get('certificates', []):
        k = c['kind']
        if k == 'tietze':
            g, r = a2lib.wirtinger_from_full(full)
            ok, msg, fin = a2lib.my_replay(g, r, [tuple(m) for m in c['moves']])
            if not ok:
                ok2, msg2, fin2 = a2lib.my_replay(g, r, [tuple(m) for m in c['moves']], rot_convention='right')
                if ok2: ok, msg = ok2, msg2 + ' (right rotation convention)'
            out.append(('tietze', ok, msg, len(c['moves'])))
        elif k == 'rep':
            g, r = a2lib.wirtinger_from_full(full)
            imgs = {int(a): tuple(b) for a, b in c['images'].items()}
            ok, msg = a2lib.check_rep(g, r, imgs, c['degree'], tuple(c['noncommuting']))
            out.append(('rep', ok, msg, c.get('group')))
        elif k == 'jones24':
            ok = D is not None and D['n'] <= 24 and a2lib.jones_unit_test(a2lib.bracket_full(full))
            out.append(('jones24', ok, 'n=%s' % (D and D['n']), None))
        elif k == 'unknot0':
            ok = D is not None and D['n'] == 0 and D['ncomp'] == 1
            out.append(('unknot0', ok, '', None))
        else:
            out.append((k, False, 'unknown kind', None))
    return out


def run_hw(hw, label='', expect=None, blind=False, tietze_budget=None, rep_budget=30.0, seed=0):
    """expect in {'nontrivial', 'unknot', None}.  Returns a result dict."""
    certify = _cert_mods()[0]
    t0 = time.time()
    full = a2lib.full_of(hw)
    D = a2lib.morse_diagram(full)
    res = {'hw': hw, 'label': label, 'expect': expect, 'blind': blind}
    if D is None:
        res['my_knot'] = False
    else:
        res['my_knot'] = True; res['n'] = D['n']
        if D['n'] > 0:
            br = a2lib.bracket_full(full)
            res['myV1'] = a2lib.jones_unit_test(br)
    try:
        st, info = certify.certify(hw, tietze_budget=tietze_budget, rep_budget=rep_budget, seed=seed,
                                   write_hits=False, blind=blind)
    except Exception as e:
        res['status'] = 'EXCEPTION'; res['err'] = repr(e)[:300]; res['secs'] = round(time.time() - t0, 3)
        return res
    res['status'] = st
    res['kinds'] = [c['kind'] + (':' + str(c.get('group')) if c['kind'] == 'rep' else '') for c in info['certificates']]
    res['tietze'] = info.get('tietze')
    res['notes'] = info.get('notes')
    res['crossings'] = info.get('crossings')
    res['VK1'] = info.get('V_K') == [(0, 1)]
    res['verify'] = verify_certs_hw(hw, info)
    res['secs'] = round(time.time() - t0, 3)
    # verdict
    bad = []
    if st in ('CERTIFIED_UNKNOT',) and (expect == 'nontrivial' or res.get('myV1') is False):
        bad.append('FALSE_UNKNOT')
    if st in ('CERTIFIED_NONTRIVIAL', 'COUNTEREXAMPLE') and expect == 'unknot':
        bad.append('FALSE_NONTRIVIAL')
    if st == 'COUNTEREXAMPLE': bad.append('COUNTEREXAMPLE_STATUS')
    if any(not v[1] for v in res['verify']): bad.append('CERT_FAILS_MY_CHECK')
    if res.get('my_knot') is False and st not in ('NOT_A_KNOT', 'UNRESOLVED'): bad.append('NONKNOT_CERTIFIED')
    res['bad'] = bad
    res['info_certs'] = info['certificates'] if (bad or st in ('CERTIFIED_UNKNOT', 'CERTIFIED_NONTRIVIAL')) else None
    return res


# ------------------------------------------------------------------ PD / Morse route
def pd_obj_from_full(full):
    """Our own PD code (a2lib.pd_from_full) wrapped as the certifier's PD object."""
    diagram = _cert_mods()[1]
    X, sg = a2lib.pd_from_full(full)
    return diagram.PD(X, sg)


def run_pd(X, sg, label='', expect=None, blind=True, tietze_budget=3.0, rep_budget=30.0, seed=0, do_rep=True,
           myV=None, skip_j24=False):
    """The certifier's pipeline on a PD code built by us.  Mirrors certify(): Tietze (if V_K = 1 or blind), jones24
    (n <= 24 and V_K = 1), else rep search.  Every success is re-checked by replay.replay_moves AND by a2lib."""
    certify, diagram, wirtinger, tietze, reps, replay = _cert_mods()
    t0 = time.time()
    res = {'label': label, 'expect': expect, 'n': len(X), 'blind': blind}
    pd = diagram.PD(X, sg)
    res['check_pd'] = diagram.check_pd(pd)
    V = diagram.jones(pd)
    v1 = (V == {0: 1})
    res['VK1'] = v1
    gens, rels = wirtinger.wirtinger(pd)
    mg, mr = a2lib.wirtinger_from_pd(X, sg)
    res['wirt_equal_mine'] = (list(gens) == list(mg) and [tuple(r) for r in rels] == [tuple(r) for r in mr])
    status = 'UNRESOLVED'; certs = []
    if v1 or blind:
        ok, moves, fin, st = tietze.simplify(gens, rels, seed=seed, time_budget=tietze_budget)
        res['tietze'] = {'success': ok, 'attempts': st.get('attempts'),
                         'final_gens': len(fin[0]) if fin else None, 'final_rels': len(fin[1]) if fin else None}
        if ok:
            mv = [tuple(m) for m in moves]
            pres, msg = replay.replay_moves(gens, rels, mv)
            okr = pres is not None and len(pres[0]) == 1 and len(pres[1]) == 0
            mine = a2lib.my_replay(mg, mr, mv)
            res['tietze']['replay'] = (okr, msg); res['tietze']['mine'] = mine[:2]
            certs.append(('tietze', okr, mine[0]))
            status = 'CERTIFIED_UNKNOT' if (okr and mine[0]) else 'TIETZE_CLAIM_REJECTED'
    if status == 'UNRESOLVED' and v1 and len(X) <= 24 and not skip_j24:
        status = 'CERTIFIED_UNKNOT'; certs.append(('jones24', True, True))
    if status == 'UNRESOLVED' and do_rep:
        A = diagram.alexander(pd)
        res['Delta'] = list(A)
        r = reps.find_rep(gens, rels, A, time_budget=rep_budget)
        if r is not None:
            img, gname, note = r
            pair = reps.noncommuting_pair(img, gens)
            if pair is not None:
                d = len(next(iter(img.values())))
                ok, msg = a2lib.check_rep(mg, mr, {int(k): tuple(v) for k, v in img.items()}, d, tuple(pair))
                certs.append(('rep', gname, ok, msg))
                status = 'CERTIFIED_NONTRIVIAL' if ok else 'REP_REJECTED_BY_MINE'
                if ok and v1: status = 'COUNTEREXAMPLE?'
    res['status'] = status; res['certs'] = certs
    bad = []
    if status == 'CERTIFIED_UNKNOT' and expect == 'nontrivial': bad.append('FALSE_UNKNOT')
    if status.startswith('CERTIFIED_NONTRIVIAL') and expect == 'unknot': bad.append('FALSE_NONTRIVIAL')
    if status in ('TIETZE_CLAIM_REJECTED', 'REP_REJECTED_BY_MINE', 'COUNTEREXAMPLE?'): bad.append(status)
    if not res['wirt_equal_mine']: bad.append('WIRT_DIFFERS')
    if not res['check_pd']: bad.append('CHECK_PD_FAILED')
    res['bad'] = bad
    res['secs'] = round(time.time() - t0, 3)
    return res


def tietze_stress(gens, rels, seeds, budget):
    """Run the simplifier with several seeds; return list of (seed, success, final sizes)."""
    tietze = _cert_mods()[3]
    out = []
    for s in seeds:
        ok, moves, fin, st = tietze.simplify(gens, rels, seed=s, time_budget=budget)
        out.append((s, ok, len(fin[0]) if fin else None, len(fin[1]) if fin else None,
                    [tuple(m) for m in moves] if ok else None))
    return out
