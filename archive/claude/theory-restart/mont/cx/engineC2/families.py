import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import plat2, lp
def show(name,ws):
    out=[]
    for w in ws:
        if not plat2.is_arc(w): out.append((w,'loop')); continue
        J=plat2.J(w); out.append((len(w),lp.span(J) if J else None))
    print(name,out)
show('a^k (k even)      ',['a'*k for k in range(2,15,2)])
show('d a^k             ',['d'+'a'*k for k in range(2,13,2)])
show('(aB)^n            ',['aB'*n for n in range(1,7)])
show('(ab)^n            ',['ab'*n for n in range(1,7)])
show('(aBd)^n           ',['aBd'*n for n in range(1,5)])
show('(aD)^n            ',['aD'*n for n in range(1,7)])
show('Dbaa+ (a^k tail)  ',['Dbaa'+'a'*k for k in range(0,10,2)])
