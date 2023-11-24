# Crie uma função lambda (anônima) para inverter uma string.

def invertString(palavra):
    # inverso = palavra[::-1]
    print(palavra[::-1])
    # print(list(palavra[::-1]))


if __name__ == '__main__':
    invertString('tharlis')
    print((lambda x: f'{x[::-1]}')('tharlis'))
