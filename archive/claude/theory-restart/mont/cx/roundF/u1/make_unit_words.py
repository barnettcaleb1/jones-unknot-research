"""make_unit_words.py -- the 11,481 J = 1 S2 words exactly as stored by engineC2 (enum2_s1p_7, enum2_s2m_7, enum2_trp_7:
first letters a, B, d), translated to halfwords (translate.s2_halfword: event-level (V)+(R), asserted equal to the closed
form).  Also the mirror copies (enum2_s1m_7, enum2_trm_7: first letters A, D) as a bonus set.  Writes [tag, halfword] lists."""
import sys, os, json, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR
C2 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2'
main = []; mirr = []
for f, dst in [('enum2_s1p_7.pkl', main), ('enum2_s2m_7.pkl', main), ('enum2_trp_7.pkl', main),
               ('enum2_s1m_7.pkl', mirr), ('enum2_trm_7.pkl', mirr)]:
    res, units, n = pickle.load(open(os.path.join(C2, f), 'rb'))
    for w, triv in units:
        h = TR.s2_halfword(w); assert h == TR.s2_halfword_closed(w)
        dst.append([w, h])
json.dump(main, open(os.path.join(HERE, 'out', 'words_s2_units.json'), 'w'))
json.dump(mirr, open(os.path.join(HERE, 'out', 'words_s2_mirror_units.json'), 'w'))
print('main', len(main), 'distinct halfwords', len(set(h for w, h in main)), '| mirror', len(mirr))
