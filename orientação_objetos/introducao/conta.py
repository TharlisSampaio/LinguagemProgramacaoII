from historico import Historico


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

    # Métodos para manipular os atributos
    def sacar(self, valor):
        # if valor <= self.saldo:
        #     self.saldo = self.saldo - valor
        # else:
        #     print('Saldo insuficiente!')
        self._saldo -= valor if valor <= self._saldo else print('Saldo insuficiente')
        self.historico.transacoes.append(f'Saque de {valor}')


    def depositar(self, valor):
        self._saldo += valor if valor > 0 else print('Valor incorreto')
        self.historico.transacoes.append(f'Depósito de {valor}')
        
    def ver_saldo(self):
        print(f'conta: {self.numero} - saldo: {self._saldo}')

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico.transacoes.append(f'Tranferencia de {valor}')
            
            return True
        else:
            return False

    def __str__(self):
        return f'Conta: {self.numero} - Titular: {self.titular}'
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        self._limite = valor
