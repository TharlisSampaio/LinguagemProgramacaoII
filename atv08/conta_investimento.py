from conta import Conta


class ContaInvestimento(Conta):
    def __init__(self, numero, cliente, saldo):
        super().__init__(numero, cliente, saldo)

    def atualizar(self, taxa):
        return super().atualizar(taxa)
