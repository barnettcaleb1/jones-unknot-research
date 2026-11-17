"""Semi-adequacy probe for branch knots L_n: simplify the natural diagram with regina (simplify, then simplifyExhaustive at
increasing heights) and test A-/B-adequacy of every diagram met; also the Jones-polynomial obstruction
(semi-adequate => at one end |c_0| = 1 and c_0 c_1 <= 0; Lickorish-Thistlethwaite, Dasbach-Lin/Stoimenow)."""
import sys, json, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk, identK, regina
def jones_end_test(V):
    ks=sorted(V); lo,hi=ks[0],ks[-1]
    okL = abs(V[lo])==1 and V[lo]*V.get(lo+1,0)<=0
    okH = abs(V[hi])==1 and V[hi]*V.get(hi-1,0)<=0
    return okL,okH
def probe(pd, heights=(1,2), label=''):
    L=regina.Link.fromPD(pd)
    V=bk.jones_t(L)
    okL,okH=jones_end_test(V)
    found=[]
    def test(Lk,tag):
        p=[tuple(x) for x in Lk.pdData()]
        A,B,_,_=bk.adequacy(p)
        if A or B: found.append((tag,len(p),A,B))
        return len(p)
    c0=test(L,'natural')
    L.simplify(); c1=test(L,'simplify')
    for h in heights:
        t0=time.time()
        try:
            L.simplifyExhaustive(h)
        except Exception as e:
            print('exhaustive failed',e); break
        c2=test(L,'exhaustive%d'%h)
        if time.time()-t0>120: break
    print(label,'crossings natural/simplified/final: %d/%d/%d'%(c0,c1,len(L.pdData())),'| Jones end test (low,high) =',(okL,okH),
          '| semi-adequate diagrams found:',found[:3],flush=True)
    return {'label':label,'c_natural':c0,'c_simpl':c1,'c_final':len(L.pdData()),'jones_end_ok':(okL,okH),'semiadequate_found':found,
            'final_pd':[list(x) for x in L.pdData()]}
if __name__=='__main__':
    import examples
    name=sys.argv[1]; ns=[int(x) for x in sys.argv[2:]] or [1,-1,2,-2]
    a,N,boxes=examples.EX[name]
    hw=identK.halfword(a,N,boxes); f=bk.frame(hw)
    out=[]
    out.append(probe(bk.pd_code(bk.full_K(hw)),label=name+' K'))
    for n in ns:
        out.append(probe(bk.pd_code(bk.full_Ln(hw,n,f)),label=name+' L_%d'%n))
    json.dump(out,open('semiadq_%s.json'%name,'w'))
