# Faça um programa que leia duas strings do teclado e informe: (i) os caracteres do primeiro
# texto que não estão no segundo; (ii) os caracteres do segundo texto que não estão no
# primeiro; (iii) os caracteres que estão em ambos os textos; (iv) o número total de caracteres
# distintos em ambos os textos.


if __name__ == '__main__':
    primeiraString = input()
    segundaString = input()

    caracteresPrim = {x for x in primeiraString if x != ' '}
    caracteresSeg = {x for x in segundaString if x != ' '}

    subConj = caracteresPrim & caracteresSeg
    uniao = caracteresPrim.union(caracteresSeg)
    # difference A diferença entre dois conjuntos é um conjunto contendo os elementos do conjunto à esquerda que não estão no conjunto à direita do operador.
    # intersection: elemento que esta presente em ambos conjuntos
    print(caracteresPrim, caracteresSeg)
    print(f'Elmento do conjunto {caracteresPrim} que não estão contidos em {caracteresSeg} = {caracteresPrim.difference(caracteresSeg)}')
    print(f'Elmento do conjunto {caracteresSeg} que não estão contidos em {caracteresPrim} = {caracteresSeg.difference(caracteresPrim)}')
    print(f'Interseão do {caracteresSeg} e {caracteresPrim} = {caracteresSeg.intersection(caracteresPrim)}')
    print(f'Elementos que não são comuns entre os conjuntos {caracteresSeg} e {caracteresPrim} = {caracteresSeg.symmetric_difference(caracteresPrim)}')
    print(f'Total de elementos distintos entre os conjuntos {caracteresPrim} e {caracteresSeg} é = {len(caracteresSeg.symmetric_difference(caracteresPrim))}')
