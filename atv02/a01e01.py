# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
# armazene os resultados em uma lista. Depois, mostre quantas vezes cada valor foi
# conseguido. Dica: use uma lista de frequência e uma função para gerar números aleatórios,
# simulando os lançamentos dos dados.

from random import randint


def jogarDado():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2, dado1+dado2


if __name__ == '__main__':
    listaResult = []
    soma = 0

    for i in range(100):
        d1, d2, result = jogarDado()
        listaResult.append(result)

    numFace = {x for x in listaResult if listaResult.count(x) > 0}
    for num in numFace:
        soma += listaResult.count(num)
        print('o numero {num} aparece {freq}.'.format(num=num, freq=listaResult.count(num)))

    print('Os dados foram jogados ', soma)
