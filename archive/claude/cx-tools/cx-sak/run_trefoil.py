import sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import templates, pipeline, kb
res = {}
for tag, al, cs in [('tref_I1_1_m1', [1], [-1]), ('tref_I1_m1_1', [-1], [1]), ('tref_I1_2_m1', [2], [-1]), ('tref_I1_m2_1', [-2], [1]), ('I1_1_1', [1], [1]), ('I1_2_2', [2], [2])]:
    wp, mk, meta = templates.build_I1(al, cs, rot_side=True)
    r = pipeline.run(tag, wp, mk, meta, verbose=False)
    res[tag] = r
    print("%-14s K: %-28s det=%g x=%3d  S: %3d cr, lk=%g, unlink=%s  V_S=%s" % (tag, kb.jones_str(r['VK']), r['detK'], r['x'], r['ncrossS'], r['lkBL'], r['unlink'], kb.jones_str(r['VS'])), flush=True)
    print("               J_S(q) =", kb.poly_str_q(r['JS']), flush=True)
