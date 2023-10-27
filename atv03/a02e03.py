# Contar o número de espaços em branco de uma frase

if __name__ == '__main__':
    
    print('Digite uam frase: ')
    frase = input()
    print(frase)
    espacos = [[i for i in frase].count(' ')][0]
    print(f'A frase: {frase} possui {espacos} em bracos')