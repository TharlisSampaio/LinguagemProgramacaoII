# Crie uma lista de todas as consoantes de uma frase


if __name__ == '__main__':
    vogais = ['a', 'e', 'i', 'o', 'u']
    print('Digite uma frase: ')
    frase = input()
    listResult = [i for i in frase if i != ' ' and not vogais.__contains__(i.lower())]
    print(listResult)
