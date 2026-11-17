import sys, json, time
from exhaustive import analyse_target
Dlist = [('1', [1]), ('1+t', [1, 1]), ('1-t', [1, -1]), ('1+t^2', [1, 0, 1]), ('1+t+t^2', [1, 1, 1]),
         ('1-t^3', [1, 0, 0, -1]), ('(1+t^2)(1+t+t^2)', [1, 1, 2, 1, 1]), ('1+t^4', [1, 0, 0, 0, 1]),
         ('1-t^5', [1, 0, 0, 0, 0, -1]), ('1+t^6', [1,0,0,0,0,0,1])]
Wmax = int(sys.argv[1]); extra = 3
out = {}
for name, Dco in Dlist:
    SD = len(Dco) - 1
    found = {}
    prof = []
    for Wn in range(0, Wmax + 1):
        B = max(1, Wn, SD); Rb = 3 * B + extra
        t0 = time.time(); newpts = []
        for m0 in range(-Rb, Rb + 1):
            for n0 in range(-Rb, Rb + 1):
                if m0 == 0 or n0 == 0 or (m0, n0) in found: continue
                f = analyse_target(m0, n0, Wn, Dco, SD)
                if f:
                    found[(m0, n0)] = Wn; newpts.append((m0, n0))
        # worst among targets whose minimal width is <= Wn, measured with B(Wn_min)
        worst = max([(min(abs(a), abs(b)) / max(1, w, SD), (a, b), w) for (a, b), w in found.items()], default=None)
        viol = [(a, b, w) for (a, b), w in found.items() if abs(a) > 3 * max(1, w, SD) and abs(b) > 3 * max(1, w, SD)]
        mxnew = max([min(abs(a), abs(b)) for a, b in newpts], default=0)
        prof.append(dict(W=Wn, B=B, new=len(newpts), max_min_new=mxnew, worst_ratio=worst, viol=viol, sec=round(time.time()-t0,1)))
        print(name, prof[-1], flush=True)
    out[name] = dict(SD=SD, profile=prof, feasible={str(k): v for k, v in found.items()})
json.dump(out, open('exhaustive_W%d.json' % Wmax, 'w'), indent=1)
print('DONE')
