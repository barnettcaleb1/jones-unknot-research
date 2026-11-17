import json
from fractions import Fraction as Fr
LIT='/Users/calebbarnett/jones-lanes/theory-restart/lit/'
def load138():
    """Unified table of the 138 inversions.  specials: list of (c, d) with d = kht++ label level (delta_);
    block of a special for the a(0)-pairing sits at q = c + {-5,-1,1,5}, delta = d - 1/2.
    rational: k, qr (mean q), dr (delta| in current-build convention), j."""
    k138 = {}
    for l in open(LIT+'kht/out/k138/k138.jsonl'):
        r = json.loads(l)
        k138[r['file']] = r
    d = json.load(open(LIT+'kwz-inversions/data.json'))
    out = []
    for inv in d['inversions']:
        name = inv['name']
        k = inv['rational_component']['slope_k']
        qr = Fr(inv['rational_component']['bigrading']['q_average'])
        dr_site = Fr(inv['rational_component']['bigrading']['delta'])
        sp = []
        for s in inv['special_components']:
            a = Fr(s['kappa_shift_h']); b = Fr(s['kappa_shift_delta'])
            c = 2*(a+b); dlab = b + Fr(1,2)
            sp += [(int(c), int(dlab))]*s['multiplicity']
        j = (qr - Fr(k*(abs(k)+2), abs(k)+1))/24
        assert j.denominator == 1, (name, j)
        rec = dict(name=name, knot=inv['knot'], k=k, j=int(j), qr=qr, dr=dr_site + Fr(1,2), specials=sorted(sp), src='site')
        r = k138.get(name)
        if r and 'khr' in r:
            rat = [c for c in r['khr'] if c['type']=='r'][0]
            sp2 = sorted((int(c['q']), int(c['delta'])) for c in r['khr'] if c['type']=='s')
            rec['chk_specials'] = (sp2 == rec['specials'])
            rec['chk_rat'] = (int(rat['slope']) == k and abs(float(qr) - rat['q']) < 1e-6)
            rec['chk_dr'] = (float(rec['dr']) == rat['delta'])
            rec['dr_build'] = rat['delta']
        out.append(rec)
    return out
if __name__ == '__main__':
    t = load138()
    print(len(t))
    print('specials agree:', sum(1 for r in t if r.get('chk_specials')), 'rat agree:', sum(1 for r in t if r.get('chk_rat')), 'dr agree:', sum(1 for r in t if r.get('chk_dr')), 'with build data:', sum(1 for r in t if 'chk_specials' in r))
    for r in t:
        if 'chk_specials' in r and not (r['chk_specials'] and r['chk_rat'] and r['chk_dr']):
            print('MISMATCH', r['name'], r['chk_specials'], r['chk_rat'], r['chk_dr'], r['dr'], r.get('dr_build'), r['specials'][:3])
    print(t[0])
