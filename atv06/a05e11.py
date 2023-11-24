# Escreva uma função geradora que imprima apenas o enésimo termo da série de Fibonacci de acordo
# com uma entrada fornecida.

def enesFibonacci(entrada):
    # if entrada == 1 or entrada == 2:
    # return 1
    # else:
    #     return enesFibonacci(entrada - 1) + enesFibonacci(entrada - 2)
    ultimo = 1
    penultimo = 1
    if entrada == 1 or entrada == 2:
        yield 1
    for i in range(2, entrada):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        if i == entrada-1:
            yield termo


if __name__ == '__main__':
    result = enesFibonacci(9)
    print(result.__next__())
