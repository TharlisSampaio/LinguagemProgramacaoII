# Retorne uma lista de tuplas onde o primeiro valor é um inteiro de 1 até 100 e o
# segundo valor é um número aleatório entre 0 e 100 quando o primeiro é ímpar, caso
# contrário será a string ‘par’


import random

if __name__ == '__main__':
    listResult = [(i, random.randint(0, 100)) if i % 2 != 0 else (i, 'par') for i in range(100)]
    print(listResult)
