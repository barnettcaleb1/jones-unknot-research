"""hitpath_test.py -- exercise the COUNTEREXAMPLE / bracket-disagreement paths of the FIXED certify.py by monkeypatching
brackets on a known nontrivial knot (the trefoil s.l1.y0.x1.u2), and the HIT-file writer into a TEST directory.
usage: hitpath_test.py OUT.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import certify, diagram, replay
certify.ALARM_DIR = os.path.join(os.path.dirname(HERE), 'out', 'validation', 'hit_writer_test')   # test alarms kept apart
TREF = 's.l1.y0.x1.u2'
res = {}
real_jones, real_vkp = diagram.jones, certify._vk_project
# (1) no patch
st, info = certify.certify(TREF, write_hits=False, tietze_budget=0.3)
res['plain'] = (st, info['notes'])
# (2) PD bracket faked to 1: Tietze tried (5 seeds), rep found, project + third bracket say V != 1 -> CERTIFIED_NONTRIVIAL + BUG note
diagram.jones = lambda pd: {0: 1}
st, info = certify.certify(TREF, write_hits=False, tietze_budget=0.3)
res['pd_faked'] = (st, info['notes'], info.get('tietze'))
# (3) PD + project faked to 1 -> COUNTEREXAMPLE (write_hits=False: no file)
certify._vk_project = lambda hw: {0: 1}     # certify's view only; the checker keeps the real bracket
st, info = certify.certify(TREF, write_hits=False, tietze_budget=0.3)
res['pd_and_project_faked'] = (st, info['notes'])
# (4) ONLY the project bracket faked (PD says V != 1): before the fix this was a silent CERTIFIED_NONTRIVIAL (audit-1 F3)
diagram.jones = real_jones
st, info = certify.certify(TREF, write_hits=False, tietze_budget=0.3)
res['project_only_faked'] = (st, info['notes'])
# (5) the HIT writer itself, into a test directory
tdir = os.path.join(os.path.dirname(HERE), 'out', 'validation', 'hit_writer_test'); os.makedirs(tdir, exist_ok=True)
certify.HIT_DIR = tdir
st, info = certify.certify(TREF, write_hits=True, tietze_budget=0.3)
res['hit_writer'] = (st, info.get('hit_file'))
certify._vk_project = real_vkp
txt = open(info['hit_file']).read() if info.get('hit_file') else ''
res['hit_file_has'] = {k: (k in txt) for k in ('halfword:', 'J (lp.J', 'V_K (PD', 'V_K (project', 'V_K (third', 'Delta_K', 'certificate')}
ok = (res['plain'][0] == 'CERTIFIED_NONTRIVIAL' and res['pd_faked'][0] == 'CERTIFIED_NONTRIVIAL'
      and any('BUG' in n for n in res['pd_faked'][1]) and res['pd_and_project_faked'][0] == 'COUNTEREXAMPLE'
      and res['project_only_faked'][0] == 'COUNTEREXAMPLE' and res['hit_writer'][0] == 'COUNTEREXAMPLE'
      and all(res['hit_file_has'].values()))
res['ALL_AS_EXPECTED'] = ok
print(json.dumps(res, indent=1, default=str))
json.dump(res, open(sys.argv[1], 'w'), indent=1, default=str)
