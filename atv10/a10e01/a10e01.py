import math
from abc import ABC, abstractmethod


class Forma(ABC):
    def __init__(self, *args):
        tam = len(args)
        if tam == 1:
            self._tipo = 'Circulo'
            self._raio = args[0]
            self._pi = 3.14159265
        elif tam == 2:
            self._tipo = 'Quatrilatero'
            self._base = args[0]
            self._altura = args[1]
            if args[0] == args[1]:
                self._tipo = 'Quadrado'
        elif tam == 3:
            self._tipo = 'Tringulo'
            self._lado_a = args[0]
            self._lado_b = args[1]
            self._lado_c = args[2]
            if ((self._lado_a + self._lado_b > self._lado_c)
                    and (self._lado_a + self._lado_c > self._lado_b)
                    and(self._lado_c + self._lado_b > self._lado_a)):
                self._tipo = 'Triangulo'
            else:
                self._tipo = 'Forma desconhecida'

    def __str__(self):
        return f'area: {self.area():.2f}; perímetro: {self.perimetro():.2f}'

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Circulo(Forma):
    def __init__(self, raio):
        super().__init__(raio)

    def area(self):
        return self._pi * (self._raio**2)

    def perimetro(self):
        return 2*(self._pi*self._raio)

    def __str__(self):
        return f'tipo: {self._tipo}, {super().__str__()}'


class Quatrilatero(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def __str__(self):
        return super().__str__()

    def area(self):
        return self._base * self._altura

    def perimetro(self):
        return (2*self._base) + (2*self._altura)


class Triangulo(Forma):
    def __init__(self, lado_a, lado_b, lado_c):
        super().__init__(lado_a, lado_b, lado_c)

    def perimetro(self):
        return self._lado_a + self._lado_b + self._lado_c

    def area(self):
        s = self.perimetro()
        return math.sqrt(s*(s-self._lado_a)*(s-self._lado_b)*(s-self._lado_c))

    def __str__(self):
        return super().__str__()


# c1 = Circulo(5)
# print(c1)


if __name__ == "__main__":
    c1 = Circulo(6)
    print(c1.__str__())

    q1 = Quatrilatero(5, 9)
    print(q1.__str__())

    t1 = Triangulo(1, 1, 1)
    print(t1.__str__())
