from banco import Banco
from conta import Conta
from conta_corrente import ContaCorrente
from conta_especial import ContaEspecial
from conta_investimento import ContaInvestimento
from conta_test import ContaTest


c1 = Conta('001', 'Tharlis', 200)
c2 = ContaCorrente(2, 'Texugo', 500)
c3 = ContaEspecial(3, 'Texugo Junio', 150, 200)
c4 = ContaInvestimento(4, 'Tadeu', 500)
c5 = ContaTest(5, 'Fulano', 50)

c2.depositar(200)
# print(c2.get_saldo)

c3.sacar(151)
# print(c3.get_saldo, c3.credito_usado)
c3.sacar(50)
# print(c3.get_saldo, c3.credito_usado)
c3.sacar(140)
# print(c3.get_saldo, c3.credito_usado)
c3.sacar(20)
# print(c3.get_saldo, c3.credito_usado)
c1.sacar(300)

b1 = Banco(275, 'Bradesco')

b1.adcionar_conta(c1)
b1.adcionar_conta(c2)
b1.adcionar_conta(c3)
b1.adcionar_conta(c4)
b1.adcionar_conta(c5)

b1.atualiza_contas()
b1.total_atualizacao()
