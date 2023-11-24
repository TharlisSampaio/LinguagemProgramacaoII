# Uma empresa lhe contratou para processar as
# faturas de cartão de crédito que estão
# organizadas em uma lista de tuplas
# ● Fatura = [(‘Net’, 199.9),(‘Ifood’, 999.87),(‘Gasolina’, 678.0),(‘Formigão’, 400)]
# ● Vc precisa manipular essas informações para:
# – Imprimir no formato ‘Tipo de gasto’ – R$ valor
# – Ordenar os itens por valor
# – Filtrar os gastos acima de R$ 500
# – Apresentar o total da fatura
from functools import reduce


def processarFatura(entrada):
    entrada.sort(key=lambda x: x[1])
    for gasto, valor in entrada:
        print(f'{gasto} - R${valor}')

    # print([(x, y) for x, y in entrada])

    # print(reduce(lambda gasto, valor: f'{gasto} {valor}')i for i in entrada)
    print(f'Total: {reduce(lambda x, y: x+y, [valor for gasto, valor in entrada])}')
    print('Valores acima de R$ 500', list(filter(lambda valor: valor > 500, [valor for gasto, valor in entrada])))


if __name__ == '__main__':
    processarFatura([('Net', 199.9), ('Ifood', 999.87), ('Gasolina', 678.0), ('Formigão', 400)])
