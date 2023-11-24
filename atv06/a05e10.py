# Utilize a função reduce() para imprimir a concatenação das palavras de uma lista, com um espaço em
# branco entre as palavras.

from functools import reduce


def concat(n):
    pass


if __name__ == '__main__':
    frase = input().split(' ')
    print(frase)
    lista = reduce(lambda x, y: x.join(y), frase)
    print(list(lista))
