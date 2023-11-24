# Usando uma função anônima e a função map() receba dois argumentos iteráveis, retorne e imprima a
# potência de cada elemento do primeiro argumento elevado ao elemento correspondente no segundo
# argumento.

if __name__ == '__main__':
    listaX = [1, 2, 3, 4]
    listay = [2, 4, 6, 8]
    result = map(lambda x, y: x ** y, listaX, listay)
    print(list(result))
