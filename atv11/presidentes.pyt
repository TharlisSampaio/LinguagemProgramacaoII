from funcionario import Funcionario


class Presidente(Funcionario):
    def __init__(self, nome, cpf, email, telefone, cargo, salario):
        super().__init__(nome, cpf, email, telefone, cargo, salario)
        self._salario_com_bonificacao = salario

    def calcular_bonificacao(self, porcentagem=0, adicional=0):
        salario_com_bonificacao = self.get_salario + (self.get_salario * (porcentagem / 100))
        self._salario_com_bonificacao = salario_com_bonificacao + adicional

    def get_salario_bonificacao(self):
        return self._salario_com_bonificacao

    def __str__(self) -> str:
        return f'{super().__str__()}, Salario com bonificação: {self.get_salario_bonificacao()}'


if __name__ == '__main__':
    p1 = Presidente('Texugo', '30030030030', 'texugo@tex.ltda.com', '6899988-4433', 'Presidente', 15000)

    print(p1.__str__())
    p1.calcular_bonificacao(50, 1000)
    print(p1.get_nome)
    p1.set_nome = 'Texugo JR'
    print(p1.__str__())
