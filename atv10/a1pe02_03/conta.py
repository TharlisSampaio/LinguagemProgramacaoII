from abc import ABC, abstractmethod


class Conta(ABC):
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

    @abstractmethod
    def atualizar(self, taxa):
        pass

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


class ContaInvestimento(Conta):
    def __init__(self, numero, cliente, saldo):
        super().__init__(numero, cliente, saldo)
        self._taxa_administracao = 9.99

    def atualizar(self, taxa):
        taxa = taxa / 100
        valor = self._saldo * taxa
        if self._saldo >= 0:
            self._saldo += valor - self._taxa_administracao
            return valor
        else:
            self._saldo -= -valor + self._taxa_administracao
            return -valor


if __name__ == "__main__":
    # ao executar ira acontecer um erro, já que classes abstratas não permitem criação
    # de objetos
    # c1 = Conta('0090', 'Texugo', 5000)

    # neste caso ocerra um erro se o método abstrato atualizar() não estiver implementado
    c1 = ContaInvestimento('0056', 'Texugo', -5000)
    c1.atualizar(10)
    print(c1.get_saldo)
