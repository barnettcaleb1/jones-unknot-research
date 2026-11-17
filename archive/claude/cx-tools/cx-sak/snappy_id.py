import sys, json, glob
sys.path.insert(0, '/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/work/braid_classification/packages')
import snappy, spherogram
for tag in sys.argv[1:]:
    f = '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak/out/%s_sakuma_proj0.json' % tag
    d = json.load(open(f))
    pd = [[e - 1 for e in x] for x in d['pd']['pd']]   # spherogram wants 0-based? it accepts any labels
    L = spherogram.Link(pd)
    L.simplify('global')
    M = L.exterior()
    try:
        vol = M.volume()
    except Exception as e:
        vol = 'err %s' % e
    try:
        ident = M.identify()
    except Exception as e:
        ident = 'err %s' % e
    print("%s: simplified to %d crossings, %d components; volume %s; identify %s" % (tag, len(L.crossings), len(L.link_components), vol, ident), flush=True)
    # linking number and sublink unknottedness via spherogram
    print("   linking matrix", L.linking_matrix())
