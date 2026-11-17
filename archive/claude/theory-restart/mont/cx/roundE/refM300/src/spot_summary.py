import sys, pickle, os, collections, glob
HERE='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/'
R=[pickle.load(open(f,'rb')) for f in glob.glob(HERE+'spot_res/*.pkl')]
st=collections.Counter(r['status'] for r in R)
done=[r for r in R if r['status']=='done']
print('results',len(R),dict(st))
print('kind',collections.Counter(r['kind'] for r in done),' how',collections.Counter(r['how'] for r in done))
print('k (boxes)',sorted(collections.Counter(len(r['xs']) for r in done).items()),' n rational',sorted(collections.Counter(len(r['rats']) for r in done).items()))
print('lp.J == vector calculus:',sum(1 for r in done if r['agree']),'/',len(done),'  J None:',sum(1 for r in done if r['Jlp'] is None))
print('UNITS (lp.J):',sum(1 for r in done if r.get('unit')),'  units among ALL Lemma-W candidates (vector calculus):',sum(len(r['units_vc']) for r in R))
if done:
    sp=sorted(r['span'] for r in done if r['Jlp'] is not None); print('min span J',sp[0],' median',sp[len(sp)//2])
    print('a2 = 0:',sum(1 for r in done if r['Jlp'] is not None and r['a2']==0),'  J(zeta10)=1:',sum(1 for r in done if r['Jlp'] is not None and r['z10']),
          '  both gates:',sum(1 for r in done if r['Jlp'] is not None and r['a2']==0 and r['z10']))
    tw=sorted(r['twall'] for r in done); print('wall time per closure: median %.1fs max %.1fs total %.0fs'%(tw[len(tw)//2],tw[-1],sum(tw)))
    print('distinct classes used',len(set(c for r in done for c in r['cls'])),' distinct boxes',len(set(x for r in done for x in r['xs'])))
    print('candidates per product (Lemma-W): total',sum(r['ncand'] for r in R))
