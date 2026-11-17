"""Analyze four saved nonzero controls only; no new braid calculation.

All pairs in this file are aggregated Laurent monomials, NOT identified
geometric intersection pairs. Variables are s,t with q=s**2.
"""
from collections import defaultdict
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def clean(d):
    return {k: v for k, v in d.items() if v}


def mul(p, q):
    d = defaultdict(int)
    for (a, b), c in p.items():
        for (i, j), k in q.items():
            d[a+i, b+j] += c*k
    return clean(d)


def mul1(p, q):
    d = defaultdict(int)
    for a, c in p.items():
        for b, k in q.items():
            d[a+b] += c*k
    return clean(d)


def divide_1_plus_s2(p):
    p = dict(p)
    lo = min(p)
    out = {}
    while p:
        high = max(p)
        assert high >= lo+2
        c = p[high]
        e = high-2
        out[e] = c
        for k in (e, high):
            p[k] = p.get(k, 0)-c
            if not p[k]:
                del p[k]
    return out


def second_jet(raw):
    out = defaultdict(int)
    for (a, b), c in raw.items():
        out[a-2*b] += c * (-1 if b % 2 else 1) * b*(b-1)
    return clean(out)


h = {(0, 0): 1, (2, 1): 1}
# L_raw = -(1-t)*(1+s^2*t)^2*(s^2-1)^2*t^-2*s^-6 * P.
factor = {(-6, -2): -1}
for p in ({(0, 0): 1, (0, 1): -1}, h, h,
          {(2, 0): 1, (0, 0): -1}, {(2, 0): 1, (0, 0): -1}):
    factor = mul(factor, p)

rows = []
for saved in json.loads((HERE/'c3_samples.json').read_text()):
    if saved['J_zero']:
        continue
    p = {(a, b): c for a, b, c in saved['Lreg_terms']}
    spec = {int(a): c for a, c in saved['specialization'].items()}
    jones = divide_1_plus_s2(spec)
    assert mul1(jones, {0: 1, 2: 1}) == spec
    raw = mul(factor, p)
    jet = second_jet(raw)
    assert jet == mul1(jones, {4: -2, 0: 4, -4: -2})
    top = max(jet)
    ptop = max(spec)
    ptop_terms = [{'s_exponent': a, 't_exponent': b, 'coefficient': c,
                  'specialized_contribution': c*(-1 if b % 2 else 1)}
                 for (a,b),c in sorted(p.items()) if a-2*b == ptop]
    contributions = []
    for (a, b), c in sorted(raw.items()):
        if a-2*b == top:
            contributions.append({
                's_exponent': a, 't_exponent': b, 'coefficient': c,
                'derivative_weight': b*(b-1),
                'weighted_contribution': c*(-1 if b % 2 else 1)*b*(b-1)})
    live = [r for r in contributions if r['weighted_contribution']]
    positive = sum(r['weighted_contribution'] for r in live if r['weighted_contribution'] > 0)
    negative = sum(r['weighted_contribution'] for r in live if r['weighted_contribution'] < 0)
    rows.append({
        'label': saved['label'], 'word': saved['word'], 'i': saved['i'], 'j': saved['j'],
        'J_hat': jones, 'J_top_s_degree': max(jones), 'J_leading_coefficient': jones[max(jones)],
        'P_top_specialized_s_degree': ptop, 'P_top_line_terms': ptop_terms,
        'raw_second_jet_top_s_degree': top, 'raw_second_jet_leading_coefficient': jet[top],
        'raw_terms': len(raw), 'collapsed_top_line_terms': len(contributions),
        'nonzero_weight_top_line_terms': len(live),
        'top_line_t_exponents': [r['t_exponent'] for r in contributions],
        'nonzero_top_line_t_exponents': [r['t_exponent'] for r in live],
        'positive_contribution_sum': positive, 'negative_contribution_sum': negative,
        'contributions': contributions,
        'interpretation': 'Aggregated polynomial monomials; no geometric intersection-point identities.'})
    assert positive+negative == jet[top]

out = {'variables': 'q=s^2; t=-s^-2(1+u)',
       'identity': 'd_u^2 L_raw|0=-2(s^2-s^-2)^2 J_hat', 'samples': rows}
(HERE/'jet_extrema.json').write_text(json.dumps(out, indent=2)+'\n')
for r in rows:
    print(r['label'], 'Jdegree', r['J_top_s_degree'], 'Jlead', r['J_leading_coefficient'],
          'rawdegree', r['raw_second_jet_top_s_degree'], 'rawlead', r['raw_second_jet_leading_coefficient'],
          'terms', r['collapsed_top_line_terms'], 'weighted', r['nonzero_weight_top_line_terms'],
          'positive', r['positive_contribution_sum'], 'negative', r['negative_contribution_sum'])
    print('  contributions', [(c['s_exponent'], c['t_exponent'], c['coefficient'], c['weighted_contribution']) for c in r['contributions']])
