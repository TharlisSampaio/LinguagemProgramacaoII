def geradora():
    for i in range(10):
        yield i


g = geradora()

for i in g:
    print(i)
