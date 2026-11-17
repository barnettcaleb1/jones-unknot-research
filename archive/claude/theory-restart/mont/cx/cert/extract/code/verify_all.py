"""Independent replay of every certificate.  For each set TAG:
  stage 1: data/TAG_certificates.jsonl.gz : replay the word moves (reduce.apply_move checks every move); CERT_c_empty needs the
           empty word; CERT_a_TS24 needs <= 24 crossings and exact V_K = 1 of the reduced diagram.
  stage 2/3: data/TAG_stage{2,3}.json : replay the alternative-word log (if any) from the reduced word, then the PD move log
           (pd.replay checks every R1/R2/R3); CERT_c_pd needs 0 crossings; CERT_a_pd_TS24 needs <= 24 and exact V_K = 1.
usage: verify_all.py TAG [STAGE_FILE]"""
import sys, json, gzip
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import rules, reduce as R, vk, pd as PDm, tietze, tietze2
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/'
def hw_of(w): return 's.l1.l1.' + rules.dec(w) + '.u2.u2' if w else 's.l1.l1.u2.u2'
def replay_alt(w, log):
    w = tuple(w)
    for mv in log:
        if mv[0] == 'insT': w = rules.TOPPAT[mv[1]][0] + w
        elif mv[0] == 'insB': w = w + rules.BOTPAT[mv[1]][0]
        else: w = R.apply_move(w, tuple(mv))
    return w
def check_stage1(tag):
    st = Counter()
    with gzip.open(D + tag + '_certificates.jsonl.gz', 'rt') as f:
        for line in f:
            c = json.loads(line)
            w = rules.enc(c['word'].split('.') if c['word'] else [])
            r = R.replay(w, [tuple(m) for m in c['moves']])
            assert rules.dec(r) == c['reduced'], c['word']
            if c['status'] == 'CERT_c_empty': ok = (r == ())
            elif c['status'] == 'CERT_a_TS24': ok = (vk.ncross(hw_of(r)) <= 24 and vk.VK(hw_of(r)) == {0: 1})
            else: ok = None
            st[(c['status'], ok)] += 1
    return st
def check_stage(fname):
    st = Counter()
    for r in json.load(open(D + fname)):
        s = r['status']
        if s == 'CERT_b_tietze':
            x = r['stage3']; hw = x['tietze_word']
            if 'alt_word_log' in x:
                w0 = rules.enc(r['reduced_halfword'][len('s.l1.l1.'):-len('.u2.u2')].split('.')) if r['reduced_halfword'] != 's.l1.l1.u2.u2' else ()
                assert hw_of(replay_alt(w0, [tuple(m) for m in x['alt_word_log']])) == hw
            else: assert hw in (r['reduced_halfword'], r['halfword'])
            if x.get('tietze_version', 1) == 2: g, rest = tietze2.replay2(hw, x['tietze_direction'], x['tietze_log'])
            else: g, rest = tietze.replay_dir(hw, x['tietze_direction'], [(tuple(k), gg) for k, gg in x['tietze_log']])
            st[(s, len(g) == 1 and not rest)] += 1; continue
        if s not in ('CERT_c_pd', 'CERT_a_pd_TS24'): st[(s, None)] += 1; continue
        if 'stage3' in r and r['stage3']['status'] == s:
            x = r['stage3']
            w0 = rules.enc(r['reduced_halfword'][len('s.l1.l1.'):-len('.u2.u2')].split('.')) if r['reduced_halfword'] != 's.l1.l1.u2.u2' else ()
            w1 = replay_alt(w0, [tuple(m) for m in x['alt_word_log']])
            assert hw_of(w1) == x['alt_halfword']
            hw, log = x['alt_halfword'], x['pd_log']
        else: hw, log = r['reduced_halfword'], r['pd_log']
        n = PDm.replay(hw, log)
        ok = (n == 0) if s == 'CERT_c_pd' else (n <= 24 and vk.VK(hw) == {0: 1})
        st[(s, ok)] += 1
    return st
if __name__ == '__main__':
    tag = sys.argv[1]
    print(tag, 'stage1', dict(check_stage1(tag)))
    for fn in sys.argv[2:]: print(tag, fn, dict(check_stage(fn)))
