import sys, json, time
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
sys.path.insert(0, '/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/work/braid_classification/packages')
import templates, pipeline, kb
import spherogram
n = int(sys.argv[1])
which = sys.argv[2] if len(sys.argv) > 2 else 'both'
p, q = 32 * n * n - 1, 16 * n * n + 2 * n
# independent 2-bridge reference: K(p/q) and its mirror K(p/(p-q)) from spherogram rational tangles
refs = {}
for lab, qq in (('K(p/q)', q), ('K(p/(p-q))', p - q)):
    T = spherogram.RationalTangle(p, qq)
    Kref = T.numerator_closure()
    pdr = [list(x) for x in Kref.PD_code()]
    # spherogram PD uses 0-based labels in the same cyclic convention
    Vr, wr, mxr = kb.jones_from_pd([[e + 1 for e in x] for x in pdr])
    refs[lab] = Vr
    print("reference %s: %d crossings, V = %s" % (lab, len(pdr), kb.jones_str(Vr)), flush=True)
cases = []
if which in ('both', '1'):
    cases.append(('n%d_inv1_I1_2_2_m%d_%d' % (n, 2 * n, n), [2, 2], [-2 * n, n]))
if which in ('both', '2'):
    cases.append(('n%d_inv2_I1_m%d_%d_m1_m1' % (n, 2 * n, 4 * n), [-2 * n, 4 * n], [-1, -1]))
out = {}
for tag, al, cs in cases:
    t0 = time.time()
    wp, mk, meta = templates.build_I1(al, cs, rot_side=True)
    r = pipeline.run(tag, wp, mk, meta, verbose=True)
    match = [lab for lab, Vr in refs.items() if Vr == r['VK']]
    print("%s: K matches reference %s ; det(K)=%s (expected %d); x=%d" % (tag, match, r['detK'], p, r['x']), flush=True)
    print("%s: S has %d crossings, lk(B,L)=%g, projections agree=%s, L unknot=%s" % (tag, r['ncrossS'], r['lkBL'], r['allsame'], r['VL'] == {0: 1}), flush=True)
    print("%s: V_S = %s" % (tag, kb.jones_str(r['VS'])), flush=True)
    print("%s: VERDICT: %s" % (tag, "EQUALS 2-UNLINK" if r['unlink'] else "NOT the 2-unlink Jones polynomial"), flush=True)
    print("time %.1f s" % (time.time() - t0), flush=True)
    out[tag] = dict(VS=r['VS'], JS=r['JS'], VK=r['VK'], x=r['x'], detK=r['detK'], ncrossS=r['ncrossS'], lkBL=r['lkBL'], unlink=r['unlink'], match=match)
json.dump(out, open('/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak/out/pilot_n%d_%s_summary.json' % (n, which), 'w'), indent=1)
