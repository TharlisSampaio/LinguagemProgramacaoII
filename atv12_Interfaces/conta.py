import abc


class Conta(abc.ABC):
    def __init__(self, numero, cliente, saldo):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo

    def atualiza(self, taxa):
        pass

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

    def ver_saldo(self):
        pass

    def transferir(self, destino, valor):
        pass

    def __str__(self):
        pass
