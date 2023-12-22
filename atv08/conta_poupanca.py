from conta import Conta


class ContaPoupanca(Conta):

    def __init__(self, numero, cliente, saldo):
        super().__init__(numero, cliente, saldo)

    def atualizar(self, taxa):
        taxa_poupanca = taxa * 3
        valor = super().atualizar(taxa_poupanca)
        return valor
