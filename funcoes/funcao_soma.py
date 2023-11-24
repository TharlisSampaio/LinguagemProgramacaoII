def soma(*args):
    print(type(args))
    r = 0
    for i in args:
        r += i
    return r


if __name__ == '__main__':
    result = soma(10, 20, 30, 40, 99)
    print(result)
