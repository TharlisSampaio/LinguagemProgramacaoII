# 4. Manipulação de Strings (Avançado): Escreva um programa que receba uma string como entrada e conte:
# Quantas vogais (a, e, i, o, u) existem na string.
# Quantas consoantes existem. Considere apenas caracteres alfabéticos
# e ignore a distinção entre maiúsculas e minúsculas.

if __name__ == '__main__':
    entrada = input("Digite uma frase: ")
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    vogais = 0
    consoantes = 0
    for i in entrada:
        if i.lower() in lista_vogais:
            vogais += 1
        else:
            consoantes += 1

    print(f'total de vogais: {vogais}, total de cosoantes: {consoantes}')
