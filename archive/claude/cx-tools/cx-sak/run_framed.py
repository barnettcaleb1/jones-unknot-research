import sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import templates, pipeline, kb
snape_h1 = {-9:1,-7:-3,-5:4,-3:-3,-1:3,1:-1,5:2,7:-2,9:2,11:-1}
snape_h2 = {-k:c for k,c in snape_h1.items()}
wp, mk, meta = templates.build_I1([2], [1], rot_side=True)
for n in [-3,-2,-1,0,1,2,3]:
    r = pipeline.run('fig8_framed_%d' % n, wp, mk, meta, verbose=False, framing=n)
    J = r['JS']
    print("framing %2d: %3d cr lk(B,L)=%g  J=%s   match h1:%s h2:%s" % (n, r['ncrossS'], r['lkBL'], kb.poly_str_q(J), J==snape_h1, J==snape_h2), flush=True)
