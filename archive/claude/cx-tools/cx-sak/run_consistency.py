import sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import templates, pipeline, kb
res = {}
cases = [('unknot_I1_0_0', [0], [0]), ('unknot_I1_1_0', [1], [0]), ('unknot_I1_2_0', [2], [0]), ('unknot_I1_m1_0', [-1], [0]),
         ('fig8_I1_2_1', [2], [1]), ('fig8_I1_m2_m1', [-2], [-1])]
for tag, al, cs in cases:
    wp, mk, meta = templates.build_I1(al, cs, rot_side=True)
    r = pipeline.run(tag, wp, mk, meta, verbose=False)
    res[tag] = r
    print("%-16s K: %-32s x=%3d  S: %3d cr, lk=%g, unlink=%s  V_S=%s" % (tag, kb.jones_str(r['VK']), r['x'], r['ncrossS'], r['lkBL'], r['unlink'], kb.jones_str(r['VS'])), flush=True)
print("fig8 pair mirror?", res['fig8_I1_2_1']['VS'] == kb.mirror(res['fig8_I1_m2_m1']['VS']))
# robustness of fig8 under eps/h/spacing changes
wp, mk, meta = templates.build_I1([2], [1], rot_side=True)
for (sp, h, eps, bw) in [(0.0025, 0.4, 0.1, 0.6), (0.005, 0.5, 0.12, 0.7), (0.005, 0.3, 0.05, 0.5)]:
    r = pipeline.run('fig8_var_%g_%g_%g' % (sp, h, eps), wp, mk, meta, spacing=sp, h=h, eps=eps, bumpw=bw, verbose=False)
    print("fig8 variant spacing=%g h=%g eps=%g: V_S same as baseline? %s  (ncross %d)" % (sp, h, eps, r['VS'] == res['fig8_I1_2_1']['VS'], r['ncrossS']), flush=True)
