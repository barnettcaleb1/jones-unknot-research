import sys; sys.path.insert(0, "/private/tmp/claude-501/-Users-calebbarnett/325b8760-550e-4462-b594-d76cd953b342/scratchpad/jones-adv/referee-prior-fresh-eyes")
import cmath, math, numpy as np
from ch4_check import gram, num_word, vc, pev
for name, th in [("Funar point 7pi/20", 7*math.pi/20), ("3pi/8", 3*math.pi/8), ("pi/3", math.pi/3)]:
    A = cmath.exp(1j*th); dl = (-A**2 - A**-2).real
    ev = np.linalg.eigvalsh(gram(dl))
    sig = (int(sum(ev > 1e-9)), int(sum(ev < -1e-9)), int(sum(abs(ev) <= 1e-9)))
    MT = num_word([1,2]*3, A)
    rot = A**-12
    order = next((k for k in range(1, 200) if abs(rot**k - 1) < 1e-9), None)
    print(f"{name}: delta={dl:.6f} signature(pos,neg,zero)={sig} tangent rotation A^-12={rot:.4f} projective order={order}")
A = cmath.exp(1j*math.pi/3)
K = num_word([1,2]*3, A)*A**6 - np.eye(5)
print("pi/3: rank(A^6 T_c - 1) =", np.linalg.matrix_rank(K, tol=1e-9), " nilpotent:", np.linalg.norm(K@K) < 1e-9)
