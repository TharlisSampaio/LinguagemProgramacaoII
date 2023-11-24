# Utilize a função map() para imprimir o tamanho e a quantidade de vogais de cada palavra de uma frase.

def imprimir(palavra):
    vogais = 'aeiou'
    qtd_vogais = sum([1 for letra in palavra if letra.lower() in vogais])
    return len(palavra), qtd_vogais


if __name__ == '__main__':
    frase = 'ola meu chapa'
    result = map(lambda x: imprimir(x), frase.split(' '))
    print(list(result))
