from forma_geometrica import FormaGeometrica


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self._raio = raio
        self._pi = 3.14159265

    def area(self):
        return self._pi * (self._raio**2)

    def perimetro(self):
        return 2*(self._pi*self._raio)

    def dados(self):
        return super().dados()


if __name__ == '__main__':
    c1 = Circulo(5)
    print(c1.area())
    print(c1.perimetro())
    print(c1.dados())
