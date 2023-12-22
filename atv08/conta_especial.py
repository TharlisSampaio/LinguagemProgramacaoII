from conta_corrente import ContaCorrente


class ContaEspecial(ContaCorrente):

    def __init__(self, numero, cliente, saldo, limite_credito):
        super().__init__(numero, cliente, saldo)
        self._limite_credito = limite_credito
        self._credito_usado = 0

    @property
    def credito_usado(self):
        return self._credito_usado

    def limite_disponivel(self):
        return self._limite_credito - self._credito_usado

    def sacar(self, valor):
        if super().sacar(valor):
            return True
        else:
            # print(self._credito_usado, self._limite_credito)
            aux = self.credito_usado
            aux = aux + valor
            if self._saldo != 0 and (self._limite_credito >= aux):
                self._saldo = self._saldo - valor
                self._credito_usado = -self._saldo
                return True
            else:
                print(f'Limite insuficiente!!. Limite disponivel: {self._limite_credito - self._credito_usado}\n')
