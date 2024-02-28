from conta_corrente import ContaCorrente
from seguro_de_vida import SeguroDeVida
from banco import Banco
from cliente import Cliente
from manipulador import ManipuladorDeTributaveis


if __name__ == '__main__':
    banco1 = Banco('001', 'Banco do Brasil')
    cl1 = Cliente('Tadeu', 'Junior', '300300300-30')
    cr1 = ContaCorrente('37890-5', cl1, 54360)

    banco2 = Banco('237', 'Bradesco')
    cl2 = Cliente('Fulano', 'Junior', '300300300-30')
    cr2 = ContaCorrente('37890-5', cl1, 5894360)

    banco3 = Banco('246', 'Banco ABC')
    cl3 = Cliente('Ciclano', 'Junior', '300300300-30')
    cr3 = ContaCorrente('37890-5', cl1, 184360)

    seg1 = SeguroDeVida('2237', 15000, cl2)
    seg2 = SeguroDeVida('2238', 5000, cl1)

    lista = [cr1, cr2, cr3, seg1, seg2]
    lista_tributaveis = []

    for i in lista:
        valor = i.valor_imposto()
        lista_tributaveis.append(valor)

    manipulador = ManipuladorDeTributaveis()

    print(f'{manipulador.calcular_impostos(lista_tributaveis):.2f}')
