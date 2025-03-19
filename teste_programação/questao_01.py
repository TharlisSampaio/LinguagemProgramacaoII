# 1. Lógica de Programação (Fácil): Escreva um programa que receba dois números inteiros como entrada e exiba
# a soma, subtração, multiplicação e divisão dos dois números. Certifique-se de tratar divisões por zero.

def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return 'Não é possivel fazer divisão por 0'

    return x / y


if __name__ == '__main__':
    entrada_a = input('Digite um valor inteiro ')
    entreda_b = input('Digite um valor inteiro ')

    try:
        entrada_a = int(entrada_a)
        entreda_b = int(entreda_b)

        print(f'soma {entrada_a} + {entreda_b} = {soma(entrada_a, entreda_b)}')
        print(f'subtracao {entrada_a} - {entreda_b} = {subtracao(entrada_a, entreda_b)}')
        print(f'multiplicação {entrada_a} * {entreda_b} = {multiplicacao(entrada_a, entreda_b)}')
        print(f'divisão {entrada_a} / {entreda_b} = {divisao(entrada_a, entreda_b)}')
    except:
        print('Valores de entreda devem ser inteiros')
