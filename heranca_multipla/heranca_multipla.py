class A:
    def m1(self):
        print('metodo de A')


class B(A):
    def m2(self):
        print('metodo de B')


class C(B):
    def m3(self):
        print('metodo C')


class D(B, C):
    pass


if __name__ == '__main__':
    d = D()
    d.m2