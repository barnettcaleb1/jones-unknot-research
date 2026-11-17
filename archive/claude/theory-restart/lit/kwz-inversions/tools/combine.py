import sys, os, json, re
from fractions import Fraction
from collections import defaultdict, Counter
allp = json.load(open(sys.argv[1]))
paper = json.load(open(sys.argv[2]))

def padd(p, e, c):
    p[e] = p.get(e, 0) + c
    if p[e] == 0: del p[e]
def pmul(p, r):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in r.items(): padd(out, e1+e2, c1*c2)
    return out
def pdiv(p, r):
    """exact division of Laurent polynomials (dict exp->coeff); None if not exact"""
    p = dict(p); out = {}
    if not p: return {}
    re_, rc = max(r), r[max(r)]
    lo = min(p) - (max(r) - min(r))
    guard = 0
    while p:
        pe = max(p); pc = p[pe]
        if pc % rc: return None
        e = pe - re_
        if e < lo: return None
        c = pc // rc
        out[e] = c
        for e2, c2 in r.items(): padd(p, e + e2, -c * c2)
        guard += 1
        if guard > 5000: return None
    return out
def pstr(p):
    if p is None: return None
    if not p: return '0'
    s = ''
    for e, c in sorted(p.items()):
        s += (' + ' if c > 0 else ' - ') + (str(abs(c)) + '*' if abs(c) != 1 else '') + 'q^' + str(e)
    return s.strip().lstrip('+ ').strip() if s.strip().startswith('+') else s.strip()
def pkeys(p): return {str(e): c for e, c in sorted(p.items())}

def euler(components):
    chiB, chiW = {}, {}
    for c in components:
        for g in c['generators']:
            padd(chiB if g['idem'] == 'B' else chiW, g['q'], (-1) ** (g['h'] % 2))
    return chiB, chiW

ONE_MINUS_Q8 = {0: 1, 8: -1}
UNIV = pmul({0: 1, 2: -1}, {0: 1, 4: 1})     # (1-q^2)(1+q^4)

def slope_paper(khtpp_slope):
    # kht++ slope p/q  <->  paper slope -q/p   (specials: kht++ 0 <-> paper infinity; rational: kht++ -1/k <-> paper k)
    if khtpp_slope is None: return None
    p, q = khtpp_slope.split('/')
    p, q = int(p), int(q)
    if p == 0: return 'infinity'
    if q == 0: return '0'
    f = Fraction(-q, p)
    return str(f.numerator) if f.denominator == 1 else str(f)

def find_page(rec):
    k = rec['knot']; i = rec['inversion']
    nm = k + ('-%d' % i if i else '')
    return nm if nm in allp else None

