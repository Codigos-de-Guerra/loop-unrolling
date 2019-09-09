#!/usr/bin/env python3

from datetime import datetime
import sys
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

def printToFile(result, filename):# {{{
    with open(filename, 'w') as output:
        buf = ""
        for line in range(len(result)):
            for col in range(len(result)):
                buf += str(result[line][col]) + " "
            buf += "\n"
        output.write(buf)

    print("Output generated! It can be found at '{}'".format(filename))# }}}

A, B = create_matrix(A_file, B_file)
matrix_size = len(A)

if len(A) != len(B) or len(A[0]) != len(B[0]):
    raise Exception("Matrices read can't be multiplied! Try others.")

a = datetime.now()
C = calc_matrix(A, B, matrix_size)
b = datetime.now()

time_took = (b-a).total_seconds() * 1000

# print(A)
# print(B)

print("Matriz Resultado:")
# buf = ""
# for i in C:
#     buf += "| "
#     for j in i:
#         buf += str(j) + " "
#     buf += '|\n'

# print(buf)
printToFile(C, "data/{}x{}/output.dat".format(matrix_size, matrix_size))
print("Sequencial took {} milliseconds".format(time_took))
