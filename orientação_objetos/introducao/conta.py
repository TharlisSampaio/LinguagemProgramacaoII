from historico import Historico


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    # Métodos para manipular os atributos
    def sacar(self, valor):
        # if valor <= self.saldo:
        #     self.saldo = self.saldo - valor
        # else:
        #     print('Saldo insuficiente!')
        self.saldo -= valor if valor <= self.saldo else print('Saldo insuficiente')
        self.historico.transacoes.append(f'Saque de {valor}')


    def depositar(self, valor):
        self.saldo += valor if valor > 0 else print('Valor incorreto')
        self.historico.transacoes.append(f'Depósito de {valor}')
        
    def ver_saldo(self):
        print(f'conta: {self.numero} - saldo: {self.saldo}')

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico.transacoes.append(f'Tranferencia de {valor}')
            
            return True
        else:
            return False

    def __str__(self):
        return f'Conta: {self.numero} - Titular: {self.titular}'
