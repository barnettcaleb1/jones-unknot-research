"""One named pair: Sakuma eta agrees on the two inversions of 9_9.

The eta equality is quoted by Watson, arXiv:1311.1085v4, the figure
caption for the two strong inversions of 9_9 in 'Distinguishing strong
inversions'. This script checks the independent J-moment distinction
and that the two actual covering-knot Jones polynomials agree.
"""
import sys,json
from fractions import Fraction
from pathlib import Path
sys.path[:0]=['/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/core',
             '/Users/calebbarnett/jones-lanes/theory-restart/mont',
             '/Users/calebbarnett/jones-lanes/theory-restart/tools']
import c1_constituents as cc,lp,kauffman
cases=[('9_9^1','s.r1.y0.y0.y1.y0.y0.y1.y1.y0.y0.y1.u2'),
       ('9_9^2','s.l1.y0.y0.y1.y0.y0.y0.y0.y1.y0.y0.y1.u2')]
rows=[]
for name,word in cases:
    J=lp.J(word)
    V=cc.V_of_bracket(kauffman.bracket(word))
    v3=-Fraction(sum(c*(e*(e-1)*(e-2)+3*e*(e-1)) for e,c in V.items()),36)
    M3=sum(c*(-1)**(e%2)*e**3 for e,c in J.items())
    j=-Fraction(sum(e*c for e,c in J.items()),8)
    iota=(Fraction(M3,36)-7*v3)/5
    rows.append(dict(name=name,word=word,J=J,V=V,v3=str(v3),M3=M3,
                     M3_over_36=str(Fraction(M3,36)),j=str(j),iota=str(iota)))
assert rows[0]['V']==rows[1]['V']
assert [r['M3'] for r in rows]==[4824,6264]
assert rows[0]['j']==rows[1]['j']=='2'
assert Fraction(rows[1]['iota'])-Fraction(rows[0]['iota'])==8
out=dict(rows=rows,eta_source='Watson arXiv:1311.1085v4, figure caption for 9_9',
         common_Sakuma_eta={-2:-2,0:4,2:-2},
         conclusion='M3 is not a function of the underlying knot together with full Sakuma eta (even with j).')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k not in ['J','V','word']} for r in rows],indent=2))
