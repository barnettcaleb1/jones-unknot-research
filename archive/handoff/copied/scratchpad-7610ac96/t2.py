import sys, time
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont/cx/cert')
import diagram, wirtinger, refs
ws = refs.random_halfwords(7, 12, minlen=4, maxlen=16, width2_frac=0.5, w2len=(1, 12))
for w in ws:
    t0=time.time(); pd=diagram.pd_from_halfword(w); t1=time.time()
    V=diagram.jones(pd); t2=time.time()
    A=diagram.alexander(pd); t3=time.time()
    full=diagram.morse_word(w); g,r=wirtinger.plat(full); t4=time.time()
    print(pd.n, 'V %.3f A %.3f plat %.3f'%(t2-t1,t3-t2,t4-t3), 'platlens', [len(x) for x in r], flush=True)
    t5=time.time(); Ar=refs.alex_ref(w); print('  sympy alex %.3f'%(time.time()-t5), flush=True)
