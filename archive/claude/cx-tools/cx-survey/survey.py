#!/usr/bin/env python3
"""survey.py -- exact four-corner survey of EKT-type fusions, certificate format.

Writes results.json (everything), certificates.md (per-configuration
certificate: diagram word, PD, site edges, four raw corners, the three identity
polynomials, K(0,0) status, grid cross-check), summary.md (tables), log.txt.
Run:  ../cx-tools/venv/bin/python survey.py
"""
import sys
import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from harness import (  # noqa: E402
    T_piece, U_piece, seam_band, sigma2, assemble, abs_bracket, analyze_corners,
    check_knot_hfk, link_geometry, jones_from_abs, boundary_mates, poly_json,
    braid_closure_traced, IdentityBraid, IntegerTangle, RationalTangle, omega,
    DELTA, pmul, padd, pneg, pshift, pstr, pclean, pdiv_delta, jones_str, Diagram,
)

LOG = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


def det_from_V(V):
    """|V(-1)| for V given in powers of t^(1/2) (t = -1 -> t^(1/2) = i)."""
    re = im = 0
    for k, c in V.items():
        r = k % 4
        if r == 0:
            re += c
        elif r == 1:
            im += c
        elif r == 2:
            re -= c
        else:
            im -= c
    return abs(re) + abs(im)


# ------------------------------------------------------------------ builders

def make_builder(T_kind, U_kind, seam_kind, top=None, bottom=None, seed=None,
                 site1=None, site2=None):
    """Return build(s1, s2, traced=False) -> Link  (or (Link, edges) if traced).

    T_kind, U_kind in {'none','lit','seed'}; seam_kind in {None,'sigma2','sigma2inv','band'};
    site1/site2 in {'T','U','seam'} name the slots receiving s1 / s2."""
    def build(s1, s2, traced=False):
        states = {site1: s1, site2: s2}
        labels = {site1: 'site1', site2: 'site2'} if traced else {}
        if 'T' in states:
            A = T_piece(T_kind, states['T'], seed=seed, label=labels.get('T'))
        else:
            A = T_piece('none', None, seed=seed)
        if 'U' in states:
            B = U_piece(U_kind, states['U'], label=labels.get('U'))
        else:
            B = U_piece('none', None)
        if seam_kind is None:
            seam = None
        elif seam_kind == 'sigma2':
            seam = sigma2(1)
        elif seam_kind == 'sigma2inv':
            seam = sigma2(-1)
        elif seam_kind == 'band':
            seam = seam_band(states.get('seam', 'I'), label=labels.get('seam'))
        else:
            raise ValueError(seam_kind)
        tp = sigma2(1) if top == 'sigma2' else (sigma2(-1) if top == 'sigma2inv' else None)
        bt = sigma2(1) if bottom == 'sigma2' else (sigma2(-1) if bottom == 'sigma2inv' else None)
        X = assemble(A, B, top=tp, seam=seam, bottom=bt)
        if traced:
            return braid_closure_traced(X, ('site1', 'site2'))
        return X.braid_closure()
    return build


def tangle_word(T_kind, U_kind, seam_kind, top, bottom, seed, site1, site2):
    """Human-readable spherogram tangle word of the family (S1, S2 = the site states)."""
    st = {site1: 'S1', site2: 'S2'}
    seedw = '' if seed is None else f' * RationalTangle({seed[0]},{seed[1]})'
    if 'T' in st:
        if T_kind == 'lit':
            A = f'(I2 | rot(IntegerTangle(3){"" if seed is None else " [= omega(seed)]"})) * (I2 | {st["T"]})'
        else:
            A = f'(I2 | rot(omega({st["T"]}{seedw})))'
    else:
        A = '(I2 | rot(IntegerTangle(3)))' if seed is None else f'(I2 | rot(omega(RationalTangle({seed[0]},{seed[1]}))))'
    if 'U' in st:
        if U_kind == 'lit':
            B = f'({st["U"]} | I2) * (rot(IntegerTangle(-3)) | I2)'
        else:
            B = f'(rot(omega_bar({st["U"]})) | I2)'
    else:
        B = '(rot(IntegerTangle(-3)) | I2)'
    mid = []
    if top:
        mid.append('sigma2' if top == 'sigma2' else 'sigma2^-1')
    mid.append('h')
    if seam_kind == 'sigma2':
        mid.append('sigma2')
    elif seam_kind == 'sigma2inv':
        mid.append('sigma2^-1')
    elif seam_kind == 'band':
        mid.append(f'(I1 | rot({st.get("seam", "I2")}) | I1)' + ('' if 'seam' in st else '  [seam band fixed fused = ZeroTangle]'))
    mid.append('h')
    if bottom:
        mid.append('sigma2' if bottom == 'sigma2' else 'sigma2^-1')
    return 'braid_closure( ' + ' * '.join([A] + mid + [B]) + ' )'


