import random


with open('pares.txt', 'w') as pares:
    with open('impares.txt', 'w') as impares:
        for i in range(10000):
            x = random.randint(1, 1000)
            if x % 2 == 0:
                pares.write(f'{str(x)}\n')
            else:
                impares.write(f'{str(x)}\n')
