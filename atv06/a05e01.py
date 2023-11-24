# Escreva duas funções que aceitem uma quantidade indeterminada de números reais e retorne a
# multiplicação entre todos os números (Uma função usando o laço for e outra usando a função reduce()).
from functools import reduce


def multiplica(*args):
    mult = 1
    for i in args:
        mult *= i
    return mult


def multiplicaComReduce(*args):
    return reduce(lambda x, y: x * y, args)


if __name__ == '__main__':
    result = multiplica(10, 10, 4)
    resultRd = multiplicaComReduce(10, 10, 4)
    print(f'multiplica sem reduce: {result} e função multiplica com reduce: {resultRd}')
