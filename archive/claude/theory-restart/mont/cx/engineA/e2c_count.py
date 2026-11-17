import sys, time, collections, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, e2b
spec=json.loads(sys.argv[1]); end=sys.argv[2]; Kd=int(sys.argv[3])
t0=time.time()
nested,rat=e2b.build(spec); allb=nested+rat; nN=len(nested)
sl=[ser.slope(b[1],end,Kd) for b in allb]
H=collections.defaultdict(list)
for x in range(len(allb)): H[(sl[x][0]%3,sl[x][1],sl[x][2])].append(x)
print('hashed',len(H),'keys over',len(allb),'boxes; largest classes:',sorted((len(v) for v in H.values()),reverse=True)[:8],round(time.time()-t0,1),flush=True)
groups=collections.defaultdict(list)
for mu in range(-spec['MU'],spec['MU']+1):
    if mu: groups[e2b.tgt(mu,end,Kd)].append(mu)
for T,gm in groups.items():
    cnt=0; src=collections.Counter()
    for i in range(nN):
        need=((T[0]-sl[i][0])%3, T[1]/sl[i][1], ser.sdiv(T[2],sl[i][2]))
        hits=H.get(need,())
        cnt+=len(hits)
        if hits: src[(allb[i][3], allb[hits[0]][3])]+=len(hits)
    print('group',gm[:2],len(gm),'candidates',cnt,src.most_common(4),round(time.time()-t0,1),flush=True)
