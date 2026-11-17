import sys, cmath, math
sys.path.insert(0, '.')
import numpy as np
from sig import mats, vc, qint
for name, th in [('theta0=3pi/8 ([4]=0)', 3*math.pi/8), ('pi/3 ([3]=0)', math.pi/3)]:
    A = cmath.exp(1j*th); d,E,S,G = mats(A)
    ev = np.linalg.eigvalsh((G+G.conj().T)/2)
    v = vc(A); w = S[2] @ v                       # v_{s3 c}
    w2 = S[2] @ S[2] @ v                          # v_{s3^2 c}
    def par(a,b):
        return np.linalg.matrix_rank(np.vstack([a,b]), tol=1e-9)
    T = np.linalg.matrix_power(S[0] @ S[1], 3)
    Tn = T * A**6                                  # normalised twist
    nil = Tn - np.eye(5)
    print(name, 'delta=%.4f'%d.real, 'Gram eigenvalues', np.round(ev,4))
    print('   rank[v_c, v_s3c]=', par(v,w), ' rank[v_c, v_s3^2c]=', par(v,w2),
          ' rank(A^6 T_c - 1)=', np.linalg.matrix_rank(nil, tol=1e-9),
          ' (A^6T_c-1)^2 = 0?', np.allclose(nil@nil, 0, atol=1e-9))
