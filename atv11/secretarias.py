from funcionario import Funcionario


class Secretaria(Funcionario):
    def __init__(self, nome, cpf, email, telefone, cargo, salario):
        super().__init__(nome, cpf, email, telefone, cargo, salario)

    def calcular_bonificacao(self):
        pass

    def __str__(self) -> str:
        pass
