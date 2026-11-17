"""Extract the stored J = 1 words of finished E3 reruns: out/<run>.json -> ../cert/words_<run>.json ([tag, halfword] pairs,
tag = run|where|count|kcert-verdict).  usage: u4_words.py RUN [RUN ...]   (RUN e.g. e3_n12_s112)"""
import sys, json
D = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/'
import time
def load_complete(path, tries=120):
    # the rerun may still be writing its (large) JSON: retry until it parses (a truncated JSON object never parses)
    for i in range(tries):
        try: return json.load(open(path))
        except (json.JSONDecodeError, ValueError): time.sleep(2)
    raise SystemExit('could not parse %s' % path)
for run in sys.argv[1:]:
    d = load_complete(D + 'e3/out/%s.json' % run)
    L = [['%s|%s|%d|%s' % (run, e['where'], e['count'], e['kcert'][0]), w] for w, e in d['j1_words'].items()]
    json.dump(L, open(D + 'cert/words_%s.json' % run, 'w'))
    print(run, 'evals', d['evals'], 'budget_reached', d['u45']['budget_reached'], 'wall', d['u45']['wall'],
          'J=1 distinct', len(L), 'probes', d['u45']['n_j1_probes'])