# ------------------------------------------------------------------ core

GRID = [(1, 0), (0, 1), (1, 1), (2, -1)]


def corner_formula_bracket(B, m, n, s1, s2):
    """<K(m,n)>_abs = A^(-6(s1 m + s2 n)) * Q(x,y), x = A^(8 s1 m), y = A^(8 s2 n)."""
    x = {8 * s1 * m: 1}
    y = {8 * s2 * n: 1}
    one = {0: 1}
    omx = padd(one, pneg(x))
    omy = padd(one, pneg(y))
    d2Q = pmul(pmul(x, y), pmul(pmul(DELTA, DELTA), B['00']))
    d2Q = padd(d2Q, pmul(pmul(omx, y), pmul(DELTA, B['10'])))
    d2Q = padd(d2Q, pmul(pmul(x, omy), pmul(DELTA, B['01'])))
    d2Q = padd(d2Q, pmul(pmul(omx, omy), B['11']))
    Q = pdiv_delta(pdiv_delta(d2Q))
    return pshift(Q, -6 * (s1 * m + s2 * n))


def run_config(key, title, spec, note=''):
    T_kind, U_kind, seam_kind, top, bottom, seed, site1, site2 = spec
    seedT = None if seed is None else RationalTangle(*seed)
    build = make_builder(T_kind, U_kind, seam_kind, top=top, bottom=bottom, seed=seedT,
                         site1=site1, site2=site2)
    log('=' * 78)
    log(f'[{key}] {title}')
    if note:
        log('   ' + note)
    t0 = time.perf_counter()
    res = dict(key=key, title=title, note=note, sites=[site1, site2],
               tangle_word=tangle_word(T_kind, U_kind, seam_kind, top, bottom, seed, site1, site2))
    log('   word: ' + res['tangle_word'])
    B = {}
    corner_info = {}
    for s1, s2, tag in (('I', 'I', '00'), ('e', 'I', '10'), ('I', 'e', '01'), ('e', 'e', '11')):
        if tag == '00':
            L, edges = build(s1, s2, traced=True)
        else:
            L = build(s1, s2)
        r = abs_bracket(L)
        B[tag] = r['bracket']
        corner_info[tag] = dict(crossings=r['crossings'], components=r['components'],
                                free_loops=r['free_loops'], writhe=r['writhe'],
                                bracket=poly_json(r['bracket']), bracket_str=pstr(r['bracket']))
        if tag == '00':
            res['K00'] = dict(pd=r['pd'], crossings=r['crossings'], components=r['components'],
                              writhe=r['writhe'],
                              site_edges={site1: edges.get('site1'), site2: edges.get('site2')})
        log(f'  B{tag}: cr={r["crossings"]:3d} comps={r["components"]} free={r["free_loops"]} w={r["writhe"]:3d}  <>_abs = {pstr(r["bracket"])}')
    res['corners'] = corner_info
    w0 = res['K00']['writhe']
    an = analyze_corners(B, w0)
    res['analysis'] = an
    log(f'  K(0,0): {res["K00"]["crossings"]} crossings, {res["K00"]["components"]} component(s), w0={w0}, site edges {res["K00"]["site_edges"]}')
    log(f'  u=(-A^3)^w0 = {an["unit_u"]}')
    log(f'  B00 - u*delta   = {an["poly_B00_minus_u_delta"]}   -> unknot-seed eq {an["unknot_seed_eq"]}')
    log(f'  delta*B10 - B11 = {an["poly_dB10_minus_B11"]}   -> {an["id_dB10_eq_B11"]}')
    log(f'  delta*B01 - B11 = {an["poly_dB01_minus_B11"]}   -> {an["id_dB01_eq_B11"]}')
    log(f'  (delta*B00 == B10 : {an["flat_site1_at_I"]};  delta*B00 == B01 : {an["flat_site2_at_I"]};  B00 = unit*delta : {an["B00_unit_times_delta"]} unit={an["B00_unit"]})')
    for c in 'abcd':
        log(f'  delta^3*{c} = {an["coeffs"][c]["delta3_times"]}   [{an["coeffs"][c]["exact"]}]')
    # K(0,0) Jones / det / unknot check
    k00 = res['K00']
    V = jones_from_abs(B['00'], w0)
    res['K00']['V_str'] = jones_str(V)
    res['K00']['V'] = poly_json(V)
    if k00['components'] == 1:
        res['K00']['det'] = det_from_V(V)
        log(f'  K(0,0) V = {jones_str(V)}, det = {res["K00"]["det"]}')
        hk = check_knot_hfk(k00['pd'])
        res['K00']['check'] = hk
        log(f'  K(0,0) HFK/identify: {hk}')
    else:
        log(f'  K(0,0) is a {k00["components"]}-component link; V = {jones_str(V)}')
    # cross-check against direct brackets at grid points
    direct = {}
    for (m, n) in GRID:
        direct[(m, n)] = abs_bracket(build(m, n))
    s_found = None
    for s1 in (1, -1):
        for s2 in (1, -1):
            ok10 = corner_formula_bracket(B, 1, 0, s1, s2) == direct[(1, 0)]['bracket']
            ok01 = corner_formula_bracket(B, 0, 1, s1, s2) == direct[(0, 1)]['bracket']
            if ok10 and ok01:
                s_found = (s1, s2)
    xc = dict(grid=[list(g) for g in GRID], handedness=s_found)
    if s_found is None:
        xc['status'] = 'FAIL: no handedness choice matches the direct brackets at (1,0),(0,1)'
        log('  CROSS-CHECK FAILED at (1,0)/(0,1)')
    else:
        s1, s2 = s_found
        allok = True
        pts = {}
        t1 = (direct[(1, 0)]['writhe'] - w0) // 2
        t2 = (direct[(0, 1)]['writhe'] - w0) // 2
        for (m, n), r in direct.items():
            f = corner_formula_bracket(B, m, n, s1, s2)
            ok = (f == r['bracket'])
            allok &= ok
            wexp = w0 + 2 * t1 * m + 2 * t2 * n
            Vd = jones_from_abs(r['bracket'], r['writhe'])
            pts[f'{m},{n}'] = dict(crossings=r['crossings'], components=r['components'],
                                   writhe=r['writhe'], writhe_formula_ok=(wexp == r['writhe']),
                                   bracket_matches_corner_formula=ok,
                                   V_str=jones_str(Vd), det=det_from_V(Vd) if r['components'] == 1 else None)
            log(f'  K({m:2d},{n:2d}): cr={r["crossings"]:3d} comps={r["components"]} w={r["writhe"]:3d} '
                f'formula {"MATCH" if ok else "MISMATCH"}  V = {jones_str(Vd)}' + (f'  det={det_from_V(Vd)}' if r['components'] == 1 else ''))
        xc['points'] = pts
        xc['all_match'] = allok
        xc['writhe_slopes'] = [t1, t2]
        xc['site_orientation'] = ['antiparallel' if s + t == 0 else 'parallel'
                                  for s, t in zip(s_found, (t1, t2))]
        xc['status'] = 'all grid points match' if allok else 'MISMATCH at some grid point'
        log(f'  handedness s=(s1,s2)={s_found}, writhe slopes t=({t1},{t2}) -> sites {xc["site_orientation"]}; {xc["status"]}')
    res['crosscheck'] = xc
    # certificate extras when BOTH turnback identities hold (coordinator item 3)
    if an['id_dB10_eq_B11'] and an['id_dB01_eq_B11']:
        log('  *** BOTH identities hold: computing crossing-circle / diagonal certificate ***')
        ex = {}
        try:
            Lr = build('ring', 'ring')
            pdr = Lr.PD_code()
            Dr = Diagram(pdr)
            ex['K_c1_c2'] = dict(crossings=len(pdr), components=Dr.num_components(),
                                 linking=({f'{a},{b}': v for (a, b), v in Dr.linking_matrix().items()}),
                                 geometry=link_geometry(Lr))
            ex['K_c1'] = dict(geometry=link_geometry(build('ring', 'I')))
            ex['K_c2'] = dict(geometry=link_geometry(build('I', 'ring')))
        except Exception as e:
            ex['ring_error'] = repr(e)
        if s_found is not None and k00['components'] == 1:
            s1, s2 = s_found
            diag = {}
            for m in (1, -1, 2):
                n = -s1 * s2 * m          # s1 m + s2 n = 0  <=> xy = 1
                r = abs_bracket(build(m, n))
                Vd = jones_from_abs(r['bracket'], r['writhe'])
                hk = check_knot_hfk(r['pd']) if r['components'] == 1 else {'note': 'not a knot'}
                diag[f'{m},{n}'] = dict(V_str=jones_str(Vd), components=r['components'], check=hk)
                log(f'  diagonal K({m},{n}): V = {jones_str(Vd)}; {hk}')
            ex['diagonal'] = diag
        res['certificate_extras'] = ex
        log(f'  extras: {ex}')
    res['seconds'] = round(time.perf_counter() - t0, 2)
    return res


