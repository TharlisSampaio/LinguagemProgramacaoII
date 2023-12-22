class Banco:
    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome
        self._taxa = 0.1
        self._lista_contas = []
        self._tota_atualizacao = 0

    # @property
    def total_atualizacao(self):
        print(f'Total de atualizações: {self._tota_atualizacao}')

    def adcionar_conta(self, conta):
        self._lista_contas.append(conta)

    def atualiza_contas(self):
        for c in self._lista_contas:
            try:
                print(f'Titular: {c.get_titualr}, Saldo anterior: {c.get_saldo}')
                valor = c.atualizar(self._taxa)
                print(f'Titular: {c.get_titualr}, Saldo atual: {c.get_saldo}\n')
                self._tota_atualizacao += valor
            except AttributeError as error:
                print(f'{error}')
