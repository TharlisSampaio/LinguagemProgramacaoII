class Conta:
    __slots__ = ['_numero', '_cliente', '_saldo', '_limite']
    _contas_criadas = 0

    def __init__(self, cliente, saldo, limite):
        self._numero = Conta._contas_criadas
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        Conta._contas_criadas += 1

    # def encerrar_conta(self):
    #     if self._saldo == 0:
    #         self.

    @property
    def get_conta(self):
        return self._numero

    @property
    def get_saldo(self):
        return self._saldo

    def encerrar_conta(self):
        if self._saldo == 0:
            print('conta deletada')
            del self

    def depositar(self, valor):
        self._saldo += valor if valor > 0 else print('Valor incorreto')
        self.historico.transacoes.append(f'Depósito de {valor}')

    def ver_saldo(self):
        print(f'conta: {self.numero} - saldo: {self._saldo}')

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico.transacoes.append(f'Tranferencia de {valor}')
            return True
        else:
            return False

    def __str__(self):
        return f'Conta: {self._numero} - Titular: {self._cliente._nome}'
