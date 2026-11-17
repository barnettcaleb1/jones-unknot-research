# Independent integrality test of D = (M3 - 432 v3)/180 and of F4 (via G4 = M4 + 1440a2^2 - 864 j4 + 120 a2 = 1440(F4 + a4))
import sys, random, time, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import refinv as R, words
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import flat_search as fs
from fractions import Fraction as Fr
mode=sys.argv[1]; seed=int(sys.argv[2]); N=int(sys.argv[3]); tmax=float(sys.argv[4]) if len(sys.argv)>4 else 240
rnd=random.Random(seed); out=[]; bad=[]; seen=set(); t0=time.time(); tries=0
def gen():
    if mode=='fs': return fs.gen(rnd,rnd.randint(16,30))
    if mode=='g2': return R.gen2(rnd,rnd.randint(10,26),maxw=rnd.choice([3,5,7]),pw=rnd.choice([0.15,0.3,0.5]))
    if mode=='mont':
        m=rnd.randint(-3,3); n=rnd.randint(1,3)
        rows=[rnd.choice([-1,1])*rnd.choice([1,3,5,7]) for _ in range(n)]
        w=words.mont(m,rows,tw=rnd.choice('xy'),ax=rnd.choice('xy'),off=rnd.choice('xy'))
        return w
    if mode=='mixed':
        # Montesinos necklace with random generic bodies spliced in (bodies from fs.gen, without 's.' and final cup)
        m=rnd.randint(-2,2); parts=['s','r2']+[rnd.choice(['x1','y1'])]*abs(m)
        for _ in range(rnd.randint(1,2)):
            b=fs.gen(rnd,rnd.randint(6,12))
            if not b: return None
            toks=b.split('.')[1:]   # body = all tokens after s (a half-word returns to one half-strand)
            parts+=toks
        parts+=['u1']; return '.'.join(parts)
while len(out)<N and time.time()-t0<tmax and tries<50*N:
    tries+=1
    w=gen()
    if not w or w in seen: continue
    seen.add(w)
    v=R.all_vals(w)
    if v is None: continue
    if mode=='g2' and v['V']=={0:1} and v['M3']==0: continue
    nwind=sum(1 for t in w.split('.') if t in ('x0','y0'))
    rec=dict(w=w,a2=str(v['a2']),v3=str(v['v3']),j4=str(v['j4']),M3=v['M3'],M4=v['M4'],D=str(v['D']),G4mod=str(v['G4']%1440),nwind=nwind,ncr=len(w.split('.')))
    out.append(rec)
    if v['D'].denominator!=1 or v['G4']%1440!=0: bad.append(rec)
print(mode,seed,'checked',len(out),'tries',tries,'time %.0fs'%(time.time()-t0),'| non-integral D or F4:',len(bad),
      '| a2=0:',sum(1 for r in out if r['a2']=='0'),'| mean windings %.1f'%(sum(r['nwind'] for r in out)/max(1,len(out))),
      '| max letters',max((r['ncr'] for r in out),default=0))
for b in bad[:6]: print('BAD',b)
json.dump(out,open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work/integ_%s_%d.json'%(mode,seed),'w'))
