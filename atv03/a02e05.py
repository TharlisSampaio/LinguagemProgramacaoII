# Obtenha apenas os números de uma frase

if __name__ == '__main__':
    print('Digite uma frase meu chapa')
    frase = input()
    listResult = [i for i in frase if ord(i) >= 48 and ord(i) <= 57]
    print(listResult)
