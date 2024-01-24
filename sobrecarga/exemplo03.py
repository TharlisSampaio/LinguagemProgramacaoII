from functools import reduce


class Calculadora:
    def soma(self, *args):
        if isinstance(args[0], str):
            total = ''
        else:
            total = 0
        for i in args:
            total += i
        return total


class Calculadora2:
    def soma(self, *args):
        return reduce(lambda a, b: a+b, args)


s1 = Calculadora()
print(s1.soma(2, 2))
print(s1.soma(2.2, 2.4))
print(s1.soma('py', 'thon'))
