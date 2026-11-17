"""make_control_words.py -- NONTRIVIAL CONTROLS: one representative word for every distinct non-unit J of engineC2's
S2 enumeration (the res dicts of enum2_s1p_7 / s2m_7 / trp_7).  J != 1 => Theta nontrivial => K nontrivial (the unknot
has a unique strong inversion, whose quotient theta-curve is trivial, J = 1).  So none of these may ever be certified
unknot.  Writes out/words_s2_controls.json as [tag, halfword]."""
import sys, os, json, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR
C2 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2'
out = []; seen = set()
for f in ['enum2_s1p_7.pkl', 'enum2_s2m_7.pkl', 'enum2_trp_7.pkl']:
    res, units, n = pickle.load(open(os.path.join(C2, f), 'rb'))
    for key, val in res.items():
        w = val[0]
        if w in seen: continue
        seen.add(w); out.append([w, TR.s2_halfword(w)])
json.dump(out, open(os.path.join(HERE, 'out', 'words_s2_controls.json'), 'w'))
print('controls', len(out))
