"""combine the two Q5 batches by seed and summarise"""
import pickle, collections
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
A = pickle.load(open(RG + 'rg_q5_lpJ.pkl', 'rb'))
try: A += pickle.load(open(RG + 'rg_q5_lpJ_c.pkl', 'rb'))
except Exception: pass
try: B = pickle.load(open(RG + 'rg_q5_lpJ_b.pkl', 'rb'))
except Exception: B = []
by = {}
for r in A + B: by[r['seed']] = r
out = list(by.values())
sj = [o['spanJ'] for o in out if o['spanJ'] is not None]
print('distinct closures', len(out), '| lp.J units', sum(o['J_unit'] for o in out), '| J None', sum(o['J_none'] for o in out),
      '| lp.J == vector calculus', sum(o['agree'] for o in out),
      '| forced Lemma-W coincidence', sum(o['forced'] for o in out),
      '| H', sum(o['fam'] == 'H' for o in out), 'V', sum(o['fam'] == 'V' for o in out))
print('by tag', dict(collections.Counter(o['tag'] for o in out)))
print('by closure parameter', sorted(collections.Counter((o['fam'], o['par']) for o in out).items()))
print('min span J', min(sj), ' span J histogram (lowest):', sorted(collections.Counter(sj).items())[:8])
print('lp.J time total %.0fs, max %.1fs' % (sum(o['t'] for o in out), max(o['t'] for o in out)))
