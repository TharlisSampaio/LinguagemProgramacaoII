interador = iter('abc')
print(interador.__next__())
print(next(interador))
print(type(interador))


lista_alunos  = ['fulano', 'fulano2', 'fulano3']
alunos_i = enumerate(lista_alunos)

print(next(alunos_i))
for index, valor in enumerate(lista_alunos):
    print(f'indice: {index}, valor: {valor}')

for valor in reversed(lista_alunos):
    print(f'valor: {valor}')


listaNum = [10, 20, 30]
quadradro = (i**2 for i in listaNum)
print(type(quadradro))
#print(quadradro.__next__())
#print(next(quadradro))

z = zip(listaNum, quadradro)
print(type(z))
for i in z:
    print(i)
