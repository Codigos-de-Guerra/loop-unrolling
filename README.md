# _Loop unrolling_

O _loop unrolling_ é uma técnica de otimização do tempo de execução de programas
aumentando o tamanho do arquivo binário. Consiste basicamente em executar as
várias iterações de um loop em paralelo.

Um exemplo de execução do _loop unrolling_ é a seguinte

```python
for i in range(3):
    print(i)
```

O código acima seria executado todo em paralelo, como se as três chamadas à
função `print` fossem executadas sequencialmente:

```python
print(0)
print(1)
print(2)
``

## Soluções implementadas

O _unrolling_ foi executado com uma função `unroll(args, func, method, res)`,
onde `args` são os argumentos passados como parâmetro para a função `func` (a
qual será executada dentro da função `unroll`) em forma de matriz, `method` pode
ser ou `'proc'` ou `'thre'`, identificando assim que se deseja paralelizar o
loop com processos (`'proc'`) ou threads (`'thre'`); e por último uma lista para
armazenar cada um dos resultados de cada execução de `func` com os argumentos
devidos.

Nesse repositório utilizamos a `unroll` para realizar a soma e multiplicação de
duas matrizes. As matrizes estão armazenadas como arquivos de texto dentro da
pasta `data`, contendo matrizes de diversos tamanhos. Também é possível gerar
matrizes com valores randômicos através do arquivo `generator.py`.

### Threads

Para executar em paralelo usando threads, se fez necessário criar uma thread
para cada execução do loop, sendo assim ficamos com o seguinte código:

```python
for i in range(len(args)):
    t = threading.Thread(target=func, args=(*args[i], res))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
```

Onde criamos uma thread com a função alvo sendo a função passada como parâmetro
para o `unroll` e os argumentos são uma tupla com os arguemntos propriamente
ditos para a execução da função e a lista para armazenar os resultados.
