class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    # Métodos para manipular os atributos
    def sacar(self, valor):
        # if valor <= self.saldo:
        #     self.saldo = self.saldo - valor
        # else:
        #     print('Saldo insuficiente!')
        self.saldo -+ valor if valor <= self.saldo else print('Saldo insuficiente')   
    
    
    def depositar(self, valor):
        self.saldo += valor if valor > 0 else print('Valor incorreto')