from nt import *
from collections import Counter
seqs=normal_seqs(3,3)
rows=[]
for s in seqs:
    u=box(s); a,b=chan(u)
    la,lb=lead(a),lead(b); ta,tb=tail(a),tail(b)
    q=ser_div(b,a,4)
    rows.append((s,la,lb,ta,tb,q))
# classify top: (deg b - deg a, lc b/lc a) 
C=Counter((lb[0]-la[0], lb[1]*la[1]) for s,la,lb,ta,tb,q in rows)
print('top (db-da, lcb*lca):',C)
C=Counter((tb[0]-ta[0], tb[1]*ta[1]) for s,la,lb,ta,tb,q in rows)
print('bot (db-da, lcb*lca):',C)
for r in rows[:40]:
    s,la,lb,ta,tb,q=r
    print(s,'a top',la,'b top',lb,'| a bot',ta,'b bot',tb,'| q~',[(e,str(c)) for e,c in q])
