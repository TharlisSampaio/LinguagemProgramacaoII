# Crie um programa que leia 5 números inteiros e os armazene em uma lista de tal forma que
# todos os números maiores ou iguais que o primeiro fiquem ao lado direito e todos os menores
# fiquem ao lado esquerdo.

if __name__ == '__main__':
    listaUniao = []
    listaEsq = []
    listaDir = []

    priElem = int(input())
    listaDir.append(priElem)
    for i in range(4):
        entrada = int(input())
        if entrada < priElem:
            listaEsq.append(entrada)
        else:
            listaDir.append(entrada)

listaUniao = listaEsq + listaDir
print(listaUniao)

# print(listaInteiros)
