"""make_residue_words.py -- word lists for the residue certification (from cert/extract/residue_S*.json, read-only):
  out/residues/words_S{1,2,3}.json = [[tag, halfword], ...], every distinct ORIGINAL halfword (tag 'orig') and every distinct
  REDUCED halfword not already an original (tag 'red'); S3 keeps window and unit_lines words in one list."""
import json, os
EX = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract'
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/out/residues'
for s in ('S1', 'S2', 'S3'):
    d = json.load(open(os.path.join(EX, 'residue_%s.json' % s)))
    seen = {}; items = []
    for x in d:
        for w in x['original_halfwords']:
            if w not in seen: seen[w] = 'orig'; items.append(['orig', w])
    for x in d:
        w = x['reduced_halfword']
        if w not in seen: seen[w] = 'red'; items.append(['red', w])
    json.dump(items, open(os.path.join(OUT, 'words_%s.json' % s), 'w'))
    print(s, 'entries', len(d), 'orig', sum(1 for t, w in items if t == 'orig'), 'red (new)', sum(1 for t, w in items if t == 'red'), 'total', len(items))
