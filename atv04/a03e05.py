# 5)Implemente uma função que recebe um iterator e retorna os elementos
# sem repetições do mesmo elemento em sequencia. Entrada:
# 'aaabbacabbbd' Saída: ['a', 'b', 'a', 'c', 'a', 'b', 'd']

def removeRept(entrada):
    atual = ''
    while True:
        try:
            prox = entrada.__next__()
            if atual != prox:
                yield prox
                atual = prox
        except StopIteration:
            break


if __name__ == '__main__':
    result = removeRept(iter('aaabbacabbbd'))
    print(list(result))