report = []
out_records = []
problems = []
for rec in paper['inversions']:
    nm = find_page(rec)
    if nm is None: problems.append(('no page', rec['name'])); out_records.append(rec); continue
    pg = allp[nm]
    def pick(sec):
        blocks = pg['sections'].get(sec, {})
        opts = [o for o in blocks if o.startswith('-c2') and 'q' in o.split('-c2')[1]]
        # prefer plain quotient option without 'o' variants
        opts.sort(key=lambda o: (('o' in o.replace('-c2', '')), len(o)))
        return (opts[0], blocks[opts[0]]) if opts else (None, None)
    ob, bn = pick('BNr'); ok, kh = pick('Khr')
    if bn is None or kh is None: problems.append(('no c2 -q block', rec['name'])); out_records.append(rec); continue
    # consistency across all c2 quotient blocks (Euler characteristics must agree)
    chiB, chiW = euler(bn['components'])
    for o, blk in pg['sections']['BNr'].items():
        if o.startswith('-c2') and 'q' in o.replace('-c2', '') and o != ob:
            cb, cw = euler(blk['components'])
            if (cb, cw) != (chiB, chiW): problems.append(('BNr euler differs between option blocks', rec['name'], ob, o))
    kB, kW = euler(kh['components'])
    # check [Khr] = (q - q^-1) [BNr]
    f = {1: 1, -1: -1}
    okcone = (pmul(chiB, f) == kB and pmul(chiW, f) == kW)
    if not okcone:
        f2 = {1: -1, -1: 1}
        okcone = 'negated' if (pmul(chiB, f2) == kB and pmul(chiW, f2) == kW) else False
    # closures (decategorified pairing with the arcs, generator at (0,0)):
    #   <a(0), Khr>   = [chi_W (1+q^-2) + chi_B q^-1] / (1-q^-2)     (paper's tau(0))
    #   <a(inf), Khr> = [chi_B (1+q^-2) + chi_W q^-1] / (1-q^-2)     (paper's tau(infinity) = unknot)
    den = {0: 1, -2: -1}
    num0 = {}; numinf = {}
    for e, c in pmul(kW, {0: 1, -2: 1}).items(): padd(num0, e, c)
    for e, c in pmul(kB, {-1: 1}).items(): padd(num0, e, c)
    for e, c in pmul(kB, {0: 1, -2: 1}).items(): padd(numinf, e, c)
    for e, c in pmul(kW, {-1: 1}).items(): padd(numinf, e, c)
    V0 = pdiv(num0, den); Vinf = pdiv(numinf, den)
    # Kh components
    comps = []
    nspec = 0; ratl = None
    site_kappa = Counter()
    for c in kh['components']:
        r = c.get('recognized', {})
        d = dict(type=r.get('type'), length_khtpp=r.get('length'), khtpp_slope=r.get('khtpp_slope'), paper_slope=slope_paper(r.get('khtpp_slope')),
                 q_average=r.get('q_average'), delta_kind=r.get('delta_kind'), delta=r.get('delta'), descriptor_raw=r.get('raw'),
                 first_generator=c['first_generator'], n_generators=c['n_generators'], chain=c['chain'],
                 generators_idem_h_q=[[g['idem'], g['h'], g['q']] for g in c['generators']])
        if r.get('type') == 'special':
            nspec += 1
            # predicted kappa summand: q_average = 2(a+b), vertical delta = b + 1/2
            X = Fraction(r['q_average']); Y = Fraction(r['delta'])
            b = Y - Fraction(1, 2); a = X / 2 - b
            d['kappa_shift_h'] = float(a); d['kappa_shift_delta'] = float(b)
            site_kappa[(float(a), float(b))] += 1
        elif r.get('type') == 'rational':
            ratl = d
        comps.append(d)
    paper_kappa = Counter()
    for sc in rec['special_components']:
        paper_kappa[(sc['kappa_shift_h'], sc['kappa_shift_delta'])] += sc['multiplicity']
    kappa_match = (paper_kappa == site_kappa)
    k_site = ratl['paper_slope'] if ratl else None
    k_match = (ratl is not None and str(rec['rational_component']['slope_k']) == k_site)
    if not kappa_match: problems.append(('kappa mismatch', rec['name'], sorted(paper_kappa.items()), sorted(site_kappa.items())))
    if not k_match: problems.append(('k mismatch', rec['name'], rec['rational_component']['slope_k'], k_site, ratl and ratl['descriptor_raw']))
    if okcone is not True: problems.append(('cone relation', rec['name'], okcone))
    eta = chiB
    eta_hat = pdiv(eta, ONE_MINUS_Q8)
    eta_tilde = pdiv(eta, UNIV)
    bnc = []
    for c in bn['components']:
        bnc.append(dict(compact=c['compact'], n_generators=c['n_generators'], first_generator=c['first_generator'], chain=c['chain'],
                        end_idempotents=(None if c['compact'] else [c['generators'][0]['idem'], c['generators'][-1]['idem']]),
                        generators_idem_h_q=[[g['idem'], g['h'], g['q']] for g in c['generators']]))
    rec2 = dict(rec)
    rec2['khtpp'] = dict(page='examples/strong_inversions/' + ('2-bridge_knots/' if os.path.exists(os.path.join(sys.argv[4], '2-bridge_knots', nm + '.html')) else '') + nm + '.html',
                         input=pg['input'][:3], options_BNr=ob, options_Khr=ok, meta_BNr=bn['meta'], meta_Khr=kh['meta'],
                         BNr_components=bnc, Khr_components=comps,
                         n_BNr_components=len(bnc), n_BNr_compact=sum(1 for c in bnc if c['compact']), n_BNr_arcs=sum(1 for c in bnc if not c['compact']),
                         arc_n_generators=[c['n_generators'] for c in bnc if not c['compact']],
                         checks=dict(kappa_gradings_match_paper=kappa_match, rational_slope_matches_paper=k_match, n_special_matches=(nspec == rec['n_special']), Khr_class_equals_q_minus_qinv_times_BNr_class=okcone))
    rec2['rational_component'] = dict(rec['rational_component'])
    if ratl:
        rec2['rational_component']['bigrading'] = dict(source='kht++ site', first_generator=ratl['first_generator'], q_average=ratl['q_average'], delta_kind=ratl['delta_kind'], delta=ratl['delta'], descriptor_raw=ratl['descriptor_raw'])
    rec2['decategorified'] = dict(
        chi_W_BNr=pkeys(chiW), chi_B_BNr=pkeys(chiB), chi_W_BNr_str=pstr(chiW), chi_B_BNr_str=pstr(chiB),
        V_tau0=pkeys(V0) if V0 is not None else None, V_tau0_str=pstr(V0),
        V_tauinf=pkeys(Vinf) if Vinf is not None else None, V_tauinf_str=pstr(Vinf),
        eta_is_zero=(not eta), eta_divisible_by_1_minus_q8=(eta_hat is not None),
        eta_over_1_minus_q8=pkeys(eta_hat) if eta_hat is not None else None, eta_over_1_minus_q8_str=pstr(eta_hat),
        eta_over_universal=pkeys(eta_tilde) if eta_tilde is not None else None, eta_over_universal_str=pstr(eta_tilde))
    out_records.append(rec2)
    report.append((rec['name'], rec['rational_component']['slope_k'], rec['n_special'], len(bnc), [c['n_generators'] for c in bnc if not c['compact']], pstr(Vinf), pstr(eta_hat), pstr(eta_tilde), rec['P_kappa_str']))
print('problems:', len(problems))
for p in problems[:40]: print('  ', p)
json.dump(dict(records=out_records, report=report), open(sys.argv[3], 'w'), ensure_ascii=False)
for r in report[:14]: print(r)
print('eta zero:', [r['name'] for r in out_records if r.get('decategorified', {}).get('eta_is_zero')])
print('eta not divisible by 1-q^8:', [r['name'] for r in out_records if 'decategorified' in r and not r['decategorified']['eta_divisible_by_1_minus_q8']])
print('Vinf values:', Counter(r['decategorified']['V_tauinf_str'] for r in out_records if 'decategorified' in r).most_common(12))
print('BNr component counts:', Counter((r['khtpp']['n_BNr_arcs'], r['khtpp']['n_BNr_compact']) for r in out_records if 'khtpp' in r).most_common())
