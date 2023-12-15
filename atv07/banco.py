# from conta import Conta


class Banco:
    __slots__ = ['_numero', '_nome', '_contas']

    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome
        self._contas = []

    def vincularConta(self, conta):
        self._contas.append({f'{conta.get_conta}': conta})

    # def removerConta(self, conta: Conta):
    #     id_conta = conta.get_conta
    #     test = self._contas[0][f'{id_conta}']
    #     del test

    def listarConta(self):
        for i, conta in enumerate(self._contas):
            print(f'Bank: {self._numero} {i} {conta[f"{i}"]}')
