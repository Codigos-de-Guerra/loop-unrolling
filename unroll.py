#!/usr/bin/env python3

from datetime import datetime
import posix_ipc
import sys
import os
import threading
# import time
# import mmap
# import signal
# import struct
import vish

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

def printToFile(result, filename):# {{{
    with open(filename, 'w') as output:
        buf = ""
        for line in range(len(result)):
            for col in range(len(result)):
                buf += str(result[line][col]) + " "
            buf += "\n"
        output.write(buf)

    print("Output generated! It can be found at '{}'".format(filename))# }}}

def calc_matrix(matrixA, matrixB, size):# {{{
    res = []
    for i in range(size):
        line = []
        for j in range(size):
            element = 0
            for l in range(size):
                element += matrixA[i][l] * matrixB[l][j]
            line.append(element)
        res.append(line)

    return res# }}}

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

    print(agrs)
    return agrs
# }}}

def MatrixSum(val1, val2, i, j, result):# {{{
    result[i][j] = val1 + val2# }}}

def argsMulti(A,B):# {{{
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

def MatrixMulti(val1, val2, i, j, result):# {{{
    result[i][j] = val1 + val2# }}}

def unroll(args, func, method, res):#{{{
    if method == 'proc':
        pass
    elif method == 'thre':
        self_t = threading.currentThread()
        for i in range(len(args)):
            func(*args[i], res)

    else:
        raise Exception("You got nothing!!")

# }}}

#---- Main ----#

# Matrices initialized{{{

MatrixSoma = [[0 for i in range(matrix_size) ] for i in range(matrix_size)]

MatrixVezes = [[0 for i in range(matrix_size) ] for i in range(matrix_size)]
#}}}

A, B = create_matrix(A_file, B_file)
matrix_size = len(A)

if len(A) != len(B) or len(A[0]) != len(B[0]):
    raise Exception("Matrices read can't be multiplied! Try others.")

argsSoma = argsSum(A,B)
argsVezes = argsMulti(A,B)

t1 = threading.Thread(target=unroll, args=(argsSoma, MatrixSum, 'thre', MatrixSoma))
# unroll(argsVezes, MatrixMulti, 'thre', MatrixVezes)
t1.start()

print(MatrixSoma)
print("Matriz Soma Resultado:")
printToFile(MatrixSoma, "data/{}x{}/output.dat".format(matrix_size, matrix_size))

print("Matriz Multiplicação Resultado:")
printToFile(MatrixVezes, "data/{}x{}/output.dat".format(matrix_size, matrix_size))
