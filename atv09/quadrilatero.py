from forma_geometrica import FormaGeometrica


class Quadrilatero(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self._base = base
        self._altura = altura

    def area(self):
        return self._base * self._altura

    def perimetro(self):
        return (2*self._base) + (2*self._altura)

    def dados(self):
        return super().dados()


if __name__ == '__main__':
    q1 = Quadrilatero(6, 4)
    print(q1.area())
    print(q1.perimetro())
    print(q1.dados())
