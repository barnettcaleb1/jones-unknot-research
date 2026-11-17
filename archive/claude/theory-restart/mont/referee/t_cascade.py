from rcore import *
import sys
sys.argv=['x']
exec(open('t_examples.py').read().split('# (1)')[0])
for (m,j) in [(5,18),(5,22),(5,30),(5,40),(5,60),(8,30),(8,60)]:
    J,sA,T,Tg,*_=J_of(3,0,[(-m,-1,-1),(-2,)+(-1,)*j])
    print('cascade m',m,'j',j,'span J',sp(J),'span A',sA,'T',T,'Tgen',Tg,'spanA-spanJ',sA-sp(J))
