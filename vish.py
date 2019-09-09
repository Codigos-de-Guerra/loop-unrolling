#!/usr/bin/env python3

import sys

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