# ------------------------------------------------------------------ config 1

def calibrate_link():
    """Single-site flatness on the unfused link for each site realization."""
    log('=' * 78)
    log('[1] LINK calibration: braid closure of A0*h*h*B0, one site varied at a time')
    out = {}
    sites = {
        'T-lit':  lambda s: assemble(T_piece('lit', s), U_piece('none', None)).braid_closure(),
        'T-seed': lambda s: assemble(T_piece('seed', s), U_piece('none', None)).braid_closure(),
        'U-lit':  lambda s: assemble(T_piece('none', None), U_piece('lit', s)).braid_closure(),
        'U-seed': lambda s: assemble(T_piece('none', None), U_piece('seed', s)).braid_closure(),
    }
    for name, bld in sites.items():
        rows = {}
        polys = {}
        for st in ('I', 'e', 1, 2, -1):
            L = bld(st)
            r = abs_bracket(L)
            V = jones_from_abs(r['bracket'], r['writhe'])
            rows[str(st)] = dict(crossings=r['crossings'], components=r['components'],
                                 free_loops=r['free_loops'], writhe=r['writhe'],
                                 bracket_str=pstr(r['bracket']), bracket=poly_json(r['bracket']),
                                 V_str=jones_str(V), V=poly_json(V))
            polys[str(st)] = (r['bracket'], V)
        BI, Be = polys['I'][0], polys['e'][0]
        E = padd(pmul(DELTA, BI), pneg(Be))
        flat = (not E)
        V0 = polys['I'][1]
        same = {}
        for st in ('1', '2', '-1'):
            Vk = polys[st][1]
            if Vk == V0:
                same[st] = 'equal'
            else:
                shift = min(Vk) - min(V0)
                sh = {k + shift: c for k, c in V0.items()}
                if sh == Vk:
                    same[st] = f'equal up to t^({shift}/2)'
                elif {k: -c for k, c in sh.items()} == Vk:
                    same[st] = f'equal up to -t^({shift}/2)'
                else:
                    same[st] = 'DIFFERENT'
        out[name] = dict(rows=rows, poly_delta_BI_minus_Be=(pstr(E) if E else '0'),
                         bracket_identity_delta_BI_eq_Be=flat, V_vs_I=same)
        log(f'  site {name:7s}: delta*B_I - B_e = {pstr(E) if E else 0}  ->  flat {flat};  V(k) vs V(0): {same}')
        for st in ('I', 'e', '1', '2', '-1'):
            rr = rows[st]
            log(f'      state {st:>2s}: cr={rr["crossings"]:3d} comps={rr["components"]} free={rr["free_loops"]} w={rr["writhe"]:3d} <>={rr["bracket_str"]}  V={rr["V_str"]}')
    return out


