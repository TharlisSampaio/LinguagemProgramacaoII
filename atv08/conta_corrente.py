from conta import Conta


class ContaCorrente(Conta):

    def __init__(self, numero, cliente, saldo):
        super().__init__(numero, cliente, saldo)
        self._taxa_deposito = 0.1

    def atualizar(self, taxa):
        taxa_correne = taxa * 2
        valor = super().atualizar(taxa_correne)
        return valor

    def depositar(self, valor):
        valor_atual = super().depositar(valor) - self._taxa_deposito
        self._saldo = valor_atual
        return valor_atual
