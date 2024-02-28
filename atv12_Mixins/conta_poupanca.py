from conta import Conta


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor

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
