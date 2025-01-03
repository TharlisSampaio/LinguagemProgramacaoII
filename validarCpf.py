from functools import reduce


if __name__ == '__main__':
    def validarCpf(entrada):
        primeiroDigito = 0
        segundoDigito = 0
        conj = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        cpf = [int(x) for x in entrada if x != '.' if x != '-']
        soma = reduce(lambda x, y: x+y, list(map(lambda x, y: x * y, cpf, conj)))
        # print(cpf)

        if (soma % 11 < 2):
            primeiroDigito = 0
        if (soma % 11 >= 2):
            primeiroDigito = 11-(soma % 11)

        conj.append(11)
        conj = sorted(conj, reverse=True)

        soma = reduce(lambda x, y: x+y, list(map(lambda x, y: x * y, cpf, conj)))
        if (soma % 11 < 2):
            segundoDigito = 0
        if (soma % 11 >= 2):
            segundoDigito = 11-(soma % 11)

        if f'{primeiroDigito}{segundoDigito}' == f'{cpf[9]}{cpf[10]}':
            return True
        else:
            return False

    cpfVerificar = ''
    cpfVerificar = input()

    print(validarCpf(cpfVerificar))
