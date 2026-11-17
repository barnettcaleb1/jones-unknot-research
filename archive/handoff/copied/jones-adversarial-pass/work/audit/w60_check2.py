import runpy, numpy as np
ns = runpy.run_path("w60_check.py")
Tc, mu4, mu1, D, A = ns["Tc"], complex(ns["mu4"]), complex(ns["mu1"]), ns["D"], ns["A"]
# use unrounded eigenvalues
ev = np.linalg.eigvals(Tc)
m1 = ev[np.argmin([min(abs(ev - e).tolist()[:i] + abs(ev - e).tolist()[i+1:]) for i, e in enumerate(ev)]) ] if False else None
# group: the singleton eigenvalue is the one farthest from the mean of the others
dist = [sum(abs(ev - e)) for e in ev]
i1 = int(np.argmax(dist)); mu1 = ev[i1]; mu4 = np.mean(np.delete(ev, i1))
print("geometric multiplicity of mu4:", D - np.linalg.matrix_rank(Tc - mu4*np.eye(D), tol=1e-7))
R = (Tc - mu4*np.eye(D)) / (mu1 - mu4)
print("rank R:", np.linalg.matrix_rank(R, tol=1e-7), " ||R^2-R|| =", np.linalg.norm(R@R - R))
print("mu1/mu4 =", mu1/mu4, " A^12 =", A**12, " A^-12 =", A**-12, " A^8=", A**8, " A^-8=", A**-8)
