import sys
# from pathlib import Path

def main():
    import sequential
    import unroll

    par_sum, par_mul = unroll.parallel()
    seq_sum, seq_mul = sequential.seq()

    a = (sys.argv[1][5:]).split('x')
    matrix_size = int(a[0])

# Terminal outputs{{{
    print("Sequential Sum time: {} milliseconds".format(seq_sum))
    print("Sequential Multiplication time: {} milliseconds".format(seq_mul))

    print("Thread Sum time: {} milliseconds.".format(par_sum))
    print("Thread Multiplication time: {} milliseconds.".format(par_mul))# }}}

    print("Matriz Soma Resultado:")
    unroll.printToFile(unroll.Sum(), "data/{}x{}/outputSum.dat".format(matrix_size, matrix_size), seq_sum, par_sum)

    print("Matriz Multiplicação Resultado:")
    unroll.printToFile(unroll.Mul(), "data/{}x{}/outputMul.dat".format(matrix_size, matrix_size), seq_mul, par_mul)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Not enough arguments! Try again.")
        # for i in sorted(Path().glob('data/*')):
        #     print(str(i)[5:])
    else:
        main()
