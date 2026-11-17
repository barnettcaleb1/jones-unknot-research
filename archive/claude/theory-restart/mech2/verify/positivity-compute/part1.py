#!/usr/bin/env python3
"""Part 1: all 138 saved half-diagrams. Own signs, own unit location, own cube counts; b-generators from k138.jsonl (jset)
and, where a chain file exists, from the chain file by the referee's parser."""
import sys, os, json, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import sidiag as S, khtio
import gtilde, alex          # brief's tools: jset (b-generators from Kh~ components); alex only for cross-checks

SI = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/'
JS = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/k138.jsonl'

# Alexander polynomials (half: coefficients from the top degree to the middle), Rolfsen table, written from memory.
ALEX = {
'3_1':[1,-1],'4_1':[1,-3],'5_1':[1,-1,1],'5_2':[2,-3],'6_1':[2,-5],'6_2':[1,-3,3],'6_3':[1,-3,5],
'7_1':[1,-1,1,-1],'7_2':[3,-5],'7_3':[2,-3,3],'7_4':[4,-7],'7_5':[2,-4,5],'7_6':[1,-5,7],'7_7':[1,-5,9],
'8_1':[3,-7],'8_2':[1,-3,3,-3],'8_3':[4,-9],'8_4':[2,-5,5],'8_5':[1,-3,4,-5],'8_6':[2,-6,7],'8_7':[1,-3,5,-5],
'8_8':[2,-6,9],'8_9':[1,-3,5,-7],'8_10':[1,-3,6,-7],'8_11':[2,-7,9],'8_12':[1,-7,13],'8_13':[2,-7,11],
'8_14':[2,-8,11],'8_15':[3,-8,11],'8_16':[1,-4,8,-9],'8_17':[1,-4,8,-11],'8_18':[1,-5,10,-13],'8_19':[1,-1,0,1],
'8_20':[1,-2,3],'8_21':[1,-4,5],
'9_1':[1,-1,1,-1,1],'9_2':[4,-7],'9_3':[2,-3,3,-3],'9_4':[3,-5,5],'9_5':[6,-11],'9_6':[2,-4,5,-5],'9_7':[3,-7,9],
'9_8':[2,-8,11],'9_9':[2,-4,6,-7],'9_10':[4,-8,9],'9_11':[1,-5,7,-7],'9_12':[2,-9,13],'9_13':[4,-9,11],
'9_14':[2,-9,15],'9_15':[2,-10,15],'9_16':[2,-5,8,-9],'9_17':[1,-5,9,-9],'9_18':[4,-10,13],'9_19':[2,-10,17],
'9_20':[1,-5,9,-11],'9_21':[2,-11,17],'9_22':[1,-5,10,-11],'9_23':[4,-11,15],'9_24':[1,-5,10,-13],'9_25':[3,-12,17],
'9_26':[1,-5,11,-13],'9_27':[1,-5,11,-15],'9_28':[1,-5,12,-15],'9_29':[1,-5,12,-15],'9_30':[1,-5,12,-17],
'9_31':[1,-5,13,-17],'9_32':[1,-6,14,-17],'9_33':[1,-6,14,-19],'9_34':[1,-6,16,-23],'9_35':[7,-13],
'9_36':[1,-5,8,-9],'9_37':[2,-11,19],'9_38':[5,-14,19],'9_39':[3,-14,21],'9_40':[1,-7,18,-23],'9_41':[3,-12,19],
'9_42':[1,-2,1],'9_43':[1,-3,2,-1],'9_44':[1,-4,7],'9_45':[1,-6,9],'9_46':[2,-5],'9_47':[1,-4,6,-5],
'9_48':[1,-7,11],'9_49':[3,-6,7]}
# genus table (KnotInfo three_genus, from memory); for these knots it equals half the span of the Alexander polynomial
GENUS = {k: len(v) - 1 for k, v in ALEX.items()}

def read_word(path):
    for line in open(path):
        line = line.strip()
        if line and not line.startswith('%') and line.startswith('s.'):
            return line
    raise ValueError(path)

