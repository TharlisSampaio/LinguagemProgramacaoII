from conta import Conta


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor

    def __str__(self):
        return f'{self.__dict__}'
