# Sanity check for the twist-family structure theorem (L2 notes, Section 3).
# Bracket vectors of 2-tangles: <T> = f[0] + g[inf], [0] = '=' (identity for horizontal sum),
# [inf] = ')(' = e with e^2 = delta e.  Laurent polys in A as dicts {exp: coeff}.
from collections import defaultdict
def add(p,q):
    r=defaultdict(int)
    for k,v in p.items(): r[k]+=v
    for k,v in q.items(): r[k]+=v
    return {k:v for k,v in r.items() if v}
def mul(p,q):
    r=defaultdict(int)
    for a,x in p.items():
        for b,y in q.items(): r[a+b]+=x*y
    return {k:v for k,v in r.items() if v}
def sc(c,e,p): return mul({e:c},p)
DEL={2:-1,-2:-1}
def hstep(f,g,s):   # T + [s], s=+1 or -1 crossing; [1] = A[0] + A^-1[inf]
    a,b = ({1:1},{-1:1}) if s>0 else ({-1:1},{1:1})
    # (f + g e)(a + b e) = af + (bf + ag + b delta g) e
    return mul(a,f), add(add(mul(b,f),mul(a,g)),mul(mul(b,DEL),g))
def vstep(f,g,s):   # T * [s]: vertical algebra, [inf] identity, [0] = e', e'^2 = delta e'
    a,b = ({1:1},{-1:1}) if s>0 else ({-1:1},{1:1})   # crossing = a[0] + b[inf]
    # T = g + f e', crossing = b + a e'; product = bg + (ag + bf + a delta f) e'
    return add(add(mul(a,g),mul(b,f)),mul(mul(a,DEL),f)), mul(b,g)
def tangle(n1,n2):
    f,g={0:1},{}           # [0]
    for _ in range(abs(n1)): f,g=hstep(f,g,1 if n1>0 else -1)
    for _ in range(abs(n2)): f,g=vstep(f,g,1 if n2>0 else -1)
    return f,g
def N(f,g): return add(mul(f,DEL),g)
def D(f,g): return add(f,mul(g,DEL))
def is_mono(p): return len(p)==1 and abs(list(p.values())[0])==1
R=9
for clos,name in ((N,'N'),(D,'D')):
    units=[]
    for n1 in range(-R,R+1):
        for n2 in range(-R,R+1):
            b=clos(*tangle(n1,n2))
            if is_mono(b): units.append((n1,n2))
    print(name,'closure: monomial brackets at',len(units),'points')
    off=[u for u in units if u[0]!=0 and u[1]!=0]
    print('  on axes n1=0:',sum(1 for u in units if u[0]==0),' n2=0:',sum(1 for u in units if u[1]==0),' off-axis:',off)
