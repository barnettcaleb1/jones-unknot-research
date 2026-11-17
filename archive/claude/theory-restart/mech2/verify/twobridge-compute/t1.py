import json,sys
from reflib import *
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
# explicit trefoil quotient word from lit/kht/REPORT.md 3.3 (without the six framing letters)
w='r1.r2.l1.l2.y0.y1.y1.y0.y0.y1.y1.y0.y2.y1.y3.y2.u4.u3.u0'
mine='.'.join('%s%d'%x for x in quotient_word(half_letters('s.l1.y0.y0.y1.u2')))
print('quotient word matches the one recorded in lit/kht/REPORT.md:',mine==w)
for word in ['s.l1.y0.y0.y1.u2','s.l1.y0.x1.u2','s.l1.y0.y0.x1.u2','s.l1.x0.x0.y1.u2','s.l1.y0.u2','s.l1.x1.u2','s.l1.u2']:
    L=half_letters(word)
    j0,jinf=J_bracket(L)
    print(word)
    print('   e0 coeff (A):',pstr(j0,'A'),'   e_inf coeff:',pstr(jinf,'A'))
    print('   J(t) =',pstr(A_to_t(j0)),'  norm',pnorm(A_to_t(j0)))
    kb=knot_bracket(L)
    print('   knot bracket:',pstr(kb,'A'),' det',det_from_bracket(kb),' writhe',half_writhe(L))
# data
recs=[json.loads(l) for l in open(base+'k138/k138.jsonl')]
for r in recs[:6]:
    print(r['file'], J_from_khr(r['khr'])[:2], pstr(J_from_khr(r['khr'])[2]))
