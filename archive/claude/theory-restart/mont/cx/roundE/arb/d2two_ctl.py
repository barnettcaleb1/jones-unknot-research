"""negative controls for d2two: (a) sum D36 = 3 and (b) include the 24 open d2 classes with sum d2 = 2: expect OPEN cases."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import d2two, lpg, classes, runner
from fractions import Fraction as Fr
from multiprocessing import Pool
mode=sys.argv[1]
if mode=='b':
    d2two.S=d2two.T+classes.d2pos(); d2two.EXTRA=[('eq',{j:Fr(1) for j in range(d2two.NT,len(d2two.S))},Fr(2))]
elif mode=='c':
    d2two.EXTRA=[('eq',{j:Fr(1) for j in range(d2two.NT,len(d2two.S))},Fr(3))]
if __name__=='__main__':
    jobs=d2two.job_list()
    with Pool(3) as P: res=P.map(d2two.one,jobs,chunksize=4)
    c=collections.Counter(r[1] for r in res); print(mode,dict(c))
    for r in res:
        if r[1]=='open': print('  ',r[0],str(r[2])[:200])
