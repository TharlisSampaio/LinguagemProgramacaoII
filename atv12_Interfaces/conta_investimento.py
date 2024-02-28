from conta import Conta


class ContaInvestimento(Conta):
    def valor_imposto(self):
        return self._saldo * 0.03
