# 3)Defina uma função geradora para imprimir 6 números (entre 1 e 60) da
# mega sena


import random


def gerarNum():
    # for i in range(6):
    #     yield random.randint(0, 60)
    listNum = []
    while len(listNum) != 6:
        num = random.randint(0, 61)
        if not (num in listNum):
            listNum.append(num)
            yield num


if __name__ == '__main__':
    numSort = gerarNum()
    print(list(numSort))