# ------------------------------------------------------------------ main

CONFIGS = [
    # key, title, (T_kind, U_kind, seam_kind, top, bottom, seed, site1, site2), note
    ('1L', 'unfused LINK, sites (T-lit, U-lit)',
     ('lit', 'lit', None, None, None, None, 'T', 'U'), 'calibration; corners of the Jones-trivial link itself'),
    ('1S', 'unfused LINK, sites (T-seed, U-seed)',
     ('seed', 'seed', None, None, None, None, 'T', 'U'), 'calibration; T = omega(S1), U = omega_bar(S2)'),
    ('2L', 'H2 knot (fixed sigma2 at the seam), sites (T-lit, U-lit)',
     ('lit', 'lit', 'sigma2', None, None, None, 'T', 'U'), 'designer K(0,0) of c4_two_site_candidate.md; literal boxes on strands 3,4 and 1,2'),
    ('2S', 'H2 knot (fixed sigma2 at the seam), sites (T-seed, U-seed)',
     ('seed', 'seed', 'sigma2', None, None, None, 'T', 'U'), 'same knot type; EKT seed sites inside omega / omega_bar'),
    ('3', 'c1 anchor (seed R(25,-9), seam band fusion), sites (seam, T-seed)',
     ('seed', 'none', 'band', None, None, (25, -9), 'seam', 'T'), 'c1_nonunit_turnback.py K(m,n) = cl(A_n h C_m h B); corners = its corner(eps,eta)'),
    ('3b', 'c1 anchor, sites (T-seed, U-seed)  [the anchor knot with the two EKT seed sites]',
     ('seed', 'seed', 'band', None, None, (25, -9), 'T', 'U'), 'seam band fixed in its fused state'),
    ('4L', 'c1 anchor, sites (seam, U-lit)',
     ('none', 'lit', 'band', None, None, (25, -9), 'seam', 'U'), ''),
    ('4S', 'c1 anchor, sites (seam, U-seed)',
     ('none', 'seed', 'band', None, None, (25, -9), 'seam', 'U'), ''),
    ('5a', 'fusion sigma2 at the TOP (between A0 and the first h), sites (T-seed, U-seed)',
     ('seed', 'seed', None, 'sigma2', None, None, 'T', 'U'), ''),
    ('5b', 'fusion sigma2 at the BOTTOM (between the second h and B0), sites (T-seed, U-seed)',
     ('seed', 'seed', None, None, 'sigma2', None, 'T', 'U'), ''),
    ('5c', 'fusion sigma2^-1 at the seam, sites (T-seed, U-seed)',
     ('seed', 'seed', 'sigma2inv', None, None, None, 'T', 'U'), ''),
    ('5aL', 'fusion sigma2 at the TOP, sites (T-lit, U-lit)',
     ('lit', 'lit', None, 'sigma2', None, None, 'T', 'U'), ''),
    ('5bL', 'fusion sigma2 at the BOTTOM, sites (T-lit, U-lit)',
     ('lit', 'lit', None, None, 'sigma2', None, 'T', 'U'), ''),
    ('6', 'torsion-free seed R(11,-4) in the c1 construction, sites (seam, T-seed)',
     ('seed', 'none', 'band', None, None, (11, -4), 'seam', 'T'),
     'S = p/(q+2pn) at n=0 with p/q = 11/-4; 13p+36q = -1, turnback link torsion-free (c1 note section 6)'),
]


