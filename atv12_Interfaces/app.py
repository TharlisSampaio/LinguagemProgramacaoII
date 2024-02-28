from conta_corrente import ContaCorrente
from seguro_de_vida import SeguroDeVida
from conta_poupanca import ContaPoupanca
from conta_investimento import ContaInvestimento
from tributavel_Interface import TributavelInterface
from manipulador import ManipuladorDeTributaveis
from banco import Banco


if __name__ == '__main__':
    TributavelInterface.register(ContaCorrente)
    TributavelInterface.register(SeguroDeVida)
    TributavelInterface.register(ContaInvestimento)
    cr1 = ContaCorrente('37890-5', 'Tadeu', 10000)
    cr2 = ContaCorrente('37590-7', 'Fulano', 100000)
    cr3 = ContaCorrente('37550-2', 'Texugo', 10000000)

    cp1 = ContaPoupanca(numero='34437-8', cliente='Josefina', saldo=500000)

    seg1 = SeguroDeVida('2237', 15000, 'Fulano')
    seg2 = SeguroDeVida('2238', 5000, 'Texugo')

    cv1 = ContaInvestimento('34479', 'Ratel', 1500000)

    manipulador = ManipuladorDeTributaveis()

    lista = [cr1, cr2, cr3, seg1, seg2, cp1, cv1]

    # print((manipulador.calcular_impostos(lista)))
    # for i in lista:
    #     manipulador.calcular_impostos(i)

    bank1 = Banco('001', 'Banco do Brasil')
    for i in lista:
        bank1.add_servico(i)

    bank1.calculadr_tributos_servicos(manipulador)
    print(bank1.get_total_tributos())
