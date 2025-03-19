lista = []
lista.append('carne')
lista.append('pão')
lista.append('')
lista.append('cerveja')

print(lista)

#  o metodo pop() sem parametro remove o ultimo da lista
lista.pop(2)

lista.sort()  # ordena a lista
print(lista)
lista[2] = 'Pão de alho'

lista2 = lista[0:1]
print(lista2)

d = dict()
d['carne'] = 15.99
d.update({'fangro': 12.99})
print(d)
print(d.items())
