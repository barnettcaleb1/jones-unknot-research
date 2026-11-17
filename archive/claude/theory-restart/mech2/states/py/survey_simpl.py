#!/usr/bin/env python3
import sys, os, glob, json, collections, re
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
from bcube import *
from survey import N_from_chainfile, euler, match_shift, SI

def simplified_word(name):
    for l in open(os.path.join(SI, name + '.kht')):
        m = re.search(r"Simplifies with options '-qs' to (\S+)", l)
        if m:
            return parse_word(m.group(1))
    return None

def analyse(name):
    word = simplified_word(name)
    rec = dict(name=name)
    if word is None:
        rec['err'] = 'no simplified word'; return rec
    ncr = len(crossings_of(word)); rec['ncr'] = ncr
    Pc = b_bracket(word)
    chain = os.path.join(SI, name, 'cxBNr-c2-qs')
    if not os.path.exists(chain):
        rec['err'] = 'no chain file'; return rec
    Npts = N_from_chainfile(chain)
    PN = euler(Npts)
    ms = match_shift(Pc, PN)
    if ms is None:
        rec['err'] = 'euler mismatch'; return rec
    shift, eps = ms
    qs = [q - shift for h, q in Npts]
    qmaxN, qminN = max(qs), min(qs)
    for sign, tag in ((1, 'top'), (-1, 'bot')):
        M, st = extreme_states(word, sign=sign)
        betti, sizes = extreme_homology(st)
        rec[tag + '_M'] = M; rec[tag + '_nE'] = len(st)
        rec[tag + '_betti'] = {h: b for h, b in betti.items() if b}
        rec[tag + '_gap'] = (M - qmaxN) if sign > 0 else (qminN - M)
    return rec

if __name__ == '__main__':
    names = sys.argv[1:] or sorted(os.path.basename(f)[:-4] for f in glob.glob(SI + '/*.kht'))
    out = open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey_simpl.jsonl', 'w') if len(sys.argv) == 1 else None
    for nm in names:
        try:
            rec = analyse(nm)
        except Exception as ex:
            rec = dict(name=nm, err=repr(ex))
        print(json.dumps(rec)); sys.stdout.flush()
        if out:
            out.write(json.dumps(rec) + '\n'); out.flush()
