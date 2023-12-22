class Conta:
    def __init__(self, numero, cliente, saldo):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo

    @property
    def get_titualr(self):
        return self._titular

    @property
    def get_saldo(self):
        return self._saldo

    def atualizar(self, taxa):
        valor = self._saldo * taxa
        if self._saldo >= 0:
            self._saldo -= valor
            return valor
        else:
            self._saldo -= -valor
            return -valor

    def sacar(self, valor):
        if valor > self._saldo:
            return False
        else:
            self._saldo -= valor
            return True

    def depositar(self, valor):
        valor_atual = self._saldo - valor
        self._saldo = valor_atual
        return valor_atual

    def ver_saldo(self):
        print(f'Número: {self._numero} Saldo: {self._saldo}')

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False

    def __str__(self):
        return f'Titular: {self._titular} Saldo: {self._saldo}'
