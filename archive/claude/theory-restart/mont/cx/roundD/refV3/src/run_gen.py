import sys
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import v3b3, v3b
from fractions import Fraction as Fr
Z=(Fr(0),Fr(0),Fr(0),Fr(0))
for nmin in (2,1):
    ok,opn,certs=v3b3.prove({'top':Z,'bot':Z},Fr(0),nmin)
    print('n_min=%d ok=%s open=%s'%(nmin,ok,opn))
    for c in certs:
        end,asg,a3,name,ys,s,r=c
        print('  ',end,'a>0' if asg>0 else 'a<0','|a|=3' if a3 else '|a|>=5',name,'ys=',[str(y) for y in ys],'sup=',s,'rhs=',r)
# print the case equations for typ '+' and '-'
for typ,a3 in (('+',True),('-',True),('-',False)):
    print('typ',typ,'a3',a3)
    for name,eqs,P0 in v3b.cases(Z,Fr(1),typ,a3):
        print('   ',name,[tuple(str(x) for x in e) for e in eqs],'P0=',P0)
