"""transplant_check.py RESULTS.jsonl -- for every saved tietze certificate and EVERY single-crossing switch of its
halfword: if replay.check accepts the transplanted certificate, the switched knot must be an unknot; we test V = 1
(own bracket) -- V != 1 with acceptance would be an unsound checker."""
import sys, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import a2lib, replay
rows = [json.loads(l) for l in open(sys.argv[1])]
certs = [c for r in rows for c in (r.get('info_certs') or []) if c['kind'] == 'tietze']
maxc = int(sys.argv[2]) if len(sys.argv) > 2 else 60
acc = rej = bad = 0; acc_kinds = {}
for c in certs[:maxc]:
    hw = c['halfword']; toks = hw.split('.')
    for i, t in enumerate(toks):
        if not t or t[0] not in 'xy': continue
        t2 = toks[:]; t2[i] = ('y' if t[0] == 'x' else 'x') + t[1:]
        hw2 = '.'.join(t2)
        ok, msg = replay.check(dict(c, halfword=hw2))
        if ok:
            acc += 1
            full = a2lib.full_of(hw2)
            v1 = a2lib.jones_unit_test(a2lib.bracket_full(full))
            if not v1:
                bad += 1; print('UNSOUND? accepted transplant with V != 1:', hw2)
        else:
            rej += 1
print('certs', min(len(certs), maxc), 'single-switch transplants: accepted', acc, '(all must have V = 1), rejected', rej, 'accepted-with-V!=1', bad)
