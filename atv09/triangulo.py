from forma_geometrica import FormaGeometrica
import math


# A área de um triângulo é dada por sqrt(s*(s-a)*(s-b)*(s-c)), onde sqrt é a
# função que calcula a raiz quadrada, a, b e c são os lados do triângulo, e s é
# a metade do perímetro do triângulo. O perímetro do triângulo é calculado
# como (a+b+c).


class Triangulo(FormaGeometrica):
    def __init__(self, lado_a, lado_b, lado_c):
        super().__init__()
        self._lado_a = lado_a
        self._lado_b = lado_b
        self._lado_c = lado_c

    def perimetro(self):
        return self._lado_a + self._lado_b + self._lado_c

    def area(self):
        s = self.perimetro()
        return math.sqrt(s*(s-self._lado_a)*(s-self._lado_b)*(s-self._lado_c))

    def dados(self):
        return super().dados()


if __name__ == '__main__':
    t1 = Triangulo(2, 2, 2)
    print(t1.area())
    print(t1.perimetro())
    print(t1.dados())
    print(type(t1))
