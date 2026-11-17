import sys
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont/cx/cert')
import diagram, refs
ws = refs.random_halfwords(1, 30)
ok=0; mir=0; bad=0
for w in ws:
    pd = diagram.pd_from_halfword(w)
    if pd is None: print('NONE', w); continue
    assert diagram.check_pd(pd), w
    V = diagram.jones(pd); Vr = refs.VK_ref(w)
    Vm = {-e:c for e,c in V.items()}
    if V == Vr: ok+=1
    elif Vm == Vr: mir+=1
    else: bad+=1; print('BAD', w, V, Vr)
print('ok',ok,'mirror',mir,'bad',bad)
