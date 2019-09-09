#!/usr/bin/env python3

from datetime import datetime
import posix_ipc
import sys
import os
import threading
# import time
# import mmap

try:
    A_file = sys.argv[1]
    B_file = sys.argv[2]

except:
    raise Exception("Not enough matrices passed down as arguments!")

def create_matrix(file1, file2):# {{{
    with open(A_file, "r") as file:
        matrix_A = []
        for line in file:
            matrix_A.append(list(map(lambda x: int(x), line.split())))


    with open(B_file, "r") as file:
        matrix_B = []
        for line in file:
            matrix_B.append(list(map(lambda x: int(x), line.split())))

    return matrix_A, matrix_B# }}}

def argsSum(A,B):# {{{
    agrs = []
    for idx_i, i in enumerate(A):
        ag = []
        for idx_j, j in enumerate(i):
            ag.append(j)
            ag.append(B[idx_i][idx_j])
            ag.append(idx_i)
            ag.append(idx_j)
            agrs.append(ag)
            ag = []

    return agrs
# }}}

def MatrixSum(val1, val2, i, j, result):# {{{
    result[i][j] = val1 + val2# }}}

def argsMulti(A,B):# {{{
    agrs = []
    for idx_i, i in enumerate(A):
        ag = []
        for idx_j, j in enumerate(i):
            a = []
            for k in range(len(A)):
                a.append(A[idx_i][k])
            ag.append(a)

            a = []
            for k in range(len(A)):
                a.append(B[k][idx_j])
            ag.append(a)

            ag.append(idx_i)
            ag.append(idx_j)
            agrs.append(ag)
            ag = []

    return agrs
# }}}

def MatrixMulti(linha, col, i, j, result):# {{{
    ans = 0
    for k in range(len(linha)):
        ans += linha[k] * col[k]

    result[i][j] = ans# }}}

def unroll(args, func, method, res):#{{{
    if method == 'proc':
        self_t = threading.currentThread()
        for i in range(len(args)):
            func(*args[i], res)

    elif method == 'thre':
        for i in range(len(args)):
            func(*args[i], res)

    else:
        raise Exception("You got nothing!!")

# }}}

#---- Main ----#
A, B = create_matrix(A_file, B_file)
matrix_size = len(A)

# Matrices initialized{{{

MatrixSoma = [[0 for i in range(matrix_size) ] for i in range(matrix_size)]

MatrixVezes = [[0 for i in range(matrix_size) ] for i in range(matrix_size)]
#}}}

if len(A) != len(B) or len(A[0]) != len(B[0]):
    raise Exception("Matrices read can't be multiplied! Try others.")

argsSoma = argsSum(A,B)
argsVezes = argsMulti(A,B)

a = datetime.now()
unroll(argsSoma, MatrixSum, 'thre', MatrixSoma)
b = datetime.now()

seq_sum = (b-a).total_seconds() * 1000 #milliseconds

c = datetime.now()
unroll(argsVezes, MatrixMulti, 'thre', MatrixVezes)
d = datetime.now()

seq_mul = (d-c).total_seconds() * 1000 #milliseconds

print("Sequential sum took {} milliseconds to complete.".format(seq_sum))
print("Sequential multiplication took {} milliseconds to complete.".format(seq_mul))
