#############################################################################################################
    #Copyright (c) 2023, 2024 , Prof. Radhamadhab Dalai, ITER , Siksha O Aanusandhan University
    #Odisha, India,
    #Author's email address :  radhamadhabdalai@soa.ac.in
 ############################################################################################################
import numpy as np

def qr(A):
      m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        #calculate Householder matrix i: rows and i: columns from A i: rows and ith column
        H[i:, i:] = make_householder(A[i:, i])
        Q = Q@H
        A = H@A
    return Q, A
 
def make_householder(a):
    #find prependicular vector to mirror
    u = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    u[0] = 1
    H = np.eye(a.shape[0])
    #finding Householder projection
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H
