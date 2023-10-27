# Escreva um programa que leia uma frase digitada pelo usuário, calcule e mostre a frequência
# relativa de cada letra na frase, em ordem lexicográfica, usando dicionários. Ignore caracteres
# brancos e pontuação.

if __name__ == '__main__':
    print('Digite uma frase que contenha caracteres de A - Z')
    frase = input()
    caracteres = [i for i in frase if i != ' ']
    caracteresOdernados = sorted(caracteres)
    dicio = {f'{i}': caracteresOdernados.count(i) for i in caracteresOdernados}
    print(dicio)
