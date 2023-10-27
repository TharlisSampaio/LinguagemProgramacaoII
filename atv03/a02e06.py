# Encontre todas as palavras em uma frase com mais de 5 letras


if __name__ == '__main__':
    print('Digite um frase meu chapa')
    frase = input().strip()
    listResult = [i for i in frase.split(' ') if f'{i}'.__len__() == 5]
    print(listResult)
