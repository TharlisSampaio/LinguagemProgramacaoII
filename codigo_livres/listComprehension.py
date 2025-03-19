lista = []

for i in range(11):
    if i % 2 == 0:
        lista.append(i**i)

lista2 = []
lista2 = [i**i for i in range(11) if i % 2 == 0]

print(lista)
print(lista2)
