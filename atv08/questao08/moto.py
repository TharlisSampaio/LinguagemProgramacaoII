from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, nome, modelo):
        super().__init__(nome, modelo)

    def abastercer(self):
        return 'Gasolina ou Alcool'
