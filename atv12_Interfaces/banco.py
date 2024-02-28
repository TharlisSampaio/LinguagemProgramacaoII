from manipulador import ManipuladorDeTributaveis


class Banco:
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._total_tributos = 0
        self._lista_servicos = []

    def calculadr_tributos_servicos(self, manipulador: ManipuladorDeTributaveis):
        self._total_tributos = manipulador.calcular_impostos(self._lista_servicos)

    def add_servico(self, servico):
        self._lista_servicos.append(servico)

    def get_total_tributos(self):
        return self._total_tributos
