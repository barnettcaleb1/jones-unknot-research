import json,collections,sys
T=json.load(open('table.json'))
def stair(a):
    """signed staircase length l_s and type"""
    steps=[tuple(s) for s in a['steps']]
    n=len(steps)
    if n==0: return 0,'pt'
    # type +: (1,0),(0,-1),(1,0),... ; type -: (-1,0),(0,1),...
    if all(steps[i]==((1,0) if i%2==0 else (0,-1)) for i in range(n)): return n//2,'+'
    if all(steps[i]==((-1,0) if i%2==0 else (0,1)) for i in range(n)): return -(n//2),'-'
    return None,str(steps)
rows=[]
for a in T:
    if 'err' in a: continue
    ls,ty=stair(a)
    nsq=len(a['squares'])
    sq=sum((-1)**(b%2) for (x,b) in a['squares'])
    levels=sorted(set(b for (x,b) in a['L']))
    rows.append((a['name'],a['k'],a['j'],a['dim'],ls,ty,nsq,sq,len(levels),min(levels),max(levels),a.get('s'),a.get('sigma'),a.get('khdim'),a['x0abs'],a['odd'],a['dDpow'],a['dPn']))
print('name      k   j  dim  l_s ty #sq s_sq lev bmin bmax   s  sig  Kh  x0abs')
for r in rows:
    print('%-8s %3d %3d %4d %4s %2s %3d %4d %3d %4d %4d %4s %4s %3s  %s %s %s %s'%(r[0],r[1],r[2],r[3],r[4],r[5] if len(r[5])<3 else '?',r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15] or '',r[16] or '',r[17] or ''))