def main():
    results = {'conventions': (
        'ABSOLUTE bracket <empty>=1, <unknot>=delta=-A^2-A^-2; '
        'PD = spherogram PD_code (ccw from incoming under-strand), A-smoothing joins (a,b),(c,d); '
        'V = (-A^3)^(-w) <D>_reduced, t = A^-4, Jones keys are exponents of t^(1/2). '
        'Sites: local I = IdentityBraid(2), local e = ZeroTangle, k = k full twists; '
        'seam band site is rotated (local I = global ZeroTangle = fused, local e = global IdentityBraid(2) = unfused link). '
        'All four corners from the same diagram, same outside framing, no per-corner writhe normalisation. '
        '<K(m,n)> = A^(-6(s1 m + s2 n)) Q(x,y), Q = xy B00 + (1-x)y/delta B10 + x(1-y)/delta B01 + (1-x)(1-y)/delta^2 B11, '
        'x = A^(8 s1 m), y = A^(8 s2 n); V = unit * (a + b x + c y + d xy) with delta^3 a = B11, '
        'delta^3 b = delta B01 - B11, delta^3 c = delta B10 - B11, delta^3 d = delta^2 B00 - delta B10 - delta B01 + B11. '
        'Identity polynomials: B00 - (-A^3)^w0 delta (unknot-seed equation), delta B10 - B11, delta B01 - B11.')}
    T0 = time.perf_counter()
    results['config1_link_single_site'] = calibrate_link()
    results['configs'] = {}
    for key, title, spec, note in CONFIGS:
        results['configs'][key] = run_config(key, title, spec, note)
        (HERE / 'results.json').write_text(json.dumps(results, indent=1, default=str))
    results['total_seconds'] = round(time.perf_counter() - T0, 1)
    (HERE / 'results.json').write_text(json.dumps(results, indent=1, default=str))
    (HERE / 'log.txt').write_text('\n'.join(LOG) + '\n')
    log(f'done in {results["total_seconds"]} s')


if __name__ == '__main__':
    main()
