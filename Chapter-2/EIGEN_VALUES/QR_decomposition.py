#############################################################################################################
    #Copyright (c) 2023, 2024 , Prof. Radhamadhab Dalai, ITER , Siksha O Aanusandhan University
    #Odisha, India,
    #Author's email address :  radhamadhabdalai@soa.ac.in
 ############################################################################################################
import numpy as np

def qr_factorization(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q @ v
            v = v - R[i, j] * q
        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R
