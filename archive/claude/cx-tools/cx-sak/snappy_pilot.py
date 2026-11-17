import sys, json
sys.path.insert(0, '/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/work/braid_classification/packages')
import snappy, spherogram
for tag in sys.argv[1:]:
    d = json.load(open('/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak/out/%s_sakuma_proj0.json' % tag))
    L = spherogram.Link([list(x) for x in d['pd']['pd']])
    raw = len(L.crossings)
    L.simplify('global')
    comps = []
    for i in range(2):
        S = L.sublink([i]); S.simplify('global'); comps.append(len(S.crossings))
    print("%s: raw %d crossings -> simplified %d; linking matrix %s; sublinks simplify to %s crossings" % (tag, raw, len(L.crossings), L.linking_matrix(), comps), flush=True)
