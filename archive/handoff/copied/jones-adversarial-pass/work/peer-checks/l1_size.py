import sys, importlib.util, io, contextlib
P='$HOME/jones-adversarial-pass/work/peer-checks/bbb_phi0.py'
spec=importlib.util.spec_from_file_location('b',P); b=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(b)
def stats(M):
    l1=max(sum(abs(c) for c in p.values()) for row in M for p in row)
    degs=[d for row in M for p in row for d in p]
    return l1, (min(degs), max(degs))
print("len Phi0", len(b.Phi0))
print("Phi0: max entry L1 norm, degree range", stats(b.MP))
y1=[3,2,1,1,-2,-3]
for m in (5,10,20):
    w=y1*m+b.Phi0+b.inv(y1*m)
    print("y1^%d Phi0 y1^-%d: len %d," % (m,m,len(w)), "max L1, degrees", stats(b.burau(w)))
