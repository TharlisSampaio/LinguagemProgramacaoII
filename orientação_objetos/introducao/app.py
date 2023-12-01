from conta import Conta
from cliente import Cliente

cliente = Cliente('Texugo', 'Junior', '30030030030')
cliente2 = Cliente('Tadeu', 'Silva', '95157365481')
# Instanciar um objeto da classe Conta
c1 = Conta(1, cliente, 1000, 500)
c2 = Conta(2, cliente2, 2000, 600)
print(c1)

c1.set_limite = 200
print(c1.limite)

c1.sacar(100)
c1.depositar(1200)
print(c1.historico.transacoes)
# print(type(c1))  # Tipo de objeto
# print(c1.titular)
# print(c1.saldo)

# c1.saldo = 1500 # manipulando o atributo da classe Conta
# print(c1.saldo)

# Não é recomendado pois altera a "receita" origianal (a class Conta)
# c1.chave_pix = 'tharlis.sampaio@com'
# print(c1.chave_pix)

# c2 = Conta(2, 'Tharlis', 2000, 750)
# print(c2.chave_pix)
