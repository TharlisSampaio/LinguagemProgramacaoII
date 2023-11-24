# Faça um programa que solicite seis números do usuário e
# exiba apenas os números com mais de 2
# dígitos. Utilize a função filter() para fazer isso.

def filterM(lista):
    print(list(filter(lambda x: x >= 100 or x <= -100, lista)))


if __name__ == '__main__':
    print('Digite seis números')
    listaNum = []
    for i in range(6):
        listaNum.append(int(input()))

    print(listaNum)
    filterM(listaNum)
