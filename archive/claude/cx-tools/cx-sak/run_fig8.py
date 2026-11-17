import sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak')
import templates, pipeline, kb
rot_side = (sys.argv[1] == '1')
wp, mk, meta = templates.build_I1([2], [1], rot_side=rot_side)
r = pipeline.run('fig8_I1_2_1_rot%d' % rot_side, wp, mk, meta)
print("rot_side", rot_side, "Jones(K)=", kb.jones_str(r['VK']), "writhe", r['x'])
