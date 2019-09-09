from random import randint
import sys

def generator(size):# {{{
    filename = "data/{}x{}/".format(size,size)

    with open(filename+"X.dat", 'w') as output:
        buf = ""
        for line in range(size):
            for col in range(size):
                rand_value = randint(0, size*size + 5)
                buf += str(rand_value) + " "
            buf += '\n'
        output.write(buf)

    with open(filename+"Y.dat", 'w') as output:
        buf = ""
        for line in range(size):
            for col in range(size):
                rand_value = randint(0, size*size + 5)
                buf += str(rand_value) + " "
            buf += '\n'
        output.write(buf)
# }}}

for num in sys.argv[1:]:
    generator(int(num))
    print("Two input files for {}x{} matrices been created!".format(num,num))
