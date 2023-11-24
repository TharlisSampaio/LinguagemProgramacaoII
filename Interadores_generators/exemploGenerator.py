def imprimeLinha():
    print('linha1')
    yield 1
    print('linha2')
    yield 2
    print('linha3')
    yield 3
    print('linha4')


# ret = imprimeLinha()
# print(ret)

gerador = imprimeLinha()
print(next(gerador))
