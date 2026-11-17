#!/usr/bin/env python3
import sys, os, glob, json, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/py')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/scripts')
from bcube import *
import khtparse

SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si'

def N_from_chainfile(path):
    """list of (h,q) of the b-generators of BN~"""
    out = []
    for line in open(path, encoding='utf-8'):
        r = khtparse.parse_line(line)
        if not r:
            continue
        h, q, gens, arrows, rest = r
        gl, cyc, ok = khtparse.gens_with_gradings(h, q, gens, arrows)
        for idem, hh, qq in gl:
            if idem == '⬮':
                out.append((hh, qq))
    return out

def euler(pts):
    P = collections.defaultdict(int)
    for h, q in pts:
        P[q] += (-1) ** (h % 2)
    return {e: c for e, c in P.items() if c}

def match_shift(Pcube, PN):
    """PN(q) = eps * q^shift * Pcube(q).  returns (shift, eps) or None"""
    if not Pcube or not PN:
        return None
    s = max(PN) - max(Pcube)
    for eps in (1, -1):
        if all(PN.get(e + s, 0) == eps * c for e, c in Pcube.items()) and len(PN) == len(Pcube):
            return s, eps
    return None

def analyse(name, verbose=False):
    half, orient, sym = read_kht(os.path.join(SI, name + '.kht'))
    word, lab, wr = quotient_word(half, with_twists=False)
    ncr = len(crossings_of(word))
    ntw = 2 * abs(wr)
    xtw = wr > 0
    rec = dict(name=name, half='.'.join('%s%d' % t for t in half), writhe=wr, ncr=ncr)
    Pc = b_bracket(word)
    chain = os.path.join(SI, name, 'cxBNr-c2-qs')
    if not os.path.exists(chain):
        rec['err'] = 'no chain file'
        return rec
    Npts = N_from_chainfile(chain)
    PN = euler(Npts)
    ms = match_shift(Pc, PN)
    rec['dimN'] = len(Npts)
    if ms is None:
        rec['err'] = 'euler mismatch'
        rec['Pc'] = sorted(Pc.items()); rec['PN'] = sorted(PN.items())
        return rec
    shift, eps = ms
    base = shift - (ntw if xtw else 0)       # n_+ - 2 n_-
    ntot = ncr + ntw
    nminus3 = ntot - base
    if nminus3 % 3:
        rec['err'] = 'n_- not integral'
        return rec
    nminus = nminus3 // 3
    hshift = (ntw if xtw else 0) - nminus
    rec['qshift'] = shift; rec['hshift'] = hshift
    # N in cube coordinates
    Ncube = sorted((h - hshift, q - shift) for h, q in Npts)
    qs = [q for h, q in Ncube]
    qmaxN, qminN = max(qs), min(qs)
    rec['N_top'] = sorted(h for h, q in Ncube if q == qmaxN)
    rec['N_bot'] = sorted(h for h, q in Ncube if q == qminN)
    rec['qmaxN'] = qmaxN; rec['qminN'] = qminN
    for sign, tag in ((1, 'top'), (-1, 'bot')):
        M, st = extreme_states(word, sign=sign)
        betti, sizes = extreme_homology(st)
        rec[tag + '_M'] = M
        rec[tag + '_nE'] = len(st)
        rec[tag + '_betti'] = {h: b for h, b in betti.items() if b}
        rec[tag + '_gap'] = (M - qmaxN) if sign > 0 else (qminN - M)
        # is the all-ones (resp. all-zeros) state of type b?
        allst = [b for (b, o, c) in st if o == (ncr if sign > 0 else 0)]
        rec[tag + '_allstate_extreme'] = bool(allst)
        # number of maximal elements of E (top: maximal in cube order; bottom: minimal)
        S = set(b for (b, o, c) in st)
        nmax = 0
        for b in S:
            ismax = True
            for j in range(len(b)):
                if b[j] == (0 if sign > 0 else 1):
                    b2 = b[:j] + ((1 if sign > 0 else 0),) + b[j + 1:]
                    if b2 in S:
                        ismax = False; break
            nmax += ismax
        rec[tag + '_nmaximal'] = nmax
    return rec

if __name__ == '__main__':
    names = sys.argv[1:] or sorted(os.path.basename(f)[:-4] for f in glob.glob(SI + '/*.kht'))
    out = open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/states/survey.jsonl', 'a') if len(sys.argv) == 1 else None
    for nm in names:
        try:
            rec = analyse(nm)
        except Exception as ex:
            rec = dict(name=nm, err=repr(ex))
        print(json.dumps(rec))
        sys.stdout.flush()
        if out:
            out.write(json.dumps(rec) + '\n'); out.flush()
