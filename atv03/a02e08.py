# Use dicionário para contar a quantidade de caracteres de cada palavra de uma frase


if __name__ == '__main__':
    print('Digite um frase meu chapa')
    frase = input()
    listResult = {f'{i}': i.__len__() for i in frase.split(' ')}
    print(listResult)
