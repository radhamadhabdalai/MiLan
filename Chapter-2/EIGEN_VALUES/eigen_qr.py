#############################################################################################################
    #Copyright (c) 2023, 2024 , Prof. Radhamadhab Dalai, ITER , Siksha O Aanusandhan University
    #Odisha, India,
    #Author's email address :  radhamadhabdalai@soa.ac.in
 ############################################################################################################
import numpy as np
def find_eig_qr(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(100):
            Q,R = qr_factorization
           # Q,R = np.linalg.qr(X) # replace this line with above
            pQ = pQ @ Q;
            X = R @ Q;
    return np.diag(X), pQ
