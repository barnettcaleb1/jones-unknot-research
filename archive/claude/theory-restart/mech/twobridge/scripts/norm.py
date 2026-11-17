from parse import recs, levels
from collections import Counter
def strip(runs):
    # drop trailing A run
    if runs and runs[-1][0]=='A': runs=runs[:-1]
    return runs
def norm(r):
    j=int(r['j']); 
    return sorted([(c-24*j,d-4*j) for c,d in r['specials']], key=lambda x:(x[1],x[0]))
if __name__=='__main__':
    rs=[r for r in recs() if not r['dup'] and r['runs']]
    seen={}
    for r in rs:
        key=tuple(n for _,n in strip(r['runs']))
        sp=tuple(norm(r))
        if key in seen:
            if seen[key]!=(r['k'],sp): print('MISMATCH',key)
            continue
        seen[key]=(r['k'],sp)
    for key in sorted(seen,key=lambda k:(len(k),k)):
        k,sp=seen[key]
        lev=levels(sp)
        def fmt(v):
            c=Counter(v); return ' '.join(('%d'%x)+('^%d'%m if m>1 else '') for x,m in sorted(c.items()))
        print(key,'k=%d'%k,' | '.join('%d: %s'%(d,fmt(v)) for d,v in sorted(lev.items())))
