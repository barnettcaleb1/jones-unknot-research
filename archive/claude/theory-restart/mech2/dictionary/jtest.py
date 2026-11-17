import json,collections
T=json.load(open('table.json')); A=json.load(open('alex.json'))
rows=[]
bad_arf=[]; bad_k=[]
for a in T:
    if 'err' in a: continue
    al=A[a['name'].replace('^','-')]['alex']
    det=abs(sum(c*(-1)**i for i,c in enumerate(al)))
    arf=0 if det%8 in (1,7) else 1
    # a2 = Delta''(1)/2 for symmetric normalised Delta: Conway coefficient a_2
    n=len(al); mid=(n-1)//2
    a2=sum(c*(i-mid)**2 for i,c in enumerate(al))//2
    sig=a['sigma']; s=a['s']; k=a['k']; j=a['j']
    if (j-arf)%2: bad_arf.append(a['name'])
    if k!=2*s: bad_k.append((a['name'],k,s,sig))
    rows.append((a['name'],k,j,sig,s,det,arf,a2,a['dim']))
print('j != Arf mod 2:',bad_arf)
print('k != 2s:',bad_k)
print('dim != det:',[(r[0],r[8],r[5]) for r in rows if r[8]!=r[5]])
# group by knot
byk=collections.defaultdict(list)
for r in rows: byk[r[0].split('^')[0]].append(r)
print('knot   sig  a2  det | (k,j) per inversion | j1+j2 | 2j+k/4 each')
for kn,rs in byk.items():
    print('%-6s %3d %3d %3d | %s | %s | %s'%(kn,rs[0][3],rs[0][7],rs[0][5],' '.join('(%d,%d)'%(r[1],r[2]) for r in rs),sum(r[2] for r in rs) if len(rs)==2 else '-',' '.join(str(2*r[2]+r[1]//4) for r in rs)))
