from conta import Conta
from tributavel import TributavelMixIn


class ContaCorrente(Conta, TributavelMixIn):
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor

    def valor_imposto(self):
        return self._saldo * 0.02

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            self._extrato.transacoes.append(f'Saque de {valor}')
            return True

    def depositar(self, valor):
        self.saldo += valor
        self._extrato.transacoes.append(f'Depósito de {valor}')

    def ver_saldo(self):
        print(f'Número: {self.numero} Saldo:{self.saldo}')

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self._extrato.transacoes.append(f'Transferência da conta '
                                            f'{self.numero} de {valor} '
                                            f'para conta '
                                            f'{destino.numero}')
            return True
        else:
            return False

    def __str__(self):
        return f'Número:{self.numero}, Titular:{self.titular}'


if __name__ == '__main__':
    c1 = ContaCorrente('037748', 'tharlis', 5000)
    print(c1.valor_imposto())
