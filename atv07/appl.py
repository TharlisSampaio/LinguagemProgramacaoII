from banco import Banco
from conta import Conta
from cliente import Cliente
from emprestimo import Emprestimo

cliente1 = Cliente('Texugo', 'rua padre jose', '04332759281', 24)

bank1 = Banco('275', 'Texugo Invest')

conta1 = Conta(cliente1, 0, 10000)
conta2 = Conta(cliente1, 5000, 10000)
conta3 = Conta(cliente1, 5000, 10000)

# conta1.encerrar_conta()
# print(conta1)

bank1.vincularConta(conta1)
bank1.vincularConta(conta2)
bank1.vincularConta(conta3)
bank1.listarConta()
# print('-'*12)
# # bank1.removerConta(conta1)
# bank1.listarConta()

print('-'*12)

emp1 = Emprestimo(conta1, 10000, 48, 10)
print(emp1.montante_final())
print(emp1._montante_final)
