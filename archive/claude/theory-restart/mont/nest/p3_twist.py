import sys
sys.path.insert(0,'nest')
from nlib import *
import alex
def Tn(n):
    tw_='.'.join(['y1']*n) if n>0 else '.'.join(['x1']*(-n))
    mid=('.'+tw_) if n!=0 else ''
    return 's.r1.x2'+mid+'.y0.r2.y0.y1.y0.y1.x2.u3.u1'
alpha=mul(mono(-5),P((1,2),(-1,1),(1,0)))
beta=add(mul(mono(2),P((1,4),(-1,3),(-1,0))), mul(mono(-6),P((1,2),(-1,1),(1,0))))
B='y0.r2.y0.y1.y0.y1.x2.u1'
print('B =',B,' J(s.B) =',fmt(J('s.'+B)) if J('s.'+B) else None, ' alex(s.B)=',alex.alex_poly('s.'+B))
c=vec(B)
print('pinned candidates',len(c) if c else c)
vB=c[0]; print('v_B =',fmt(vB[0]),' | ',fmt(vB[1]),' eps',eps(vB),' n0',nax(B))
for n in range(-3,6):
    w=Tn(n)
    Jw=J(w)
    if Jw is None: print(n,'not a knot'); continue
    cl=normalize(add(mul(mono(2*n),alpha), mul(mono(n,(-1)**(n%2)),beta)))
    iso=J('s.'+body(n+1,[B]))   # s.r2.(y1)^(n+1).B.u1
    iso2=J('s.r2.'+tw(n+1)+'y0.r2.y0.y1.y0.y1.x2.u3.u1')
    pred=normalize(close(-(n+1),vB))
    print('n=%d'%n,'claimed formula',cl==Jw,' necklace word s.r2.(y1)^(n+1).B.u1 same J',iso==Jw,' (u3.u1 version',iso2==Jw,')  formula e1^T X^-(n+1) v_B',pred==Jw,' span',span(Jw), ' a2',a2(Jw))
print('T_1 J =',fmt(J(Tn(1))))
print('alex T_1',alex.alex_poly(Tn(1)),' alex T_0',alex.alex_poly(Tn(0)),' alex T_-1',alex.alex_poly(Tn(-1)))
