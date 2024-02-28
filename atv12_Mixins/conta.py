import abc
from historico import Historico


class Conta(abc.ABC):
    def __init__(self, numero, cliente, saldo):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._extrato = Historico()

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
