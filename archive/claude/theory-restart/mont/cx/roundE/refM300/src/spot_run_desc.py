"""spot-check runner: NSEED closures (seeds SEED0..), lp.J in subprocesses with a timeout, one result file per seed
(resumable).  Units by lp.J -> HIT protocol."""
import sys, os, pickle, time, subprocess, collections
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
import spot_lib2, lp
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
PY='/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python'
SEED0=int(sys.argv[1]); NSEED=int(sys.argv[2]); NW=int(sys.argv[3]); TO=int(sys.argv[4])
def z10(Jn):
    r=[0]*5
    for e,c in Jn.items():
        q,rem=divmod(e,5); r[rem]+=c*(-1)**(q%2)
    r[0]-=1; c4=r[4]; r=[r[0]-c4,r[1]+c4,r[2]-c4,r[3]+c4,0]
    return all(x==0 for x in r)
def task(seed):
    rf=HERE+'spot_res/%d.pkl'%seed
    if os.path.exists(rf): return
    m=spot_lib2.build(seed)
    tf=HERE+'spot_tasks/%d.pkl'%seed; pickle.dump(m,open(tf,'wb'))
    jf=HERE+'spot_tasks/%d.J.pkl'%seed
    t=time.time()
    try:
        subprocess.run([PY,HERE+'src/spot_worker.py',tf,jf],timeout=TO,check=True,capture_output=True)
        J=pickle.load(open(jf,'rb'))['Jlp']; m['status']='done'
    except subprocess.TimeoutExpired:
        J=None; m['status']='timeout'
    except Exception as ex:
        J=None; m['status']='error:'+repr(ex)[:200]
    m['twall']=time.time()-t; m['Jlp']=J
    if J is not None:
        m['agree']=(J==m['Jvc']); m['unit']=(len(J)==1); m['span']=max(J)-min(J); m['a2']=lp.a2(J); m['z10']=z10(J)
        if m['unit']:
            open(HERE+'UNIT_FOUND_seed%d.txt'%seed,'w').write(repr(m))
    pickle.dump(m,open(rf+'.tmp','wb')); os.replace(rf+'.tmp',rf)
    for f in (tf,jf):
        try: os.remove(f)
        except OSError: pass
if __name__=='__main__':
    t0=time.time()
    with ThreadPoolExecutor(NW) as ex: list(ex.map(task,range(SEED0+NSEED-1,SEED0-1,-1)))
    print('done',time.time()-t0)
