"""Assemble the residue files and stage counts.
residue_S*.json            = configurations NOT certified by the word-level reduction (stage 1), deduplicated by reduced
                             halfword (equal reduced words = identical theta-curves, the word moves being equivariant
                             isotopies), each with provenance and its FINAL status after the knot-level stages (PD / Tietze).
final_unresolved_S*.json   = configurations not certified by any method (status UNRESOLVED).
counts.json                = stage counts."""
import json
from collections import Counter, defaultdict
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/'
CERT = ('CERT_c_empty', 'CERT_a_TS24', 'CERT_c_pd', 'CERT_a_pd_TS24', 'CERT_a_TS24_original', 'CERT_b_tietze')
def final_stage(tag):
    for fn in (tag + '_stage3.json', tag + '_stage2.json', tag + '_stage1_residue.json'):
        try: return json.load(open(D + 'data/' + fn)), fn
        except FileNotFoundError: pass
    return None, None
def summary(r):
    s = r['status']; x = r.get('stage3', {})
    if s == 'CERT_b_tietze':
        return {'method': '(b) Tietze to <a|>', 'word_used': x.get('tietze_word'), 'direction': x.get('tietze_direction'),
                'tietze_version': x.get('tietze_version', 1), 'steps': len(x.get('tietze_log', []))}
    if s in ('CERT_c_pd', 'CERT_a_pd_TS24'):
        hw = x.get('alt_halfword') if x.get('status') == s else r['reduced_halfword']
        n = x.get('pd_best_crossings') if x.get('status') == s else r.get('pd_best_crossings')
        return {'method': '(c) Reidemeister to 0 crossings' if s == 'CERT_c_pd' else '(a) <= 24-crossing diagram + exact V_K = 1',
                'diagram_halfword': hw, 'final_crossings': n}
    return {'method': None}
def build(tag, subset):
    R, fn = final_stage(tag)
    if R is None: return None
    out = defaultdict(lambda: {'provenance': [], 'original_halfwords': []})
    for r in R:
        k = r['reduced_halfword']; e = out[k]
        e['reduced_halfword'] = k; e['ncross_reduced'] = r.get('ncross_reduced')
        e['original_halfwords'].append(r['halfword'])
        e['ncross_original_min'] = min(e.get('ncross_original_min', 999), r.get('ncross_original') or 999)
        e['certified_by_reduction'] = False
        e['final_status'] = r['status']; e['unresolved'] = r['status'] not in CERT
        e['certificate'] = summary(r); e['certificate_file'] = 'data/' + fn
        if subset: e['subset'] = subset
        e['provenance'].extend(r['provenance'])
    return list(out.values()), dict(Counter(r['status'] for r in R)), fn, len(R)
if __name__ == '__main__':
    counts = {}
    for S, sets in (('S1', [('s1', None)]), ('S2', [('s2', None)]), ('S3', [('s3a', 'window'), ('s3b', 'unit_lines')])):
        res = []; counts[S] = {}
        for t, sub in sets:
            b = build(t, sub)
            if b is None: counts[S][t] = 'not available'; continue
            entries, st, fn, n = b
            c1 = json.load(open(D + 'data/' + t + '_stage1_counts.json'))
            counts[S][t] = {'stage1': c1, 'not_certified_by_reduction_words': n, 'not_certified_by_reduction_distinct_reduced': len(entries),
                            'final_status_of_those': st, 'final_unresolved': sum(1 for e in entries if e['unresolved']),
                            'final_stage_file': fn}
            res.extend(entries)
        json.dump(res, open(D + 'residue_%s.json' % S, 'w'), indent=0)
        json.dump([e for e in res if e['unresolved']], open(D + 'final_unresolved_%s.json' % S, 'w'), indent=1)
        print(S, 'not certified by reduction (distinct reduced words):', len(res), 'final unresolved:', sum(1 for e in res if e['unresolved']))
    json.dump(counts, open(D + 'counts.json', 'w'), indent=1)
