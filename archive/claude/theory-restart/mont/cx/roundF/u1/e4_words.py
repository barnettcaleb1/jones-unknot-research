"""e4_words.py -- rebuild engineC2's 65 E4 unit (box, N) pairs exactly as engineC2/cert_e4.py does (special S2 word W_s,
slot box body = engineA vc.word(T) on (A_l, k) at the end of the top half, point-symmetric gluing), translate each event
list to a halfword (translate.transfer + events_to_halfword; round trip asserted), check lp.J(halfword) = 1 (engineC2's
cert_e4.py had verified theta.J_events(original) = 1 on all 65).  Records the ring levels m used by rule (R).
Writes out/e4_halfwords.json and out/words_e4_units.json ([tag, halfword])."""
import sys, os, json, pickle, glob, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR
C2 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2'
sys.path.insert(0, C2); sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import theta, sym, plat2, vc, lp
def ring_levels(ev):
    cols = []; ms = []; i = 0
    while i < len(ev):
        typ = ev[i][0]
        if typ in ('X', 'Y'):
            p = ev[i][1]
            if p + 1 == len(cols) - 1 and cols[p + 1] == 'a': ms.append(p); i += 2; continue
            cols[p], cols[p + 1] = cols[p + 1], cols[p]
        elif typ in ('capA', 'capK'): p = ev[i][1]; c = 'a' if typ == 'capA' else 'k'; cols[p:p] = [c, c]
        elif typ == 'cup': del cols[ev[i][1]:ev[i][1] + 2]
        elif typ == 'splitR': cols[ev[i][1] + 1:ev[i][1] + 1] = ['k']
        elif typ == 'mergeL': break
        i += 1
    return ms
rows = []; t0 = time.time()
for f in sorted(glob.glob(os.path.join(C2, 'e4_*_4.pkl'))):
    out, units = pickle.load(open(f, 'rb'))
    for w, tg, Tr, N in units:
        T = ('p', [Tr, ('w', ('Y' if N > 0 else 'y') * abs(N))]) if N else Tr
        body = vc.word(T)
        ev = sym.symmetric(plat2.top_events(w) + sym.body(body, 0))
        ev2, nr = TR.transfer(ev)
        h = TR.events_to_halfword(ev2)
        J2 = lp.J(h)
        rows.append({'file': os.path.basename(f), 'W_s': w, 'box_tag': tg, 'N': N, 'body': body, 'rings_transferred': nr,
                     'ring_levels_m': ring_levels(ev), 'halfword': h, 'J_lp': sorted(J2.items()) if J2 else None,
                     'ok': J2 == {0: 1}})
        print(len(rows), w, body, 'm =', sorted(set(ring_levels(ev))), 'lp.J==1:', J2 == {0: 1}, round(time.time() - t0, 1), flush=True)
json.dump(rows, open(os.path.join(HERE, 'out', 'e4_halfwords.json'), 'w'), indent=1)
json.dump([['E4:%s|%s|N=%d' % (r['W_s'], r['body'], r['N']), r['halfword']] for r in rows], open(os.path.join(HERE, 'out', 'words_e4_units.json'), 'w'))
print('E4 unit pairs', len(rows), 'lp.J = 1:', sum(r['ok'] for r in rows), '| distinct halfwords', len(set(r['halfword'] for r in rows)),
      '| ring levels m used:', sorted(set(m for r in rows for m in r['ring_levels_m'])))
