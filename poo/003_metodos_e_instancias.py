# Métodos em instâncias de classes em Python
# self - propria instância da classe
# Método é uma função que está dentro da classe, e seu primeiro parâmetro é self.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
