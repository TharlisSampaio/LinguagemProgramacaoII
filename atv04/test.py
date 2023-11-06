def geradora():
    for i in range(10):
        yield i


ger = geradora()

while True:
    try:
        print(next(ger), end=' ')
    except:
        break

ger = geradora()
lista = list(ger)
print(lista)
