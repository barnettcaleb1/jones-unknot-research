"""C1's witnesses for ALL 4,400 'BOTH' signatures (46,771 boxes), regenerated with C1's own search (read-only import) and
re-checked EXACTLY in my framework; plus my own generator verdict.  Single process (no pool), one result file per
signature in rg_results_sig/ (index = position in the 'both' list of gen2_res.pkl), resumable; counts from files only."""
import sys, os, time, pickle, collections
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_gen as G
import rg_q4_boxes as Q4
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
C1 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
OUT = RG + 'rg_results_sig/'
def both_list():
    Gr = pickle.load(open(C1 + '/gen2_res.pkl', 'rb'))
    sigs = Gr['sigs']; resV = Gr['resV']; resH = Gr['resH']
    return [k for k in sigs if resV[k][0] and all(not v for v in resH[k].values())], sigs
def main():
    os.makedirs(OUT, exist_ok=True)
    G.load_gtab(RG + 'rg_gtab.pkl')
    both, sigs = both_list()
    t0 = time.time(); k = 0
    for i, key in enumerate(both):
        fn = OUT + '%d.pkl' % i
        if os.path.exists(fn): continue
        r = Q4.verify_sig({'top': key[0], 'bot': key[1]}, key[2], key[3], 1)
        r['key'] = key; r['nbox'] = len(sigs[key])
        tmp = fn + '.tmp'
        pickle.dump(r, open(tmp, 'wb')); os.replace(tmp, fn); k += 1
        if k % 200 == 0: print('  %d signatures, %.0fs' % (k, time.time() - t0), flush=True)
    status()
def status():
    both, sigs = both_list()
    rs = []
    for i, key in enumerate(both):
        fn = OUT + '%d.pkl' % i
        if os.path.exists(fn):
            r = pickle.load(open(fn, 'rb'))
            assert r['key'] == key
            rs.append(r)
    print('signatures with results: %d/%d (boxes %d/%d)' % (len(rs), len(both), sum(r['nbox'] for r in rs),
          sum(len(sigs[k]) for k in both)))
    print('own generator proves all classes: %d signatures' % sum(not r['mine_open'] for r in rs))
    print('C1 witnesses regenerated %d; pass my exact re-check %d; FAIL %d; C1 rows != my rows %d; C1 no witness %d' % (
        sum(r['nwit'] for r in rs), sum(r['wit_ok'] for r in rs), sum(r['nbad'] for r in rs),
        sum(r['rows_diff'] for r in rs), sum(r['c1_none'] for r in rs)))
    bad = [r for r in rs if r['mine_open'] or r['nbad'] or r['c1_none']]
    for r in bad[:10]: print('  ISSUE', r['key'], r['mine_open'], r['wit_bad'], r['c1_none'])
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'status': status()
    else: main()
