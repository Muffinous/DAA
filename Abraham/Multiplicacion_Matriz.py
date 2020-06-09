from random import randint
import numpy as np

def mat_mult(A,B):
    M = len(A)
    N = len(A[0]) #Longitud filas

    assert N == len(B)
    L = len(B[0])

    result = np.zeros(M,L)
    for i in range(M):
        for j in range(L):
            cell = 0
            for k in range(N):
                cell += A[i][k]* B[k][j]
            result [i][j] = cell
    return result

def rand_mat(exp):
    return np.random.randint(30, size={2 ** exp, 2 ** exp})

def test_Random():
    A = rand_mat(9)
    B = rand_mat(9)
