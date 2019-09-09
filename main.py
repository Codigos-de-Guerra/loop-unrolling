import sys

def main():
    import sequential
    import unroll

    # par_sum = par_mul = seq_sum = seq_mul = (b-a).total_seconds()

    par_sum, par_mul = unroll.parallel()
    seq_sum, seq_mul = sequential.seq()

    print("Sequential Sum time: {} milliseconds".format(seq_sum))
    print("Sequential Multiplication time: {} milliseconds".format(seq_mul))

    print("Thread Sum time: {} milliseconds.".format(par_sum))
    print("Thread Multiplication time: {} milliseconds.".format(par_mul))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Hell no nigga")
    else:
        main()
