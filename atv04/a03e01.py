# 1)Crie uma função geradora para a série e imprima no formato lista: [(0, 2),
# (1, 3), (2, 4), (4, 6), (5, 7)]


def gerarSerie():
    for i in range(5):
        if i < 3:
            yield (i, i+2)
        else:
            yield (i+1, i+3)


if __name__ == '__main__':
    # for i in range(5):
    #     print(i)
    test = gerarSerie()
    print(list(test))
