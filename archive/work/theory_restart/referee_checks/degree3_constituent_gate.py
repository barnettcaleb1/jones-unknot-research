"""Four fixed named inversion calibrations; no fit or search.

Tests the proposed linear identification M3/36 = a v3(K)+b v3(C_in)+c v3(C_out).
All four C_out are unknots. Two controls determine a,b; the next named knot refutes.
"""
import sys,json
from pathlib import Path
from fractions import Fraction
sys.path[:0]=['/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/core',
             '/Users/calebbarnett/jones-lanes/theory-restart/mont',
             '/Users/calebbarnett/jones-lanes/theory-restart/tools']
import c1_constituents as cc,lp,kauffman
cases=[
 ('3_1','s.l1.y0.y0.y1.u2'),
 ('4_1^1','s.l1.y0.y0.x1.u2'),
 ('5_2^1','s.l1.y0.y0.y0.y0.y1.u2'),
 ('5_2^2','s.r1.y0.y0.y1.y1.u2')]
def v3(V):
 return -Fraction(sum(c*(e*(e-1)*(e-2)+3*e*(e-1)) for e,c in V.items()),36)
rows=[]
for name,w in cases:
 J=lp.J(w);VK=cc.V_of_bracket(kauffman.bracket(w));Vi,Vo=cc.constituents(w)
 m3=sum(c*(-1)**(e%2)*e**3 for e,c in J.items())
 row=dict(name=name,word=w,J=J,VK=VK,Vin=Vi,Vout=Vo,
          M3=m3,M3_over_36=str(Fraction(m3,36)),
          v3K=str(v3(VK)),v3in=str(v3(Vi)),v3out=str(v3(Vo)))
 rows.append(row)
actual=[(Fraction(r['M3_over_36']),Fraction(r['v3K']),Fraction(r['v3in']),Fraction(r['v3out'])) for r in rows]
assert actual==[(7,1,-1,0),(-5,0,-5,0),(26,3,-14,0),(16,3,3,0)]
# Figure-eight forces b=1; trefoil then forces a=8; 5_2^1 contradicts.
a,b=Fraction(8),Fraction(1)
assert actual[0][0]==a*actual[0][1]+b*actual[0][2]
assert actual[1][0]==a*actual[1][1]+b*actual[1][2]
assert actual[2][0] != a*actual[2][1]+b*actual[2][2]
result={'rows':rows,'forced_coefficients_from_first_two':{'a':str(a),'b':str(b)},
        'third_prediction':str(a*actual[2][1]+b*actual[2][2]),
        'third_actual':str(actual[2][0]),
        'conclusion':'No rational linear combination of the three constituent/cover v3 invariants equals M3/36 universally.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'values':[[str(x) for x in t] for t in actual], 'forced_a':str(a),'forced_b':str(b),'prediction':'10','actual':'26'},indent=2))
