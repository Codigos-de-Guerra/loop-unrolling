import matplotlib.pyplot as plt
import sys

with open(sys.argv[1], 'r') as file:
    a = []
    for line in file:
        a.append(list(map(lambda x:float(x), line.split())))

with open(sys.argv[2], 'r') as file:
    b = []
    for line in file:
        b.append(list(map(lambda x:float(x), line.split())))

x = [ 1,2,3,4,5,6,8,10,20,30,40,50,75,100 ]
tempos_seq = a[0]
tempos_par = a[1]

plt.plot(x,tempos_seq, label='Sequencial')
plt.plot(x,tempos_par, label='Thread')

plt.title('Tamanho matriz por tempo (ms) | Multiplicação')
plt.xlabel("Tamanho da matriz NxN")
plt.ylabel("Tempo em millisegundos (ms)")

plt.legend()
plt.show()

tempos_seq = b[0]
tempos_par = b[1]

plt.plot(x,tempos_seq, label='Sequencial')
plt.plot(x,tempos_par, label='Thread')

plt.title('Tamanho matriz por tempo (ms) | Soma')
plt.xlabel("Tamanho da matriz NxN")
plt.ylabel("Tempo em millisegundos (ms)")

plt.legend()
plt.show()
