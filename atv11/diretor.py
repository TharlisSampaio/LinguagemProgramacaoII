from funcionario import Funcionario


class Diretor(Funcionario):
    def __init__(self, nome, cpf, email, telefone, cargo, salario):
        super().__init__(nome, cpf, email, telefone, cargo, salario)
        self._salario_com_bonificacao = salario

    def calcular_bonificacao(self, porcentagem=0, adicional=0):
        salario_com_bonificacao = self.get_salario + (self.get_salario * (porcentagem / 100))
        self._salario_com_bonificacao = salario_com_bonificacao

    def get_salario_bonicacao(self):
        return self._salario_com_bonificacao

    def __str__(self) -> str:
        return f'{super().__str__()}, Salario com bonificação: {self.get_salario_bonicacao()}'


if __name__ == '__main__':
    g1 = Diretor('Texugo', '30030030030', 'texugo@tex.ltda.com', '6899988-4433', 'Diretor Gerente', 15000)
    g1.calcular_bonificacao(40)
    print(g1.__str__())
