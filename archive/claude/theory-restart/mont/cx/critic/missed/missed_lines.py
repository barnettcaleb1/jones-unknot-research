"""critic: which unit lines / unit planes of regress's corrected census (5,5), (6,6) sit on a bottom representative whose
projective class hides a DIFFERENT bottom tangle (cert/run geo_bfs: 420 missed geometric classes of depth <= 7)?
For such a line (V, b, d, offset) and a missed tangle U' ~ b (same rho_2 covector up to a unit, different tangle), the line
(V, U', d, offset) has the SAME J at every point (J depends on the covector only) but possibly different knots, and it was
never classified or certified.  Read-only on regress/ and cert/run/; writes critic/missed/."""
import json, pickle, glob
from collections import Counter, defaultdict
g = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/out/dedup/geo_bfs_d7.json'))
missed = [m for m in g['bottom']['missed'] if 'missed_word' in m]
res = {}
for D in (5, 6):
    by_rep = defaultdict(list)
    for m in missed:
        if m['depth'] <= D: by_rep[m['mitm_rep']].append(m['missed_word'])
    nmiss = sum(len(v) for v in by_rep.values())
    lines = Counter(); planes = Counter(); ex = []; lines_list = []
    for f in sorted(glob.glob('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/census_%d_%d_w*.pkl' % (D, D))):
        st, units, pls = pickle.load(open(f, 'rb'))
        for u in units:
            kind, wt, wb, d, m0, n0 = u[:6]
            if wb in by_rep:
                for U in by_rep[wb]:
                    lines[(kind, d)] += 1
                    lines_list.append([wt, U, wb, list(d), m0, n0, kind])
                    if len(ex) < 12: ex.append((kind, wt, wb, U, d, m0, n0))
        for p in pls:
            wt, wb, nz, Sv, Sw, isunit = p
            if isunit and wb in by_rep:
                planes['unit_plane'] += len(by_rep[wb])
    res[D] = {'missed_classes_depth_le_D': nmiss, 'reps_with_missed': len(by_rep),
              'missed_unit_lines_by_kind_dir': {str(k): v for k, v in lines.items()},
              'missed_unit_lines_total': sum(lines.values()), 'missed_unit_planes': planes['unit_plane'], 'examples': ex}
    json.dump(lines_list, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/missed_lines_%d_%d.json' % (D, D), 'w'))
json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/missed_lines_summary.json', 'w'), indent=1)
for D in res:
    r = res[D]; print(D, {k: v for k, v in r.items() if k != 'examples'})
    for e in r['examples'][:6]: print('   ', e)
