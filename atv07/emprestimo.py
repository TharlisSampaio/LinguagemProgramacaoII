class Emprestimo:
    __slots__ = ['_valor', '_parcelas', '_juros', '_conta', '_montante_final']

    def __init__(self, conta, valor, parcelas, juros):
        self._valor = valor
        self._parcelas = parcelas
        self._juros = juros / 100
        self._conta = conta
        self._montante_final = 0

    def montante_final(self):
        montante = 0
        montante = self._valor * ((1 + self._juros)**self._parcelas)
        self._montante_final = montante
        return montante
