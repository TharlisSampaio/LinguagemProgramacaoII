from conta import Conta


class ContaCorrente(Conta):
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor

    def valor_imposto(self):
        return self._saldo * 0.02


if __name__ == '__main__':
    c1 = ContaCorrente('037748', 'tharlis', 5000)
    print(c1.valor_imposto())
