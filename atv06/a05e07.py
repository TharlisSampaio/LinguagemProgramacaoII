# Usando uma função anônima que receba dois argumentos iteráveis e a função filter(), imprima os
# valores que são comuns nos dois argumentos.

if __name__ == '__main__':
    listaX = [1, 2, 3, 4]
    listay = [2, 4, 6, 8]
    result = filter((lambda x: x in listaX), listay)
    print(list(result))
