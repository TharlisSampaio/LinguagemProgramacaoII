# Estruturas de Controle (Intermediário): Considere que você tem uma lista de números inteiros: [10, 15, 20, 25, 30].
# Escreva um algoritmo que verifique quais números na lista são divisíveis por 5 e exiba apenas esses números.

if __name__ == '__main__':
    lista = [10, 15, 20, 25, 30]

    for i in lista:
        if i % 5 == 0:
            print(f'{i} é divisivel por 5')