def main():
    recs = {}
    for line in open(JS):
        r = json.loads(line); recs[r['file'].replace('^', '-')] = r
    rows = []
    names = sorted(os.path.basename(p)[:-4] for p in glob.glob(SI + '*.kht'))
    assert len(names) == 138 and set(names) == set(recs), (len(names), set(names) ^ set(recs))
    issues = collections.defaultdict(list)
    for name in names:
        word = read_word(SI + name + '.kht')
        knot = name.split('-')[0]
        half = S.parse(word)
        hs = S.half_signs(word)
        if hs is None:
            issues['not a knot'].append(name); continue
        K = hs['K']
        row = dict(name=name, word=word, knot=knot, c=hs['c'], c_axis=hs['c_axis'], c_off=hs['c_off'], wr=hs['wr'],
                   one_sign=hs['one_sign'])
        # cross-checks against the brief's alex.py (symmetrised word, total writhe)
        fa = alex.symmetrize(alex.parse(word))
        mine = [(('l' if t[0] == 'cap' else t[0]), t[1]) for t in S.full_word(half)]
        theirs = [(('l' if c in 'lr' else c), i) for c, i in fa]
        if mine != theirs:
            issues['symmetrised word differs from alex.py'].append(name)
        if alex.writhe(word) != K.writhe():
            issues['total writhe differs from alex.py'].append(name)
        # the letters of axis crossings must fix the sign: y0 negative, x0 positive
        for (cc, s, sg) in hs['signs']:
            if s == 0 and sg != (-1 if cc == 'y' else 1):
                issues['axis crossing sign rule violated'].append(name)
        # Alexander polynomial and genus
        ap = K.alexander_poly()
        g_alex = (len(ap) - 1) // 2
        top = ap[::-1][:g_alex + 1]
        tab = ALEX[knot]
        sgn = 1 if top[0] * tab[0] > 0 else -1
        row['alex_ok'] = ([sgn * x for x in top] == tab) and ap == ap[::-1]
        if not row['alex_ok']:
            issues['Alexander polynomial differs from table'].append((name, ap))
        row['g'] = GENUS[knot]; row['g_alex'] = g_alex; row['g_diag'] = K.diagram_genus()
        # saved quotient picture: compare with my band word (with wr twist pairs)
        svg = SI + name + '/' + name + '-q.svg'
        if os.path.exists(svg):
            lev = khtio.svg_levels(svg)
            if lev != S.band_word(half, twists=hs['wr']):
                issues['quotient word in saved svg differs from band_word(wr)'].append(name)
            row['svg'] = True
        else:
            row['svg'] = False
        # b-generators from the saved Kh~ components (jset) and from the chain file
        r = recs[name]
        row['has_kht'] = bool(r.get('khr'))
        c, wr = hs['c'], hs['wr']
        # my own cube counts for the twist-free band diagram (done for all 138, also without kht++ output)
        cnt = S.cube_counts(S.band_word(half, 0))
        assert set(cnt) <= {S.TYPE_B, S.TYPE_C}
        cb = cnt.get(S.TYPE_B, {})
        Pc = S.euler_from_counts(cb)
        uc = S.unit_of(Pc)
        row['unit_cube'] = uc
        if uc != (1, 2 * c - 4 * wr):
            issues['cube unit != (+, 2c-4wr)'].append((name, uc, 2 * c - 4 * wr))
        M = max(a + kk for (a, kk) in cb); m = min(a - kk for (a, kk) in cb)
        row['M'] = M; row['m'] = m
        row['Etop'] = sum(v for (a, kk), v in cb.items() if a + kk == M)
        row['Ebot'] = sum(v for (a, kk), v in cb.items() if a - kk == m)
        row['d0'] = 2 * c - 4 * wr
        row['Jcube'] = {e - uc[1]: v * uc[0] for e, v in Pc.items()} if uc else None
        if not row['has_kht']:
            issues['no kht++ output in k138.jsonl'].append(name)
            rows.append(row); continue
        js = gtilde.jset(r['khr']) if gtilde.valid(r['khr']) else None
        if js is None:
            issues['jset not applicable'].append(name); rows.append(row); continue
        k, j, pts = js
        gens = []
        for (q, d) in pts:
            h2 = q - 2 * d
            assert h2 % 2 == 0
            gens.append((h2 // 2, q))
        gens.sort()
        row['k'] = k; row['j'] = j; row['gens'] = gens
        chain = SI + name + '/cxBNr-c2-qs'
        if os.path.exists(chain):
            gb = khtio.b_generators(chain)
            row['chain'] = True
            if gb != gens:
                issues['jset differs from chain file'].append((name, gens, gb))
        else:
            row['chain'] = False
        P = {}
        for (h, q) in gens:
            S.padd(P, {q: (-1) ** (h % 2)})
        row['P'] = P
        u = S.unit_of(P)
        row['unit'] = u
        if u is None:
            issues['chi(N) is not a unit mod (q^2+1)^2'].append(name); continue
        if u != (1, 24 * j):
            issues['unit from congruence != (+, 24 j)'].append((name, u, 24 * j))
        d = u[1]
        row['d'] = d
        row['coef_at_unit'] = P.get(d, 0)
        row['gens_at_unit_q'] = [g for g in gens if g[1] == d]
        row['unit_gen'] = (8 * j, 24 * j) in gens
        qs = [q for h, q in gens]
        row['qmin'] = min(qs); row['qmax'] = max(qs)
        # same J from both sources?
        if uc is not None:
            J1 = {e - d: v * u[0] for e, v in P.items()}
            if J1 != row['Jcube']:
                issues['J from kht data != J from my cube state sum'].append(name)
            row['J'] = J1
        # the shift cube -> kht coordinates in q
        row['qshift'] = d - (2 * c - 4 * wr)
        rows.append(row)
    json.dump([{k: (v if k not in ('P', 'J', 'Jcube') else ({str(a): b for a, b in v.items()} if v else None)) for k, v in r.items()} for r in rows],
              open('part1_rows.json', 'w'))
    print('half-diagrams analysed:', len(rows))
    print('ISSUES:')
    for k, v in issues.items():
        print('  ', k, ':', len(v), v[:12])
    if not issues:
        print('   none')
    one = [r for r in rows if r['one_sign']]
    print('one-sign half-diagrams (|wr| = c by my signs):', len(one), ' negative:', sum(r['wr'] < 0 for r in one),
          ' positive:', sum(r['wr'] > 0 for r in one), ' without kht++ output:', [r['name'] for r in one if not r['has_kht']])
    print('genus: table == half span of my Alexander polynomial for all 138:', all(r['g'] == r['g_alex'] for r in rows),
          '; diagram genus == table genus on the one-sign ones:', all(r['g'] == r['g_diag'] for r in one))
    print()
    print('%-8s %-36s %3s %3s %2s %3s %3s %5s %5s %5s %5s %6s %5s %4s %s' % ('name', 'word', 'c', 'wr', 'g', 'k', 'j', 'd=24j', 'qmin', 'qmax', 'dist', 'coef@d', 'cube', '|E|', 'verdict'))
    bad = []; cube_bad = []
    for r in one:
        g = r['g']
        if r['wr'] < 0:
            cube_edge = r['d0'] - r['M']; E = r['Etop']
        else:
            cube_edge = r['m'] - r['d0']; E = r['Ebot']
        r['cube_edge'] = cube_edge; r['E'] = E
        if cube_edge != 2 * g:
            cube_bad.append(r['name'])
        if not r['has_kht']:
            print('%-8s %-36s %3d %3d %2d   -   -     -     -     -     -      - %5d %4d %s' % (r['name'], r['word'], r['c'], r['wr'], g, cube_edge, E, 'no kht++ output; cube count only'))
            continue
        d = r['d']
        if r['wr'] < 0:
            dist = d - r['qmax']; side = r['qmax'] < d
        else:
            dist = r['qmin'] - d; side = r['qmin'] > d
        ok = side and r['coef_at_unit'] == 0 and not r['gens_at_unit_q'] and dist == 2 * g and cube_edge == 2 * g
        r['dist'] = dist
        if not ok:
            bad.append(r['name'])
        print('%-8s %-36s %3d %3d %2d %3d %3d %5d %5d %5d %5d %6d %5d %4d %s' % (r['name'], r['word'], r['c'], r['wr'], g, r['k'], r['j'], d,
              r['qmin'], r['qmax'], dist, r['coef_at_unit'], cube_edge, E, 'ok' if ok else 'CHECK'))
    print('one-sign rows failing (support one-sided, no generator in the unit degree, distance = 2g):', bad)
    print('one-sign rows where the cube edge (d0 - M resp. m - d0) is not 2g:', cube_bad)
    json.dump([{k: v for k, v in r.items() if k not in ('P', 'J', 'Jcube', 'gens')} for r in one], open('part1_onesign.json', 'w'))
    # census numbers
    both = [r['name'] for r in rows if r['Etop'] == 1 and r['Ebot'] == 1]
    top = [r['name'] for r in rows if r['Etop'] == 1 and r['Ebot'] != 1]
    bot = [r['name'] for r in rows if r['Etop'] != 1 and r['Ebot'] == 1]
    nei = [r['name'] for r in rows if r['Etop'] != 1 and r['Ebot'] != 1]
    print()
    print('CENSUS by my cube counts (unique extreme type-b state = adequate end): both', len(both), both)
    print('  top (1-end) only:', len(top), ' bottom (0-end) only:', len(bot), ' neither:', len(nei))
    A = [r for r in rows if r['Etop'] == 1 or r['Ebot'] == 1]
    A_ok = [r for r in A if (r['Etop'] == 1 and r['M'] != r['d0']) or (r['Ebot'] == 1 and r['m'] != r['d0'])]
    print('  with at least one adequate end:', len(A), '; of these with the unit away from an adequate corner (Thm 2.3):', len(A_ok))
    sA = set(r['name'] for r in A_ok); sB = set(r['name'] for r in one)
    print('  one-sign:', len(sB), ' intersection:', len(sA & sB), sorted(sA & sB), ' UNION:', len(sA | sB))
    print('  not covered:', len(rows) - len(sA | sB))
    for r in rows:
        for key in ('Etop', 'Ebot'):
            e = r[key]
            if e & (e - 1) or (e.bit_length() - 1) % 2:
                print('  |E| not a power of 4:', r['name'], key, e)
    # is N one-dimensional at the cube corner exactly when the end is adequate?  (kht generators moved to cube coordinates)
    mism = []; n_cmp = 0
    for r in rows:
        if not r['has_kht'] or 'd' not in r:
            continue
        n_cmp += 1
        topq = r['M'] + r['qshift']; botq = r['m'] + r['qshift']
        ntop = sum(1 for h, q in r['gens'] if q == topq); nbot = sum(1 for h, q in r['gens'] if q == botq)
        over = [g for g in r['gens'] if g[1] > topq or g[1] < botq]
        if over:
            mism.append((r['name'], 'generator outside the cube range', over))
        if (r['Etop'] == 1) != (ntop >= 1):
            mism.append((r['name'], 'top', r['Etop'], ntop))
        if (r['Ebot'] == 1) != (nbot >= 1):
            mism.append((r['name'], 'bottom', r['Ebot'], nbot))
        if ntop > 1 or nbot > 1:
            mism.append((r['name'], 'corner of N more than one-dimensional', ntop, nbot))
    print('  adequate end <=> N non-zero (then one-dimensional) at the cube corner; compared on', n_cmp, 'cases; violations:', mism)
    print('  all with kht++ output have dim N > 1:', all(len(r['gens']) > 1 for r in rows if r['has_kht'] and 'gens' in r))
    print('  top q-degree of N one-dimensional fails for:', [r['name'] for r in rows if r.get('gens') and sum(1 for h, q in r['gens'] if q == r['qmax']) != 1],
          ' bottom:', [r['name'] for r in rows if r.get('gens') and sum(1 for h, q in r['gens'] if q == r['qmin']) != 1])

if __name__ == '__main__':
    main()
